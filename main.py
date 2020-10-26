#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 patch <patch@patchbox>
#
# Distributed under terms of the MIT license.

"""

"""
import configparser
from datetime import datetime
import speedtest
from psycopg2 import sql
import psycopg2


def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


def get_speedtest():
    """Gets current time DL/UL data"""
    node = speedtest.Speedtest()
    time_now = str(datetime.utcnow())[:19]
    downspeed = round((round(node.download()) / (1024 * 1024)), 2)
    upspeed = round((round(node.upload()) / (1024 * 1024)), 2)

    return (time_now, downspeed, upspeed)


def upload_to_table(config, data):
    connection = psycopg2.connect(host=config['DATABASE']['HOST'],
                                  database=config['DATABASE']['DB'],
                                  user=config['DATABASE']['USERNAME'],
                                  password=config['DATABASE']['PASSWORD'])
    cur = connection.cursor()
    query = """INSERT INTO {}
               (date, download_speed, upload_speed)
               VALUES (%s,%s,%s);""".format(config['DATABASE']['TABLE'])
    cur.execute(query, data)
    connection.commit()


def main():
    """Gets data and uploads it"""
    config = get_config()
    entry = get_speedtest()
    upload_to_table(config, entry)


if __name__ == "__main__":
    main()

