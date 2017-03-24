#Team Number : 47
#Student ID : 20150262 20150326
#homework number : 3
#homework file : problem2.py
import random
import time

def randselect(S,k):
    if len(S)==1: return S[0]
    else:
        p=random.randrange(len(S))  #pick a random element 'pivot' using random integer index.
        pivot = S[p]
        S_great=[]
        S_less=[]
        S_eq=[]
        # S split into 3 subsequences.
        for e in S:
            if e > pivot:
                S_great.append(e)
            elif e < pivot:
                S_less.append(e)
            else:
                S_eq.append(e)
        #recursive call for conditions.
        if k <= len(S_less):
            return randselect(S_less,k)
        else:
            if k<=len(S_less)+len(S_eq):
                return pivot
            else:
                return randselect(S_great,k-len(S_less)-len(S_eq))

def cntcomps_randselect(S,k): #function for count the number of comparisons of randselect.
    cnt=0
    if len(S)==1: return cnt
    else:
        p=random.randrange(len(S))
        pivot = S[p]
        S_great=[]
        S_less=[]
        S_eq=[]
        for e in S:
            if e > pivot:
                cnt +=1
                S_great.append(e)
            elif e < pivot:
                cnt+=1
                S_less.append(e)
            else:
                cnt+=1
                S_eq.append(e)
        if k <= len(S_less):
            cnt+=cntcomps_randselect(S_less,k)
        else:
            if k<=len(S_less)+len(S_eq):
                cnt+=1
            else:
                cnt+=cntcomps_randselect(S_great,k-len(S_less)-len(S_eq))
        return cnt

fi = open("./input.txt","r") # open the file "input.txt".
fo = open("./output.txt","w") # open the file "output.txt".
l = fi.readlines()

num = int(l[0]) # number of test cases.
fo.writelines(str(num)+"\n") # first line of "output.txt".
C=[] # list for asked constant.

for i in range(1,2*num+1,2):    # 1 to 2n+1 with step of 2.
    l1=l[i].split()             #first line of each test cases.
    insize=int(l1[0])           #first element of first line = input size.
    inx=int(l1[1])              #second element of first line = index.
    S=l[i+1].split()            #second line of each test cases = input sequence.
    for j in range(len(S)):
        S[j]=int(S[j]) # cast string to int for every element of S.

    t1=time.time()
    elem=randselect(S,inx)
    t2=time.time()
    runtime = t2-t1 # calculate runtime using difference between time before function call and after function call.

    comps=cntcomps_randselect(S,inx) #count number of comparisons.
    C.append(comps/float(insize)) # comps/insize = C (asked constant)

    fo.writelines([str(elem)+" ",str(insize)+" ",str(runtime)+" ","\n"])

#Find asked constant Const for O(n) by average of each testcase's constant.
#In fact, 'randselect' is randomized selection algorithm, so we need many samples for determine asked constant.
#But, in this problem, we assume that average of constants is asked constant.
#If there are many samples, we can get more exact constant.
sum = 0
for c in C:
    sum = sum+c
Const=sum/len(C) # asked constant. (proportional constant for O(n))
fo.writelines(str(Const)) # last line of "output.txt".

fi.close()
fo.close()
