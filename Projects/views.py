# Create your views here.
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('base_project.html')

def project(request, project_name="projects"):
    return render_to_response('base_project.html', {'project':{'title':project_name}})