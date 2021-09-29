# Page 102-1.5

def one_away(sen1: str, sen2: str) -> bool:
    length_diff = abs(len(sen1) - len(sen2))
    if length_diff >= 2:
        return False

    shorter = sen1 if len(sen1) < len(sen2) else sen2
    longer = sen2 if len(sen1) < len(sen2) else sen1
    foundDifference = False

    index1 = 0
    index2 = 0
    while index2 < len(longer) and index1 < len(shorter):

        if shorter[index1] != longer[index2]:
            if foundDifference:
                return False
            foundDifference = True
            if length_diff == 0:
                index1 += 1

        else:
            index1 += 1

        index2 += 1

    return True


if __name__ == '__main__':
    print(one_away("four", "fok"))




