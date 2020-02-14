This is a free service to the GRIN community. 

In order to keep the 24/7 high-availability we have to log some of our incoming requests in order to find problems between each nodes. 

Our Webservers and Loadbalancer are logging requests when using grinnode.live including the following attributes:

* Request date/time
* Page requested
* Protocol requested 
* IP address
* Amount of Bytes served 
* User agent
* Referrer
* Error logs

These log are stored on the servers and deleted after 14 day log-rotation on the server. 





