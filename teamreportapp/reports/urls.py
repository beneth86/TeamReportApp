from django.urls import path
from reports import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('queued/', views.ProjectQueuedListView.as_view(), name='projects-queued'),
    path('inprogress/', views.ProjectInProgressListView.as_view(), name='projects-inprogress'),
    path('completed/', views.ProjectCompletedListView.as_view(), name='projects-completed'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('projects/create/', views.ProjectCreate.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
]
