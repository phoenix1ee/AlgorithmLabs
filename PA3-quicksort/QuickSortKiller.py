def median_of_three_killer(n):
    output = [0]*n
    output[0]=1
    output[-1] = 2
    i=3
    while i<n:
        if i%2>0:
            output[i-1]=i
        else:
            output[i-3]=i
        i+=1
    if i%2>0:
        output[i - 2] = i
    else:
        output[i - 3] = i
    return output
# Example usage:
sample = (median_of_three_killer(20))
print(sample)
