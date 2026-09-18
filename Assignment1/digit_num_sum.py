a = int(input("Enter a number"))
sum =0
while a>0: 
   num = a %10
   sum+=num
   a//= 10
print(sum)