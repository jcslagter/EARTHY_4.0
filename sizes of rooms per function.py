x = list(range(0,400))
y = list(range(0,400))
Grid_size = 2
Area_funct = 215
values = []
Area_function = 300

for i in (list(range(180))):
    values.append((Grid_size**2)*i)

def takeClosest(Values, Area_function):
    newlst = []
    for i in values:
        newlst.append(i - Area_function)
    lstt = [abs(ele) for ele in newlst]
    _A_ = values[lstt.index(min(lstt))]
    return _A_

def x_and_yRange (x, y, _Area_function, Grid_size):
    x_coordinate = []
    y_coordinate = []
    pairs = []

    for i in x:
        for j in y:
            if (Grid_size*i)*(Grid_size*j) == _Area_function:
                x_coordinate.append(i)
                y_coordinate.append(j)
            else:
                pass
    
    for t in range(len(x_coordinate)):
        if t < ((1/2)*(len(x_coordinate))):
            pairs.append(x_coordinate[t])
            pairs.append(y_coordinate[t])
        else:
            pass


    return pairs, x_coordinate, y_coordinate


_Area_function = takeClosest(values, Area_function)

outcome = x_and_yRange (x, y, _Area_function, Grid_size)


pair_size = outcome[0]

x_size = outcome[1]
x_cells = x_size[:int((len(x_size))/2)]


y_size = outcome[2]
y_cells = y_size[:int((len(y_size))/2)]


final_pairs = [pair_size[i:i + 2] for i in range(0, len(pair_size), 2)]




print(_Area_function)
print(x_cells)
print(y_cells)
print(final_pairs)
