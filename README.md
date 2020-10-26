Wanted to keep track of my ISP internet speeds throughout the day, as I've noticed downtimes when working from home for some time. 

This script checks for DL speeds and uploads the data (timestamp, dl, up speeds) into a local postgresql server. 

Script runs off of an example crontab: 
```* * * * * cd /path/to/speedtest-checker && venv/bin/python main.py```

The data is then graphed in Grafana, which is also running on the RPI connected to the router. 

The config.ini1 is an example one, rename it to config.ini and update it to match your local DB settings for it to work. 
