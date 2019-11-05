# program to count the consecutive zeros between the 1's of any integer binary form

def solution(N):
    binaryDone = True
    nums = []
    # to generate the binary number from integer
    while binaryDone:
        d = N%2
        nums.append(d)
        if N > 1:
            N = int(N / 2)
        else:
            binaryDone = False
    nums.reverse()
    #print(nums)
    startIndex = endIndex = False
    finalCount = 0
    for k,num in enumerate(nums):
        #print(num)
        if num == 1: #modify the start and endpoint depends on current digit
            if startIndex == False:
                startIndex = True
                endIndex = False
                gapCount = 0
            elif startIndex == True:
                endIndex = True
                startIndex = False
           
        if endIndex == True: #update the max gap if endpoint reached
            #print('count', gapCount)
            if finalCount < gapCount:
                finalCount = gapCount
                gapCount = 0
            endIndex = False
            startIndex = True
                
        if num == 0: #eligible to count the gap
            if startIndex == True:
                #print('counting..')
                gapCount+=1         #count the gap
    return finalCount
    pass

d = solution(805306373)
print(d)