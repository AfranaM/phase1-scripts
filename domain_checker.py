# 1. imports
import requests
import argparse

# 2. argparse setup
parser = argparse.ArgumentParser(description="Domain Status Checker")
parser.add_argument("domains", nargs='+', help="domains to check")
args = parser.parse_args()

# 3. loop through domains
for domain in args.domains:
    try:
        response = requests.get(domain, timeout=5)
        print(domain, response.status_code)
    except requests.exceptions.ConnectionError:
        print(domain, "ERROR: could not connect")
    except requests.exceptions.Timeout:
        print(domain, "ERROR: timed out")
