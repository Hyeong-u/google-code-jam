# Qualification Round 2019 - Google Code Jam 2019
# You Can Go Your Own Way
#
#
#
# ==============================================================================


def get_reverse_direction(direction):
    reverse_direction = {"S": "E", "E": "S"}
    return reverse_direction.get(direction)


t = int(input())

for test in range(1, t + 1):
    n = int(input())
    rival_directions = input()
    answer = ""
    for direction in rival_directions:
        answer += get_reverse_direction(direction)
    print("Case #{test}: {answer}".format(test=test, answer=answer))
