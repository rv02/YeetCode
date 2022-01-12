
class Solution:
    # needs to be improved with rolling hash
    def search(self, patt, s):
        # code here
        indices = []
        patt_hash = hash(patt)
        for i in range(len(s) - len(patt) + 1):
            if patt_hash == hash(s[i: i + len(patt)]):
                if patt == s[i: i + len(patt)]:
                    indices.append(i+1)
        if not indices:
            indices.append(-1)
        return indices