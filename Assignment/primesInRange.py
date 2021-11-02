def primesInRange(lowBound=None, highBound=None):  
    ERROR_VALUE = None
    LOWER_BOUND = 1
    UPPER_BOUND = 1000
    
    
    if(not(isinstance(lowBound, int) and isinstance(highBound, int))):
        return ERROR_VALUE
    if (lowBound <= LOWER_BOUND):
        return ERROR_VALUE
    if (highBound > UPPER_BOUND):
        return ERROR_VALUE
    if (lowBound > highBound):
        return ERROR_VALUE
    
    result = []
    
    for i in range(lowBound, highBound+1):
        if (i < 6):
            if i == 4:
                continue
            result.append(i)
            continue
        upperSearch = i//2
        for j in range(2, upperSearch):
            if i % j == 0:
                break
        else:
            result.append(i)
                
            
    return result
     
    