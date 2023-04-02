#!/usr/bin/python3
"""Defines isWinner function."""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    winners = {'Maria': 0, 'Ben': 0}
    for n in nums:
        if max(nums) < 2:
            winners['Ben'] += 1
            continue

        primes = [i for i in range(2, n + 1) if is_prime(i)]
        maria_turn = True
        while primes:
            can_remove = False
            for p in primes:
                if n % p == 0:
                    can_remove = True
                    primes.remove(p)
                    for i in range(p, n + 1, p):
                        if i in primes:
                            primes.remove(i)
                    n -= n // p
                    break
            if not can_remove:
                break
            maria_turn = not maria_turn
        if maria_turn:
            winners['Ben'] += 1
        else:
            winners['Maria'] += 1

    if winners['Maria'] == winners['Ben']:
        return None
    else:
        return max(winners, key=winners.get)
