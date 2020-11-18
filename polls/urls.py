from django.urls import path
from . import views  #.一般表示当前目录
#项目URL配置polls/路径，应用配置/index路径，那么要访问就要/polls/index这样访问
app_name = 'polls' #指定url所在的app名，以免多个app有相同命名时html无法区分
urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
