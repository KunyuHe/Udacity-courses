from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.__is_word = False
        self.children = defaultdict(TrieNode)

    @property
    def is_word(self):
        return self.__is_word

    @is_word.setter
    def is_word(self, value):
        self.__is_word = value

    def __repr__(self):
        return str({char: {'word_end': self.is_word,
                           **child.children}
                    for char, child in self.children.items()})
