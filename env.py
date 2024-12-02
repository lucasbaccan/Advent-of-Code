import os
from dotenv import load_dotenv


def get_session_cookie():
    load_dotenv()
    session_cookie = os.getenv("SESSION_COOKIE")

    if session_cookie is None:
        raise Exception("SESSION_COOKIE is not set in .env file")

    return session_cookie


def get_year():
    load_dotenv()
    year = os.getenv("YEAR")

    if year is None:
        return None

    return int(year)


def get_day():
    load_dotenv()
    day = os.getenv("DAY")

    if day is None:
        return None

    return int(day)


def get_part():
    load_dotenv()
    part = os.getenv("PART")

    if part is None:
        return None

    return int(part)
