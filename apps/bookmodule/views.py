from django.shortcuts import render,redirect

from django.http import HttpResponse

def index(request): 
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name":name})


def index2(request, val1 = 0): #add the view function (index2) 
    return HttpResponse("value1 = "+str(val1))


def viewbook(request, bookId):
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    targetBook = None 
    if book1['id'] == bookId: targetBook = book1
    elif book2['id'] == bookId: targetBook = book2
    else:
        return redirect('https://github.com/Yousef10p')
    context = {'book':targetBook} 
    return render(request, 'bookmodule/show.html', context)