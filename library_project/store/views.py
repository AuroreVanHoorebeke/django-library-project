# from django.shortcuts import render
from django.http import HttpResponse

from .models import BOOKS

# Create your views here.


def index(request):
    message = "Hello world!"
    return HttpResponse(message)


def bookshelf(request):
    books = ["<li>{}</li>".format(book['name']) for book in BOOKS]
    message = """<ul>{}</ul>""".format("\n".join(books))
    return HttpResponse(message)


def details(request, book_id):
    id = int(book_id)
    book = BOOKS[id]
    print('wokin details func')
    authors = " ".join([author['name'] for author in book['authors']])
    message = "The book's name is {}. It was written by {}".format(book['name'], authors)
    return HttpResponse(message)


def search(request):
    query = request.GET.get('query')
    if not query:
        message = "No search keywords were used"
    else:
        books = [
            book for book in BOOKS
            if query in " ".join(author['name'] for author in book['authors'])
        ]

        if len(books) == 0:
            message = "Oops, we didn't find anything matching what you're looking for!"
        else:
            books = ["<li>{}</li>".format(book['name']) for book in books]
            message="""
                We found some books for you! Here they are:
                <ul>
                    {}
                </ul> 
            """.format("<li></li>".join(books))

    return HttpResponse(message)
