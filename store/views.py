from django.shortcuts import render, redirect, get_object_or_404
import os
import sys
import urllib.request
import json
import xml.etree.ElementTree as ET
from .models import Book
import datetime
from cart.forms import AddBookForm
from django.template.defaultfilters import slugify
# Create your views here.
def store(request):
    page = request.GET.get('page')
    
    if page is None:
        page = "1"

    keyword = request.GET.get('keyword')
    if keyword is None or keyword == 'None' or keyword == "":
        bookList = bookListApi("다", page)
    else:
        bookList = bookListApi(keyword, page)
    return render(request, 'store.html', {'bookList':bookList, 'keyword':keyword, 'page':page})


def detail(request, id,book_slug=None):
    book = get_object_or_404(Book,id=id,slug=book_slug)
    add_to_cart = AddBookForm(initial={'quantity':1})
    return render(request, 'bookdetail.html',{'book':book,'add_to_cart':add_to_cart})

def bookListApi(keyword, page):
    client_id = os.environ.get("client_id")
    client_secret = os.environ.get('client_secret')
    encText = urllib.parse.quote(keyword)
    display = 10
    start = (int(page)-1)*display+1
    # url = "https://openapi.naver.com/v1/search/book.json?query=" + encText # json 결과
    url = "https://openapi.naver.com/v1/search/book.xml?query=" + encText +"&start="+str(start) # xml 결과 
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        data = response_body.decode('utf-8')
        # jsonObj = json.loads(data)
        # items = jsonObj.get('items')
        # for item in items:
        #     print(item.get('title'))
        #     print(item.get('author'))
        #     print(item.get('isbn'))
        #     print(item.get('price'))
        #     print(item.get('description'))
        tree = ET.ElementTree(ET.fromstring(data))
        note = tree.getroot() 
        items = note.find('channel').findall('item')

        bookList = []
        for item in items:
            title = item.find('title').text.replace('<b>', "").replace('</b>', "").replace('!', "").replace(' / ', "").replace('/', "").replace('.', "")
            author = item.find('author').text.replace('<b>', "").replace('</b>', "")
            #slug = slugify(title)
            slug = title.replace(' ', "-")
            #print(title)
            #print("-------------------")
            #print(slug)
            isbn = item.find('isbn').text
            image = item.find('image').text
            publisher = item.find('publisher').text.replace('<b>', "").replace('</b>', "")
            pubdate = item.find('pubdate').text
            pubdate = dateString(pubdate)
            price = item.find('price').text
            if item.find('description').text is None:
                description = ""
            else:
                description = item.find('description').text.replace('<b>', "").replace('</b>', "")

            if Book.objects.filter(isbn=isbn).exists():
                book = get_object_or_404(Book,isbn=isbn)
                bookList.append(book)
            else:
                book = Book.objects.create(title=title, author=author,slug=slug, isbn=isbn, image=image, publisher=publisher, pubdate=pubdate, price=price, description=description)
                bookList.append(book)
        return bookList
    else:
        print("Error Code:" + rescode)

def dateString(date):
    year = date[:4]
    month = date[4:6]
    day = date[6:8]
    if day != "00":
        string = year+"년 "+month+"월 "+day+"일"
    else:
        string = year+"년 "+month+"월"
    return string