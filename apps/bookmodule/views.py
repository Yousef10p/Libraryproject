from django.shortcuts import render,redirect

from django.http import HttpResponse


## ------------------------ LAB 3 ----------------------------
# def index(request): 
#     name = request.GET.get("name") or "world!"
#     return render(request, "bookmodule/index.html", {"name":name})


# def index2(request, val1 = 0): #add the view function (index2) 
#     return HttpResponse("value1 = "+str(val1))


# def viewbook(request, bookId):
#     book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
#     book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'} 
#     targetBook = None 
#     if book1['id'] == bookId: targetBook = book1
#     elif book2['id'] == bookId: targetBook = book2
#     else:
#         return redirect('https://github.com/Yousef10p')
#     context = {'book':targetBook} 
#     return render(request, 'bookmodule/show.html', context)

## ------------------------ LAB 4 ----------------------------
def index(request):
    return render(request,'bookmodule/index.html')

def list_books(request):
    return render(request,'bookmodule/list_books.html')


def viewbook(request,bookId):
    return render(request,'bookmodule/one_book.html')


def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


## ------------------------ LAB 5 ----------------------------
def links(request):
    return render(request,"bookmodule/lap5/links.html")


def text_formatting(request):
    return render(request,"bookmodule/lap5/text_formatting.html")

def listing(request):
    return render(request,"bookmodule/lap5/listing.html")

def tables(request):
    return render(request,"bookmodule/lap5/tables.html")
    

## ------------------------ LAB 6 ----------------------------
def search(request):
    if request.method == 'POST':
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        books = __getBooksList()
        newBooks = []
        for book in books:
            contained = False
            if isTitle and string in book['title'].lower():
                contained = True
            if not contained and isAuthor and string in book['author'].lower():
                contained=True
            
            if contained:
                newBooks.append(book)
        return render(request,'bookmodule/bookList.html',{'books':newBooks})
    return render(request, 'bookmodule/search.html')

def __getBooksList(): 
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'} 
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'} 
    return [book1, book2, book3]


