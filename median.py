
# Brute force solution
def median(a, b):
    result = []
    ptra = 0
    ptrb = 0
    while (ptra <= len(a) or ptrb <= len(b)):
        if ptra >= len(a):
            result.extend(b[ptrb:])
            break
        elif ptrb >= len(b):
            result.extend(a[ptra:])
            break
        elif a[ptra] < b[ptrb] and ptra < len(a):
            result.append(a[ptra])
            ptra += 1
        else:
            # b[ptrb] < a[ptra] and ptrb < len(b):
            result.append(b[ptrb])
            ptrb += 1
        # print(result, len(result)//2)
        # print(f"ptra:{ptra}")
        # print(f"ptrb:{ptrb}")
    print(result)
    return result[len(result)//2], result[(len(result)//2) - 1]






a = [1 ,3 ,3, 3, 10, 21,25 , 98]
b = [0 ,2 ,5, 6, 7, 12, 18,90]
print(median(a, b))
