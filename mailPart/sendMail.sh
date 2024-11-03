#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")
echo ">>>>>> Starting runing send mail with ip $DATE"
IP=$(curl ifconfig.me -s)
python sendMail.py $IP
DATE=$(date +"%Y-%m-%d_%H%M")
echo ">>>>>> ending runing send mail with ip $DATE"