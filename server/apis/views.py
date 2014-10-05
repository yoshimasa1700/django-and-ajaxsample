from django.http import HttpResponse
def main(request):
    return HttpResponse("Hello World!!")

def book_search(request):
    query = request.GET['word']

    response = HttpResponse()
    response.status = 200

    if query == "toyos":
        response.write("OK!")

    else:
        response.write("boooo!")

    return HttpResponse("booooo!")
    
    
