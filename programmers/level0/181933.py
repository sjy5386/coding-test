"""
flag에 따라 다른 값 반환하기
https://school.programmers.co.kr/learn/courses/30/lessons/181933
"""


def solution(a, b, flag):
    return a + b if flag else a - b


if __name__ == '__main__':
    print(solution(-4, 7, True))  # 3
    print(solution(-4, 7, False))  # -11
