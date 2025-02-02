paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

def foo(paths : list[list[str]]) -> str:
    paths = zip(*paths)
    StartingCities = next(paths)
    DestinationCities =  next(paths)
    
    for i in DestinationCities:
        if i not in StartingCities:
            return i
    


print(foo(paths))