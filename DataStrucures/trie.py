class TrieNode:
  def __init__(self, children={}, value=None, is_last=False):
    self.children = {}
    self.value = value
    self.is_last = is_last

class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  def add(self, value, root, index = 0):
    if not root:
      root = self.root

    if not root.value:
      root.value = value[index]
      
      if index == len(value) - 1:
        root.is_last = True
        return
      
      node = TrieNode(value=value[index + 1], children={})
      root.children.update({
        node.value:node
      })

      return self.add(value=value, index = index + 2, root = node)
    
    if index == len(value) - 1:
      if not root.value:
        root.value = value[index]
        root.is_last = True
      else:
        node = TrieNode(value=value[index], children={})
        node.is_last = True
        root.children.update({
          node.value:node
        })
      return
    
    node_item = root.children.get(value[index + 1])
    
    if node_item:
      return self.add(value=value, root=node_item, index = index + 2)

    node = TrieNode(value=value[index], children={})
    root.children.update({
      node.value:node
    })

    return self.add(value=value, index = index + 1, root = node)
  
  def add_value(self, value):
    return self.add(value=value.lower(), root=self.root, index=0)
  
  def search(self, word, root, index=0):
    if not root.value:
      return False
    
    if root.value != word[index]:
      return False

    if index == len(word) - 1:
      return root.is_last
    
    next = root.children.get(word[index + 1])

    return self.search(word=word, root=next, index = index + 1) if next else False

  def is_valid_word(self, word):
    return self.search(word=word.lower(), root=self.root, index=0)

trie = Trie()
trie.add_value('Brian')
trie.add_value('Bruno')
trie.add_value('Bria')
print(trie.is_valid_word('BrUno'))
print(trie.is_valid_word('Bria'))
print(trie.is_valid_word('ian'))