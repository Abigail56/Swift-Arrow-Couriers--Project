# SWIFT ARROW COURIERS --- TRACKING WINDOW

## Wakatime:
[![wakatime](https://wakatime.com/badge/user/77836673-856e-42c2-a445-90ef6e65ce04/project/4a452c46-0c00-40ad-a67c-2db79ef855dc.svg)](https://wakatime.com/badge/user/77836673-856e-42c2-a445-90ef6e65ce04/project/4a452c46-0c00-40ad-a67c-2db79ef855dc)

## The Overview
Swift Arrow Couriers is a courier company that provides parcel delivery services and a lightweigth parcel tracking and management system. It provides staff authentication, parcel ledger management, caching for fast lookups, and a simple command-line interface for daily operations.

## Features
1: Authentication===>Staff sign-in with their usernam and password. The password will be hashed with Argon2, stored in a dictionary, then they will be issued a token also known as day pass which will be valid for 5 minutes.

2: Parcel ledger management===>Staff can add, update and delete parcels.

3: Caching===>Parcels are cached in a memory for fast lookups.

4: Indexing===>Parcels are indexed by the tracking code and destination city.

5: Command line interface===>This is a simple command-line interface that allows staff to sign in, sign out, and perform various operations on the parcel ledger.

## Tech Stack
1: Python 3.14
2: Argon2-cffi for password hashing
3: Uvicorn for the web server
4: JSON for data storage
5: Secrets for generating secure tokens
6: Time for time management
7: Collections.OrderedDict for data storage
8: JSON and OS for ledger persistence

## Project structure
1: src: This contains all the source codes for the project.
2: main.py: This is the main file that will be executed when the project is run(without it the project will not run).

## Installation
1: Install poetry with `pip install poetry`
2: Run `poetry install` to install the project dependecies
3: Run `poetry run python main.py` to run the project

