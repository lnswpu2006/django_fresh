
from apps.user import views
from django.urls import path,include
from django.conf.urls import url
from apps.user.views import RegisterView

urlpatterns = [
    # path('register/',views.register,name="register"),
    # path('register_handle',views.register_handle,name="register_handle"),#注册处理
    path('register/',RegisterView.as_view(),name='register')#注册

]
