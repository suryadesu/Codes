def printCountRec(dist): 
    if dist < 0: 
        return 0   
    if dist == 0: 
        return 1
    return (printCountRec(dist-1) +
            printCountRec(dist-2) +
            printCountRec(dist-3)) 
#best use dp .
dist = 10
print(printCountRec(dist)) 
