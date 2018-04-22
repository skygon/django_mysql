from django.http import HttpResponse


def get_all(request):
    return HttpResponse("Hello! This is the get all API")

def get_specific(request, projectId):
    msg = "Hello! This is the get specific API for project %s" %(projectId)
    return HttpResponse(msg)
