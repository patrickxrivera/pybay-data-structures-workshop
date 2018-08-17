# Doubly Linked List

# Triple: [value, triple_or_none, triple_or_none]
# Raymond <--> Rachel <--> Matthew

VALUE, PREV, NEXT = 0, 1, 2

a = ['Raymond', None, None]
b = a[NEXT] = ['Rachel', a, None]  # 1st make list, 2nd assign b, 3rd a[NEXT]
c = b[NEXT] = ['Matthew', b, None]

# TODO: Write a recursive algorithm that walks backward
