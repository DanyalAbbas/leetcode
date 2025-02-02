paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

def foo(paths : list[list[str]]) -> str:
    NewList = []
    for i in zip(*paths): NewList.append(i)

    for i in NewList[1]:
        if i not in NewList[0]:
            return i
    


print(foo(paths))