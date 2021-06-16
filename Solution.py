n=int(input())
i=0
count=0
while(2**i<=n):
    count=2**i
    i+=1
print(2*(n-count)+1)