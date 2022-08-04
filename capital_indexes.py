def capital_indexes(letters):
    list_1 = []
    
    for count, values in enumerate(letters):
        if values.isupper():
            list_1.append(count)
    
    return list_1
    
result = capital_indexes("TEsT")
print(result)