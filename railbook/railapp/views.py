from django.shortcuts import render


# Create your views here.
def login(request):
    if(request.method=='POST'):
        return render(request,'login.html')
    else:
        return render(request, 'login.html')
def register(request):
    if(request.method=='POST'):
        username=request.POST['US']
        data= store(username=US)
        data.save()
        print(username)
        return render(request,'login.html')
    else:
        return render(request,'registration.html')
