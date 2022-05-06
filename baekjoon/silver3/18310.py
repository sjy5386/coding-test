"""
안테나
https://www.acmicpc.net/problem/18310
"""

from typing import List


def solution(n: int, houses: List[int]) -> int:
    houses.sort()
    return houses[(n - 1) // 2]


def main():
    n = int(input())
    houses = list(map(int, input().split()))
    print(solution(n, houses))


if __name__ == '__main__':
    print(solution(4, [5, 1, 7, 9]))  # 5
