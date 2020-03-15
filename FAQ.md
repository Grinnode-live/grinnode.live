## FAQ 

We are receiving a lot of questions about GRIN-Node and Grinnode.live,
so we setup this section trying to answer some of these questions


#### Can I get the whole Grin-Blockchain since Block 0, when connected to https://Grinnode.live ?
**Short: No**

In your ```grin-server.toml``` file set your archive_mode = true
```
#run the node in "full archive" mode (default is fast-sync, pruned node)
archive_mode = true
```
This will allow you to store all GRIN blocks since you started the Grin-Node. But it will **NOT** download the complete
Grin-Blockchain. 


