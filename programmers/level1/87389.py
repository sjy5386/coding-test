"""
나머지가 1이 되는 수 찾기
https://programmers.co.kr/learn/courses/30/lessons/87389
"""


def solution(n):
    for x in range(2, n):
        if n % x == 1:
            return x


if __name__ == '__main__':
    print(solution(10))  # 3
    print(solution(12))  # 11
