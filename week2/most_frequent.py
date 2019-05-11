

def fn(arr):
    hashmap = {}
    for char in arr:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1

    max_val = 0    
    count = 0
    for key in hashmap:
        if hashmap[key] > count:
            count = hashmap[key]
            max_val = key
        
    return max_val





l = [1,3, 2,3,1,1,2]
print(fn(l))
