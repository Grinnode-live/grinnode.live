# grinnode.live
Grinnode.live Website

       
# Using HA-GRIN Node 
1. Setup a GRIN Wallet e.g. https://github.com/mimblewimble/docs/wiki/How-to-use-the-Grin-wallet

2. Use it as API Endpoint or add it to your grin-wallet.toml 
```bash
CLI:
           ./grin-wallet --api_server_address "http://grinnode.live:3413"

grin-wallet.toml :
          check_node_api_http_addr = "http://grinnode.live:3413"
```


#### Other GRIN wallets 

Tested wallets | can use grinnode.live | problems
------------ | ------------- | -------------
grin-wallet 2.1.0 | ```diff + yes ```  | no known problems 
gin++ | <p style='color:red'> not tested </p> | please send feedback if its working


