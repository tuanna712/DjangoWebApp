from django.http import HttpResponse


"""
To render html web pages
"""
HTML_STRING = """
<h1> This is Home Page </h1>
"""


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response
    """
    return HttpResponse(HTML_STRING)