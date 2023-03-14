sen = input()
n = int(input())
trie = {}
_end = "*"
for _ in range(n):
    word = input()
    current_dict = trie
    for letter in word:
        current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = _end

def in_trie(word):
    current_dict = trie
    for letter in word:
        if letter not in current_dict:
            return False
        current_dict = current_dict[letter]
    return _end in current_dict

lim = 1_000_000_007
paths = [0 for _ in range(len(sen))]
paths[-1] = 1
for i in range(len(sen)-2, -1, -1):
    curr_paths = 0
    j = i + 1
    while j < len(sen):
        print(sen[i:j], paths, curr_paths)
        if in_trie(sen[i:j]):
            curr_paths = (curr_paths + paths[j+1]) % lim
        j += 1
    paths[i] = curr_paths
        
print(paths[0])

    

