import os
import textwrap

import requests

STOIC_API = "https://stoic-quotes.com/api/quote"


def call_api() -> dict:
    response = requests.get(STOIC_API)
    json_dict = response.json()
    return json_dict


def get_text(json_dict) -> str:
    return json_dict.get('text')


def get_author(json_dict) -> str:
    return json_dict.get('author')


def formatting_response(text, author) -> None:
    terminal_width = os.get_terminal_size().columns - 1

    wrapped_text = textwrap.wrap(text)
    for lines in wrapped_text:
        print(lines.center(terminal_width))

    author = f'~~~ {author} ~~~'
    formatted_author = author.center(terminal_width)
    print(f'\n{formatted_author}')


def main() -> None:
    call = call_api()
    formatting_response(get_text(call), get_author(call))


if __name__ == "__main__":
    main()
