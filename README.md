# Swift Arrow Couriers — Tracking Window

A lightweight courier parcel-tracking and management application with staff authentication, a parcel ledger, in-memory caching, and a command-line workflow for daily operations.

## Features

- Staff sign-in using username and password
- Argon2 password hashing
- Short-lived staff access tokens
- Create, update, and delete parcel records
- Parcel lookup by tracking code and destination
- In-memory caching for faster lookups
- Command-line interface for staff operations
- JSON-backed persistence

## Tech stack

- Python
- Argon2-cffi
- Uvicorn
- JSON file storage
- Python standard library: `secrets`, `time`, `collections`

## Run locally

The repository uses Poetry for dependency management.

```bash
git clone https://github.com/Abigail56/Swift-Arrow-Couriers--Project.git
cd Swift-Arrow-Couriers--Project
pip install poetry
poetry install
poetry run python main.py
```

## Project structure

```text
src/       Application source code
main.py    Application entry point
```

## Notes

This project demonstrates foundational backend concepts: authentication, password hashing, token expiry, data persistence, indexing, and caching. The JSON storage and in-memory cache are suitable for a learning project; a production service would use a database and shared cache such as PostgreSQL and Redis.
