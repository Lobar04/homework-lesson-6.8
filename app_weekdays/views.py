from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def weekdays(request):
    return HttpResponse(f"<h2>weekdays</h2><table style='width:100%'><tr><th>HAFTA KUNLARI</th><th>ДНИ НЕДЕЛИ</th><th>WEEKDAYS</th></tr><tr><td>dushanba</td><td>Понедельник</td><td>monday</td></tr><tr><td>seshanba</td><td>Вторник</td><td>tuesday</td></tr><tr><td>chorshanba</td><td>Среда</td><td>wednesday</td></tr><tr><td>payshanba</td><td>Четверг</td><td>thursday</td></tr><tr><td>juma</td><td>Пятница</td><td>friday</td></tr><tr><td>shanba</td><td>Суббота</td><td>saturday</td></tr><tr><td>yakshanba</td><td>Воскресенье</td><td>sunday</td></tr></table><br><a href='http://127.0.0.1:8000/weekdays/'>Weekdays table uz-en-ru</a><br><a href='http://127.0.0.1:8000/weekdays/uz/'>Weekdays table uz</a><br><a href='http://127.0.0.1:8000/weekdays/en/'>Weekdays table en</a><br><a href='http://127.0.0.1:8000/weekdays/ru/'>Weekdays table ru</a>")

def weekdays_uz(request):
    return HttpResponse("<h2>HAFTA KUNLARI</h2><br><ul><li>dushanba</li><li>seshanba</li><li>chorshanba</li><li>payshanba</li><li>juma</li><li>shanba</li><li>yakshanba</li></ul><br><a href='http://127.0.0.1:8000/weekdays/'>Weekdays table uz-en-ru</a><br><a href='http://127.0.0.1:8000/weekdays/uz/'>Weekdays table uz</a><br><a href='http://127.0.0.1:8000/weekdays/en/'>Weekdays table en</a><br><a href='http://127.0.0.1:8000/weekdays/ru/'>Weekdays table ru</a>")

def weekdays_ru(request):
    return HttpResponse("<h2>ДНИ НЕДЕЛИ</h2><br><ul><li>Понедельник</li><li>Вторник</li><li>Среда</li><li>Четверг</li><li>Пятница</li><li>Суббота</li><li>Воскресенье</li></ul><br><a href='http://127.0.0.1:8000/weekdays/'>Weekdays table uz-en-ru</a><br><a href='http://127.0.0.1:8000/weekdays/uz/'>Weekdays table uz</a><br><a href='http://127.0.0.1:8000/weekdays/en/'>Weekdays table en</a><br><a href='http://127.0.0.1:8000/weekdays/ru/'>Weekdays table ru</a>")

def weekdays_eng(request):
    return HttpResponse("<h2>WEEKDAYS</h2><br><ul><li>monday</li><li>tuesday</li><li>wednesday</li><li>thursday</li><li>friday</li><li>saturday</li><li>sunday</li></ul><br><a href='http://127.0.0.1:8000/weekdays/'>Weekdays table uz-en-ru</a><br><a href='http://127.0.0.1:8000/weekdays/uz/'>Weekdays table uz</a><br><a href='http://127.0.0.1:8000/weekdays/en/'>Weekdays table en</a><br><a href='http://127.0.0.1:8000/weekdays/ru/'>Weekdays table ru</a>")


def main(request):
    return HttpResponse("<h1>Weekdays:</h1><br><a href='http://127.0.0.1:8000/weekdays/'>Weekdays table uz-en-ru</a><br><a href='http://127.0.0.1:8000/weekdays/uz/'>Weekdays table uz</a><br><a href='http://127.0.0.1:8000/weekdays/en/'>Weekdays table en</a><br><a href='http://127.0.0.1:8000/weekdays/ru/'>Weekdays table ru</a>")