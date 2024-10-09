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

# a=input("enter the word : ")
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)





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




# s={1,2,3,4,5,6}
# s1={1,2,3,6}
# # print(s1.difference(s))
# # print(s.union(s1))
# # print(s.intersection(s1))
# # print(s.symmetric_difference(s1))
# s2={6,7,8,9}
# # print(s.isdisjoint(s2))
# # print(s.issubset(s2))
# # print(s.issuperset(s2))
# # s.update({10,11,12})
# # print(s)
# s.different_update(s2)
# print(s)

# set program

# s=set()
# a=int(input("enter the limit :"))
# for i in range(a) : 
#     name=str(input("enter the name :"))
#     s.add(name)
#     print(s)



# php=set()
# java=set()
# python=set()
# a=int(input("enter the limit :"))
# for i in range(a) : 
#     name=str(input("enter the name :"))
#     php.add(name)
#     java.add(name)
#     python.add(name)
#     print(php)
#     print(java)
#     print(python)




# php=set()
# java=set()
# python=set()


# php={'a','b','c'}
# a=int(input("enter the limit :"))
# for i in range(a) : 
#     name=str(input("enter the name :"))
#     php.add(name)
#     print(php)

# java=set('a','d','c','e')
# a=int(input("enter the limit :"))
# for i in range(a) : 
#     name=str(input("enter the name :"))
#     java.add(name)
#     print(java)

# python=set()
# a=int(input("enter the limit :"))
# for i in range(a) : 
#     name=str(input("enter the name :"))
#     python.add(name)
#     print(python)


# set of program using method

# php={'a','b','c'}
# java={'a','b','d','e'}
# python={'a','b','c','f','g'}
# s=php.difference(java).difference(python)
# s1=java.difference(php).difference(python)
# s2=python.difference(java).difference(php)
# # print(s)
# # print(s1)
# # print(s2)
# f=s.union(s1).union(s2)
# print(f)


# function

# def new():
#     print('welcome')
#     print('morning')
#     print('night')
# new()
# a=[1,2,3,4,5,6]
# print(a)
# a.append(10)
# new()
# a=[1,2,3,4,5,6]
# print(a)
# a.append(10)
# new()



# function variables

# def new():
#     b=10       #local variable
#     print('inside the function a=',a)
#     print('inside the function b=',b)
# a=20            #global variable
# new()
# print('outside the function a=',a)
# print('outside the function a=',b)

# def new():
#     a=10       #local variable
#     print('inside the function a=',a)
# a=20            #global variable
# new()
# print('outside the function a=',a)

# return

# def sample():
#     a=10
#     b=20
#     return 'welcome',a,b
# # print(sample())
# c,a1,b1=sample()
# print(a1)
# print(b1)
# print(c)

# calculator using function


# def number():
#     a=int(input("enter no :"))
#     b=int(input("enter no :"))
#     return a,b

# while True:
#     print('''
# 1.addition
# 2.substraction
# 3.multiplication
# 4.division
# 5.floor division
# 6.modules
# 7.exponenet
# 8.exit    
#     ''')

#     choice=int(input("enter the choice :"))
#     if choice==1:
#         a,b=number()
#         print(a+b)
#     elif choice==2:
#         a,b=number()
#         print(a-b)
#     elif choice==3:
#         a,b=number()
#         print(a*b)
#     elif choice==4:
#         a,b=number()
#         print(a/b)
#     elif choice==5:
#         a,b=number()
#         print(a//b)
#     elif choice==6:
#         a,b=nuber()
#         print(a%b)
#     elif choice==7:
#         a,b=number()
#         print(a**b)
#     elif choice==8:
#         break
#     else:
#         print('invalid')



# def sample():
#     print(a,b)
# sample(10,20)


# def sample(name='sha',age=20):
#     print(name,age)

# sample('sh',22)
# sample(age=30)
# sample('njn',33)


# def sample(*a):
#     print(a)

# sample()
# sample('hellooo','hi')
# sample('helo','welcome',10,2,0,)


# def sample(**a):
#     print(a)

# sample()
# sample(name='shahid',age=20)







# emp=[]
# def login():
#     uname=input("enter uname :")
#     passw=input("enter passw :")
#     f=0
#     user=''
#     if uname == 'admin' and passw == 'admin':
#         f=1
#     for i in emp:
#         if uname.isdigit():
#             uname=int(uname)
#             if uname==i['id'] and passw==i['password']:
#                 f=2
#                 user=i
#     return f,user
# def add_emp():
#     id=int(input("enter the id :"))
#     f1=0
#     for i in emp:
#         if i['id']==id:
#             f1=1
#             add_emp()
#     if f1==0:
#         name=str(input("enter the name :"))
#         salary=int(input("enter salary :"))
#         dob=str(input("enter dob :"))
#         position=str(input("enter the position :"))
#         password=dob
#         emp.append({'id':id,'name':name,'salary':salary,'dob':dob,'position':position,'password':password})
# def view_emp():
#     id=int(input("enter the id :"))
#     f1=0
#     for i in emp:
#         print(i)
#     if f1==0:
#         print('invalid id')
# def update_emp():
#     id=int(input("enter the id :"))
#     f1=0
#     for i in emp:
#         if i['id']==id:
#             f1=1
#             salary=int(input("enter the salary :"))
#             position=str(input("enter position :"))
#             i['salary']=salary
#             i['position']=position
#     if f1==0:
#         print('invalid id')
# def delete_emp():
#     id=int(input("enter the id :"))
#     f1=0
#     for i in emp:
#         if i['id']==id:
#             f1=1
#             emp.remove(i)
#     if f1==0:
#         print('invalid id')

# def profile(user):
#     print(user)
# def pro_update(user):
#     name=str(input("enter the name :"))
#     dob=str(input("enter dob :"))
#     user['name']=name
#     user['dob']=dob

# while True:
#     print('''
# 1.login
# 2.exit    
#     ''')
#     choice=int(input("enter the choice :"))
#     if choice==1:
#         f,user=login()
#         if f==1:
#             while True:
#                 print('''
#                 1.add employ
#                 2.view 
#                 3.update 
#                 4.delete
#                 5.logout''')

#                 sub_choice=int(input("enter the choice :"))
#                 if sub_choice==1:
#                     add_emp()
#                 elif sub_choice==2:
#                     view_emp()
#                 elif sub_choice==3:
#                     update_emp()
#                 elif sub_choice==4:
#                     delete_emp()
#                 elif sub_choice==5:
#                     break
#         elif f==2:
#             if user['dob']==user['password']:
#                 password=input("enter new password :")
#                 user['password']=password
#             while True:
#                 print('''
# 1.view profile
# 2.update profile
# 3.log out
#                 ''')
#                 sub_choice=int(input("enter the number :"))
#                 if sub_choice==1:
#                     profile(user)
#                 elif sub_choice==2:
#                     pro_update(user)
#                 elif sub_choice==3:
#                     break
#         else:
#             print('invalid login')
#     elif choice==2:
#         break
#     else:
#         print('invalid login')


# users=[]
# lib=[]
# def register():
#     if len(users)==0:
#         id=1
#     else:
#         id=user[-1]['id']+1
    

#     email=str(input("enter the email :"))
#     f=0
#     for i in users:
#         if i['email']==email:
#             f=1
#             register()
#     if f==0:
#         name=str(input("enter the name :"))
#         username=email
#         phone=int(input("enter the no :"))
#         password=str(input("enter password :"))
#         users.append({'name':name,'id':id,'email':email,'phone':phone,'books':[],'username':username,'password':password})

# def login():
#     uname=input("enter uname : ")
#     passw=input("enter passw : ")
#     f=0
#     if uname == 'admin' and passw == 'admin':
#         f=1
#     cust=''
#     for i in users:
#         if uname == i['email'] and passw == i['password']:
#             f=2
#             cust=i
#     return f,cust

# def add_book():
#     if len(lib)==0:
#         id=101
#     else:
#         id=lib[-1]['id']+1
#     f=0
#     for i in lib:
#         if i['id']==id:
#             f=1
#             add_book()
#     if f==0:
#         name=str(input("enter the book name : "))
#         price=int(input("enter the price : "))
#         stock=int(input("enter the stock : "))
#         lib.append({'id':id,'name':name,'price':price,'stock':stock})

# def view_book():
#     for i in lib:
#         print(i)

# def update_book():
#     id=int(input("enter the id : "))
#     f=0
#     for i in lib:
#         if i['id']==id:
#             f=1
#             price=int(input("enter the price : "))
#             stock=int(input("enter the stock : "))
#             i['price']=price
#             i['stock']=stock
#     if f==0:
#         print('invalid id')

# def delete():
#     id=int(input("enter the id : "))
#     f=0
#     for i in lib:
#         if i['id']==id:
#             f=1
#             lib.remove(i)
#     if f==0:
#         print('invalid id')

# def view_user():
#     for i in users:
#         print('name',i['name'])
#         print('id',i['id'])
#         print('email',i['email'])
#         print('phone',i['phone'])

# def view_profile(cust):
#     print(users)


# def update_pro(cust):
#     name=str(input("enter the name : "))
#     phone=int(input("enter phone : "))
#     cust['name']=name
#     cust['phone']=phone
    
# def lend_book(cust):
#     id=int(input("enter the id : "))
#     f=0
#     for i in lib:
#         if i['id']==id:
#             f=1
#             i['stock']-=1
#             cust['books'].append(id)
#             print('book added')
#     if f==0:
#         print("invalid id")

# def return_book(cust):
#     id=int(input("enter the id : "))
#     f=0
#     for i in lib:
#         if i['id']==id and id in cust['books']:
#             f=1
#             i['stock']+=1
#             cust['books'].remove(id)
#             print('book returned')
#     if f==0:
#         print('invalid id')


# def books_in_hand(cust):
#     print(cust['books'])

# while True:
#     print('''
#     1.register
#     2.login
#     3.exit 
# ''')
#     choice=int(input("enter the choice :"))
#     if choice==1:
#         register()
#     elif choice==2:
#         f,cust=login()
#         if f==1:
#             while True:
#                 print('''
#                 1.add book
#                 2.view book
#                 3.update books
#                 4.delete
#                 5.view user
#                 6.exit
#                 ''')
#                 sub_choice=int(input("enter the choice : "))
#                 if sub_choice==1:
#                     add_book()
#                 elif sub_choice==2:
#                     view_book()
#                 elif sub_choice==3:
#                     update_book()
#                 elif sub_choice==4:
#                     delete()
#                 elif sub_choice==5:
#                     view_user()
#                 elif sub_choice==6:
#                     break
#                 else:
#                     print('invalid choice')
#         elif f==2:
#             while True:
#                 print('''
#                 1.view profile
#                 2.view book
#                 3.update profile
#                 4.lend book
#                 5.return book
#                 6.books in hand
#                 7.exit
#                 ''')
#                 sub_ch=int(input("enter the choice : "))
#                 if sub_ch==1:
#                     view_profile(cust)
#                 elif sub_ch==2:
#                     view_book()
#                 elif sub_ch==3:
#                     update_pro(cust)
#                 elif sub_ch==4:
#                     lend_book(cust)
#                 elif sub_ch==5:
#                     return_book(cust)
#                 elif sub_ch==6:
#                     books_in_hand(cust)
#                 elif sub_ch==7:
#                     break
#                 else:
#                     print("invalid choice")
#         else:
#             print('invalid username or password')
#     elif choice==3:
#         break
#     else:
#         print('invalid')



# lanbda function


# filter using even numbers

# l=[1,2,3,4,5,6,7,8]
# print(list(filter(lambda x:x%2!=0,l)))

# lambda using in a word to find letters


# l=['welcome','apple','kiwi','hello']
# print(list(filter(lambda x: 'e' in x,l)))



# map using in lambda

# l=[1,2,3,4,5,6,7]
# # print(list(map(lambda x:x+10,l)))

# def num(x):
#     return x+10
# print(list(map(num,l)))


# file handling

# modes

# create ---> x
# read  ---> r
# write ---> w
# append ---> a



# f=open('demoo.txt','x')
# f.write('welcome')
# f.write('hello')
# f.write('123')



# f=open('demoo.txt','r')
# a=f.read()
# print(a)
# f.seek(0)
# b=f.read(10)
# print(b)


# f=open('demoo.txt','r')
# a=f.readline(5)
# print(a)
# b=f.readline()
# print(b)
# c=f.readline()
# print(c)


# f=open('demoo.txt','r')
# a=f.readlines()
# print(a)
# print(len(a))
# print(f.tell())


# reverse 

# f=open('demoo.txt','r')
# a=f.readlines()
# l=len(a)
# f.seek(0)
# for i in range(l):
#     b=f.readline().strip()
#     print(b[::-1])



# count of letters and count of cap and small letters

# f=open('demoo.txt','r')
# a=f.readlines()
# l=len(a)
# letter=0
# cap=0
# f.seek(0)
# for i in range(l):
#     b=f.readline().strip()
#     for i in b:
#         if i !=' ':  
#             letter+=1
#             if i.isupper():
#                 cap+=1
# print(letter)
# print('cap',cap)
# print('small',letter-cap)



# count of words

# f=open('demoo.txt','r')
# a=f.readlines()
# l=len(a)
# word=0
# f.seek(0)
# for i in range(l):
#     b=f.readline().strip()
#     a=b.split(' ')
#     for j in a:
#         if j!='':
#             word+=1
# print(word)


# write

# f=open('demoo.txt','w')
# f.write('welcome')
# f.write('123')
# f.write('hi'+'hello')



# f=open('new.txt','w')
# f.write('hello')
# f.write('123')
# f.write('hello'+'welcome')


# MULTIPLICATION USING WRITE

# f=open('new.txt','w')
# n=int(input("enter a number : "))
# for i in range(1,11):
#     for j in range(1,n+1):
#         mult=j*i
#         f.write(f'{i} x {j} = {mult}\t')
#     f.write('\n') 



# append

# f=open('demoo.txt','a')
# f.write('java')


# delete

import os


# os.remove('sample1.py')

# if os.path.exists('sample1.py'):
#     os.remove('sample1.py')
# else:
#     print('invalid file')



# import datetime
# x=datetime.datetime.now().strftime('%a')            short form of date
# print(x)

# import datetime
# x=datetime.datetime.now().strftime('%A')            full-form of date
# print(x)

# import datetime
# x=datetime.datetime.now().strftime('%b')           short of month
# print(x)


# import datetime
# x=datetime.datetime.now().strftime('%B')            full of month
# print(x)


# import datetime
# x=datetime.datetime.now().strftime('%Y')                current year
# print(x)


# import datetime
# x=datetime.datetime.now().strftime('%y')
# print(x)


import math


# print(math.ceil(11.1))                  
# print(math.floor(11.9))
# print(math.factorial(5))
# print(math.sqrt(64))



# class syn:
#     def python():
#         print('python prgrm')
#     def java():
#         print('java prgrm')
#     def php():
#         print('php prgrm')

# manu=syn
# manu.python()
# akhil=syn
# akhil.php()


# class bank:
#     def __init__(s):
#         s.name=input('name')
#         s.age=int(input('age'))
#         s.bal=0


#     def deposit(self,amt):
#         self.bal+=amt
#         print('deposit')
#     def withdrow(self,amt):
#         self.bal-=amt
#         print('withdrow')
#     def balance(self):
#         print('balance',self.bal)

# obj=bank()
# obj.deposit(5000)
# obj.balance()
# obj.withdrow(2000)shahid=std()
# shahid.reg()
# shahid=std()
# shahid.reg()

# obj.balance()
# print(obj.bal)

# obj1=bank()
# obj1.deposit(1000)
# obj1.balance()



# inheritance

# single inheritance

# class syn:
#     def python(self):
#         # self a=10
#         print('python')
#     def php(self):
#         print('php')
#     def java(self):
#         print('java')

# class novavi(syn):
#     def dm(self):
#         print('dm wrkr')
#     def web(self):
#         print('web')

# n=novavi()
# n.dm()
# n.python()
# n.a()

# std1=syn()
# std1.python()


# multiple inheritance

# class school:
#     def english(self):
#         print('english')
#     def science(self):
#         print('science')

# class tution:
#     def maths(self):
#         print('maths')
#     def computer(self):
#         print('computer')

# class std(school,tution):
#     def art(self):
#         print('art')

# shahid=std()
# shahid.maths()
# shahid.art()
# shahid.english()


# multilevel inheritance


# class c_u():
#     def exam(self):
#         print('exam')
#     def result(self):
#         print('result')

# class clg(c_u):
#     def notes(self):
#         print('notes')
#     def prgrms(self):
#         print('prgrms')

# class std(clg):
#     def uniform(self):
#         print('unifrom')
#     def lab(self):
#         print('lab')


# shahid=std()
# shahid.lab()
# shahid.exam()
# shahid.prgrms()



# hirarchieal inheritance

# one parent and morethan one child


# class syn:
#     def python(self):
#         print('python')
#     def php(self):
#         print('php')

# class non_teaching_staff(syn):
#     def administration(self):
#         print('administration')

# class teaching_staff(syn):
#     def python_course(self):
#         print('python course')


# staff1=non_teaching_staff()
# staff2=teaching_staff()
# staff1.python()
# staff1. administration()
# staff2.php()
# staff2.python_course()

# hybrid inheritance

# class syn:
#     def python(self):
#         print('python')
#     def php(self):
#         print('php')

# class non_teaching_staff(syn):
#     def administration(self):
#         print('administration')

# class teaching_staff(syn):
#     def python_course(self):
#         print('python course')

# class student(teaching_staff):
#     def notes(self):
#         print('notes')


# staff1=non_teaching_staff()
# staff2=teaching_staff()
# staff1.python()
# staff1. administration()
# staff2.php()
# staff2.python_course()
# std=student()
# std.notes()
# std.python_course()
# std.php()



# class animal():
#     def animals(self):
#         print('animals')

# class dog(animal):
#     def dogs(self):
#         print('dogs')

# class cat(animal):
#     def cats(self):
#         print('cats')

# class persian_cat(cat):
#     def persian_cats(self):
#         print('persian cats')


# a=animal()
# d=dog()
# c=cat()
# p=persian_cat()

# a.animals()
# d.dogs()
# d.animals()
# c.cats()
# c.animals()
# p.persian_cats()
# p.cats()
# p.animals()



# polymorphism


# class ed():
#     def notes(self):
#         print('notes in ed')

# class school(ed):
#     def notes(self,sub):
#         print('notes in school',sub)

# class std(school):
#     def notes(self,sub):
#         print('notes in std')
#         super().notes(sub)

# sha=std()
# sha.notes('py')



# class bank():
#     def __init__(self):
#         print('add bank dtls')
    
# class user():
#     def __init__(self):
#         print('add user dtls')
#         super().__init__()

# sbi=bank()
# shahid=user()



# from abc import ABC,abstractmethod
# class syn(ABC):
#     @abstractmethod
#     def reg(self):
#         pass

#     def py(self):
#         print('py')

# class std(syn):
#     def reg(self):
#         name=input('name')
#     def notes(self):
#         print('notes')

# class staff(syn):
#     def regi(self):
#         print('staff reg')


# shahid=std()
# shahid.reg()

import re
# a='welcome to all '
# print(re.sub('to','TO',a))
# print(re.sub('too','TO',a))
# print(re.split(' ',a))
# print(re.findall('to',a))
# print(re.findall('toO',a))
# a='welcome to all to to to'
# print(re.findall('to',a))
# print(re.search('to',a))
# a='aBcd'
# print(re.search('a',a))
# print(re.search('a.',a))
# print(re.search('d.',a))
# print(re.search('d.*',a))
# print(re.search('a.*',a))
# print(re.search('a.+',a))
# print(re.search('d.+',a))
# print(re.search('c.+',a))
# print(re.search('c.?',a))
# print(re.search('d.?',a))
# print(re.search('a.?',a))
# print(re.search('[a-z]',a))
# print(re.search('[A-Z]',a))
# a='AIFS123'
# print(re.search('[M-Z]',a))
# print(re.search('[A-Z][0-9]',a))
# a='214343213'
# print(re.search('[a-z0-9]',a))
# a='ggvbfjg'
# print(re.search('[a-z0-9]',a))
# a='abcd'
# print(re.search('[a-z].',a))
# print(re.search('[a-z]+',a))
# print(re.search('[a-z]?',a))
# print(re.search('[a-z]?.',a))

# a='abchd2'
# print(re.search('[a-z].*[0-9]',a))
# print(re.search('[a-z].{5}',a))


# mob number validation

# import re
# a=(input("enter your number : "))
# if len(a)==10 and re.search('[6-9].{9}',a) and a.isdigit():
#     print('valid')
# else:
#     print('not ')



# email validation

# import re
# a=input("enter your email  : ")
# if re.search('^[a-z].*@gmail.com$',a):
#     print('valid')
# else:
#     print('not ')


# password validation 

# import re 

# a=input('enter your password : ')
# if re.search('^[A-z0-9].*[@#$&0-9]',a) and  not(a.isdigit()) and len(a)>=8:
#     print('valid')
# else:
#     print('not')

# a=hello
# print(a)




        #   DBMS 
        # ------------


import sqlite3

con = sqlite3.connect('batch7.db')
try:
    con.execute("create table std(rool_no int,name text,age int)")
except:
    pass

# con.execute("insert into std(rool_no,name,age)values(1,'shahid',20),(2,'fayas',90),(3,'yaseen',85),(4,'aslam',100),(5,'althaf',10)")
# con.commit()


roll=int(input("enter roolno : "))
name=input("enter the name : ")
age=int(input("enter the age : "))


con.execute("insert into std(rool_no,name,age)values(?,?,?)",(roll,name,age))
con.commit()