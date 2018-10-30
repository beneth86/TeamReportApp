from django.db import models
from django.urls import reverse

class Project(models.Model):
    name = models.CharField(max_length=255, help_text='Enter a project name')

    PROJECT_STATUS = (
        ('q', 'Queued'),
        ('i', 'In Progress'),
        ('c', 'Completed'),
    )

    status = models.CharField(
        max_length=1,
        choices=PROJECT_STATUS,
        blank=True,
        default='q',
        help_text='Project status',
    )

    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    date_completed = models.DateTimeField(auto_now=True, blank=True)
    
    #project_status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

##class Status(models.Model):
##    name = models.CharField(max_length=50, help_text='Enter a project status')
##
##    def __str__(self):
##        return self.name




    
