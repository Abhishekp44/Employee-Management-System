from django.urls import path
from EMSapp import views

urlpatterns = [
    path('home', views.home),
    path('emp', views.emp),
    path('dept', views.dept),
    path('salary', views.salary),
    path('editemp/<eid>', views.editemp),
    path('delemp/<eid>', views.delemp),
    path('editdept/<eid>', views.editdept),
    path('deldept/<eid>', views.deldept),
    path('editsalary/<eid>', views.editsalary),
    path('delsalary/<eid>', views.delsalary),
    path('salaryrep',views.salaryrep),
    
]
