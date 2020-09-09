#!/usr/bin/expect 
#send "date"
#send "md5s=`md5sum zhang.txt | cut -d " " -f1`"
#send "echo $md5s >> /data1/asiainfo/interface/BAS/data/check"
set user "root"
set host "192.168.232.129"
set password "***"
set timeout -1
set sourceFilePath "/data1/***"
set filename [ lindex $argv 0 ]
set hostFilePath "/data7/***"
spawn scp $sourceFilePath$filename check $user@$host:$hostFilePath
expect "*assword:*"
send "$password\r"
expect eof
