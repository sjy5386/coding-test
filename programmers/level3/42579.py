"""
베스트앨범
https://programmers.co.kr/learn/courses/30/lessons/42579
"""


def solution(genres, plays):
    answer = []
    dict1 = {}
    dict2 = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in dict1:
            dict1[genre] = 0
        if genre not in dict2:
            dict2[genre] = []
        dict1[genre] += play
        dict2[genre].append((i, play))
    genre_order = []
    for genre in set(genres):
        genre_order.append((genre, dict1[genre]))
        dict2[genre].sort(key=lambda e: (-e[1], e[0]))
        dict2[genre] = dict2[genre][:2]
    genre_order.sort(key=lambda e: -e[1])
    for genre, _ in genre_order:
        answer.extend(map(lambda e: e[0], dict2[genre]))
    return answer


if __name__ == '__main__':
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]
