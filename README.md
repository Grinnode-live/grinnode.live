# https://Grinnode.live Website

## HA-IP: 213.239.215.236 

### Ports available
### To Connect your GRIN Node use:
_$ cat grin-server.toml
[..]
peers_preferred = ["213.239.215.236:3414"]

Use the IP address "213.239.215.236" instead of the FQDN "grinnode.live"

## To Connect your GRIN Wallet use:

### Using HA-GRIN Node 
1. Setup a GRIN Wallet e.g. https://github.com/mimblewimble/docs/wiki/How-to-use-the-Grin-wallet

2. Use it as API Endpoint or add it to your grin-wallet.toml 
```bash
CLI:
           ./grin-wallet --api_server_address "https://grinnode.live:3413"

grin-wallet.toml :
          check_node_api_http_addr = "https://grinnode.live:3413"
```


## What is grinnode.live
It is an High Available (HA) API Calls service for the GRIN community 
see: https://grinnode.live/


#### Other GRIN wallets 

Tested wallets | can use grinnode.live | problems
------------ | ------------- | -------------
grin-wallet 2.1.0 | **yes**  | no known problems 
grin-wallet 3.0.0-beta.1 | **yes**  | no known problems 
grin++ |  not tested | please open an issue if tested
Wallet 713 |  not tested | please open an issue if tested
Wimble |  not tested | please open an issue if tested


#### Grin default Ports

**Port 3414** is for connecting GRIN nodes

**Port 3413** is for connecting GRIN wallets


#### CORS disabled
as of December 2019 CORS on the HTTP(s) API is disabled and can be used from your application or website
