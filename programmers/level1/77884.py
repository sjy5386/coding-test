"""
약수의 개수와 덧셈
https://programmers.co.kr/learn/courses/30/lessons/77884
"""


def solution(left, right):
    answer = 0
    for x in range(left, right + 1):
        a = 0
        for y in range(1, x + 1):
            if x % y == 0:
                a += 1
        answer += x if a % 2 == 0 else -x
    return answer


if __name__ == '__main__':
    print(solution(13, 17))  # 43
    print(solution(24, 27))  # 52
