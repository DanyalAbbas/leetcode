path = "/../"

def foo(path : str) -> str:
    SimplifiedPath = ["/"]
    PathList = path.split("/")
    PathList = [i for i in PathList if i != ""]
    for i in PathList:
        if i == "..":
            if len(SimplifiedPath) >1:
                SimplifiedPath.pop()
        elif i != ".":
            SimplifiedPath.append(i + "/")

    return "".join(SimplifiedPath)[:-1] if len(SimplifiedPath) >1 else "/"

print(foo(path))
