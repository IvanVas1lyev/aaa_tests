"""
Morse code decoder test
"""
import pytest as pytest

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': '/'
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


@pytest.mark.parametrize(
    'source_morse_string, result_eng_string',
    [
        ('-.. .- - .- / ... -.-. .. . -. -.-. .', 'DATA SCIENCE'),
        ('.- ...- .. - ---', 'AVITO'),
        ('-- .- -.-. .... .. -. . / .-.. . .- .-. -. .. -. --.',
         'MACHINE LEARNING'),
        ('.-.. --- ...- . / -- . -.-. .... -- .- -', 'LOVE MECHMAT'),
    ],
)
def test_decode(source_morse_string, result_eng_string):
    assert decode(source_morse_string) == result_eng_string


if __name__ == '__main__':
    pass
