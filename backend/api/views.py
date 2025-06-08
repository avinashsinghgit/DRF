import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_home(request, *args, **kwargs):
    body = request.body
    # print(body)
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    print("Method : ", request.method)
    print("GET params : ", request.GET)
    print("POST params : ", request.POST)
    data["query"]= "yoou in are in django views"
    print("Raw body : ", request.body)
    print("headers : ", request.headers)
    print("Content type : ", request.content_type)
    print("URL : ", request.build_absolute_uri())
    return JsonResponse(data)








