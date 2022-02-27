"""
피로도
https://programmers.co.kr/learn/courses/30/lessons/87946
"""

import itertools


def solution(k, dungeons):
    answer = 0
    ways = itertools.permutations(dungeons)
    for way in ways:
        fatigue = k
        i = 0
        for w in way:
            if fatigue < w[0]:
                break
            fatigue -= w[1]
            i += 1
        answer = max(answer, i)
    return answer


if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))  # 3
