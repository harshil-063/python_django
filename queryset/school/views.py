from dataclasses import fields
from unicodedata import name
from django.shortcuts import render
from .models import Student, teacher
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
    student_data = Student.objects.order_by('name').first()
    print(student_data)
    # student_data = Student.objects.get(name='harshil')

    # it return last record
    student_data = Student.objects.order_by('name').last()

    student_data = Student.objects.latest('pass_date')
    print("data:",student_data)
    # print("sql query:",student_data.query)
    return render(request,'school/home.html',{'students':student_data})