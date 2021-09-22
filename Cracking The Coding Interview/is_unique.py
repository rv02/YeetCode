# Page 101-1.1
def is_unique(sen: str) -> bool:
    if len(sen) > 128:
        return False
    characters = [False for i in range(128)]
    for c in sen:
        if characters[ord(c)]:
            return False
        characters[ord(c)] = True
    return True


if __name__ == '__main__':
    print(is_unique("HanirhHe-=4"))
