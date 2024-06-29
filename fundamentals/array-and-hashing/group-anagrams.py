from collections import defaultdict
from typing import List


# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]



def groupAnagrams(strs: List[str]) -> List[List[str]]:

        #we need to set the defaultdict as list because we need to append the matching string to a key
        #and we can only access the .append method by declarating the dict as a list
        res = defaultdict(list) #the structure will be {a-z: strings that match the occurences}

        for s in strs:
            #I need to create my hashmap key, who will identify the anagram pattern
            #count is going to be the key of our hashmap
            count = [0] * 26 #this creates a list of index from elements from "a" to "z"
            #for example "a" is at index 0, and "z" is at index 25, so count[25] = "z"

            #Here we are counting the number of occurences
            #the ord() returns the unicode of a letter
            #so if "a" is at position 1, and "b" is at position 2, the result is 1, meaning "b" is at index 1
            for c in s:
                count[ord(c) - ord("a")] += 1

            #we need to declare the hashmap key as a tuple because a tuple is immutable
            #so python accept this as a key
            res[tuple(count)].append(s)
        
        return res.values()

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
