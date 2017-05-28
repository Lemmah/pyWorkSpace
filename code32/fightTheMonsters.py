#!/bin/python3


def getMaxMonsters(n, hit, t, h):
    """This function returns the maximum number of monsters Jason can kill in t seconds"""
    # keeping track of the remaining time
    remainingSeconds = t
    # blasting monsters only when time is greater than 0
    while remainingSeconds > 0:
        # checking each monster's health
        vulnerableMonster = min([health for health in h if health > 0])
        # getting the position of the vulnerable monster
        vulnerableMonsterPos = h.index(vulnerableMonster)
        # blasting the monster
        h[vulnerableMonsterPos] = vulnerableMonster - hit
        remainingSeconds -= 1
    # counting dead monsters
    deadMonsters = len([health for health in h if health <= 0])
    return deadMonsters


def getDetails():
    n, hit, t = input().strip().split(' ')
    n, hit, t = [int(n), int(hit), int(t)]
    h = list(map(int, input().strip().split(' ')))
    result = getMaxMonsters(n, hit, t, h)
    print(result)


if __name__ == '__main__':
    getDetails()
