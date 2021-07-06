import collections
from typing import List


def get_neighbors(word):
    neighbors = set()
    for i in range(len(word)):
        for j in range(26):
            neighbor = word[:i] + chr(j + 97) + word[i + 1:]
            neighbors.add(neighbor)
    return neighbors


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        visited = set()
        visited.add(beginWord)

        queue = collections.deque()
        queue.append(beginWord)

        ans = 1
        while queue:
            ans += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                neighbors = get_neighbors(cur)
                for ne in neighbors:
                    if ne in word_set and ne not in visited:
                        if ne == endWord:
                            return ans
                        else:
                            visited.add(ne)
                            queue.append(ne)
        return 0


if __name__ == '__main__':
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    #
    # print(Solution().ladderLength(beginWord, endWord, wordList))

    beginWord = "red"
    endWord = "tax"
    wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]

    print(Solution().ladderLength(beginWord, endWord, wordList))
