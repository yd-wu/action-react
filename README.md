
# action-react

`action-react` is a tool that reacts to Telegram chat messages.

![GitHub](https://img.shields.io/github/license/yd-wu/action-react)
![GitHub](https://img.shields.io/github/issues/yd-wu/action-react)
[![Build Status](https://github.com/yd-wu/action-react/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/yd-wu/action-react/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/yd-wu/action-react/branch/main/graph/badge.svg)](https://codecov.io/gh/yd-wu/action-react)

[Project Board](https://github.com/users/yd-wu/projects/1/views/1)

## Overview
`action-react` specifically listens to an account in a Telegram chat and makes corresponding http calls given the content of the message. This is inspired by [tuixue.online-visa](https://github.com/Trinkle23897/tuixue.online-visa), a tool that periodically checks and publishes US consulate visa appointment availabilities across the world.

A possible application of this tool is to use it to listen to a Telegram bot publishing messages about new visa appointments, and makes http calls to the consulate appointment service to grab the desired spot.

## Details
This project is a pure python project using modern tooling. It uses a `Makefile` as a command registry, with the following commands:
- `make`: list available commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make format`: autoformat this library using `black`
- `make annotate`: run type checking using `mypy`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information
- `make dist`: package library for distribution
