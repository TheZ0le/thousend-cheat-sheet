from pywebio.output import (
    toast,
    put_markdown,
    use_scope,
    clear,
    put_buttons,
    put_button,
    put_text,
)
from functools import partial


allcards = [
    "AceOfHearts",
    "10OfHearts",
    "KingOfHearts",
    "QueenOfHearts",
    "JackOfHearts",
    "9OfHearts",
    "AceOfDiamonds",
    "10OfDiamonds",
    "KingOfDiamonds",
    "QueenOfDiamonds",
    "JackOfDiamonds",
    "9OfDiamonds",
    "AceOfClubs",
    "10OfClubs",
    "KingOfClubs",
    "QueenOfClubs",
    "JackOfClubs",
    "9OfClubs",
    "AceOfSpades",
    "10OfSpades",
    "KingOfSpades",
    "QueenOfSpades",
    "JackOfSpades",
    "9OfSpades",
]
yourcards = []
enemycards = []


def remove_card_fromlist(cardvalue):
    yourcards.remove(cardvalue)
    selectet_if_cards_correct()


def selectet_if_cards_correct():
    with use_scope("scopmain"):
        yourcards.sort()
        with use_scope("scopemain1"):
            clear(scope="scopemain1")
            put_markdown(
                r""" #### Are These Cards Correct?
        """
            )
            put_button("Yes", onclick=whosplaying, color="success", outline=True)
            put_text("If not Click to Remove the Wrong Cards.")
            put_buttons(
                [dict(label=i, value=i) for i in yourcards],
                onclick=partial(remove_card_fromlist),
            )


def back_select_cards(value, symbol):
    cardvalue = "%sOf%s" % (value, symbol)
    cardvalue_readable = "%s Of %s" % (value, symbol)

    if len(yourcards) == 10:
        toast("You reached the Maximum of Cards")
        selectet_if_cards_correct()

    elif len(yourcards) == 9:
        if cardvalue in yourcards:
            toast("This Card you already added")

        else:
            yourcards.append(cardvalue)
            toast("Added " + cardvalue_readable + " to your Cards")
            selectet_if_cards_correct()

    elif len(yourcards) == 0:
        yourcards.append(cardvalue)
        toast("Added " + cardvalue_readable + " to your Cards")

    else:
        if cardvalue in yourcards:
            toast("This Card you already added")

        else:
            yourcards.append(cardvalue)
            toast("Added " + cardvalue_readable + " to your Cards")


def gamephase(varenemycards, varallycards):
    gameenemycards = varenemycards
    gameallycards = varallycards
    clear(scope="scopemain")
    with use_scope("scopemain"):
        put_markdown(
            r""" #### Your Cards
    """
        )
        put_buttons(
            [dict(label=i, value=i) for i in gameallycards],
            onclick=partial(remove_card_from_your, varallycards=gameallycards, varenemycards=gameenemycards),
        )
        put_markdown(
            r""" #### Enemy Cards
    """
        )
        put_buttons(
            [dict(label=i, value=i) for i in gameenemycards],
            onclick=partial(remove_card_from_enemy, varallycards=gameallycards, varenemycards=gameenemycards),
        )


def whosplaying():
    clear(scope="scopemain")
    clear(scope="scopemain1")
    for i in yourcards:
        enemycards = [item for item in allcards if item not in yourcards]
    gamephase(enemycards, yourcards)


def remove_card_from_your(value, varenemycards, varallycards):
    gameenemycards = varenemycards
    gameallycards = varallycards
    gameallycards.remove(value)
    gamephase(gameenemycards, gameallycards)


def remove_card_from_enemy(value, varenemycards, varallycards):
    gameenemycards = varenemycards
    gameallycards = varallycards
    gameenemycards.remove(value)
    gamephase(gameenemycards, gameallycards)
