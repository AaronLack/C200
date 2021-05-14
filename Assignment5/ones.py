def lr(xlst):
    maxCount = 0
    count = 0
    for i in xlst:
        if i == 1:
            count += 1
        else:
            count = 0
        if count > maxCount:
            maxCount +=1
    return maxCount
            

x = [0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0]
print(lr(x))


if __name__=="main":
    pass 