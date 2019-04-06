# Qualification Round 2019 - Google Code Jam 2019
# You Can Go Your Own Way
#
#
#
# ==============================================================================


def move(x, y, direction):
    if direction == "E":
        x += 1
    else:
        y += 1
    return x, y


def get_reverse_direction(direction):
    reverse_direction = {"S": "E", "E": "S"}
    return reverse_direction.get(direction)


def back_track(rival_directions, rival_paths, inter_idx, answer):
    x, y = rival_paths[inter_idx]
    next_direction = answer[x + y]
    x, y = move(x, y, next_direction)
    next_direction = get_reverse_direction(answer[x + y])
    answer[x + y] = next_direction
    x, y = move(x, y, next_direction)
    return x, y


t = int(input())

for test in range(1, t + 1):
    n = int(input())
    rival_directions = input()
    rival_paths = [[0, 0]]
    for direction in rival_directions:
        x, y = rival_paths[-1]
        if direction == "E":
            path = [x + 1, y]
        else:
            path = [x, y + 1]
        rival_paths.append(path)
    intersection_indices = []
    x, y = 0, 0
    answer = [0 for x in rival_directions]
    total = 2 * n - 2
    answer = ["X"] * total
    reverse_direction = {"S": "E", "E": "S"}
    while x + y < total:
        idx = x + y
        r_x, r_y = rival_paths[idx]
        rival_direction = rival_directions[r_x + r_y]
        next_direction = reverse_direction[rival_direction]
        if x == r_x and y == r_y:
            if (rival_direction == "S" and x + 1 == n) or (rival_direction == "E" and y + 1 == n):
                x, y = back_track(rival_directions, rival_paths,
                                  intersection_indices.pop(), answer)
            else:
                intersection_indices.append(idx)
                answer[idx] = next_direction
                x, y = move(x, y, next_direction)
            continue
        if x < y:
            next_direction = "E"
        else:
            next_direction = "S"
        answer[x + y] = next_direction
        x, y = move(x, y, next_direction)
    answer = ''.join(answer)
    print("Case #{test}: {answer}".format(test=test, answer=answer))
