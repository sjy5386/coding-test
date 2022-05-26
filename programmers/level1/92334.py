"""
신고 결과 받기
https://programmers.co.kr/learn/courses/30/lessons/92334
"""

import collections


def solution(id_list, report, k):
    report_from = collections.defaultdict(lambda: set())
    report_to = collections.defaultdict(lambda: set())
    for r in report:
        a, b = r.split()
        report_from[b].add(a)
        report_to[a].add(b)
    blocked = set(filter(lambda e: len(report_from[e]) >= k, report_from))
    return [len(list(filter(lambda e: e in blocked, report_to[x]))) for x in id_list]


if __name__ == '__main__':
    print(solution(["muzi", "frodo", "apeach", "neo"],
                   ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))  # [2, 1, 1, 0]
    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))  # [0, 0]
