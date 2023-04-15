T=int(input())
for t in range(T):
    D=[0 for i in range(26)]
    temp=input()
    D=temp.split(' ')
    N=int(input())
    S=["" for i in range(N)]
    for i in range(N):
        S[i]="".join([str(D[ord(c)-65]) for c in input()])
    if(len(S)==len(set(S))):
        print("Case #"+str(t+1)+": NO")
    else:
        print("Case #"+str(t+1)+": YES")
