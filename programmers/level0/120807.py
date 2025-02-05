"""
숫자 비교하기
https://school.programmers.co.kr/learn/courses/30/lessons/120807
"""


def solution(num1, num2):
    return (num1 == num2) * 2 - 1


if __name__ == '__main__':
    print(solution(2, 3))  # -1
    print(solution(11, 11))  # 1
    print(solution(7, 99))  # -1
