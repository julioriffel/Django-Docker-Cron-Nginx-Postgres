#!/bin/bash

#
# Copyright (c) 2021. Julio Cezar Riffel
# https://github.com/julioriffel
#

service cron start && gunicorn core.wsgi:application --bind 0.0.0.0:8000
