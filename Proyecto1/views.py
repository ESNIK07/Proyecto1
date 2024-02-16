from django.http import HttpResponse
# from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

documento =f"""<html>
               <body>
               <h1>Date: Hola mundo!!!</h1>
               </body>
               </html>"""


class Person(object):
    
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    

def saludo(request):
    p1 = Person("ING Juan", "Agudelo")
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    date = (datetime.datetime.now()).strftime("%d/%m/%Y")
    ctx={"name_person":p1.name, "last_name_person": p1.last_name, "date_now":date, "temas_course":temas}
    # documento = get_template('index.html').render(context=ctx)
    # return HttpResponse(documento)
    return render(request, 'index.html', ctx)

def despedida(request):
    return HttpResponse("Hasta Luego Mundo!!!")

def now_date(request):
    #Forma optima de llamar un template
    doc_template=get_template('date.html')
    date = datetime.datetime.now()
    ctx={"date":date}
    documento = doc_template.render(ctx)
    return HttpResponse(documento)
    
def calcule_age(request, age, year):
    period = year - int(datetime.datetime.now().year)
    age_future = age + period
    return HttpResponse(f"""<html>
                        <body>
                        <h2>In Year {year} you wil be {age_future} years old</h2>
                        </body>
                        </html>""")
    
def shop(request):
    doc_template=get_template('shop.html')
    documento = doc_template.render()
    return HttpResponse(documento)