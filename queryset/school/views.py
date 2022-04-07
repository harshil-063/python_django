from ast import keyword
from dataclasses import fields
from datetime import date,time
from itertools import count
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from .models import Student, teacher
from django.db.models import Avg,Sum,Min,Max,Count,Q




# Create your views here.
def home(request):
#    student_data = Student.objects.all()
    # student_data = Student.objects.filter(marks=80)
    # student_data = Student.objects.exclude(marks=80)

    # student_data = Student.objects.order_by('name')
    # student_data = Student.objects.order_by('-name')
    # student_data = Student.objects.order_by('?')

    # ascending order and reverse 3 column                      
    # student_data = Student.objects.order_by('name').reverse()[:3] 


    # generate list of dictionary
    # student_data = Student.objects.values('name','city')

    # get data in touple form
    # student_data = Student.objects.values_list('name','city')

    # get data in touple with field name
    # student_data = Student.objects.values_list('name','city',named=True)

    # show all distinct date,month and year from among records
    # student_data = Student.objects.dates('pass_date','month')


    # print("data:",student_data)
    # # print("sql query:",student_data.query)
    # return render(request,'school/home.html',{'students':student_data})
# =================================================================================================================

    # giving all data from both table but excluding duplicate fields
    # qs1 = Student.objects.values_list('id','name',named=True)
    # qs2 = teacher.objects.values_list('id','name',named=True)

    # giving all data from both table but excluding duplicate fields
    # using all we can show duplicate fields also
    # student_data = qs2.union(qs1,all=True)

    # show same filed on both table
    # student_data = qs1.intersection(qs2)

    # show different field from both table (same fields name not how)
    # student_data = qs1.difference(qs2)

# ==============================AND OR Operator=================================================
    # show records only if both field are match
    # student_data = Student.objects.filter(id=1) & Student.objects.filter(roll=15)
    # student_data = Student.objects.filter(Q(id=1) & Q(roll=15))

    #show records if any one field is match
    # student_data = Student.objects.filter(id=1) | Student.objects.filter(roll=16)
    # student_data = Student.objects.filter(Q(id=1) | Q(roll=16)) 



    # print("data:",student_data)
    # # print("sql query:",student_data.query)
    # return render(request,'school/home.html',{'students':student_data})

################################################ methods tha not return new queryset###############################################


    # it does not return any list it returns only one object
    # student_data = Student.objects.get(pk=1)

    # return first record
    # student_data = Student.objects.order_by('name').first()
    # print(student_data)
    # student_data = Student.objects.get(name='harshil')


    # it return last record
    # student_data = Student.objects.order_by('name').last()

    # return a latest date records
    # student_data = Student.objects.latest('pass_date')

    # return a earliest date records
    # student_data = Student.objects.earliest('pass_date')

    # it return a true if data is exist in table
    # student_data = Student.objects.all()
    # print(student_data.exists())

    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk))

    # its create a new record in database
    # student_data = Student.objects.create(name="hk",roll=115,city='london', marks=60,pass_date='2022-5-4')

    # its get record object and return false if it already exist in table otherwise it creats a new record and returns true
    # student_data = Student.objects.get_or_create(name="john",roll=20,city='london', marks=60,pass_date='2022-5-4')


    # its update a record
    # student_data =Student.objects.filter(id=12).update(name='ellie',marks=80)
    # student_data = Student.objects.filter(marks=90).update(city='newyork')

    # error occured because get() is only return object not queryset and update() is only set on queryset not an object
    # student_data =Student.objects.get(id=12).update(name='ellie',marks=80)

    # student_data =Student.objects.update_or_create(id=1,name='hk', defaults={'name':'harshil','roll':62})


    # bulk used to add multiple record at atime
    # objs = [Student(name='atif',roll=78,city='tokyo',marks=98,pass_date='2022-5-15'),
    #         Student(name='arijit',roll=79,city='berlin',marks=98,pass_date='2022-3-12'),
    #         Student(name='jubin',roll=80,city='dubai',marks=98,pass_date='2022-10-6'),
    #         Student(name='neha',roll=81,city='helsinki',marks=98,pass_date='2022-8-8')
    # ]
    # student_data= Student.objects.bulk_create(objs)

    # student_data = Student.objects.in_bulk([6,2])
    # for st in student_data:
    #     print(st.name)
    # print(student_data[6].name)



    # student_data =Student.objects.get(roll=15).delete()

    # to count the records
    # student_data = Student.objects.all().explain()
    # # print(student_data.count())

    # print("data:",student_data)
    # # print("sql query:",student_data.query)
    # return render(request,'school/home.html',{'students':student_data})


# ==========================================================Field Lookup ================================================================= 




    # student_data = Student.objects.all()
    # get fields with exact name
    student_data = Student.objects.filter(name__iexact='harshil')

    # get all fields contain har keyword
    student_data = Student.objects.filter(name__contains='har')

    # student_data = Student.objects.filter(id__in=[2,5,7])

    student_data = Student.objects.filter(marks__in=[70])

    student_data = Student.objects.filter(marks__gte=80)

    student_data = Student.objects.filter(name__startswith='m')

    student_data = Student.objects.filter(name__endswith='l')

    student_data = Student.objects.filter(pass_date__range=('2022-05-01','2022-06-01'))


    # can only use in dateTime field datatype
    # student_data = Student.objects.filter(admdatetime_date=date(2022,5,4))

    # student_data = Student.objects.filter(pass_date__year__gt=2021) #can use gt,lt,gte,lte

    # student_data = Student.objects.filter(pass_date__month=5)

    # student_data = Student.objects.filter(pass_date__week=15)

    # student_data = Student.objects.filter(pass_date__week_day=7) #1= sunday,7=saturday  gt,lt used

    # student_data = Student.objects.filter(pass_date__quarter=2)

    # student_data = Student.objects.filter(pass_date__time__gt=time(21,17))

    # student_data = Student.objects.filter(pass_date__hour__gt=5)

    # student_data = Student.objects.filter(pass_date__minute__gt=26)

    # student_data = Student.objects.filter(pass_date__second__gt=30)

# ================================Aggregation==============================


    # student_data = Student.objects.all()
    # average = student_data.aggregate(Avg('marks'))
    # sum = student_data.aggregate(Sum('marks'))
    # min = student_data.aggregate(Min('marks'))
    # max = student_data.aggregate(Max('marks'))
    # count =student_data.aggregate(Count('marks'))
    # context = {'students':student_data,'average':average,'min':min,'max':max,'sum':sum,'count':count}

# ==============================Q object=============================================

    # Q object is use and or not operator(&,|,~)
    student_data = Student.objects.filter(Q(id=6) & Q(roll=56))
    student_data = Student.objects.filter(Q(id=6) | Q(roll=115))
    student_data = Student.objects.filter(~Q(id=6))

# ================================== limiting queryset ==============================
    #student_data = Student.objects.all()[:5]   
    #student_data = Student.objects.all()[2:5]
    student_data = Student.objects.all()[1::2]




    print("data:",student_data)
    # print("sql query:",student_data.query)
    return render(request,'school/home.html',{'students':student_data})
    # return render(request,'school/home.html',context)