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
            if e > pivot: S_great.append(e)
            elif e < pivot: S_less.append(e)
            else:
                S_eq.append(e)
        #recursive call for conditions.
        if k <= len(S_less): return randselect(S_less,k)
        else:
            if k<=len(S_less)+len(S_eq): return pivot
            else : return randselect(S_great,k-len(S_less)-len(S_eq))

fi = open("./input.txt","r") # open the file "input.txt".
fo = open("./output.txt","w") # open the file "output.txt".
l = fi.readlines()

num = int(l[0]) # number of test cases.
fo.writelines(str(num)+"\n") # first line of "output.txt".
runtimes=[] # list for runtimes.

for i in range(1,2*num+1,2):    # 1 to 2n+1 with step of 2.
    l1=l[i].split()             #first line of each test cases.
    insize=int(l1[0])           #first element of first line = input size.
    inx=int(l1[1])              #second element of first line = index.
    S=l[i+1].split()            #second line of each test cases = input sequence.
    for j in range(len(S)):
        S[j]=int(S[j])          # cast string to int for every element of S.

    t1=time.time()
    elem=randselect(S,inx)
    t2=time.time()
    runtime = t2-t1             # calculate runtime using difference between time before function call and after function call.
    runtimes.append(runtime/insize) # normalized runtime for input size.

    fo.writelines([str(elem)+" ",str(insize)+" ",str(runtime)+" ","\n"])

#find constant c for O(n). average of normalized runtime.
sum = 0
for runtime in runtimes:
    sum = sum+runtime
C=sum/len(runtimes) # asked constant. (proportional constant for O(n))
fo.writelines(str(C))

fi.close()
fo.close()
