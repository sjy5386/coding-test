"""
공백으로 구분하기 2
https://school.programmers.co.kr/learn/courses/30/lessons/181868
"""


def solution(my_string):
    return my_string.split()


if __name__ == "__main__":
    print(solution(' i    love  you'))  # ["i", "love", "you"]
    print(solution('    programmers  '))  # ["programmers"]
