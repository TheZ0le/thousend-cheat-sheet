from pywebio.output import use_scope, put_markdown, put_buttons

from duo import choose_cards as select_cardsDuo
from trio import choose_cards as select_cardsTrio


def choose_mode():
    """
    Creating the main Site, Layout and Buttons
    """
    # Setting Up the Header
    with use_scope("scopetop"):
        put_markdown(
            r""" # Thousand Cheat Sheet
        """
        )
    # Setting Up the Buttons and scopes
    with use_scope("scopemain"):
        put_buttons(
            ["Duo", "Trio"], onclick=([select_cardsDuo, select_cardsTrio]), outline=True
        )
