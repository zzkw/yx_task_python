#!/bin/bash
date +%F_%H
cd /data1/asiainfo/interface/BAS/data/
lastmon=$(date "+%Y%m" -d "-1 months")
filename="guangdong_zhuanpinpai_"$lastmon".txt"
while true
do
  if [ -f "$filename" ];then
    size=`ls -l $filename |awk '/ /  {print $5}'`
    sleep 5
    size1=`ls -l $filename |awk '/ /  {print $5}'`
    if [ "$size" == "$size1" ];then
      mv $filename $filename".tmp"
      echo "${filename} transfer complete!Renamed ${filename}".tmp""
      break;
    fi
  fi
done

filename1=$filename".tmp"
sftp_Host="192.168.232.129"
sftp_userName="root"
sftp_passWord="zzkw135"
sftp_port=22
sftpRemotePath="/data7/asiainfo/interface/temp/houqiang/"
sftpLocalPath="/data1/asiainfo/interface/BAS/data/"

sftp_transfer()
{
  expect <<- EOF
  set timeout 5
  spawn sftp -P $sftp_port $sftp_userName@$sftp_Host

  expect "*assword:"
  send "$sftp_passWord\r"
  expect "sftp>"
  send "put $sftpLocalPath$filename1 $sftpRemotePath \r"
  expect "sftp>"
  send "rename $sftpRemotePath$filename1 $sftpRemotePath$filename \r"
  expect "sftp>"
  send "bye\r"
EOF
}

sftp_transfer

mv $filename1 $filename
