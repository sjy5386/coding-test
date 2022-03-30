"""
로또의 최고 순위와 최저 순위
https://programmers.co.kr/learn/courses/30/lessons/77484
"""

RANKS = [6, 6, 5, 4, 3, 2, 1]


def solution(lottos, win_nums):
    unknown = lottos.count(0)
    known = 0
    for lotto in lottos:
        if lotto in win_nums:
            known += 1
    return [RANKS[unknown + known], RANKS[known]]


if __name__ == '__main__':
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]
