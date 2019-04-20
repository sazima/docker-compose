#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
SS_IP=$(echo ${3})
SS_PORT=$(echo ${4})
GOOGLE=http://clients1.google.com/generate_204
HTTP_CODE=`curl --socks5  $SS_IP:$SS_PORT -o /dev/null -s -w %{http_code} $GOOGLE`
echo  $SS_IP:$SS_PORT
if [ $HTTP_CODE == 204 ]
then
            echo 0
            exit 0
else
            echo 1
            exit 1
fi