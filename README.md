# Python SRE Automation

## About

This repository contains practical Python scripts and exercises focused on Site Reliability Engineering (SRE), DevOps and infrastructure automation.

The objective is to develop Python programming skills through small, practical projects that introduce concepts commonly used in SRE and platform engineering.

## Project Structure

| Script | Description |
|---|---|
| `server_variables.py` | Iterates through a list of server names using a Python `for` loop. |
| `http_health_check.py` | Checks multiple HTTP/HTTPS endpoints and reports their HTTP response status codes. |

## Task 1: Server List Loop

A basic Python exercise using a list and a `for` loop to iterate through server names and print a message for each server.

**Skills practised:**
- Python lists
- `for` loops
- String formatting with f-strings
- Basic scripting concepts

**Run:**

```bash
python3 server_variables.py
```

## Task 2: HTTP Service Health Checker

A Python script that checks the availability of multiple HTTP/HTTPS endpoints.

The script uses Python's built-in `urllib` library to make HTTP requests and reports the response status code for each endpoint.

**Implementation:**
- Defines a reusable `check_health()` function.
- Stores multiple URLs in a Python list.
- Uses a `for` loop to iterate through endpoints.
- Uses SSL/TLS certificate validation through Python's `ssl` module and the `certifi` package.
- Configures a five-second connection timeout.

**Skills practised:**
- Python functions and arguments
- HTTP requests and response status codes
- Python lists and iteration
- SSL/TLS certificate validation
- Python imports and external packages
- Virtual environments and package management

**Dependencies:**
- Python
- `certifi`

**Run:**

```bash
python3 http_health_check.py
```

**Current functionality:**

The script checks each configured endpoint and prints its HTTP response status. The current implementation has successfully returned HTTP 200 responses from multiple public endpoints.

**Planned improvements:**
- Introduce healthy/unhealthy status classification.
- Add exception handling for HTTP errors and connection failures.
- Improve timeout handling.
- Introduce structured logging using Python's `logging` module.

## Development Environment

Python dependencies should be installed within a project-specific virtual environment.

Create and activate the environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the HTTP health-check dependency:

```bash
python -m pip install certifi
```

Deactivate the environment when finished:

```bash
deactivate
```

## CI/CD

This repository uses GitHub Actions for automated Python code quality checks.

The CI workflow runs on pushes to `main` and feature branches matching `feat/**`, as well as pull requests targeting `main`.

**Current checks:**
- Ruff linting (`ruff check .`)
- Ruff formatting validation (`ruff format --check .`)

## Future Development

Planned areas of development include:

- HTTP health-check improvements.
- TCP connectivity checks.
- Structured logging and error handling.
- Python unit testing using pytest.
- Infrastructure and AWS automation.
- Additional SRE monitoring and operational scripts.