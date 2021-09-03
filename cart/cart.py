from decimal import Decimal
from django.conf import settings

from store.models import Book

class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        book_ids = self.cart.keys()

        books = Book.objects.filter(id__in = book_ids)

        for book in books:
            self.cart[str(book.id)]['book'] = book
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item

    def add(self,book,quantity=1,is_update=False):
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id]= {'quantity':0 ,'price' : str(book.price)}

        if is_update:
            self.cart[book_id]['quantity'] = quantity
        else :
            self.cart[book_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session [settings.CART_ID]=self.cart
        self.session.modified = True

    def remove(self,book):
        book_id = str(book.id)
        if book_id in self.cart:
            del(self.cart[book_id])
            self.save()
    
    def remove_all(self):
        for book_id in list(self.cart):
            del(self.cart[book_id])
        self.save()
    
    def clear(self):
        self.session[settings.CART_ID]={}
        self.session.modified = True
        
    def get_book_total(self):
        return sum(item['price']*item['quantity'] for item in self.cart.values())
