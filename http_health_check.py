import logging
import ssl
import urllib.error
import urllib.request
from logging.handlers import RotatingFileHandler

import certifi

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Log to console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Log to file with rotation
file_handler = RotatingFileHandler(
    "http_health_check.log",
    maxBytes=1_000_000,
    backupCount=3,
)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def check_health(url):
    # Load trusted SSL/TLS certificates
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    try:
        # Make HTTP request with a five-second timeout
        with urllib.request.urlopen(
            url,
            timeout=5,
            context=ssl_context,
        ) as response:
            status_code = response.status

    except urllib.error.HTTPError as error:
        status_code = error.code

    except TimeoutError:
        logger.error("%s - TIMEOUT: Request exceeded five seconds", url)
        return

    except urllib.error.URLError as error:
        logger.error("%s - UNREACHABLE: %s", url, error.reason)
        return

    # Classify HTTP response
    if 200 <= status_code < 300:
        health = "HEALTHY"
        logger.info("%s - HTTP Status: %s - %s", url, status_code, health)
    else:
        health = "UNHEALTHY"
        logger.warning("%s - HTTP Status: %s - %s", url, status_code, health)


# List of URLs to monitor
urls = [
    "https://google.com",
    "https://github.com",
    "https://apple.com",
    "https://httpbin.org/status/404",
    "https://this-domain-should-not-exist-12345.com",
    "https://httpbin.org/delay/10",
]


# Iterate through each URL and check its health
for url in urls:
    check_health(url)
