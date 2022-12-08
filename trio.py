import pywebio
from pywebio.output import put_buttons, use_scope


def test():
    print("test")

def choose_cards():
    with use_scope("scopemain"):
        put_buttons(
            ["1 ", "2 "], onclick=([test, test]), outline=True
        )
