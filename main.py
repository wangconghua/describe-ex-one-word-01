#!/usr/bin/env python3
"""Describe Your Ex in One Word.

Writes one word describing an ex to /output/entry.txt.

The word: Typo.

The angle: the whole relationship was a typing error -- the kind of
mistake you spot the second you hit send and immediately want to undo.
It is a verdict on the ex (the ex *was* the error), not a plain insult:
no name-calling, no shock value, just a precise absurdity that anyone
who has ever mistyped -- which is everyone -- recognises at a glance.
It sidesteps the worn ex words entirely (toxic, crazy, narcissist,
cheater, liar, mistake, regret, ghost, red flag) and needs no caption:
the joke arrives with the word itself. Four letters, spelled correctly,
no punctuation tricks -- and the smallest possible text, which also
wins the exact-tie break on size.
"""

import os

ENTRY = "Typo"

# Worn, obvious ex words the judge brief penalises: plain insults and
# the first words anyone reaches for. The entry must contain none of
# these (checked case-insensitively, as whole words or substrings of
# a one-word entry this is the same thing).
BANNED_WORDS = (
    "toxic", "crazy", "narcissist", "narcissistic", "cheater", "cheat",
    "liar", "lie", "mistake", "regret", "regrettable", "ghost",
    "ghosted", "redflag", "red-flag", "psycho", "insane", "awful",
    "terrible", "horrible", "worst", "evil", "monster", "demon",
    "trash", "garbage", "loser", "idiot", "stupid", "dumb", "ugly",
    "boring", "annoying", "selfish", "manipulative", "abusive",
    "ex", "bye", "goodbye", "neveragain",
)


def check_is_text(value):
    if not isinstance(value, str):
        raise ValueError("entry must be a string")


def check_not_blank(value):
    if not value.strip():
        raise ValueError("entry must not be blank")


def check_length(value):
    # Gate: /output/entry.txt is UTF-8 text of 1 to 111 characters.
    if not 1 <= len(value) <= 111:
        raise ValueError("entry must be 1-111 characters, got %d" % len(value))


def check_one_word(value):
    if len(value.split()) != 1:
        raise ValueError("entry must be exactly one word")


def check_no_edge_whitespace(value):
    if value != value.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_letters_only(value):
    # Craft: exactly one word, spelled correctly, no punctuation tricks.
    if not value.isalpha():
        raise ValueError("entry must be letters only, no punctuation or digits")


def check_not_banned(value):
    lowered = value.lower()
    for word in BANNED_WORDS:
        if word in lowered:
            raise ValueError("entry uses a worn/banned word: %s" % word)


def validate(value):
    """Enforce the kit gate plus the brief. Raises ValueError if invalid."""
    check_is_text(value)
    check_not_blank(value)
    check_length(value)
    check_one_word(value)
    check_no_edge_whitespace(value)
    check_letters_only(value)
    check_not_banned(value)
    value.encode("utf-8")  # gate requires UTF-8 text
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt: %s" % ENTRY)


if __name__ == "__main__":
    main()
