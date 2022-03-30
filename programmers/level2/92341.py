"""
주차 요금 계산
https://programmers.co.kr/learn/courses/30/lessons/92341
"""

import datetime
import math

LAST_TIME = datetime.datetime.strptime('23:59', '%H:%M')


def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees
    cars = {}
    for record in records:
        time, car, action = record.split(' ')
        time = datetime.datetime.strptime(time, '%H:%M')
        if action == 'IN':
            if car not in cars:
                cars[car] = [0, None]
            cars[car][1] = time
        else:
            cars[car][0] += int((time - cars[car][1]).total_seconds()) // 60
            cars[car][1] = None
    answer = []
    for k in sorted(cars.keys()):
        v = cars[k]
        if v[1] is not None:
            v[0] += int((LAST_TIME - v[1]).total_seconds()) // 60
        fee = default_fee
        if v[0] > default_time:
            fee += math.ceil((v[0] - default_time) / unit_time) * unit_fee
        answer.append(fee)
    return answer


if __name__ == '__main__':
    print(solution([180, 5000, 10, 600],
                   ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                    "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))  # [14600, 34400, 5000]
    print(solution([120, 0, 60, 591],
                   ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))  # [0, 591]
    print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))  # [14841]
