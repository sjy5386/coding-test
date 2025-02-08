"""
뒤에서 5등까지
https://school.programmers.co.kr/learn/courses/30/lessons/181853
"""


def solution(num_list):
    return sorted(num_list)[:5]


if __name__ == '__main__':
    print(solution([12, 4, 15, 46, 38, 1, 14]))  # [1, 4, 12, 14, 15]
