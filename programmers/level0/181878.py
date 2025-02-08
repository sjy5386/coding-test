"""
원하는 문자열 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/181878
"""


def solution(myString, pat):
    return int(pat.lower() in myString.lower())


if __name__ == '__main__':
    print(solution("AbCdEfG", "aBc"))  # 1
    print(solution("aaAA", "aaaaa"))  # 0
