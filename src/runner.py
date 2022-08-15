#!/usr/bin/env python3

import io
import json
import pathlib
import argparse

import requests

from .utils import *
from .constants import *
from .payload import Payload
from .configurator import Config

__author__ = "mentix02"
__version__ = "0.0.1a"


def setup_configurator(configurator: argparse.ArgumentParser):

    configurator.add_argument(
        "infile", type=argparse.FileType("r"), help="file with a NodeJS fetch to parse"
    )
    configurator.add_argument(
        "-o",
        "--outfile",
        default="config.json",
        help="output file to store config data",
    )


def setup_fetcher(fetcher: argparse.ArgumentParser):

    fetcher.add_argument(
        "-u",
        "--url",
        type=valid_url,
        default=DEFAULT_URL,
        help="Zomato endpoint to send payload",
    )
    fetcher.add_argument(
        "-o",
        "--offset",
        type=int,
        default=0,
        help="offset to start from",
    )
    fetcher.add_argument(
        "-n",
        "--number",
        type=int,
        default=20,
        help="number of orders to fetch",
    )
    fetcher.add_argument(
        "outfile",
        help="output file to store response data",
    )
    fetcher.add_argument(
        "-c",
        "--config-file",
        type=pathlib.Path,
        default=pathlib.Path(DEFAULT_CONFIG_FILE),
        help="path to JSON config file (default config.json)",
    )


def run_config(infile: io.TextIOWrapper, outfile: str):
    config = Config.from_node_fetch(infile.read())
    with open(outfile, "w+") as f:
        f.write(config.to_json())
    infile.close()


def run_fetch(
    url: str,
    offset: int,
    number: int,
    outfile: str,
    config_file: pathlib.Path,
):

    config = Config.from_config_file(config_file)
    payload = Payload(
        count=number,
        offSet=offset,
        res_ids=config.res_ids,
    ).to_json()

    req = requests.post(
        url,
        data=payload,
        headers=config.headers,
        cookies=config.cookies,
    )

    if req.status_code == 200:
        response_data = req.json()
        with open(outfile, "w+") as f:
            json.dump(response_data["orders"], f, indent=2)
    else:
        print("\bError: ", req.text)


def run():

    parser = argparse.ArgumentParser(
        description="a CLI to interact with the (unofficial) Zomato Partner API"
    )
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s " + __version__
    )

    subparsers = parser.add_subparsers(required=True, dest="command")

    configurator = subparsers.add_parser(
        "config",
        aliases=["c"],
        help="generate a config file",
        description="generate a config file",
    )
    fetcher = subparsers.add_parser(
        "fetch",
        aliases=["f"],
        help="fetches data from the API",
        description="fetches data from the API",
    )

    setup_fetcher(fetcher)
    setup_configurator(configurator)

    args = vars(parser.parse_args())

    spinner = AsyncSpinner()
    spinner.start()

    command = args.pop("command", "").lower()
    command_funcs = {
        "f": run_fetch,
        "c": run_config,
        "fetch": run_fetch,
        "config": run_config,
    }

    runner = command_funcs.get(command)

    if runner:
        runner(**args)
    else:
        parser.print_help()

    spinner.stop()
