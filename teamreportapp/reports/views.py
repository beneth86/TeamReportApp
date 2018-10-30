from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from reports.models import Project

def index(request):
    num_projects = Project.objects.count()

    queued_projects = Project.objects.filter(status__exact='q').count()

    inprogress_projects = Project.objects.filter(status__exact='i').count()

    completed_projects = Project.objects.filter(status__exact='c').count()

    context = {
        'num_projects': num_projects,
        'queued_projects': queued_projects,
        'inprogress_projects': inprogress_projects,
        'completed_projects': completed_projects,
    }

    return render(request, 'index.html', context=context)

class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 10

class ProjectQueuedListView(generic.ListView):
    model = Project
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.filter(status='q')

class ProjectInProgressListView(generic.ListView):
    model = Project
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.filter(status='i')

class ProjectCompletedListView(generic.ListView):
    model = Project
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.filter(status='c')
    
class ProjectDetailView(generic.DetailView):
    model = Project

class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'

class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects')
