"""
문자열 재정렬
"""


def solution(s: str) -> str:
    a = []
    n = None
    for x in s:
        if x.isalpha():
            a.append(x)
        else:
            if n is None:
                n = 0
            n += int(x)
    a.sort()
    if n is not None:
        a.append(str(n))
    return ''.join(a)


def main():
    s = input()
    print(solution(s))


if __name__ == '__main__':
    print(solution('K1KA5CB7'))  # ABCKK13
    print(solution('AJKDLSI412K4JSJ9D'))  # ADDIJJJKKLSS20
