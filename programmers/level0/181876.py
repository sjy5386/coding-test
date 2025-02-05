"""
소문자로 바꾸기
https://school.programmers.co.kr/learn/courses/30/lessons/181876
"""


def solution(myString):
    return myString.lower()


if __name__ == '__main__':
    print(solution('aBcDeFg'))  # "abcdefg"
    print(solution('aaa'))  # "aaa"
