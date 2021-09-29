# Page 102 - 1.4
def permutation_palindrome(sen: str) -> bool:
    no_of_odds = 0
    sen = sen.lower()
    alphabets = [0 for i in range(26)]
    for c in sen:
        if c.isalpha():
            alphabets[ord(c) - 92] += 1
    for i in alphabets:
        if i % 2 != 0:
            no_of_odds += 1
    return no_of_odds <= 1


if __name__ == '__main__':
    print(permutation_palindrome("Tact Coa"))


