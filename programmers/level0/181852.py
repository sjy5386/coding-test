"""
뒤에서 5등 위로
https://school.programmers.co.kr/learn/courses/30/lessons/181852
"""


def solution(num_list):
    return sorted(num_list)[5:]


if __name__ == '__main__':
    print(solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))  # [15, 32, 38, 46, 56]
