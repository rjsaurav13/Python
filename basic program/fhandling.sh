#!/bin/sh
echo "enter the two files"
read f1
read f2
sort -u $f1 $f2 >d3.txt
cat d3.txt

