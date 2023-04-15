T=int(input())
for t in range(T):
    N=int(input())
    S=input().split(' ')[:N]
    i=0
    while(i<N-1):
        if(S[i]==S[i+1]):
            del S[i+1]
            N-=1
        else:
            i+=1
        #print(N,len(S))
    if(len(S)==len(set(S))):
        print("Case #"+str(t+1)+": "+" ".join(S))
    else:
        print("Case #"+str(t+1)+": IMPOSSIBLE")
