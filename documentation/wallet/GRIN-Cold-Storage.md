# Work in progress, not working atm 

# GRIN Cold Storage 

### Description:
In GRIN wallet version 5 we are are getting the possibility of setting up a GRIN cold storage solution. 
This solutions requires two GRIN-Wallets to start with and one GRIN-Node. 
You will be able to send funds to an offline GRIN-Wallet after this tutorial. 
One of the GRIN-Wallets  will be called hot GRIN-Wallet and the other cold GRIN-Wallet.

A retirement to archive the GRIN cold-storage solution will include to per-generate a few (or many) transaction which are not yet finalized. This allows us to send GRIN to the cold GRIN-Wallet and finalitze a transaction on the hot GRIN-Wallet without having all our GRINs locked in the hot GRIN-Wallet. 

Prior to GRINv5 we had the problem, if you did a transaction, all remaining GRINS where beeing locked in your wallet, if you dint generate enough `outputs` (See  `grin-wallet help send` :  ` -o, --change_outputs <change_outputs>     Number of change outputs to generate (mainly for testing) [default: 1]`)

This is changing due to the following GRIN-Wallet changes:
- https://github.com/mimblewimble/grin-wallet/pull/530
- https://github.com/mimblewimble/grin-wallet/pull/485

### Tested on Version 
[1] HOT-Wallet: https://github.com/mimblewimble/grin-wallet/releases/tag/v5.0.0-beta.2

[2] Cold-Wallet: https://github.com/mimblewimble/grin-wallet/releases/tag/v5.0.0-beta.2

[3] Node: https://github.com/mimblewimble/grin/tree/v5.0.0-beta.2

[4] Linux System 64bit 

### Prerequisites:
1. Have a full synced GRIN node [3] and two GRIN wallet [1] + [2] having API access to the node[2].
2. Some GRINs for testing. 

### Workflow 
Both GRIN-Wallets [1] + [2] have to have access to the GRIN-Node [2] for this initial process to work. 

Given is the hot GRIN-Wallet[1] with `5 GRINs` [appendix 1] 

```____ Wallet Summary Info - Account 'default' as of height 989031 ____

 Confirmed Total                  | 0.000000000 
 Awaiting Confirmation (< 10)     | 0.000000000 
 Awaiting Finalization            | 0.000000000 
 Locked by previous transaction   | 0.000000000 
 -------------------------------- | ------------- 
 Currently Spendable              | 5.000000000 

Command 'info' completed successfully
```

Given is the cold GRIN-Wallet[2] with `0 GRINs` [appendix 2] 
```
____ Wallet Summary Info - Account 'default' as of height 989033 ____

 Confirmed Total                  | 0.000000000 
 Awaiting Confirmation (< 10)     | 0.000000000 
 Awaiting Finalization            | 0.000000000 
 Locked by previous transaction   | 0.000000000 
 -------------------------------- | ------------- 
 Currently Spendable              | 0.000000000 

Command 'info' completed successfully
```
Now we are per-generating a transaction from Wallet[1] sending future GRINs to the cold Wallet[2] 
This can be done using the `Slatepack Address` as a recipient or just a plain transaction not assigning a `slatepack address`
We are showing both options in the following examples:

Pre-generate transactions **with** `Slatepack Address` 
*Slatepack address: grin1tt74pwyywxds403nydk5rjk9tlxvpkf9u9t50u3td69a6dfrrs4qxvwhg3 [appendix 3]*

`_$:/tmp/wallet/v5-1$ ./grin-wallet -t /tmp/wallet/v5-1 send --late-lock --outfile /tmp/wallet/v5-1/slatepack/1-GRIN-Cold-storage..slatepack --dest grin1tt74pwyywxds403nydk5rjk9tlxvpkf9u9t50u3td69a6dfrrs4qxvwhg3 1`
Output see [appendix 4] 

**Explaination:**
--late-lock : EXPERIMENTAL - Do not lock the coins immediately, instead only lock them during finalization. 
This allows us to generate multiple transactions without locking our funds in the wallet[1]. 

--outfile /tmp/wallet/v5-1/slatepack/1-GRIN-Cold-storage..slatepack 
We are defining our own names for each transaction we want to send to the cold wallet[2] later. 







Pre generate transactions **without** `Slatepack Address` 






### appendix 
**All GRIN-Wallet outputs are in `debug` mode**

[1] 
```
_$:/tmp/wallet/v5-1$ ./grin-wallet -t /tmp/wallet/v5-1 info
20201205 15:14:36.035 INFO grin_util::logger - log4rs is initialized, file level: Debug, stdout level: Debug, min. level: Debug
20201205 15:14:36.035 INFO grin_wallet - Using wallet configuration file at /tmp/wallet/v5-1/grin-wallet.toml
20201205 15:14:36.035 INFO grin_wallet - This is Grin Wallet version 5.0.0-beta.2 (git v5.0.0-beta.2), built for x86_64-unknown-linux-gnu by rustc 1.47.0 (18bf6b4f0 2020-10-07).
20201205 15:14:36.035 DEBUG grin_wallet - Built with profile "release", features "".
Password: 
20201205 15:14:39.156 DEBUG grin_store::lmdb - DB Mapsize for /tmp/wallet/v5-1/wallet_data/db/lmdb is 134217728
20201205 15:14:39.166 DEBUG grin_wallet_impls::lifecycle::seed - Using wallet seed file at: /tmp/wallet/v5-1/wallet_data/wallet.seed
20201205 15:14:39.203 DEBUG grin_wallet_libwallet::api_impl::owner_updater - Updating outputs from node
20201205 15:14:39.398 DEBUG grin_wallet_libwallet::internal::updater - Refreshing wallet outputs
20201205 15:14:39.607 DEBUG grin_wallet_libwallet::api_impl::owner_updater - Updating transactions
20201205 15:14:40.158 DEBUG grin_wallet_libwallet::api_impl::owner_updater - Starting UTXO scan
20201205 15:14:40.158 WARN grin_wallet_libwallet::api_impl::owner_updater - Scanning - 0% complete
20201205 15:14:40.825 DEBUG grin_wallet_libwallet::api_impl::owner_updater - Checking 143 outputs, up to index 8836482. (Highest index: 8836482)
20201205 15:14:40.825 WARN grin_wallet_libwallet::api_impl::owner_updater - Scanning - 99% complete
20201205 15:14:40.837 DEBUG grin_wallet_libwallet::api_impl::owner_updater - Identified 0 wallet_outputs as belonging to this wallet
20201205 15:14:40.837 WARN grin_wallet_libwallet::api_impl::owner_updater - Scanning - 99% complete
20201205 15:14:40.838 WARN grin_wallet_libwallet::api_impl::owner_updater - Scanning Complete

____ Wallet Summary Info - Account 'default' as of height 989031 ____

 Confirmed Total                  | 0.000000000 
 Awaiting Confirmation (< 10)     | 0.000000000 
 Awaiting Finalization            | 0.000000000 
 Locked by previous transaction   | 0.000000000 
 -------------------------------- | ------------- 
 Currently Spendable              | 5.000000000 

Command 'info' completed successfully
```
[2]
```
_$:/tmp/wallet/v5-2$ ./grin-wallet -t /tmp/wallet/v5-2 info
20201205 15:18:04.925 INFO grin_util::logger - log4rs is initialized, file level: Debug, stdout level: Debug, min. level: Debug
20201205 15:18:04.925 INFO grin_wallet - Using wallet configuration file at /tmp/wallet/v5-2/grin-wallet.toml
20201205 15:18:04.925 INFO grin_wallet - This is Grin Wallet version 5.0.0-beta.2 (git v5.0.0-beta.2), built for x86_64-unknown-linux-gnu by rustc 1.47.0 (18bf6b4f0 2020-10-07).
20201205 15:18:04.925 DEBUG grin_wallet - Built with profile "release", features "".
Password: 
20201205 15:18:05.539 DEBUG grin_store::lmdb - DB Mapsize for /tmp/wallet/v5-2/wallet_data/db/lmdb is 134217728
20201205 15:18:05.549 DEBUG grin_wallet_impls::lifecycle::seed - Using wallet seed file at: /tmp/wallet/v5-2/wallet_data/wallet.seed
20201205 15:18:05.591 DEBUG grin_wallet_libwallet::api_impl::owner_updater - Updating outputs from node
20201205 15:18:05.787 DEBUG grin_wallet_libwallet::internal::updater - Refreshing wallet outputs
20201205 15:18:06.006 DEBUG grin_wallet_libwallet::api_impl::owner_updater - Updating transactions
20201205 15:18:06.583 DEBUG grin_wallet_libwallet::api_impl::owner_updater - Starting UTXO scan
20201205 15:18:06.583 WARN grin_wallet_libwallet::api_impl::owner_updater - Scanning - 0% complete
20201205 15:18:07.386 DEBUG grin_wallet_libwallet::api_impl::owner_updater - Checking 139 outputs, up to index 8836490. (Highest index: 8836490)
20201205 15:18:07.386 WARN grin_wallet_libwallet::api_impl::owner_updater - Scanning - 99% complete
20201205 15:18:07.405 WARN grin_wallet_libwallet::api_impl::owner_updater - Scanning Complete

____ Wallet Summary Info - Account 'default' as of height 989033 ____

 Confirmed Total                  | 0.000000000 
 Awaiting Confirmation (< 10)     | 0.000000000 
 Awaiting Finalization            | 0.000000000 
 Locked by previous transaction   | 0.000000000 
 -------------------------------- | ------------- 
 Currently Spendable              | 0.000000000 

Command 'info' completed successfully
```
[3]
```
_$:/tmp/wallet/v5-2$ ./grin-wallet -t /tmp/wallet/v5-2 listen
20201205 15:24:51.871 INFO grin_util::logger - log4rs is initialized, file level: Debug, stdout level: Debug, min. level: Debug
20201205 15:24:51.871 INFO grin_wallet - Using wallet configuration file at /tmp/wallet/v5-2/grin-wallet.toml
20201205 15:24:51.871 INFO grin_wallet - This is Grin Wallet version 5.0.0-beta.2 (git v5.0.0-beta.2), built for x86_64-unknown-linux-gnu by rustc 1.47.0 (18bf6b4f0 2020-10-07).
20201205 15:24:51.871 DEBUG grin_wallet - Built with profile "release", features "".
Password: 
20201205 15:24:52.530 DEBUG grin_store::lmdb - DB Mapsize for /tmp/wallet/v5-2/wallet_data/db/lmdb is 134217728
20201205 15:24:52.540 DEBUG grin_wallet_impls::lifecycle::seed - Using wallet seed file at: /tmp/wallet/v5-2/wallet_data/wallet.seed
20201205 15:24:52.591 WARN grin_wallet_controller::controller - Starting TOR Hidden Service for API listener at address ll6vboeeognqvprtenwudswfl7gmbwjf4flup4rln2f52njddqvhsdqd, binding to 127.0.0.1:3415
20201205 15:24:52.597 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:52.597 [notice] Tor 0.4.4.6 running on Linux with Libevent 2.1.8-stable, OpenSSL 1.1.1, Zlib 1.2.11, Liblzma 5.2.2, and Libzstd 1.3.3.
20201205 15:24:52.597 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:52.597 [notice] Tor can't help you if you use it wrong! Learn how to be safe at https://www.torproject.org/download/download#warning
20201205 15:24:52.597 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:52.597 [notice] Read configuration file "/tmp/wallet/v5-2/tor/listener/torrc".
20201205 15:24:52.598 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:52.598 [warn] Path for DataDirectory (./data) is relative and will resolve to /tmp/wallet/v5-2/tor/listener/./data. Is this what you wanted?
20201205 15:24:52.598 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:52.598 [warn] Path for HiddenServiceDir (./onion_service_addresses/ll6vboeeognqvprtenwudswfl7gmbwjf4flup4rln2f52njddqvhsdqd) is relative and will resolve to /tmp/wallet/v5-2/tor/listener/./onion_service_addresses/ll6vboeeognqvprtenwudswfl7gmbwjf4flup4rln2f52njddqvhsdqd. Is this what you wanted?
20201205 15:24:52.600 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:52.000 [notice] Parsing GEOIP IPv4 file /usr/share/tor/geoip.
20201205 15:24:52.712 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:52.000 [notice] Parsing GEOIP IPv6 file /usr/share/tor/geoip6.
20201205 15:24:52.797 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:52.000 [notice] Bootstrapped 0% (starting): Starting
20201205 15:24:52.965 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:52.000 [notice] Starting with guard context "default"
20201205 15:24:53.991 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:53.000 [notice] Bootstrapped 5% (conn): Connecting to a relay
20201205 15:24:54.008 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:54.000 [notice] Bootstrapped 10% (conn_done): Connected to a relay
20201205 15:24:54.034 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:54.000 [notice] Bootstrapped 14% (handshake): Handshaking with a relay
20201205 15:24:54.069 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:54.000 [notice] Bootstrapped 15% (handshake_done): Handshake with a relay done
20201205 15:24:54.069 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:54.000 [notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits
20201205 15:24:54.069 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:54.000 [notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits
20201205 15:24:54.069 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:54.000 [notice] Bootstrapped 95% (circuit_create): Establishing a Tor circuit
20201205 15:24:54.214 DEBUG grin_wallet_impls::tor::process - Dec 05 15:24:54.000 [notice] Bootstrapped 100% (done): Done
20201205 15:24:54.215 WARN grin_wallet_controller::controller - Starting HTTP Foreign listener API server at 127.0.0.1:3415.
20201205 15:24:54.215 WARN grin_wallet_controller::controller - HTTP Foreign listener started.
20201205 15:24:54.215 WARN grin_wallet_controller::controller - Slatepack Address is: grin1tt74pwyywxds403nydk5rjk9tlxvpkf9u9t50u3td69a6dfrrs4qxvwhg3
```

[4]
```
_$:/tmp/wallet/v5-1$ ./grin-wallet -t /tmp/wallet/v5-1 send --late-lock --outfile /tmp/wallet/v5-1/slatepack/1-GRIN-Cold-storage..slatepack --dest grin1tt74pwyywxds403nydk5rjk9tlxvpkf9u9t50u3td69a6dfrrs4qxvwhg3 1
20201205 15:27:47.572 INFO grin_util::logger - log4rs is initialized, file level: Debug, stdout level: Debug, min. level: Debug
20201205 15:27:47.573 INFO grin_wallet - Using wallet configuration file at /tmp/wallet/v5-1/grin-wallet.toml
20201205 15:27:47.573 INFO grin_wallet - This is Grin Wallet version 5.0.0-beta.2 (git v5.0.0-beta.2), built for x86_64-unknown-linux-gnu by rustc 1.47.0 (18bf6b4f0 2020-10-07).
20201205 15:27:47.573 DEBUG grin_wallet - Built with profile "release", features "".
Password: 
20201205 15:27:48.902 DEBUG grin_store::lmdb - DB Mapsize for /tmp/wallet/v5-1/wallet_data/db/lmdb is 134217728
20201205 15:27:48.955 DEBUG grin_wallet_impls::lifecycle::seed - Using wallet seed file at: /tmp/wallet/v5-1/wallet_data/wallet.seed
20201205 15:27:49.544 DEBUG grin_wallet_libwallet::internal::updater - Refreshing wallet outputs
20201205 15:27:49.572 INFO grin_wallet_controller::command - Tx created: 1.000000000 grin to grin1tt74pwyywxds403nydk5rjk9tlxvpkf9u9t50u3td69a6dfrrs4qxvwhg3 (strategy 'smallest')
20201205 15:27:49.572 WARN grin_wallet_api::owner - Attempting to send transaction via TOR
20201205 15:27:49.572 INFO grin_wallet_impls::adapters::http - Starting TOR Process for send at Some(127.0.0.1:59050)
20201205 15:27:49.582 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:49.582 [notice] Tor 0.4.4.6 running on Linux with Libevent 2.1.8-stable, OpenSSL 1.1.1, Zlib 1.2.11, Liblzma 5.2.2, and Libzstd 1.3.3.
20201205 15:27:49.582 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:49.582 [notice] Tor can't help you if you use it wrong! Learn how to be safe at https://www.torproject.org/download/download#warning
20201205 15:27:49.582 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:49.582 [notice] Read configuration file "/tmp/wallet/v5-1/./tor/sender/torrc".
20201205 15:27:49.583 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:49.583 [warn] Path for DataDirectory (./data) is relative and will resolve to /tmp/wallet/v5-1/tor/sender/./data. Is this what you wanted?
20201205 15:27:49.585 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:49.585 [notice] Opening Socks listener on 127.0.0.1:59050
20201205 15:27:49.585 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:49.585 [notice] Opened Socks listener on 127.0.0.1:59050
20201205 15:27:49.586 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:49.000 [notice] Parsing GEOIP IPv4 file /usr/share/tor/geoip.
20201205 15:27:49.702 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:49.000 [notice] Parsing GEOIP IPv6 file /usr/share/tor/geoip6.
20201205 15:27:49.770 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:49.000 [notice] Bootstrapped 0% (starting): Starting
20201205 15:27:49.770 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:49.000 [notice] Starting with guard context "default"
20201205 15:27:50.772 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:50.000 [notice] Bootstrapped 5% (conn): Connecting to a relay
20201205 15:27:50.983 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:50.000 [notice] Bootstrapped 10% (conn_done): Connected to a relay
20201205 15:27:51.202 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:51.000 [notice] Bootstrapped 14% (handshake): Handshaking with a relay
20201205 15:27:51.830 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:51.000 [notice] Bootstrapped 15% (handshake_done): Handshake with a relay done
20201205 15:27:51.830 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:51.000 [notice] Bootstrapped 20% (onehop_create): Establishing an encrypted directory connection
20201205 15:27:51.969 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:51.000 [notice] Bootstrapped 25% (requesting_status): Asking for networkstatus consensus
20201205 15:27:52.000 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:52.000 [notice] Bootstrapped 30% (loading_status): Loading networkstatus consensus
20201205 15:27:52.380 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:52.000 [notice] I learned some more directory information, but not enough to build a circuit: We have no usable consensus.
20201205 15:27:52.412 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:52.000 [notice] Bootstrapped 40% (loading_keys): Loading authority key certs
20201205 15:27:52.547 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:52.000 [notice] The current consensus has no exit nodes. Tor can only build internal paths, such as paths to onion services.
20201205 15:27:52.549 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:52.000 [notice] Bootstrapped 45% (requesting_descriptors): Asking for relay descriptors
20201205 15:27:52.549 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:52.000 [notice] I learned some more directory information, but not enough to build a circuit: We need more microdescriptors: we have 0/6914, and can only build 0% of likely paths. (We have 0% of guards bw, 0% of midpoint bw, and 0% of end bw (no exits in consensus, using mid) = 0% of path bw.)
20201205 15:27:52.712 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:52.000 [notice] Bootstrapped 50% (loading_descriptors): Loading relay descriptors
20201205 15:27:52.963 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:52.000 [notice] The current consensus contains exit nodes. Tor can build exit and internal paths.
20201205 15:27:53.215 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:53.000 [notice] Bootstrapped 57% (loading_descriptors): Loading relay descriptors
20201205 15:27:53.363 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:53.000 [notice] Bootstrapped 64% (loading_descriptors): Loading relay descriptors
20201205 15:27:53.392 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:53.000 [notice] Bootstrapped 69% (loading_descriptors): Loading relay descriptors
20201205 15:27:53.425 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:53.000 [notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits
20201205 15:27:53.796 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:53.000 [notice] Bootstrapped 80% (ap_conn): Connecting to a relay to build circuits
20201205 15:27:53.823 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:53.000 [notice] Bootstrapped 85% (ap_conn_done): Connected to a relay to build circuits
20201205 15:27:53.888 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:53.000 [notice] Bootstrapped 89% (ap_handshake): Finishing handshake with a relay to build circuits
20201205 15:27:53.921 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:53.000 [notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits
20201205 15:27:53.921 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:53.000 [notice] Bootstrapped 95% (circuit_create): Establishing a Tor circuit
20201205 15:27:54.909 DEBUG grin_wallet_impls::tor::process - Dec 05 15:27:54.000 [notice] Bootstrapped 100% (done): Done
20201205 15:27:54.909 DEBUG grin_wallet_impls::tor::process - Dropping TOR process
20201205 15:28:14.914 DEBUG grin_wallet_api::owner - Send (TOR): Could not send Slate via TOR: Client Callback Error: Performing version check (is recipient listening?): Request error: Cannot make request: error trying to connect: deadline has elapsed
20201205 15:28:14.914 DEBUG grin_wallet_impls::tor::process - Dropping TOR process
20201205 15:28:14.914 DEBUG grin_wallet_api::owner - Unable to send via TOR: Client Callback Error: Performing version check (is recipient listening?): Request error: Cannot make request: error trying to connect: deadline has elapsed
20201205 15:28:14.914 WARN grin_wallet_api::owner - Unable to send transaction via TOR
20201205 15:28:15.170 DEBUG grin_wallet_libwallet::internal::selection - Change amount is: 0
/tmp/wallet/v5-1/slatepack/1-GRIN-Cold-storage..slatepack

Slatepack data follows. Please provide this output to the other party

--- CUT BELOW THIS LINE ---

BEGINSLATEPACK. ppyASHmXeNw648x j2VxSrmtKm8DzUG 9HyyfhP1QjRWfk6 BwBdtnWZ6F5nvp8 jLxY6ntScY6iNFo j4qpQ8XxBuAo9t1 MEznmMaHzs2qhR6 fDrXXbHTGUhnquK vzkQcPqo2DRkvpL tHezMKWUbSCpw1y qpAzjN1CGnoXRou ocimsDGrpSC8YPZ A4MFGLDWjtzPZxS GTf8YS3B6vZsGPd NdywDJsUzAqTDjs SAPfevDa4qJ5UuL UCSVukxL19F56nv C6NcNWduwoBAUxA BSFMX7ZCAacBrWF 9sULZVQAuuVQKJ2 iNA48Fe7xXz24Z3 vmWgNqhigEQZSDh buXjpUddqWyWsS9 eBo56BeJLhAxVzX QVB8s6Wrx5m6Qm8 LgZd2jn3dbmfq3K GP2BApYvV9jKSXd c1sYRdpFcQ2qsMX MDTXdkZVKNGUD4Q GwbdZGxqo5eHFpt sZrmmyDgPkxzZFj 5ddQ7MKgPak2TGY KsSQsFbtpjLXqeR XtjTjx7pEDgJGZi UUJvtEpMB54gA4y emXd5zanBoyijig B6tv5yeXRgTQfGz aj68ojvW3CEj8RA e1cohXVkjJyRBvD n1G7BoUGjogHZMa eSSq6SsKokHFiBv nHMxkU2YBZhhimZ sCpEi695VCTzf8L rXz1sSSia7tboXv xBZs1V2Egzyr53G SFFYRYDfeZoKM9v HqZH8qAy3Ae7GnX ma2FFkJR5cRFghR xav6ypNtzkM1kRx yenigdXD4u8U7HX w5FM8HM9vads7r3 5812HjQMH3wgYhR 3BA61gYi4q2hjsu cdg671HPHyxdxtk 3UruaAyVHdQgS5i hBHYXDekx4PDHpR Wh6pX1XeQrBy3Cy Poc8. ENDSLATEPACK.

--- CUT ABOVE THIS LINE ---

Slatepack data was also output to

/tmp/wallet/v5-1/slatepack/1-GRIN-Cold-storage..slatepack

The slatepack data is encrypted for the recipient only

Command 'send' completed successfully
```

[5]






