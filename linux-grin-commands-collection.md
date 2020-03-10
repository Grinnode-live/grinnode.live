Use GRIN-Wallet without own GRIN-Node:

```_$ grin-wallet --api_server_address "https://grinnode.live:3413" info```

____ Wallet Summary Info - Account 'default' as of height 602336 ____
```
 Confirmed Total                  | 1.000000000 
 Awaiting Confirmation (< 10)     | 0.000000000 
 Awaiting Finalization            | 0.000000000 
 Locked by previous transaction   | 0.000000000 
 -------------------------------- | ------------- 
 Currently Spendable              | 1.000000000 
```

-----------------------------------------

Check if Tor address is up and running:

```curl --expect100-timeout 10 -X POST http://cgosdfdjue5g7ebqv3bgrt6sfwbvq4ricibnxjwkqimu2apbdyn7c752iyd.grinplusplus.com/v2/foreign -d '{"jsonrpc": "2.0","method": "check_version","id": 1,"params": []}' ```

If OK:

```
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "Ok": {
      "foreign_api_version": 2,
      "supported_slate_versions": [
        "V3",
        "V2"
      ]
    }
  }
```

Not OK:

```curl: (52) Empty reply from server```


-----------------------------------------

Send GRIN using GRIN-Wallet command line

```grin-wallet --api_server_address "https://grinnode.live:3413" send -d http://wallet.grinnode.live:3415 --message "Donation Grinnode.live" -m http 5```


```--api_server_address "https://grinnode.live:3413```  If you dont have your own node, you can always use our public API

```-d http://wallet.grinnode.live:3415``` Destination where you want to send GRIN via HTTP(s)

```--message "Donation Grinnode.live"``` Message is optional

```-m http 5```  sending via HTTP "5" (amount) GRIN
