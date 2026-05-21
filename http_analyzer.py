import requests
import argparse

parser = argparse.ArgumentParser(description="HTTP Security Header Analyzer")
parser.add_argument("url", help="URL to analyze")
args = parser.parse_args()

url = args.url

try:
    response = requests.get(url, timeout=5)
except requests.exceptions.ConnectionError:
    print("Error: could not connect to", url)
    exit(1)
except requests.exceptions.Timeout:
    print("Error: connection timed out")
    exit(1)

print("URL:", url)
print("Status code:", response.status_code)
print("---")

if response.headers.get('Content-Security-Policy') is None:
    print("MISSING: Content-Security-Policy")
else:
    print("FOUND: Content-Security-Policy")

if response.headers.get('X-Frame-Options') is None:
    print("MISSING: X-Frame-Options")
else:
    print("FOUND: X-Frame-Options")

if response.headers.get('Strict-Transport-Security') is None:

    print("MISSING: Strict-Transport-Security")

else:

    print("FOUND: Strict-Transport-Security")



if response.headers.get('Referrer-Policy') is None:

    print("MISSING: Referrer-Policy")

else:

    print("FOUND: Referrer-Policy")

if response.headers.get('X-Content-Type-Options') is None:

    print("MISSING: X-Content-Type-Options")

else:

    print("FOUND: X-Content-Type-Options")


