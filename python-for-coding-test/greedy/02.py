"""
곱하기 혹은 더하기
"""


def solution(s: str) -> int:
    numbers = map(int, sorted(s, reverse=True))
    answer = next(numbers)
    for number in numbers:
        if number > 1:
            answer *= number
        else:
            answer += number
    return answer


def main():
    s = input()
    print(solution(s))


if __name__ == '__main__':
    print(solution('02984'))  # 576
    print(solution('567'))  # 210
