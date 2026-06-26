s = "leetcode"

def foo(s : str) -> str:
    s_better = list(map(ord, list(s)))
    result = []
    while s_better:
        result.append(s_better.pop(s_better.index(min(s_better))))
        while True:
            try:
                result.append(s_better.pop(s_better.index(min(filter(lambda a: a > result[-1], s_better)))))
            except:
                break
        
        if s_better:
            result.append(s_better.pop(s_better.index(max(s_better))))
        else:
            break

        while True:
            try:
                result.append(s_better.pop(s_better.index(max(filter(lambda a: a < result[-1], s_better)))))
            except:
                break
    return "".join(list(map(chr, result)))


def bar(s : str) -> str:
    s_better = {i : s.count(i) for i in s}
    result = ''
    while any(s_better.values()):
        for i in sorted(list(set(s))):
            if s_better[i]:
                s_better[i] -= 1
                result += i

        for i in sorted(list(set(s)), reverse=True):
            if s_better[i]:
                s_better[i] -= 1
                result += i
    return result




print(bar(s))