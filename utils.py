import requests


def donwload_data(
    year: int,
    day: int,
    session_cookie: str,
    filename: str = "input.txt",
) -> str:

    # Download the content of the input file using requests and the session cookie
    request = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": session_cookie},
    )

    # Check if the request was successful
    if request.status_code != 200:
        raise Exception("Failed to download input file")

    # Save the content of the input file to a local file
    with open(filename, "w") as file:
        file.write(request.text)

    # Parse the input file content and return it as a list of strings
    return request.text.strip().split("\n")
