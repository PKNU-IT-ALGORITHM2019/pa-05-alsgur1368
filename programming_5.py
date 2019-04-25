# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, word, pron, mean):
        self.word = word
        self.pron = pron
        self.mean = mean
        self.left = self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, word, pron, mean):
        self.root = self._insert_value(self.root, word, pron, mean)
        return self.root is not None

    def _insert_value(self, node, word, pron, mean):
        if node is None:
            node = Node(word, pron, mean)
     #       print(node.word)
        else:
            if word <= node.word:
                node.left = self._insert_value(node.left, word, pron, mean)
            else:
                node.right = self._insert_value(node.right, word, pron, mean)
        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):

        if root is None:
            return False
        if root.word == key:
            return root

        elif key < root.word:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)


    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.word:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.word:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted


    def node_count(self,node):

        if node == None:
            return 0

        return 1 + self.node_count(node.right) + self.node_count(node.left)




##word, pron, mean


fp = open("shuffled_dict.txt", 'r', encoding='UTF-8')
bst = BinarySearchTree()
while True:
    line = fp.readline().split("\n")[0]
    if not line:
        break
    wpm = line.split()
    word = wpm[0]
    pron = wpm[1]
    mean = ''
    for i in wpm[2:]:
        mean += i+' '
    bst.insert(word, pron, mean)
fp.close()

while True:
    command1 = command = ''
    command = input("$ ")
    tmp = command.split()
    command1 = command2 = ''
    if len(tmp) > 1:
        command2 = tmp[1]
    command1 = tmp[0]
    if command1 == "add":
        word = input("word: ")
        pron = input("class:  ")
        mean = input("meaning: ")
        pron = "("+pron + ".)"
        bst.insert(word, pron, mean)

    if command1 == "delete":
        key = command2
        if bst.delete(key):
            print("Delete successfully.")
        else:
            print("Not Found.")
    if command1 == "deleteall":
        filename=command2
        fp = open(filename, "r", encoding='UTF-8')
        del_count = 0
        while True:
            word = fp.readline().split("\n")[0]
            if not word:
                break
            if bst.delete(word):
                del_count += 1
        fp.close()
        print("%d words were deleted successfully." % del_count)

    if command1 == "size":
        print(bst.node_count(bst.root))

    if command1 == "find":
        key = command2
        result = bst.find(key)
        if result != False:
            print(result.word + ' ' + result.pron + ' ' + result.mean)
        else:
            print("Not Found.")
    if command1 == "exit":
        break







