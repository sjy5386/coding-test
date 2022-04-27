"""
가장 긴 팰린드롬
https://programmers.co.kr/learn/courses/30/lessons/12904
"""


def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            length = j - i
            if length < answer:
                continue
            sub = s[i:j]
            rev = sub[::-1]
            if sub == rev:
                answer = max(length, answer)
    return answer


if __name__ == '__main__':
    print(solution("abcdcba"))  # 7
    print(solution("abacde"))  # 3
