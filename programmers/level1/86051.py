"""
없는 숫자 더하기
https://programmers.co.kr/learn/courses/30/lessons/86051
"""


def solution(numbers):
    return sum(filter(lambda e: e not in numbers, range(10)))


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 6, 7, 8, 0]))  # 14
    print(solution([5, 8, 4, 0, 6, 7, 9]))  # 6
