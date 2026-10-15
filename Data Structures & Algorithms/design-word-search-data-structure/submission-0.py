class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            current = root

            for j in range(i, len(word)):
                char = word[j]

                if char == ".":
                    for child in current.children.values():
                        if dfs(j + 1, child):
                            return True

                    return False

                else:
                    if char not in current.children:
                        return False

                    current = current.children[char]

            return current.endOfWord

        return dfs(0, self.root)

        

        
