from multiprocessing import context
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

projectsList = [
    {'id': '1',
     'title': 'Portfolio',
     'descriptions': 'PortfolioPortfolioPortfolioPortfolioPortfolioPortfolio',
     },
    {'id': '2',
     'title': 'SOCIAL NETWORK ',
     'descriptions': 'SOCIAL NETWORKSOCIAL NETWORKSOCIAL NETWORKSOCIAL NETWORKSOCIAL NETWORKSOCIAL NETWORK',
     },
    {'id': '3',
     'title': 'Python',
     'descriptions': 'PythonPythonPythonPythonPythonPython',
     },
    ]
def projects(request):
    page = 'projects'
    number = 11
    context = {'page':page,'number':number,'projects':projectsList}
    return render(request, 'projects/projects.html',context)
    
def project(request,pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html',{'project':projectObj})