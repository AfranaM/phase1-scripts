# Phase 1 Scripts

Bash automation scripts built during my systems learning journey.

## backup.sh
Backs up a folder with a timestamped compressed archive.

**Usage:**
bash backup.sh /path/to/folder


## logfinder.sh
Finds log files older than 7 days in a given directory and prints their size.

**Usage:**
bash logfinder.sh /path/to/folder

## http_analyzer.py
Checks a website for missing HTTP security headers.

**Usage:**
python3 http_analyzer.py https://github.com


## domain_checker.py
Checks if multiple domains are reachable and prints their status codes.

**Usage:**
python3 domain_checker.py https://google.com https://github.com
