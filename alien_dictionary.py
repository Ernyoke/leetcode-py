from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        d = {c: set() for words in words for c in words}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_length = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                return ""

            for j in range(min_length):
                if w1[j] != w2[j]:
                    d[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True
            for next_c in d[c]:
                if dfs(next_c):
                    return True
            visited[c] = False
            res.append(c)

        for c in d.keys():
            if dfs(c):
                return ""

        res.reverse()
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.foreignDictionary(["hrn", "hrf", "er", "enn", "rfnn"]))

    s = Solution()
    print(s.foreignDictionary(["wrtkj", "wrt"]))

    s = Solution()
    print(s.foreignDictionary(["wrt", "wrf", "er", "ett", "rftt", "te"]))

    s = Solution()
    print(s.foreignDictionary(
        ["abcdefgh", "bdefghij", "cghij", "dfghij", "efghij", "fghij", "ghij", "hij", "ij", "j", "abcdefghi",
         "bdefghijk", "cghijk", "dfghijk", "efghijk", "fghijk", "ghijk", "hijk", "ijk", "jk", "k"]))
