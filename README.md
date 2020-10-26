Wanted to keep track of my ISP internet speeds throughout the day, as I've noticed downtimes when working from home for some time. 

This script checks for DL speeds and uploads the data (timestamp, dl, up speeds) into a local postgresql server. 

Script runs off of an example crontab: 
```* * * * * cd /path/to/speedtest-checker && venv/bin/python main.py```

The data is then graphed in Grafana, which is also running on the RPI connected to the router. 

The config.ini1 is an example one, rename it to config.ini and update it to match your local DB settings for it to work. 

Example speeds taken from Grafana:  
![Grafana graph](https://user-images.githubusercontent.com/25779373/97232614-21af8500-17e6-11eb-8377-8fe6dccacfb3.png)

PSQL DB example:
```
patchbox_data=> select * from speedtests limit 10;
        date         | download_speed | upload_speed
---------------------+----------------+--------------
 2020-10-26 16:40:02 |          23.13 |          2.2
 2020-10-26 16:41:02 |           16.7 |         2.61
 2020-10-26 16:42:02 |          20.33 |         1.89
 2020-10-26 16:43:02 |          16.17 |         2.61
 2020-10-26 16:44:02 |          25.83 |         2.21
 2020-10-26 16:45:02 |          15.43 |          2.6
 2020-10-26 16:46:02 |          22.08 |         2.26
 2020-10-26 16:47:02 |          12.64 |         2.15
 2020-10-26 16:48:03 |          20.51 |         2.42
 2020-10-26 16:49:02 |          17.03 |          2.5
(10 rows)
```
