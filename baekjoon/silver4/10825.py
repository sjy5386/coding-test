"""
국영수
https://www.acmicpc.net/problem/10825
"""

from typing import List


def solution(n: int, students: List[str]) -> List[str]:
    arr = []
    for student in students:
        s = student.split()
        name = s[0]
        korean, english, math = map(int, s[1:])
        arr.append((name, korean, english, math))
    arr.sort(key=lambda e: (-e[1], e[2], -e[3], e[0]))
    return list(map(lambda e: e[0], arr))


def main():
    n = int(input())
    students = []
    for i in range(n):
        students.append(input())
    for answer in solution(n, students):
        print(answer)


if __name__ == '__main__':
    print(solution(12,
                   ['Junkyu 50 60 100', 'Sangkeun 80 60 50', 'Sunyoung 80 70 100', 'Soong 50 60 90', 'Haebin 50 60 100',
                    'Kangsoo 60 80 100', 'Donghyuk 80 60 100', 'Sei 70 70 70', 'Wonseob 70 70 90', 'Sanghyun 70 70 80',
                    'nsj 80 80 80', 'Taewhan 50 60 90']))
"""
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
"""
