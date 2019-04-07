# Qualification Round 2019 - Google Code Jam 2019
# Foregone Solution
#
#
#
# ==============================================================================

t = int(input())

for test in range(1, t + 1):
    n = int(input())

    start_i = 0
    string_n = str(n)
    length_n = len(string_n)
    for idx in range(length_n):
        if string_n[idx] == '4':
            start_i += 10 ** (length_n - idx - 1)
    for i in range(start_i, n):
        a = str(n - i)
        b = str(i)
        if '4' not in a and '4' not in b:
            break

    print("Case #{test}: {a} {b}".format(test=test, a=a, b=b))
