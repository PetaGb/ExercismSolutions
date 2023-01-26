from collections import Counter

YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: x.count(1)*1 
TWOS = lambda x: x.count(2)*2 
THREES = lambda x: x.count(3)*3 
FOURS = lambda x: x.count(4)*4
FIVES = lambda x: x.count(5)*5
SIXES = lambda x: x.count(6)*6
FULL_HOUSE = lambda x: sum(x) if sorted(Counter(x).values()) == [2,3] else 0
FOUR_OF_A_KIND = lambda x: four_of_a_kind(x)
LITTLE_STRAIGHT = lambda x: 30 if len(set(x)) == 5 and max(x) == 5 else 0
BIG_STRAIGHT = lambda x: 30 if len(set(x)) == 5 and min(x) == 2 else 0
CHOICE = sum

def four_of_a_kind(x):
    a, b = (Counter(x).most_common()[0])
    return a * b if b == 4 else a * (b - 1) if b == 5 else 0


def score(dice, category):
    return category(dice)
