# You are given an array of strings arr. Your task is to construct a string from the words in arr, starting with the 0th character from each word (in the order they appear in arr), followed by the 1st character, then the 2nd character, etc. If one of the words doesn't have an ith character, skip that word.

# Return the resulting string.

# Example

# For arr = ["Daisy", "Rose", "Hyacinth", "Poppy"], the output should be solution(arr) = "DRHPaoyoisapsecpyiynth".

# First, we append all 0th characters and obtain string "DRHP";
# Then we append all 1st characters and obtain string "DRHPaoyo";
# Then we append all 2nd characters and obtain string "DRHPaoyoisap";
# Then we append all 3rd characters and obtain string "DRHPaoyoisapaecp";
# Then we append all 4th characters and obtain string "DRHPaoyoisapaecpyiy";
# Finally, only letters in the arr[2] are left, so we append the rest characters and get "DRHPaoyoisapaecpyiynth";

# For arr = ["E", "M", "I", "L", "Y"], the output should be solution(arr) = "EMILY".

# Since each of these strings have only one character, the answer will be 
# concatenation of each string in order, so the answer is EMILY.

def solution(arr):
    a =""
    arr2 = [list(c) for c in arr]
    print(arr2)
    while len(arr2) >0:
        for i in range(len(arr2)):
            if i < len(arr2)  and len(arr2[i])>0:
                a+= arr2[i].pop(0)
            if i < len(arr2) and len(arr2[i]) == 0:
                del arr2[i]
                
    return a
        
        
        
    
