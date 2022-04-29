"""
모험가 길드
"""


def solution(n: int, fear: list[int]) -> int:
    answer = 0
    fear.sort()
    adventurers = 0
    for x in fear:
        adventurers += 1
        if adventurers >= x:
            answer += 1
            adventurers = 0
    return answer


def main():
    n = int(input())
    fear = list(map(int, input().split()))
    print(solution(n, fear))


if __name__ == '__main__':
    print(solution(5, [2, 3, 1, 2, 2]))  # 2
