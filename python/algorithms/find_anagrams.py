def anagrams(query, words):
    result = []
    query = query.lower()
    query_sorted = sorted(query)
    for w in words:
        w1= w.lower()
        if sorted(w1) == query_sorted:
            result.append(w)
        
    
    
    return result

words = [ "terse", "rest", "tears", "steer", "street" ]
query = "trees"

print(anagrams(query, words))


# result = [ "terse", "steer" ]
