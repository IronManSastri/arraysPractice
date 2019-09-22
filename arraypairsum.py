def arraySum(arr, sum):

    if len(arr) < 2:
        return 
    
    seen = set()
    output = set()

    for key in arr:

        target = sum - key
        if target not in seen:
            seen.add(key)
        
        else:
            output.add( ( min(target,key), max(target,key) ) )

    return list(output)

print(arraySum([1,2,2,1,3], 4))