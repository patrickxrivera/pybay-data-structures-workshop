# Binary Tree
# Node: [value, node_or_None, node_or_None]

NAME, MOM, POP = 0, 1, 2


def person(name, mom=None, pop=None):
    return [name, mom, pop]


sharon = person('Sharon')
dennis = person('Dennis')
jackie = person('Jackie')
ramon = person('Ramon')
rachel = person('Rachel', sharon, dennis)
raymond = person('Raymond', jackie, ramon)
matthew = person('Matthew', rachel, raymond)

# print('Grandfathers')
# print('|- (maternal)', matthew[MOM][POP][NAME])
# print('|- (paternal)', matthew[POP][POP][NAME])

# Tree Traversal (output list)
# Left, Curr, Right <-- Inorder
# Curr, Left, Right <-- Preorder
# Left, Right, Curr <-- Postorder


# def preorder(p):
#     if p is None:
#         return []
#     return [p[NAME]] + preorder(p[MOM]) + preorder(p[POP])

def tree_traversal(first, second, third):
    def fn(p):
        if p is None:
            return []
        return [p[first]] + fn(p[second]) + fn(p[third])
    return fn


preorder_order = [NAME, MOM, POP]
inorder_order = [MOM, NAME, POP]
postorder_order = [MOM, POP, NAME]

preorder = tree_traversal(*preorder_order)
inorder = tree_traversal(*inorder_order)
postorder = tree_traversal(*postorder_order)

print(inorder(matthew))
