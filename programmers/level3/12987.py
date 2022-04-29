"""
숫자 게임
https://programmers.co.kr/learn/courses/30/lessons/12987
"""

import collections


def solution(A, B):
    answer = 0
    a = collections.deque(sorted(A))
    b = collections.deque(sorted(B))
    for x in a:
        while len(b) > 0:
            y = b.popleft()
            if x < y:
                answer += 1
                break
    return answer


if __name__ == '__main__':
    print(solution([5, 1, 3, 7], [2, 2, 6, 8]))  # 3
    print(solution([2, 2, 2, 2], [1, 1, 1, 1]))  # 0
