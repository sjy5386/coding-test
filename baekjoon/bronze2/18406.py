"""
럭키 스트레이트
https://www.acmicpc.net/problem/18406
"""


def solution(n: int) -> str:
    arr = list(map(int, list(str(n))))
    center = len(arr) // 2
    left = sum(arr[:center])
    right = sum(arr[center:])
    return 'LUCKY' if left == right else 'READY'


def main():
    n = int(input())
    print(solution(n))


if __name__ == '__main__':
    print(solution(123402))
    print(solution(7755))
