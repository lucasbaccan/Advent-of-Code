# AoC - Advent of Code

This repository contains my solutions for the [Advent of Code](https://adventofcode.com/) challenges.

## History

I discovered the Advent of Code challenges in 2023, and I decided to give it a try, but I didn't have time to finish them all. In 2024, I decided to try again and here I am.

## Requirements

The solutions are written in Python, so you need to have Python installed on your machine. The solutions are written in Python 3.11, but they should work with any Python 3 version.

You can run using docker, if you don't want to install Python on your machine.

## How to run

You need to have the `SESSION_COOKIE` from the Advent of Code website. You can get it by inspecting the cookies in your browser and put the value in the `.env` file.

```bash
cp .env.example .env
```

### With Python

```bash
male run-python
# or
python main.py
```

The script will ask you for the `YEAR`, `DAY` and `PART` you want to run. By default, it will ask you the `YEAR`, `DAY` and `PART` you want to run.

### With Docker

If you are running with Docker, remebember to change the `.env` file with the correct `YEAR`, `DAY` and `PART` you want to run.

```bash
make run-docker
# or
docker compose up --build
```

## Boilerplate

In the folder `0000` and `day00` you will find an example how to create the boilerplate for a new day. Remeber to change the file name to the correct part you are solving.
