def coordinates(in_str:str):
    delimiter=in_str.find(",")
    if in_str[:delimiter].isnumeric and in_str[delimiter+1:].isnumeric:
        return int(in_str[:delimiter]), int(in_str[delimiter+1:])
    else:
        return None
    
test="1,34"
x,y=coordinates(test)
print(x,y)