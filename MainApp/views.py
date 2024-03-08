from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item


# Create your views here.
author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru",
}

#items = [
    #{"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    #{"id": 2, "name": "Куртка кожаная", "quantity": 2},
    #{"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    #{"id": 7, "name": "Картофель фри", "quantity": 0},
    #{"id": 8, "name": "Кепка", "quantity": 124},
#]


def home(request):
    # text = """<h1>"Изучаем django"</h1>
    #     <strong>Автор</strong>: <i>Иванов И.П.</i>
    #     """
    # return HttpResponse(text)
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru",
    }
    return render(request, "index.html", context)


def about(request):
    text = f"""
    <header>
        / <a href="/"> Home </a> / <a href="/items"> Items </a> / <a href="/about"> About </a>
    </header>
    Имя: <b>{author["Имя"]}</b><br>
    Отчество: <b>{author["Отчество"]}</b><br>
    Фамилия: <b>{author["Фамилия"]}</b><br>
    телефон: <b>{author["телефон"]}</b><br>
    email: <b>{author["email"]}</b><br>
    """
    return HttpResponse(text)


def get_item(request, item_id: int):
    """ По указанному item_id возращаем имя элемента и количество. """
    try:
        item = Item.objects.get(id=item_id)   
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Item with id={item_id} not found')
    else:
        context = {
            "item": item,
        }
        return render(request, "item_page.html", context)


def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)