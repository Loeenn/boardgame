f = open('24.txt', 'r')
l = [line.strip() for line in f]
a=''
for i in range(len(l)):
    a+=l[i]
k=0
b=[]
for i in range(2,len(a),2):
    if a[i]!= a[i-1] and a[i]!=a[i-2]:
        k+=1
    else:
        b.append(k)
        k=0

print(b)
print(max(b))