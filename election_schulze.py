'''
Election Script
Schulze-method version

Before using, you need to install py3votecore package, as:
$ pip install python3-vote-core
'''
from collections import Counter, defaultdict
import py3votecore
from py3votecore.schulze_method import SchulzeMethod
from py3votecore.condorcet import CondorcetHelper

votes = []
candidates = set()
while True:
    try:
        v = list(input().strip().upper())
        candidates |= set(v)
        votes.append(v)
    except EOFError:
        break
N = len(votes)

ballots = []
for v in votes:
    d = {'count':1}
    order = [[c] for c in v]
    order.append(list(candidates - set(v)))
    d['ballot'] = order
    ballots.append(d)

print(SchulzeMethod(ballots, ballot_notation = CondorcetHelper.BALLOT_NOTATION_GROUPING).as_dict())
