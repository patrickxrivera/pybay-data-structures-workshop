from pprint import pprint
from collections import defaultdict

# How to model one-to-many mappings
# the key is the one
# the value is a list of the many

# 2D data structure: english down and spanish horizontally
e2s = dict(
    one=['uno'],
    two=['dos'],
    three=['tres'],
    four=['cuatro'],
    five=['cinco'],
    trio=['tres'],
    free=['libre', 'gratis']
)

# sub-optimal
# for eng, span_words in e2s.items():
#     for span in span_words:
# print(eng, '-->', span)

s2e = defaultdict(list)

# We get a 2-D data structure with spanish -> eng

# for eng, span_words in e2s.items():
#     for span in span_words:
#         if span not in s2e:
#             s2e[span] = []
#         s2e[span].append(eng)


# If you can do this, you are advanced enough to do difficult algos in Python
for eng, span_words in e2s.items():
    for span in span_words:
        s2e[span].append(eng)

pprint(s2e, width=40)
