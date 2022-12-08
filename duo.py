import pywebio
from pywebio.output import put_buttons, use_scope, clear, put_table
from functools import partial

from selectcardsduo import back_select_cards


def test():
    print("yes")


def choose_cards():

    pywebio.output.clear(scope="scopemain")

    with use_scope("scopemain"):
        put_table(
            [
                ["Symbol", "Card"],
                [
                    "Hearts ♥",
                    put_buttons(
                        ["Ace", "10", "King", "Queen", "Jack", "9"],
                        onclick=partial(back_select_cards, symbol="Hearts"),
                        outline=True,
                    ),
                ],
                [
                    "Diamonds ♦",
                    put_buttons(
                        ["Ace", "10", "King", "Queen", "Jack", "9"],
                        onclick=partial(back_select_cards, symbol="Diamonds"),
                        outline=True,
                    ),
                ],
                [
                    "Clubs ♣",
                    put_buttons(
                        ["Ace", "10", "King", "Queen", "Jack", "9"],
                        onclick=partial(back_select_cards, symbol="Clubs"),
                        outline=True,
                    ),
                ],
                [
                    "Spades ♠",
                    put_buttons(
                        ["Ace", "10", "King", "Queen", "Jack", "9"],
                        onclick=partial(back_select_cards, symbol="Spades"),
                        outline=True,
                    ),
                ],
            ]
        )
