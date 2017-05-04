import math
A = [-1000,1000]
s = sum(A)-A[0]
print("s =",s)
s1 = A[0]
print("s1 =",s1)
min = abs(s - s1)
print("min =",min)
for i in range(1,len(A)):
  
  s1 = s1 + A[i]
  print("s1` = ",s1)
  s = s - A[i]
  print("s` = ", s)
  if abs(s - s1) < min:
    min = abs(s - s1)
print(min) 