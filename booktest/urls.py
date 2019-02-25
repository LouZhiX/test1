from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index', views.index), #建立/index与视图之间的关系
    url(r'^books$', views.books),
    url(r'^books/(\d+)', views.heros_in_book),
]
