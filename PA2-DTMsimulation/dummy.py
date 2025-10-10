def replace(in_str,index,char):
    return in_str[:index]+char+in_str[index+1:]

# Testing
if __name__ == "__main__":
    test = "b010"
    for i in range(4):
        print(replace(test,i,"x"))