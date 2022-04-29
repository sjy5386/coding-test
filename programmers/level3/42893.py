"""
매칭 점수
https://programmers.co.kr/learn/courses/30/lessons/42893
"""

import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self, word: str):
        super(MyHTMLParser, self).__init__()
        self.word = word.lower()
        self.regex = re.compile(f'[a-z]+')
        self.link: str = ''
        self.default_score: int = 0
        self.external_links: list = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag == 'a':
            external_link = attrs[0][1].lower()
            if external_link != self.link:
                self.external_links.append(external_link)
        elif tag == 'meta' and attrs[0][1] == 'og:url':
            self.link = attrs[1][1].lower()

    def handle_data(self, data: str) -> None:
        for x in self.regex.findall(data.lower()):
            if x == self.word:
                self.default_score += 1


def solution(word, pages):
    n = len(pages)
    default_score = [0] * n
    external_links = [None] * n
    link_score = [0] * n
    matching_score = [0] * n
    link_to_index = {}
    index_to_link = [None] * n
    for i in range(n):
        page = pages[i]
        parser = MyHTMLParser(word)
        parser.feed(page)
        default_score[i] = parser.default_score
        link_to_index[parser.link] = i
        index_to_link[i] = parser.link
        external_links[i] = parser.external_links
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if index_to_link[i] in external_links[j]:
                link_score[i] += default_score[j] / len(external_links[j])
        matching_score[i] = default_score[i] + link_score[i]
    return matching_score.index(max(matching_score))


if __name__ == '__main__':
    print(solution('blind', [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))  # 0
    print(solution('Muzi', [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))  # 1
