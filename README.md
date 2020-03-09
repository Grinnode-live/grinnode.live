# https://Grinnode.live 

## HA-IP: 213.239.215.236 (ipv4)
## HA-IP: [2a01:4f8:a0:905b::2]  (ipv6)

#### +++UPDATE+++
#### IPv6 enabled for grinnode.live services. 

##### We enabled GRIN API v2 on our high-available GRIN-Node's

Scheduled downtime: n/a 

## What is grinnode.live
It is an High Available (HA) public and free API service and seed node for the GRIN community
see: https://grinnode.live/


### To Connect your GRIN Node to our high available GRIN-Node system:
_$ cat grin-server.toml
[..]
peers_preferred = ["213.239.215.236:3414"]
or
peers_preferred = ["http://grinnode.live:3414"]


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




#### Other GRIN wallets 

Tested wallets | can use grinnode.live | problems
------------ | ------------- | -------------
grin-wallet 2.1.0 | **yes**  | no known problems 
grin-wallet 3.0.X-beta.1 | **yes**  | no known problems 
niffler version 0.5.0 | **yes** | no known problems
grin++ |  not tested | please open an issue if tested
Wallet 713 |  not tested | please open an issue if tested
Wimble |  not tested | please open an issue if tested
IronBelly | not tested | please open an issue if tested

#### Do I need a API secret? 
No! 
All API's can be used without any API secret or owner secrets. 

#### Grin default Ports

**Port 3414** is for connecting GRIN nodes

**Port 3413** is for connecting GRIN wallets


#### grin-server.toml basic setup to connect to Grinnode.live 

```
peers_preferred = [213.239.215.236:3414]

#maximum number of inbound peer connections
peer_max_inbound_count = 30

#maximum number of outbound peer connections
peer_max_outbound_count = 10

#preferred minimum number of outbound peers (we'll actively keep trying to add peers
#until we get to at least this number)
peer_min_preferred_outbound_count = 10

#amount of incoming connections temporarily allowed to exceed peer_max_inbound_count
peer_listener_buffer_count = 5


```
You can download an example grin-server.toml here: https://github.com/MCM-Mike/grinnode.live/blob/master/grin-server.toml 




#### CORS disabled
as of December 2019 CORS on the HTTP(s) API is disabled and can be used from your application or website
01/2020 - enabled API v2 on all high-available public GRIN-Node
