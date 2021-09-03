from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST


from store.models import Book
from .forms import AddBookForm
from .cart import Cart

@require_POST
def add(request,book_id):
    cart = Cart(request)
    book = get_object_or_404(Book,id=book_id)

    form = AddBookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book,quantity=cd['quantity'],is_update=cd['is_update'])

    return redirect('cart:detail')

def remove(request,book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id= book_id)
    cart.remove(book)
    return redirect('cart:detail')

def remove_all(request):
    cart = Cart(request)
    cart.remove_all()
    return redirect('cart:detail')

def detail(request):
    cart = Cart(request)
    for book in cart :
         book['quantity_form'] = AddBookForm(initial={'quantity':book['quantity'],'is_update':True})
    return render(request, 'detail.html',{'cart':cart})