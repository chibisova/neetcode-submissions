class TrieNode:
    def __init__(self):
        self.children = {} # maps each character to its next node
        self.endOfWord = False # tells whether a complete word ends at this node

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] # Go one level deeper
        
        cur.endOfWord = True
        return None

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
        
        if cur.endOfWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True
        
        