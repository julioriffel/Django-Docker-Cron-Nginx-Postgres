#!/bin/bash

#
# Copyright (c) 2021. Julio Cezar Riffel
# https://github.com/julioriffel
#

scriptPath=$(dirname "$(readlink -f "$0")")
source "${scriptPath}/.env.sh"

for var in "$@"; do
  if [ $var = "one" ]; then
    /usr/local/bin/python /home/app/web/manage.py chat_newmessage1
  elif [ $var = "three" ]; then
    /usr/local/bin/python /home/app/web/manage.py chat_newmessage3
  elif [ $var = "five" ]; then
    /usr/local/bin/python /home/app/web/manage.py chat_newmessage5
  else
    echo "try again"
  fi
done

#/usr/local/bin/python /home/app/web/manage.py chat_newmessage1
