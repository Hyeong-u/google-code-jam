# Qualification Round 2019 - Google Code Jam 2019
# Cryptopangrams
#
#
#
# ==============================================================================
import math


def get_prime_numbers(n=10000):
    prime_numbers = [2]
    for i in range(3, n + 1):
        for k in range(2, int(math.sqrt(i)+3)):
            if i % k == 0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers


def decrypt(candidates, codes):
    table = {}
    for i in range(len(codes)):
        table[codes[i]] = chr(i+65)
    answer = ""
    for candidate in candidates:
        answer += table[candidate]
    return answer


t = int(input())

for test in range(1, t + 1):
    limit, length = map(int, input().split())
    cryptopangrams = list(map(int, input().split()))
    answer = ""
    cryptopangram = cryptopangrams[0]
    prime_numbers = get_prime_numbers(limit)
    for prime_number in prime_numbers:
        if cryptopangram % prime_number == 0:
            candidates = [prime_number, cryptopangram // prime_number]
            break
    cryptopangram = cryptopangrams[1]
    previous = candidates[0]
    for candidate in candidates:
        if cryptopangram % candidate == 0:
            previous = candidate
    if candidates[0] == previous:
        candidates.reverse()

    for cryp in cryptopangrams[1:]:
        previous = cryp // previous
        candidates.append(previous)
    codes = sorted(list(set(candidates)))
    answer = decrypt(candidates, codes)
    print("Case #{test}: {answer}".format(test=test, answer=answer))
