# Zotcher

![GitHub top language](https://img.shields.io/github/languages/top/mentix02/zotcher)
![GitHub](https://img.shields.io/github/license/mentix02/zotcher)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> made with ❤️ by [mentix02](https://github.com/mentix02)

A simple (unofficial) Zomato&trade; Partner API client library & CLI.

**Note**: Zotcher is in no way affiliated with Zomato&trade; or any of its subsidiaries. All trademarks are the property of their respective owners. The project itself is licensed under the GPLv3 license.

## Installation

```
pip install zotcher
```

## Etymology

Important things first.
```
Zomato™ + fetcher = Zotcher
```

## Motivation

Zomato&trade; devs were too incompetent to provide order items in their CSV exports and after
tearing my hair out by scraping their dashboard via client side Javascript, it became
readily apparent that hacking around their private API would be far easier than sitting around and praying for them do the sensible thing. So I did.

## Config & Usage

Zotcher was built with convention over configuration in mind. All that is required by
the user is the Node.js fetch call to 
[fetch-orders-by-states](https://www.zomato.com/merchant-api/orders/fetch-orders-by-states)
that can be grabbed from Chrome's Network tab in it's developer tools.

1. Open up the [Zomato Partner Dashboard](https://www.zomato.com/partners/onlineordering/orderHistory/) in Chrome.
2. Open the developer tools (F12). Click on "Network".
3. Right click `fetch-orders-by-states` and select "Copy" -> "Copy as Node.js fetch".
![Copy Node.js fetch](https://github.com/mentix02/zotcher/raw/master/imgs/Screenshot%202022-08-15%20at%2000.35.05.png)
4. Paste the copied code into a file, e.g. `fetch.js`.
5. Run the `config` command to generate a config file. This should create a `config.json` file.
```bash
$ zotcher.py config fetch.js
```
6. Fetch the orders using the `fetch` command.
```bash
$ zotcher.py fetch orders.json
```

This should save the orders from the past 10 days to `orders.json`. You can go further by tweaking the
flags of the `fetch` command. Enjoy!
