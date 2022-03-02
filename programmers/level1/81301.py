"""
숫자 문자열과 영단어
https://programmers.co.kr/learn/courses/30/lessons/81301
"""

import string


def solution(s):
    while max([x in s for x in string.ascii_letters]):
        s = s.replace('zero', '0')
        s = s.replace('one', '1')
        s = s.replace('two', '2')
        s = s.replace('three', '3')
        s = s.replace('four', '4')
        s = s.replace('five', '5')
        s = s.replace('six', '6')
        s = s.replace('seven', '7')
        s = s.replace('eight', '8')
        s = s.replace('nine', '9')
    return int(s)


if __name__ == '__main__':
    print(solution("one4seveneight"))  # 1478
    print(solution("23four5six7"))  # 234567
    print(solution("2three45sixseven"))  # 234567
    print(solution("123"))  # 123
