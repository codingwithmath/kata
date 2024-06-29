
#bruteforce
#the complexity of this is 0(n2) since we are looking inside the array twice
def has_duplicate1(n):
    p = 0

    while p < len(n):
        for i in range(p + 1, len(n)):
            if (n[p] == n[i]):
                return True
            
        p += 1

#using a hashSet
#the complexity of this one is O(n) since we are looking inside the array only once.
#But we added a memory complexity of O(n) since we are storing the values in a hashSet. 
def has_duplicate(n):
    hashSet = set()

    for i in range(len(n)):
        if n[i] in hashSet:
            return True

        hashSet.add(n[i])
    
    return False

print(has_duplicate([1,0,4,3,5,6,7,2]))