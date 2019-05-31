s=list(map(str,input())
t=""
for i in range(0,len(s)-1,2):
t=s[i]
s[i]=s[i+1]
s[i+1]=t
for i in rangr(0,len(s)):
print(s[i],end"")
