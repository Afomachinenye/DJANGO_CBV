from django.urls import path
from  .views import TodoAppCreateView
from  .views import TodoAppListView
from .views import TodoAppDetailView
from .views import TodoAppUpdateView


urlpattern = [
    path('', TodoAppCreateView.as_view(), name = 'home'),
    path('list/', TodoAppListView.as_view()),
    path('<pk>/', TodoAppDetailView.as_view()),
    path('<pk>/update', TodoAppUpdateView.as_view())
      
      
]