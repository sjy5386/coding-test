"""
ad 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/181870
"""


def solution(strArr):
    return list(filter(lambda x: 'ad' not in x, strArr))


if __name__ == '__main__':
    print(solution(["and", "notad", "abcd"]))  # ["and","abcd"]
    print(solution(["there", "are", "no", "a", "ds"]))  # ["there","are","no","a","ds"]
