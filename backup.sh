#!/bin/bash
DIR=$1
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_NAME="backup_${TIMESTAMP}.tar.gz"

if [ ! -d "$DIR" ]; then
    echo "Error: $DIR does not exist"
    exit 1
fi

mkdir -p ~/backups
tar -czf ~/backups/$BACKUP_NAME "$DIR"
echo "Backup saved to ~/backups/$BACKUP_NAME"
