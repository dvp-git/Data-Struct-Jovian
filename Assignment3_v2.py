
# Match the length
def resolve_len(poly1, poly2):
    if len(poly1) == len(poly2):
        return poly1
    if len(poly1) < len(poly2):
        poly1.append(0)
        poly1 = resolve_len(poly1, poly2)
    return poly1
#
# ==========Start test===========
# True
# Actual : [6, 12, 18, 30]
# Expected: [6, 12, 18, 30]
# ==========End test===========

poly1= [0, 1, 19, 2]
poly2= [2, 2, 2]
# print(multiply_dnc(poly1, poly2))



def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly

def multiply_dnc(poly1, poly2):
    if len(poly1) == 1:
        temp = [poly1[0] * poly2[i] for i in range(len(poly2))]
        return temp
    elif len(poly2) == 1:
        temp = [poly2[0] * poly1[i] for i in range(len(poly1))]
        return temp
    (poly1_0, poly1_1),(poly2_0, poly2_1) = split(poly1, poly2)
    print((poly1_0, poly1_1),(poly2_0, poly2_1))
    U = multiply_dnc(poly1_0, poly2_0)
    print(f"U:{U}")

    print((poly1_0, poly1_1),(poly2_0, poly2_1))
    V = multiply_dnc(poly1_0, poly2_1)
    print(f"V:{V}")

    print((poly1_0, poly1_1),(poly2_0, poly2_1))
    W = multiply_dnc(poly1_1, poly2_0)
    print(f"W:{W}")

    print((poly1_0, poly1_1),(poly2_0, poly2_1))
    Z = multiply_dnc(poly1_1, poly2_1)
    print(f"Z:{Z}")
    result = add(U , add(increase_exponent(add(V , W),len(poly1)//2),increase_exponent(Z ,len(poly1))))
    print(f"Component : {result}")
    print()
    return result







test0 = {     # fail
    'input': {
        'poly1': [2, 0, 5, 7],
        'poly2': [3, 4, 2]
    },
    'output': [6, 8, 19, 41, 38, 14]
}
test1 = {
    'input': {
        'poly1': [7],
        'poly2': [2]
    },
    'output': [14]
}
test2 = {
    'input': {
        'poly1': [1, 3, 5, 7],
        'poly2': [1, 3, 5, 7]
    },
    'output': [1, 6, 19, 44, 67, 70, 49]
}
test3 = {     # fail
    'input': {
        'poly1': [2, 4, 6, 10],
        'poly2': [3]
    },
    'output': [6, 12, 18, 30]
}
test4 = {
    'input': {
        'poly1': [0, 1, 19, 2],
        'poly2': [2, 2, 2, 2]
    },
    'output': [0, 2, 40, 44, 44, 42, 4]
}
test5 = {     # fail
    'input': {
        'poly1': [1, 2, 3, 4],
        'poly2': [0, 0, 0, 0]
    },
    'output': [0]
}


print(f"==========Start test===========")  ## Failing
print(f"Actual : {multiply_dnc(test0['input']['poly1'],test0['input']['poly2'])}")
print(f"Expected: {test0['output']}")
print(f"==========End test===========")

print(f"==========Start test===========")
# print(multiply_dnc(test1['input']['poly1'],test1['input']['poly2']) == test1['output'])
print(f"Actual : {multiply_dnc(test1['input']['poly1'],test1['input']['poly2'])}")
print(f"Expected: {test1['output']}")
print(f"==========End test===========")

print(f"==========Start test===========")
# print(multiply_dnc(test2['input']['poly1'],test2['input']['poly2']) == test2['output'])
print(f"Actual : {multiply_dnc(test2['input']['poly1'],test2['input']['poly2'])}")
print(f"Expected: {test2['output']}")
print(f"==========End test===========")

print(f"==========Start test===========")   ## Failing
# print(multiply_dnc(test3['input']['poly1'],test3['input']['poly2']) == test3['output'])
print(f"Actual : {multiply_dnc(test3['input']['poly1'],test3['input']['poly2'])}")
print(f"Expected: {test3['output']}")
print(f"==========End test===========")


print(f"==========Start test===========")
# print(multiply_dnc(test4['input']['poly1'],test4['input']['poly2']) == test4['output'])
print(f"Actual : {multiply_dnc(test4['input']['poly1'],test4['input']['poly2'])}")
print(f"Expected: {test4['output']}")
print(f"==========End test===========")


print(f"==========Start test===========")   ## Failing
# print(multiply_dnc(test5['input']['poly1'],test5['input']['poly2']) == test5['output'])
print(f"Actual : {multiply_dnc(test5['input']['poly1'],test5['input']['poly2'])}")
print(f"Expected: {test5['output']}")
print(f"==========End test===========")
