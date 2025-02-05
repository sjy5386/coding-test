"""
더 크게 합치기
https://school.programmers.co.kr/learn/courses/30/lessons/181939
"""


def solution(a, b):
    ab = int(f'{a}{b}')
    ba = int(f'{b}{a}')
    return max(ab, ba)


if __name__ == '__main__':
    print(solution(9, 91))  # 991
    print(solution(89, 8))  # 898
