'''  +=
-=
*=
/=
%=
//==
** = '''


# print(20+30)
# print('shahid '+'thaha')
# print(20-30)
# print(20*30)
# print(20/30)
# print(30/5)

# print(30%8)

# print(30//5)

# print(10**2)

# a=10
# # print(a)

# # a=a+5
# a+=5
# print(a)

# # b=a-5
# a-=5
# print(a)

# # a=a*2
# a*=2
# print(a)

# # a=a/2
# a/=2
# print(a)


# ==
# >
# <
# >=
# <=

# print(10==10)
# print(10==12)
# print(10>11)
# print(10<12)
# print(10>=5)
# print(10<=5)



# and
# or
# not

# and

# print(True and True)
# print(10==10)

# print(True and False)
# print(10>12)

# print(True and False )
# print(10==10 and 10<8 )

# print(False and False)
# print(10!=10)


# or


# print(True or True)
# print(10==10)

# print(True or False)
# print(10>11 or 10<11)

# print(True or False )
# print(10==10 or 10<8 )

# print(False or False)
# print(10!=10 or 10>20)


# not

# print(not(True))
# print(not(10>9))

# print(not(False))
# print(not(10<1))


# in
# not in

# print('t' not in 'python')
# print('i' not in  'python')


# is 
# is not

# a=10
# b=10
# print(a is b)
# print(a is not b)


# Name=(input("enter name : "))
# age=int(input ("enter age : "))
# weight=float(input("enter weight :"))
# print("name :" ,Name)
# print("age :", age)
# print("weight :", weight)




# if condition:
#     statment

# if 10==11:
#     print('equal')
# else:
#     print('not equal')

# a=int(input("enter first number :"))
# b=int(input("enter second number :"))
# if a==b:
#     print('equal')
# else:
#     print('not equal')



# a=int(input("enter first number :"))
# b=int(input("enter second number :"))
# if a>b:
#     print('a is largest')
# else:
#     print('b is largest')



# a=int(input(" enter the salary : "))
# b=int(input(" year of service : "))
# if b>=5:
#     print(a*0.05)
# else:
#     print('no bonus')



# a=int(input(" enter the number :"))
# d=a%10
# if d%3==0:
#     print('number is divisible')
# else:
#     print('not divisible' )



# a=30
# b=30
# if a==b:3
#     print('equal')
# elif a>b:
#     print(a)
# else:
#     print(b)


# a=int(input("enter a number :"))
# if a==1:
#     print('sunday')
# elif a==2:
#     print('monday')
# elif a==3:
#     print('tuesday')
# elif a==4:
#     print('wednesday')
# elif a==5:
#     print('thursday')
# elif a==6:
#     print('friday')
# elif a==7:
#     print('saturday')
# else:
#     print('invalid')


# a=input("enter the city : ")

# if a=='delhi':
#     print('red fort')
# elif a=='agra':
#     print('taj mahal')
# elif a=='jaipur':
#     print('jal mahal')
# else:
#     print('not found')


# a=int(input("enter the bike price : "))

# if a>100000:
#     print(a*0.15)
# elif a>50000 and a<=100000:
#     print(a*0.10)
# else:
#     print(a*0.05)



# a=int(input("enter the unit : "))

# if a<=100:
#     print('no charge')
# elif a>100 and a<=200:
#     print((a-100)*5)
# elif a>=200:
#     print((a-200)*10+500)
# else:
#     print('invalid')


# while condition:
#     statment
#     increment/decrement


# i=1
# while i<=10:
#     print(i)
#     i+=1


# a=int(input("enter the fisrt number :" ))
# b=int(input("enter the second number :"))
# c=0
# while a<=b:
#     c+=a 
#     a+=1
# print(c)



# a=int(input("enter the first number :"))
# b=int(input("enter the last number :"))
# c=0
# while a<=b:
#     if a%2!=0:
#         c+=a
#     a+=1
# print(c)


# c=0
# while a<=b:
#     if a%2!=0:
#         c+=a
#     a+=1
# print(c)




# i=1
# a=int(input("enter the number :" ))
# while i<=10:
#     print(i,'*',a,'=',a*i)
#     i+=1



# i=1
# a=int(input("enter a number :"))
# s=1
# while i<=a:
#       s*=i
#       i+=1
# print(s)





# a=int(input("enter the number : "))
# rev=0
# while a>0:
#     d=a%10
#     rev=rev*10+d
#     a//=10
# print(rev)


''''
a=123
rev=0
d=3
rev=rev*10+d
rev= 0*10+3
rev=3
a=12
------------
a=12
rev=3
d=2
rev=rev*10+d
rev= 3*10+2
rev=32
a=1
-------------
a=1
rev=32
d=1
rev=rev*10+d
rev= 32*10+1
rev=321
a=0
'''



# a=int(input("enter the number :"))
# rev=0
# while a>0:
#     d=a%10
#     rev=rev*10+d
#     a//=10
# print(rev)


# a=input("enter the word : ")
# rev=""
# i=0
# l=len(a)
# while i<l:
#     # print(a[i])
#     rev=(a[i])+rev
#     i+=1
# print(rev)



# forloop
# for iteration_var in iterables:
#     stm 



# range()
# list
# tuple
# set
# dict
# str

# (range(limit))
# for i in range(10):
#     print(i)

# # range(start,end)
# for i in range(2,11):
#     print(i)


# range(start,end,updation)
# for i in range(2,11,2):
#     print(i)


# a="python"
# for i in a:
#     print(i)




# sum of 2 numbers

# a=int(input("enter first number : "))
# b=int(input("enter second numbre : "))
# s=0
# for i in range(a,b+1):
#     s+=i
# print(s)



# odd number 

# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# for i in range(a,b+1):
#     if i%2!=0:
#         print(i)




# sum of odd numbers

# a=int(input("enter first number : "))
# b=int(input("enter another number : "))
# s=0
# for i in range(a,b+1):
#     if i%2!=0:
#         s+=i
# print(s)


# multiplication of numbers

# a=int(input("enter a number : "))
# for i in range(1,11):
#     print(i,'*',a,'=',a*i)





# factorial of number

# a=int(input("enter a number : "))
# s=1
# for i in range(1,a+1):
#     s*=i
# print(s)



# reverse of a string

# a=input("enter the word : ")
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)





# loop control statments


# break

# for i in range(10):
#     print(i)
#     if i==5:
#       break



# continue

# for i in range(10):
#     if i==5:
#      print(" is the value")
#      continue
#     print(i)        


# pass

# for i in range(10):
#     pass



# reverse of a number

# a=int(input("enter a number : "))
# rev=0
# for i in range(a):
#     d=a%10
#     rev=rev*10+d
#     a//=10
#     if a==0:
#         break
# print(rev)

# a=input("enter a word : ")
# l=len(a)
# for i in a:
#     if a[i]%2==0:
#         print()








a=input("enter the word : ")
i=0
l=len(a)
for i in (a):
    if i%2==0:
      print(i)