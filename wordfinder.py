"""Word Finder: finds random words from a dictionary."""

words = {'car', 'house', 'boat', 'cat', 'dog'}

class WordFinder:
    ...
    def __init__(self, word):
        self.word = word

    def random(self):
        for search_word in words:
            if search_word== self.word:
                return self.word