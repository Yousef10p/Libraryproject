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
            if not contained and isAuthor and string in book['author'].lower:
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




## ------------------------ LAB 7 ----------------------------
from .models import Book
def simple_query(request):
    books = Book.objects.all()
    return render(request,'bookmodule/bookList.html', {'books':books})
    
def complex_query(request):
    books = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).filter(price__lte=1000)[:10]
    
    if len(books) >= 1:
        return render(request, 'bookmodule/bookList.html',{'books':books})
    
    return render(request, 'bookmodule/bookList.html')



#---------------- LAB 8 -------------------
from .models import Book
from django.db.models import Q
def lap8_task1(request):
    query = Book.objects.filter(Q(price__lte=80))
    return render(request,'bookmodule/lap8_task1_task2_task3_task4.html', {"books":query})

def lap8_task2(request):
    query = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request,'bookmodule/lap8_task1_task2_task3_task4.html', {"books":query})


def lap8_task3(request):
    query = Book.objects.filter(~Q(edition__gt=3) & (~Q(title__icontains='qu') | ~Q(author__icontains='qu')))
    return render(request,'bookmodule/lap8_task1_task2_task3_task4.html', {"books":query})


def lap8_task4(request):
    query = Book.objects.order_by('title')
    return render(request,'bookmodule/lap8_task1_task2_task3_task4.html', {"books":query})



from django.db.models import Count, Sum, Avg, Min, Max
def lap8_task5(request):
    query = Book.objects.aggregate(
        count=Count('id'),
        total=Sum('price'),
        avg=Avg('price'),
        min=Min('price'),
        max=Max('price')
    )
    
    context = {
        "books_count": query['count'],
        "books_total_price": query['total'],
        "books_average_price": query['avg'],
        "books_min_price": query['min'],
        "books_max_price": query['max'],
    }

    return render(request, 'bookmodule/lap8_task5.html', context)




# --------------------------------------- lap9 ------------------------------------------
from .models import Book,Publisher,Author

def lap9_task1(request):
    books = Book.objects.all()
    total_quantity = sum(b.quantity for b in books)
    total_quantity = total_quantity if total_quantity != 0  else 1

    for b in books:
        b.availability_percentage = round((b.quantity / total_quantity) * 100, 2)

    return render(request, 'bookmodule/lap9/lap9_task1.html', {'books': books})

def lap9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lap9/lap9_task2.html', {'publishers': publishers})


def lap9_task3(request):
    publishers = Publisher.objects.annotate(oldest_pubdate=Min('book__pubdate'))
    return render(request, 'bookmodule/lap9/lap9_task3.html', {'publishers': publishers})


def lap9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lap9/lap9_task4.html', {'publishers': publishers})


def lap9_task5(request):
    highly_rated = Count("book", filter=Q(book__rating__gte = 4))
    Publishers = Publisher.objects.annotate(num_books = Count("book"),
    highly_rated_books = highly_rated)
    return render(request, 'bookmodule/lap9/lap9_task5.html', {'publishers':     Publishers})


def lap9_task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books_count=Count('book', filter=Q(book__price__gt=50, book__quantity__lt=5, book__quantity__gte=1))
    )
    return render(request, 'bookmodule/lap9/lap9_task6.html', {'publishers': publishers})