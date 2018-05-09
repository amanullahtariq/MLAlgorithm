from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        pass

    def __repr__(self):
        pass

    def comparator(a, b):
        pass


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)



