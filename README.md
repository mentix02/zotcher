# Zotcher

A simple (unofficial) Zomato Partner API client library.

## Configuration

Zotcher was built with convention over configuration in mind. All that is required by
the user is the Node.js fetch call to 
[fetch-orders-by-states](https://www.zomato.com/merchant-api/orders/fetch-orders-by-states)
that can be grabbed from Chrome's Network tab in it's developer tools.

1. Open up the [Zomato Partner Dashboard](https://www.zomato.com/partners/onlineordering/orderHistory/) in Chrome.
2. Open the developer tools (F12). Click on "Network".
3. Right click `fetch-orders-by-states` and select "Copy" -> "Copy as Node.js fetch".
![Copy Node.js fetch](imgs/Screenshot%202022-08-15%20at%2000.35.05.png)
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
