from django.http import HttpResponse
from django.template import loader
from django.template.defaulttags import register
from requests import post
from .constants import BACKEND_URL, BACKEND_PORT


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    index_template = loader.get_template("index.html")
    if request.method == "GET":
        try:
            query = request.GET['Q']
            if query:
                # Sample results
                # results = {}
                # TODO: Add status checks
                results = post(f"http://{BACKEND_URL}:{BACKEND_PORT}/search", data={"Q": query}).json()
                print(results)
                context = {
                    "Q": query,
                    "R": results
                }
            else:
                context = {}
        except KeyError:
            context = {}
    else:
        context = {}

    return HttpResponse(index_template.render(context, request))
