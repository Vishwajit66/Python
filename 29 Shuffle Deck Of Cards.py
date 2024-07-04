# Shuffle Deck of Cards 

import random, itertools

deck = list(itertools.product(range(1,14),["Spade","Club","Hearts","Diomade"]))

random.shuffle(deck)

print(deck)

for i in range(5):
    print(deck[i][0],"of",deck[i][1])

