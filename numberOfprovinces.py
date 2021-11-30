


def component_count(arr):
    length = 0
    visited = []
    for i in range(len(arr)):
        if i not in visited:
            if arr[i] == 1:
                visited.append(i)
                if arr[i] == arr[(i+1)%len(arr)]:
                    continue
                else:
                    length+=1
    return length



array_1 = [1,0,1,0,1,0,0]
print(component_count(array_1))


def num_of_provinces(provinces):
    for i in range(len(provinces)):
        for j in range(len(provinces[0])):
            a = component_count(provinces)
q!
