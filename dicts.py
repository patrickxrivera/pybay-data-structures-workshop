# Compound Keys

from pprint import pprint

# How to make compound keys when the fields are ordered
# pref = {}

# pref['raymond', 'hettinger'] = 'red'
# pref['rachel', 'hettinger'] = 'blue'
# pref['raymond', 'romano'] = 'orange'
# pref['rachel', 'ray'] = 'green'

# pprint(pref, width=50)

# How to make compound keys when the fields are unordered
pref = {}
pref[frozenset(['san jose', 'los angeles', 'washington d.c.'])] = 'purple'
# print(pref[frozenset(['los angeles', 'san jose', 'washington d.c.'])])

# Simple dictionary with a bijection (one-to-one and onto)
e2s = dict(one='uno', two='dos', three='tres', four='cuatro', five='cinco')

# Forward lookups are fast and easy
eng = 'three'
# print(eng, '-->', e2s[eng])

spanish = 'cuatro'


def s_to_e(span):
    for e, s in e2s.items():
        if s == span:
            print(s, '--->', e)


# Multiple reverse lookups
span_words = ['cuatro', 'cuatro', 'uno', 'tres', 'dos', 'tres', 'dos']

# [s_to_e(s) for s in span_words]

# How to reverse a bijection

s2e = {}
for e, s in e2s.items():
    s2e[s] = e
# pprint(s2e, width=25)

# Reverse Lookup Fast Way
for span in span_words:
    print(span, '-->', s2e[span])

# Most important invention in mathematics -> logarithm
a = 123412348
b = 68438303
# print(a + b, 'Easy')
# print(a * b, 'Hard')

# from math import log, exp
# print(exp(log(a)), log(b))
