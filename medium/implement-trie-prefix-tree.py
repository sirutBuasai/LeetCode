class Trie:

    def __init__(self):
        self.d = {}


    def insert(self, word: str) -> None:
        for i in range(len(word)-1):
            if word[:i+1] not in self.d:
                self.d[word[:i+1]] = 1
        self.d[word] = 2

    def search(self, word: str) -> bool:
        if word in self.d:
            return self.d[word] > 1

        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.d:
            return self.d[prefix] > 0

        return False
