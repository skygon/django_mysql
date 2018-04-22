from django.http import HttpResponse, JsonResponse


def get_list(request):
    page_id = request.GET.get('page')
    if page_id is None:
        page_id = 1
        
    msg = "<p> Hello! this is get list for page %s. </p>" %(page_id)
    response = HttpResponse()
    response.write(msg)
    return response

def get_specific(request, projectId):
    msg = "Hello! This is the get specific API for project %s" %(projectId)
    data = {}
    data['name'] = "New York"
    data['location'] = "wall street"
    response = JsonResponse(data)
    return response
