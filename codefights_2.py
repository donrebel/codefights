class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.terminal = False
        self.children = {}

    def add_fragment(self, fragment):
        current_node = self
        for letter in fragment:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode(letter)
            current_node = current_node.children[letter]
        current_node.terminal = True

def findSubstringInWord(w, root):
    lenLongSubstr, longestPos = 0, 0

    for start_pos in range(len(w)):
        currNode = root
        for position in range(start_pos, len(w)):
            letter = w[position]
            if letter not in currNode.children:
                break
            currNode = currNode.children[letter]
            length = position - start_pos + 1
            if currNode.terminal and length > lenLongSubstr:
                lenLongSubstr = length
                longestPos = start_pos

    if lenLongSubstr == 0:
        return w
    end = longestPos + lenLongSubstr
    return w[:longestPos] + "[" + w[longestPos: end] + "]" + w[end:]

def findSubstrings(words, parts):
    root = TrieNode('')
    for p in parts:
        root.add_fragment(p)
    return [findSubstringInWord(w, root) for w in words]

words = ["Watermelon"]
parts = ["a", "mel", "lon", "el", "An"]
assert findSubstrings(words, parts) == ["Water[mel]on"]
print(findSubstrings(words, parts))
