"""
디스크 컨트롤러
https://programmers.co.kr/learn/courses/30/lessons/42627
"""


def solution(jobs):
    t = 0
    a = []
    while len(jobs) > 0:
        j = sorted(filter(lambda e: e[0] <= t, jobs), key=lambda e: e[1])
        if len(j) == 0:
            t += 1
            continue
        job = j[0]
        jobs.remove(job)
        t += job[1]
        a.append(t - job[0])
    return sum(a) // len(a)


if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]))  # 9
