class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for s in word:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return node.endOfWord
            if word[i] != ".":
                if word[i] not in node.children:
                    return False
                # פשוט מחזירים את התשובה מההמשך ישירות
                return dfs(node.children[word[i]], i+1)
            else: 
            # במקרה של נקודה, מספיק שילד *אחד* יחזיר True
                for nei in node.children.values():
                    if dfs(nei, i+1):
                        return True
                # אם עברנו על כל הילדים ואף אחד לא התאים (או שאין ילדים)
                return False
                
        return dfs(self.root, 0)







        
