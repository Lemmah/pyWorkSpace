from math import ceil


def getMaxMonsters(n, hit, t, h):
    # sort the monsters with their health
    h.sort()
    # record dead monsters
    deadMonsters = 0
    for health in h:
        if health > hit * t:
            break
        t -= ceil(health / hit)
        deadMonsters += 1
    return deadMonsters


def getDetails():
    n, hit, t = input().strip().split(' ')
    n, hit, t = [int(n), int(hit), int(t)]
    h = list(map(int, input().strip().split(' ')))
    result = getMaxMonsters(n, hit, t, h)
    print(result)


if __name__ == '__main__':
    getDetails()
