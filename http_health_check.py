
import ssl
import urllib.request
import certifi


def check_health(url):
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    response = urllib.request.urlopen(
        url,
        timeout=5,
        context=ssl_context
    )

    print(f"URL: {url}")
    print(f"HTTP Status: {response.status}")
    print("-" * 40)


# List of URLs to monitor
urls = [
    "https://google.com",
    "https://github.com",
    "https://apple.com"
]


# Iterate through each URL and check its health
for url in urls:
    check_health(url)
