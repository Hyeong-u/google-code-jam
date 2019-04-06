# Qualification Round 2019 - Google Code Jam 2019
# You Can Go Your Own Way
#
#
#
# ==============================================================================


def move(location, direction):
    if direction == "E":
        location[0] += 1
    else:
        location[1] += 1
    return


def get_direction(current_location, rival_location, rival_direction, n):
    reverse_direction = {"S": "E", "E": "S"}
    if current_location == rival_location:
        next_direction = reverse_direction[rival_direction]
        move(current_location, next_direction)
        move(rival_location, rival_direction)
        return next_direction

    move(rival_location, rival_direction)
    if current_location[0] == n - 1:
        next_direction = "S"
        move(current_location, next_direction)
        return next_direction
    elif current_location[1] == n - 1:
        next_direction = "E"
        move(current_location, next_direction)
        return next_direction
    elif current_location[0] > current_location[1]:
        next_direction = "S"
    else:
        next_direction = "E"
    move(current_location, next_direction)
    return next_direction


t = int(input())

for test in range(1, t + 1):
    n = int(input())
    rival_directions = input()
    current_location = [0, 0]
    rival_location = [0, 0]
    answer = ""
    for direction in rival_directions:
        answer += get_direction(current_location, rival_location, direction, n)

    print("Case #{test}: {answer}".format(test=test, answer=answer))
