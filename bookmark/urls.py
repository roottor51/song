from django.urls import path, re_path

from .views import *

#url 이름을 가지고 패턴을 찾고자 할 때 namespace를 사용하려면 app_name이 필수!
app_name = 'bookmark'
urlpatterns = [
    #list, write, update, delete
    #함수형부 : 함수 이름만
    #클래스형뷰 : 클래스이름.as_view()
    path('', BookmarkListView.as_view(), name='list'),
    path('write/', BookmarkCreateView.as_view(), name='write'),
    #<1:2> 1. data type, 2. data name 1번은 빠져도 되지만 2번은 빠져도 됨
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    #re_path(regexp,,),
]