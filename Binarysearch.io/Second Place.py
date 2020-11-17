'''
Second Place

Given a binary tree root, return the depth of the second deepest leaf. 
Note that if there are multiple deepest leaves, the second deepest leaf is the next highest one.
The root has a depth of 0 and you can assume the answer is guaranteed to exist for the trees given.

'''


def solve(self, root):

    queue = [root]
    levels = set()
    l = 0

    while len(queue) > 0:

        size = len(queue)

        for i in range(size):

            curr = queue.pop(0)

            if curr.left is None and curr.right is None:
                levels.add(l)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        l += 1

    return list(levels)[-2]
