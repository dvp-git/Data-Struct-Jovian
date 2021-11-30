def comp_area(l1, l2, dos=0):
    print(l1, l2)
    print("DOS:",dos)
    area = min(l1, l2 ) * dos
    return area

def compute_max_area(n , dos=0):
    max_area = 0
    for i in range(0,len(n)-1):
        print("-----------")
        dos = 0
        for j in range(i+1, len(n)):
            dos += 1
            max_area = max(max_area,comp_area(n[i], n[j], dos))
            print("AREA",max_area)
    return max_area, n[i], n[j]



n = [1,8,6,2,5,4,8,3,7]
compute_max_area(n)

def compute_optimized(n , first, last,max_area=0):
    while (first < last):
        max_area = max(min(n[first] , n[last]) * (last - first), max_area)
        print(max_area)
        if (n[first] < n[last]):
            first += 1
        else:
            last -= 1
    return max_area


a = compute_optimized([1,8,6,2,5,4,8,3,7],0,len(n)-1)
print(a)
