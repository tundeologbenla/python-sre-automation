# Python SRE Automation

A collection of practical Python scripts and exercises focused on Site Reliability Engineering (SRE), DevOps and infrastructure automation.

The goal of this repository is to develop practical Python skills through small automation projects relevant to day-to-day SRE and platform engineering tasks.

## Project Structure

```text
python-sre-automation/
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── server_variables.py
├── http_health_check.py
├── README.md
└── .gitignore
```

## Task 1: Server Variables and Loops

**Script:** `server_variables.py`

A basic exercise demonstrating how to define a list of server names and iterate through them using a Python `for` loop.

The script prints a message for each server in the list.

**Concepts covered:**
- Python lists
- `for` loops
- Variables
- f-strings

**Run the script:**

```bash
python server_variables.py
```

## Task 2: HTTP Service Health Checker

**Script:** `http_health_check.py`

A simple HTTP health-checking script that monitors multiple URLs and determines whether services are healthy based on their HTTP response status.

The script uses Python's built-in `urllib` library to make HTTP requests and checks each endpoint individually.

### Features

- Monitors multiple HTTP and HTTPS endpoints.
- Classifies HTTP 2xx responses as `HEALTHY`.
- Classifies other HTTP responses as `UNHEALTHY`.
- Handles HTTP errors, including 404 responses.
- Handles connection and DNS resolution errors.
- Handles request timeouts using a five-second timeout.
- Uses SSL/TLS certificate verification through `certifi`.
- Logs results to the console and a log file.
- Uses Python's logging levels: INFO, WARNING and ERROR.
- Implements rotating file logging to manage log file size.

### Logging

The health checker uses Python's built-in `logging` module.

Log entries include a timestamp, severity level and message.

| Log level | Purpose |
|---|---|
| INFO | Successful HTTP responses |
| WARNING | Unsuccessful HTTP responses |
| ERROR | Connection failures and timeouts |

Logs are written to:

- Console output
- `http_health_check.log`

The script uses `RotatingFileHandler` with a maximum file size of approximately 1 MB and retains up to three backup log files.

Log files are excluded from Git using `.gitignore`.

### Example output

```text
2026-11-11 13:55:26 - INFO - https://google.com - HTTP Status: 200 - HEALTHY
2026-11-11 13:55:26 - INFO - https://github.com - HTTP Status: 200 - HEALTHY
2026-11-11 13:55:27 - WARNING - https://httpbin.org/status/404 - HTTP Status: 404 - UNHEALTHY
2026-11-11 13:55:27 - ERROR - https://example-invalid-domain.com - UNREACHABLE: DNS error
2026-11-11 13:55:32 - ERROR - https://httpbin.org/delay/10 - TIMEOUT: Request exceeded five seconds
```

*Example output is illustrative; actual timestamps and error messages will vary.*

### Run the script

```bash
python http_health_check.py
```

## Python Environment Setup

This project uses a Python virtual environment to isolate project dependencies.

Create and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required third-party dependency:

```bash
python -m pip install certifi
```

Python's `urllib`, `ssl` and `logging` modules are part of the standard library. `certifi` provides a trusted collection of SSL/TLS certificates.

## Code Quality and CI

The repository uses Ruff for Python linting and formatting checks.

A GitHub Actions workflow runs the following checks:

- Ruff lint checks: `ruff check .`
- Python formatting checks: `ruff format --check .`

The workflow runs on pushes to `main` and feature branches matching `feat/**`, and on pull requests targeting `main`.

## Skills and Concepts Covered

| Area | Concepts |
|---|---|
| Python fundamentals | Variables, lists, loops, functions and imports |
| HTTP monitoring | HTTP requests and response status codes |
| Error handling | Exceptions, timeouts and connection failures |
| SSL/TLS | Certificate verification |
| Logging | Log levels, formatters and handlers |
| File management | Rotating log files |
| Development workflow | Virtual environments and dependency management |
| Code quality | Ruff linting and formatting |
| CI/CD | GitHub Actions |

## Future Improvements

Potential enhancements include:

- Configurable URL lists rather than hardcoded endpoints.
- Command-line arguments for selecting URLs and timeout values.
- Unit tests using Python's `unittest` or `pytest`.
- Exporting health-check results in JSON format.
- Integration with monitoring and alerting platforms.
