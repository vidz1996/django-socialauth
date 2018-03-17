from django.shortcuts import render


def home(request):
   context = {'request': request, 'user': request.user}
   return render(request,'social_auth/home.html',context)