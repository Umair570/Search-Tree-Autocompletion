import time
class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False
        self.frequency = 1

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.words = 0

    def insertWords(self, file):
        try:
            with open(file, 'r') as path:
                for newFiles in path:
                    newFiles = newFiles.strip()
                    self._insertHelper1(newFiles)
            return True
        except FileNotFoundError:
            return False

    def _insertHelper1(self, fileName):
        try:
            with open(fileName, 'r', encoding="utf-8") as file:
                for line in file:
                    allWords = line.strip().split()
                    for word in allWords:
                        self._insertHelper2(word)
        except FileNotFoundError:
            print(f"File {fileName} not found")
            return

    def _insertHelper2(self, word):
        node = self.root
        normalWord = self.cleanWord(word)
        # Skip empty words
        if normalWord == "":  
            return

        for char in normalWord:  
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # If word exists, increment frequency
        if node.wordEnd:  
            node.frequency += 1
        else:
            node.wordEnd = True
            self.words += 1

    def cleanWord(self, word):
        clean = ""
        specialChars = ".,?/;:\"'{}()[]"
        for i in word:
            # Include both uppercase and lowercase
            if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):  
                clean += i.lower()  
        return clean

    def autoComplete(self, prefix):
        node = self.root
        allWords = []
        # Ensure prefix is in lowercase
        prefix = prefix.lower()  

        for char in prefix:
            # If any character of the prefix is not found, return empty list
            if char not in node.children:
                return [] 
            node = node.children[char]

        self.prefixWords(node, prefix, allWords)
        self.sortWords(allWords)
        return allWords

    def prefixWords(self, node, prefix, result):
        stack = []
        stack.append([node, prefix])
        while stack:
            temp = stack.pop()
            tempNode = temp[0]
            tempPrefix = temp[1]
            if tempNode.wordEnd:
                result.append([tempPrefix, tempNode.frequency])
            for char, childNode in tempNode.children.items():
                stack.append([childNode, tempPrefix + char])

    def sortWords(self, allWords):
        # Sort by frequency in descending order and alphabetically if frequencies are equal
        allWords.sort(key=lambda x: (-x[1], x[0]))

def autoCompleteTrie():
    myTrie = Trie()
    fileName = input("Enter File name: ")
    start = time.time()
    validFile = myTrie.insertWords(fileName)
    if not validFile:
        print("File not found")
        return
    end = time.time()
    print(f"{fileName} loaded. {myTrie.words} words loaded into myTrie in {end - start} seconds")

    while True:
        inputWord = input("Enter a word to find prefixes (0 to quit program): ")
        print()
        if inputWord == '0':
            print("Bye!!!. See you next time.")
            break
        prefixes = myTrie.autoComplete(inputWord)
        if prefixes:
            print(f"Ranked prefixes of '{inputWord}':")
            for pref, freq in prefixes:
                print(f"{pref} (frequency: {freq})")
            print()
        else:
            print("No prefixes found")

autoCompleteTrie()
