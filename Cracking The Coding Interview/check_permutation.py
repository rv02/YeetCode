# Page 101-1.2
from typing import List


def check_permutation(sen1: str, sen2: str) -> bool:
    if len(sen1) != len(sen2):
        return False
    return get_char_freq(sen1) == get_char_freq(sen2)


def get_char_freq(sen: str) -> List[int]:
    characters = [0] * 128
    for c in sen:
        characters[ord(c)] += 1
    return characters


if __name__ == '__main__':
    print(check_permutation("yauia&o", "oi/yuaa"))


