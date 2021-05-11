import sys
from collections import defaultdict


def pre_order(node):
    if node.n is None:
        return

    preorder.append(node.n)
    pre_order(nodes[node.l])
    pre_order(nodes[node.r])


def in_order(node):
    if node.n is None:
        return

    in_order(nodes[node.l])
    inorder.append(node.n)
    in_order(nodes[node.r])


def post_order(node):
    if node.n is None:
        return

    post_order(nodes[node.l])
    post_order(nodes[node.r])
    postorder.append(node.n)


class Node():
    def __init__(self, n=None, l=None, r=None):
        self.n = n

        if l == '.':
            self.l = None
        else:
            self.l = l

        if r == '.':
            self.r = None
        else:
            self.r = r


if __name__ == "__main__":
    read = sys.stdin.readline

    preorder = list()
    inorder = list()
    postorder = list()

    nodes = defaultdict(Node)

    for i in range(int(read())):
        n, l, r = read().replace('\n', '').split()
        nodes[n] = Node(n, l, r)

    pre_order(nodes['A'])
    print(''.join(preorder))
    in_order(nodes['A'])
    print(''.join(inorder))
    post_order(nodes['A'])
    print(''.join(postorder))
