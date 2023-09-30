def catalan_numbers(upper_limit: int)-> "list[int]":
    if upper_limit<0:
        raise ValueError("Limit for the Catalan sequence must be $\leq$ 0")
    catalan_list=[0]*(upper_limit+1)
    catalan_list[0]=1
    if upper_limit>0:
        catalan_list[1]=1
    for i in range(2, upper_limit+1):
        for j in range(i):
            catalan_list[i]+=catalan_list[j]*catalan_list[i-j-1]
    return catalan_list

if __name__=="__main__":
    try:
        while True:
            N=int(input().strip())
            if N<0:
                print("Fail!")
                break
            else:
                print(catalan_numbers(N))
    except (NameError, ValueError):
        print("Fail!")
    import doctest
    doctest.testmod()
    
                