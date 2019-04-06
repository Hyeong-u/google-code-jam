# Qualification Round 2019 - Google Code Jam 2019
# You Can Go Your Own Way
#
#
#
# ==============================================================================
import itertools


def move(x, y, direction):
    if direction == "E":
        x += 1
    else:
        y += 1
    return x, y


def get_reverse_direction(direction):
    reverse_direction = {"S": "E", "E": "S"}
    return reverse_direction.get(direction)


def make_candidates(n):
    elements = "E" * (n-1) + "S" * (n-1)
    all_candidates = itertools.permutations(elements)
    candidates = set()
    for c in all_candidates:
        candidates.add("".join(c))

    return candidates


def find_answer(candidates, rival_directions, rival_paths):
    for candidate in candidates:
        x, y, r_x, r_y = 0, 0, 0, 0
        for direction in candidate:
            r_x, r_y = rival_paths[x + y]
            rival_direction = rival_directions[x+y]
            if x == r_x and y == r_y and direction == rival_direction:
                break
            else:
                x, y = move(x, y, direction)
        else:
            return candidate


t = int(input())

for test in range(1, t + 1):
    n = int(input())
    rival_directions = input()
    candidates = make_candidates(n)
    rival_paths = [[0, 0]]
    answer = ""
    for direction in rival_directions:
        x, y = rival_paths[-1]
        if direction == "E":
            path = [x + 1, y]
        else:
            path = [x, y + 1]
        rival_paths.append(path)
    answer = find_answer(candidates, rival_directions, rival_paths)
    print("Case #{test}: {answer}".format(test=test, answer=answer))
