
from apps.goods import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name="index")#首页
]
