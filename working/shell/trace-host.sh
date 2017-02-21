#!/bin/bash

host=$1

echo "------"
echo "MTR Trace Report - UDP"
echo "______________________"
mtr -r -w -c 10 --show-ips -u $host 
echo "------"


echo "------"
echo "MTR Trace Report - ICMP"
echo "_______________________"
mtr -r -w -c 10 --show-ips $host
echo "------"



echo "------"
echo "MTR Trace Report - TCP"
echo "______________________"
mtr -r -w -c 10 --show-ips -T $host
echo "------"

echo ""
echo "------"

echo "Parsed hosts for configuration gathering:"
echo "_________________________________________"
tracepath $host  | gawk -F' ' '{print $2}'| grep -v pmtu| grep -v LOC | uniq 
echo "---- end of testing ----"
