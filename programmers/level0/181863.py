"""
rny_string
https://school.programmers.co.kr/learn/courses/30/lessons/181863
"""


def solution(rny_string):
    return rny_string.replace('m', 'rn')


if __name__ == '__main__':
    print(solution('masterpiece'))  # "rnasterpiece"
    print(solution('programmers'))  # "prograrnrners"
    print(solution('jerry'))  # "jerry"
    print(solution('burn'))  # "burn"
