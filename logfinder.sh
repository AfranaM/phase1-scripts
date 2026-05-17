#!/bin/bash 

DIR=$1 

 

if [ ! -d "$DIR" ]; then 

 echo "Log: $DIR doesnt exist" 

 exit 1 

fi

name=$(find $1 -name "*.log" -mtime +7 -printf "%s bytes - %p\n") 
if [ -z "$name" ]; then
    echo "No old log files found"
else
    echo "Old log files found: $name"
fi

