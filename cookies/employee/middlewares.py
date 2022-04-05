from urllib import response


def my_middleware(get_response):
    print("one time initialization")
    def my_function(request):
        print("this is before view")
        response = get_response(request)
        print("this is after view")
        return response
    return my_function