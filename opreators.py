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
rev=321d
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








# a=input("enter the word : ")
# i=0
# l=len(a)
# for i in (a):
#     if i%2==0:
#       print(i)




# list

# l=[1,2,10,30,2,'abcd']
# print(l[0])
# print(l[1])

# if 10 in l:
#     print('available')
# else:
#     print('not available')



# if 20 in l:
#     print('available')
# else:
#     print('not available')


# for i in l:
#     print(i)




# updation of the list

# l[0]=22
# print(l)




# # append
# l=[]
# l.append(10)
# print(l)

# l.append('shahid')
# print(l)

# l.append([10,20,'abc'])
# print(l)

# l.append(10,)
# print(l)


# # extend

# l.extend([100,200,300])
# print(l)

# # insert

# l.insert(2,'don')
# print(l)


# delete

# clear

# l=[10,20,30]
# l.clear()
# print(l)


# pop()

# l.pop()
# # print(l)

# pop Index

# l.pop(1)
# print(l)


# remove

# l.remove(30)
# print(l)





# l=[10,20,30,8,5,6,]
# # # print(l.index(6))
# # # print(l.count(20))
# # print(l)

# l.sort()
# # print(l)


# l.reverse()
# print(l)



# sum of the listed items (int and float)

# l=[1,10,12,'abc',8.5]
# s=0
# for i in l:
#     if type(i)==int or type(i)==float:
#         s+=i
# print(s)




# sum of odd and even numbers of a list

# l=[10,1,2,3,5,8,6]
# even=0
# odd=0
# for i in l:
#      if i%2==0:
#           even+=i
#      else:
#           odd+=i  
# print(even)
# print(odd)





# remove the duplicates the value

# using set

# l=[10,1,2,3,5,8,6,1,3,5]
# s=set(l)
# l=list(s)                           
# print(l)


# using in /not in

# l=[10,1,2,3,5,8,6,1,3,5]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)


# using count and remove

# l=[10,1,2,3,5,8,6,1,3,5]
# for i in l:
#     if l.count(i)>=2:
#         l.remove(i)
# print(l)


# l=[10,1,2,3,5,8,6,1,3,5]
# largest=[]
# for i in l:
#      if i>largest:
#           print(l)
          


# checking palindrome

# l=['malayalam','apple','amma','python']
# for i in l:
#     rev=i[::-1]
#     if rev==i:
#         print(rev,'its palindrome')
#     else:
#         print(rev,'its not palindrome')




# list of numbers divisible by 3

# l=[1,2,5,8,9,3,12]
# for i in l:
#     if i%3==0:
#         print(i,'divisible')
#     else:
#         print(i,'not divisible')



# <----------choice------------>

# while True:
#     print('''
# 1.add
# 2.sub
# 3.mul
# 4.div
# 5.exit
#           ''')
    
#     choice=int(input("enter your choice :"))
#     if choice==1:
#         a=int(input("enter first no :"))
#         b=int(input("enter second no :"))
#         c=a+b
#         print(c)
#     elif choice==2:
#         a=int(input("enter first no :"))
#         b=int(input("enter second no :"))
#         c=a-b
#         print(c)
#     elif choice==3:
#         a=int(input("enter first no :"))
#         b=int(input("enter second no :"))
#         c=a*b
#         print(c)
#     elif choice==4:
#         a=int(input("enter first no :"))
#         b=int(input("enter second no"))
#         c=a/b
#         print(c)
#     elif choice==5:
#         break
#     else:
#         print("invalid choice")



# student details and choices

# std=[]
# while True:
#  print('''
# 1.student details
# 2.view std details
# 3.upadte std details
# 4.delete std details
# 5.exit
#           ''')
 
#  choice=int(input("enter your choice :"))
#  if choice==1:
#          name=str(input("enter name :"))
#          age=int(input("enter age :"))
#          mark=int(input("enter mark :"))
#          std.append([name,age,mark])
#  elif choice==2:
#       for i in std:
#            print(i)
#  elif choice==3:
#       name=str(input("enter name :"))
#       f=0
#       for i in std:
#            if name in i:
#              mark=int(input("enter mark :"))
#              i[2]=mark
#              f=1
#       if f==0:
#                print('invalid name')
#  elif choice==4:
#       name=str(input("enter name :"))
#       f=0
#       for i in std:
#            if name in i:
#                 std.remove(i)
#                 f=1
#       if f==0:
#            print('invalid name')
#  elif choice==5:
#      break
#  else:
#      print('invalid choice')

      

# employ details

# employ=[['shahid',100,25,'mumbai',100000000,'ceo',10]]
# import datetime
# while True:
#     print('''
# 1.register
# 2.view
# 3.update
# 4.delete
# 5.add work
# 6.search
# 7.exit
#           ''')
    
#     choice=int(input("enter your choice :"))
#     if choice==1:
#          name=str(input("enter name :"))
#          id=int(input("enter id :"))
#          age=int(input("enter age :"))
#          place=str(input("enter place :"))
#          salary=int(input("enter salary :"))
#          position=str(input("enter position :"))
#          experiance=int(input("enter experiance :"))
#          employ.append([name,id,age,place,salary,position,experiance])
#     elif choice==2:
#          for i in employ:
#               print(i)
#     elif choice==3:
#          name=str(input("enter name :"))
#          f=0
#          for i in employ:
#               if name in i:
#                    choice=int(input("enter your choice :"))
#                    if choice==1:
#                         age=int(input("enter age :"))
#                         i[2]=age
#                    elif choice==2:
#                         place=str(input("enter place :"))
#                         i[3]=place
#                    elif choice==3:
#                         salary=int(input("enter salary :"))
#                         i[4]=salary
#                    elif choice==4:
#                         position=str(input("enter position :"))
#                         i[5]=position
#                    elif choice==5:
#                         experiance=int(input("enter experiance :"))
#                         i[6]=experiance
#                    f=1           
#          if f==0:
#               print('invalid name') 
#     elif choice==4:
#          name=str(input("enter name :"))
#          f=0
#          for i in employ:
#               if name in i:
#                    employ.remove(i)
#                    f=1
#          if f==0:
#               print('invalid name')
#     elif choice==5:
#           id=int(input("enter id :"))
#           for i in employ:
#                if id in i:
#                     task=input("enter task :")
#                     date=datetime.datetime.now().strftime('%x')
#                     i.append([task,date])
#                     print(i)
#     elif choice==6:
#          name=str(input("enter name :"))
#          f=0
#          for i in employ:
#               if name in i:
#                    print(i)
#                    f=1
#          if f==0:
#               print('invalid name')         
#     elif choice==7:
#          break
#     else :
#          print('invalid choice')


# tuple

# t=(10,20,30,)
# print(t)

# t1=(1)
# print(t1)

# t2=('abc',)
# t3=(1,)
# print(t3)

# t=10,11,12
# print(t)



# list in tuple

# t=(10,[1,2,3,4],12)
# # print(t[1])
# t[1].append(5)
# print(t)

# modifing tuple 

# t=(1,2,3)
# l=list(t)
# # print(l)
# l.pop()
# # print(l)
# t=tuple(l)
# print(t)



# t=(1,2,3)
# l=list(t)
# # print(l)
# l.append(5)
# # print(l)
# t=tuple(l)
# print(t)


# finding the position and count of the tuple

# t=(1,2,3,4,1,2,3,5,3,6)
# a=int(input("enter the value :"))
# c=t.count(a)
# print(c)
# pos=0
# while c>0:
#     p=t.index(a,pos)
#     pos=p+1
#     print('index:',p)
#     c-=1




# Dictionary

# d={'name':'shahid','age':20,'place':'kottayam',}
# print(d)
# print(d['name'])
# print(d['age'])
# print(d['place'])

# for i in d:
#     print(i,d[i])

#update value 

# d['age']=22
# print(d)


# add new Key

# d['mark']=82
# print(d)

# for i in d:
#     print(i,d[i])


# for checking the values

# if d['name']=='shahid':
#     print('true')
# else:
#     print('false')

# print(d.get('name'))
# print(d.items())
# print(d.values())
# for i in d.values ():
#     print(i)
# print(d.keys())

# a=d
# a=d.copy()
# print(id(a))
# print(id(d))
# d['mark']=45
# print(a)
# print(d)

# # d.pop('place')
# # d.popitem()
# d.setdefault('exp')
# l=[10,11,12]
# print(d.fromkeys(l))



# d={}
# name=str(input("enter name :"))
# age=int(input("enter age :"))
# place=str(input("enter place :"))

# d['name']=name
# d['age']=age
# d['place']=place

# print(d)



# shop=[{'pname': 'box', 'id': 101, 'stock': 300, 'price': 100},{'pname': 'pen', 'id': 103, 'stock': 200, 'price': 10}]
# while True:
#     print('''
# 1.product details
# 2.view the product 
# 3.update the product 
# 4.delet the product
# 5.exit
#           ''')
#     choice=int(input("enter the number :"))
#     if choice==1:
#           pname=str(input("enter name :"))
#           id=int(input("enter id :"))
#           stock=int(input("enter stock :"))
#           price=int(input("enter price :"))
#           shop.append({'pname':name,'id':id,'stock':stock,'price':price})
#     elif choice==2:
#          for i in shop:
#               print(i)
#     elif choice==3:
#              name=str(input("enter name :"))
#              f=0
#              for i in shop:
#                    if name == i['pname']:
#                          print('''
# 1.upadte stock
# 2.upadte price
#                                ''')
#                          choice=int(input("enter your choice :"))
#                          if choice==1:
#                                stock=int(input("enter stock :"))
#                                i['stock']=stock
#                          elif choice==2:
#                                price=int(input("enter price :"))
#                                i['price']=price
#                                f=1
#              if f==0:
#                    print('invalid name') 
#     elif choice==4:
#            name=str(input("enter name :"))
#            f=0
#            for i in shop:
#                  if name == i['pname']:
#                        shop.remove(i)
#                        f=1
#            if f==0:
#                  print('invalid name')
#     elif choice==5:
#           break
#     else:
#           print('invalid choice')





# lib=[{'bname': 'Wuthering Heights', 'id': 101, 'stock': 300, 'price': 500},{'bname': 'Sherlock Holmes', 'id': 102, 'stock': 200, 'price': 600},{'bname': 'goatlife', 'id': 103, 'stock': 200, 'price': 800}]
# while True:
#     print('''
# 1.book details
# 2.view the details 
# 3.update the product 
# 4.delet the product
# 5.search product
# 6.exit
#           ''')
#     choice=int(input("enter the number :"))
#     if choice==1:
#           bname=str(input("enter name :"))
#           id=int(input("enter id :"))
#           stock=int(input("enter stock :"))
#           price=int(input("enter price :"))
#           lib.append({'bname':name,'id':id,'stock':stock,'price':price})
#     elif choice==2:
#          for i in lib:
#               print(i)
#     elif choice==3:
#              name=str(input("enter name :"))
#              f=0
#              for i in lib:
#                   if name == i['bname']:
#                         print('''
# 1.upadte stock
# 2.upadte price
#                                ''')
#                         choice=int(input("enter your choice :"))
#                         if choice==1:
#                               stock=int(input("enter stock :"))
#                               i['stock']=stock
#                         elif choice==2:
#                               price=int(input("enter price :"))
#                               i['price']=price
#                               f=1
#                               if f==0:
#                                     print('invalid name') 
#     elif choice==4:
#       name=str(input("enter name :"))
#       f=0
#       for i in lib:
#             if name == i['bname']:
#                   lib.remove(i)
#                   f=1
#                   if f==0:
#                         print('invalid name')
#     elif choice==5:
#       name=str(input("enter name :"))
#       f=0
#       for i in lib:
#             if name== i['bname']:
#                   print(i)
#                   f=1
#                   if f==0:
#                         print('invalid name')
#     elif choice==6:
#           break
#     else:
#           print('invalid choice')





# data=[{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':45}]
# print('{:<10} {:<10}'.format("name","age"))
# print('-'*20)
# for i in data:
#        if i['age']<=30:
#               print('{:<10} {:<10}'.format(i["name"],i["age"]))
#        elif i['age']>30:
#               print('{:<10} {:<10}'.format("name","age"))
#               print('-'*20)




# data=[{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':45}]
# a=[]
# b=[]
# for i in data:
#     if i['age']>30:
#         a.append(i)
#     else:
#         b.append(i)
# print(a)
# print(b)



# data=[{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':45}]
# b=[i for i in data if i['age']>30]
# a=[i for i in data if i['age']<=30]
# print(a)
# print(b)


# odd or even using 

# l=[1,2,3,4,5,6,7,8,9,10]
# o=[i for i in l if i%2!=0]
# e=[i for i in l if i%2==0]
# print(o)
# print(e)



# convert value to digit 

# dict={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# num=int(input("enter the number :"))
# s=''
# while num>0:
#     d=num%10
#     s=dict[d]+' '+s
#     num//=10
# print(s)




# l=[{'name':'a','age':20,'project':['ems','sms']}]
# a=str(input("enter the word :"))
# for i in l:
#     i['project'].append(a)
#     print(i)


# set

# s={1,2,3,4,'abc',8.5,7,1}

# # for i in s:
# #     print(i)
 
# # if 7 in s:
# #     print('true')
# # else:
# #     print('false')

# print(s)

# remove duplicate values from list using set

# l=[1,2,3,4,1,2,3,5]
# s=set(l)
# print(s)
# l=list(s)
# print(l)


# for add a value to an empty set

# s=set()   [for creating an empty set]
# s=set() 
# s.add(10)
# print(s)

# for deleting a unknown value from set

# s={10,11,12}
# s.pop()
# print(s)

# s.discard(12)
# print(s)

# remove the  specific value

# s.remove(12)
# print(s)




s={1,2,3,4,5,6}
s1={1,2,3,6}
# print(s1.difference(s))
# print(s.union(s1))
# print(s.intersection(s1))
# print(s.symmetric_difference(s1))
s2={6,7,8,9}
# print(s.isdisjoint(s2))
# print(s.issubset(s2))
# print(s.issuperset(s2))
# s.update({10,11,12})
# print(s)
s.different_update(s2)
print(s)