def outer(a,b):
    
    def add(a,b):
        sum = a+b
        return sum
    
    result = add(a,b)
    result=result+5
    return result