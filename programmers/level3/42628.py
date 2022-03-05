"""
이중우선순위큐
https://programmers.co.kr/learn/courses/30/lessons/42628
"""


def solution(operations):
    queue = []
    for operation in operations:
        cmd, arg = operation.split(' ')
        if cmd == 'I':
            queue.append(int(arg))
        elif len(queue) > 0:
            if arg == '1':
                queue.remove(max(queue))
            else:
                queue.remove(min(queue))
    return [max(queue), min(queue)] if len(queue) > 0 else [0, 0]


if __name__ == '__main__':
    print(solution(["I 16", "D 1"]))  # [0, 0]
    print(solution(["I 7", "I 5", "I -5", "D -1"]))  # [7, 5]
