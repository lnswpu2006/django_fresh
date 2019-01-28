from django.shortcuts import render,redirect

#
def index(request):
    '''首页'''
    return render(request,'index.html',)