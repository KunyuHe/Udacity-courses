# Problem Statement

A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

To implement our autocomplete feature, we need to add the ability to list suffixes. To do that, we need to implement a new method on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie. For example, if our trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.

# Solution

To generate the suffixes, we first find the node by prefix. This runs in `O(n)` as it traverse the characters in the input string. If the prefix is not in our trie, the `Trie.find()` method would return `None`. If it is, then we call `Trie.suffixes()` method on the returned node. The recursive function traverses all the children of the node and appends those `TrieNode.is_word()` along the way to an empty list that hosts the suffixes. If the input prefix is a word in the trie but does not have children, then the `Trie.suffixes()` method would return an empty list.

# Complexity

Since we will traverse all the nodes in the trie in the worst case, the time complexity is `O(n)`. Also we use a list to host the suffixes, the space complexity is also `O(n)`.