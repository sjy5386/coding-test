"""
뒤집기
https://www.acmicpc.net/problem/1439
"""


def solution(s: str) -> int:
    count = [0] * 2
    prev = None
    for x in s:
        if x != prev:
            count[int(x)] += 1
            prev = x
    return min(count)


def main():
    s = input()
    print(solution(s))


if __name__ == '__main__':
    print(solution('0001100'))  # 1
