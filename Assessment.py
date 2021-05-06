#Question1
a={6,7,8,9,10}
b={5,6,7,8,9}
a.add(4)
b.add(3)

print(a)
print(b)
c=a.union(b)
print(c)

c=a.difference(b)
print(c)
d=b.difference(a)
print(d)

c=a.intersection(b)
print(c)

#Question2
lst= [11, 100, 99, 1000, 999,99]
lst.insert(0,-1)
print(lst)

print(lst[1])
print(lst[-1])

count=0
for number in lst:
    if number==99:
        count+=1;
print(count)

sum=0
for num in lst:
    sum+=num
print(sum)

least_num=lst[0]
for nums in lst:
    if nums<least_num:
        least_num==nums
print(least_num)


#Question3
for year in range(2020,2070):
    if year%4==0:
        print(year)

#Question4
for number in range(1000,2000):
     if number%7==0 and number%5!=0:
         print(number)

#Question5
#Write a program to print counting from 1 to 10
for num in range(1,11):
    print(num)

#Question6
for number in range(30,50):
    if number%2!=0:
        print(number)
        
#Question7
x=[]
for number in range(100,200):
    if number%7==0:
        x.append(number)
print(x)


#Question8
for number in range(1,50):
    if number%3==0 and number%5==0:
        print("PurpleWhite")
    elif number %3==0:
        print("Purple")
    elif number%5==0:
        print("White")
    else:
        print(number)

