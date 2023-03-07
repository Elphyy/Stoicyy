import requests


STOIC_API = "https://stoic-quotes.com/api/quote"


def call_api():
    response = requests.get(STOIC_API)
    json_dict = response.json()
    return json_dict


def get_text(json_dict):
    return json_dict.get('text')


def get_author(json_dict):
    return json_dict.get('author')


def formatting_response(text, author): # TODO: add the formatting of the code should be something like the next comment
    """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce dui risus, laoreet eu eros vitae,
                interdum fermentum lectus. In hac habitasse platea dictumst. Praesent blandit.

                                            ~~~ AUTHOR ~~~
    """


call = call_api()
formatting_response(get_text(call), get_author(call))
