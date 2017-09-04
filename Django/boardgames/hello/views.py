from django.shortcuts import render

def home(request):
    return render(request, "hello/hello.html",
            {"message": "This is the message"})
