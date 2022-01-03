from django.shortcuts import render,redirect

# Create your views here.
def showIndex(request):
    #print(request.COOKIES)
    return render(request,"index.html",{"data":request.COOKIES})


def save_cookie(request):
    k = request.POST.get("t1")
    v = request.POST.get("t2")
    response = redirect('main')

    response.set_cookie(k,v) # Cookie Set

    # age of the cookie in seconds
    #response.set_cookie(k,v,max_age=30)
    #response.set_cookie(k,v,max_age=0)

    return response