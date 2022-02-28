"""
단어 변환
https://programmers.co.kr/learn/courses/30/lessons/43163
"""


def compare(word1, word2):
    a = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            a += 1
    return a


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    while begin != target:
        if len(words) == 0:
            return 0
        arr = []
        for word in words:
            if compare(word, begin) == 1:
                arr.append((word, compare(word, target)))
        arr.sort(key=lambda e: e[1])
        begin = arr[0][0]
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
