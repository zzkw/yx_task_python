#!/bin/bash
ips=(
192.168.232.129
192.168.1.102
)
ports=(
3306
21
22
20
10004
445
)
for ip in ${ips[@]}
do
  for port in ${ports[@]}
  do
    echo > /dev/tcp/${ip}/${port} > /dev/null 2>&1
    if [ $? -eq 0 ];then
      echo -e "\033[32m${ip}:${port} is open.\033[0m"
    fi
  done
done
