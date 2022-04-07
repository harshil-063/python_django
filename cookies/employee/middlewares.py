from urllib import response

from django.http import HttpResponse
from django.shortcuts import render


def my_middleware(get_response):
    print("one time initialization")
    def my_function(request):
        print("this is before view")
        response = get_response(request)
        print("this is after view")
        return response
    return my_function

class brothermiddleware:
    def __init__(self,get_response) -> None:
        self.get_response = get_response
        print("One time brother initialization code")

    def __call__(self,request):
        print("this is brother before view")
        response =self.get_response(request)
        print("this is brother after view")
        return response

class fathermiddleware():
    def __init__(self,get_response) -> None:
        self.get_response = get_response
        print("One time father initialization code")

    def __call__(self,request):
        print("this is father before view")
        # response =self.get_response(request) ///because of this line next middleware does not call
        response = render(request,'employee/siteuc.html')
        print("this is father after view")
        return response

# class mothermiddleware(fathermiddleware):
#     def __init__(self,get_response) -> None:
#         self.get_response = get_response
#         print("One time mother initialization code")

#     def __call__(self,request):
#         print("this is mother before view")
#         response =self.get_response(request)
#         print("this is mother after view")
#         return response

class mytemplateresponsemiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self,request,response):
        print("process template response from middleware")
        response.context_data['name'] = 'Kumbhani'
        response.context_data['surname'] = 'patel'
        return response