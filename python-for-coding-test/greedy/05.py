"""
볼링공 고르기
"""

import itertools
from typing import List


def solution(n: int, m: int, balls: List[int]) -> int:
    return len(list(filter(lambda x: balls[x[0]] != balls[x[1]], itertools.combinations(range(0, n), r=2))))


def main():
    n, m = map(int, input().split())
    balls = list(map(int, input().split()))
    print(solution(n, m, balls))


if __name__ == '__main__':
    print(solution(5, 3, [1, 3, 2, 3, 2]))  # 8
    print(solution(8, 5, [1, 5, 4, 3, 2, 4, 5, 2]))  # 25
