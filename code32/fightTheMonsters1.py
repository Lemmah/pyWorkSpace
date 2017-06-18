#!/bin/python3


def getMaxMonsters(n, hit, t, h):
    """This function returns the maximum number of monsters Jason can kill in t seconds"""
    # sort the  monsters according to health  as in hlist
    h.sort()
    # know the dead monsters if any
    deadMonsters = 0
    # start killing monsters
    for eachMonster in h:
        if t > 0:
            while eachMonster > 0:
                t -= 1
                if t > 0:
                    eachMonster -= hit
                else:
                    break
            deadMonsters += 1
    return deadMonsters


def getDetails():
    n , hit, t = input().strip().split(' ')
    n, hit, t = [int(n), int(hit), int(t)]
    h = list(map(int, input().strip().split(' ')))
    result = getMaxMonsters(n, hit, t, h)
    print(result)


if __name__ == '__main__':
    getDetails()
