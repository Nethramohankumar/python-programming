start=int(input())
end=int(input())
for num in range(start,end+1):
if(num>1):
for n in range(2,num):
if(num%n)==0:
break
else:
print(num,end=" ")
