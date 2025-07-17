number=int (input("Input a number"))
sum=0
for i in range(1, number+1):
    sum=sum+i
    print("/n The result is",sum)

string=input("Enter a word")
string2=(" ")
for i in string:
    string2=i+string2
    print("/n The original word is ",string)
    print("/n The reversed word is ",string2)

num=int (input("Enter a number"))
print("Numbers from 5-1" .format(num,1))
for i in range(num,0,-1):
    print(i)