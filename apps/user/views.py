import re

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View

from apps.user.models import User


def register(request):
    '''注册'''
    if request.method == 'GET':
        '''显示注册页面'''
        return render(request,'register.html')
    else:
        '''进行注册处理'''
        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        print(username, password)
        # 进行数据校验
        if not all([username, password, email, allow]):
            # 数据不完整
            return render(request, "register.html", {'errmsg': '数据不完整'})
        # 校验邮箱
        if not re.match('^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱不正确'})
        if allow != "on":
            return render(request, 'register.html', {'errmsg': '请同意协议'})
        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None
        if user:
            return render(request, 'register.html', {'errmsg': '用户已存在'})
        # 进行业务处理
        # user = User()
        # user.username = username
        # user.password = password
        # user.email = email
        # user.save()
        '''不需要使用上述的,可以直接使用django封装好的方法'''
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()

        # 返回应答
        return redirect(reverse('goods:index'))

class RegisterView(View):
    '''注册类,基于类视图'''
    def get(self,request):
        '''显示注册页面'''
        return  render(request,'register.html')
    def post(self,request):
        '''进行注册处理'''
        '''进行注册处理'''
        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        print(username, password)
        # 进行数据校验
        if not all([username, password, email, allow]):
            # 数据不完整
            return render(request, "register.html", {'errmsg': '数据不完整'})
        # 校验邮箱
        if not re.match('^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱不正确'})
        if allow != "on":
            return render(request, 'register.html', {'errmsg': '请同意协议'})
        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None
        if user:
            return render(request, 'register.html', {'errmsg': '用户已存在'})
        # 进行业务处理
        # user = User()
        # user.username = username
        # user.password = password
        # user.email = email
        # user.save()
        '''不需要使用上述的,可以直接使用django封装好的方法'''
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()

        # 返回应答
        return redirect(reverse('goods:index'))


