from django.http import HttpResponse
from django.template import Template, Context
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
    # Trayendo Plantilla html de manera poco optima pero funcional
    p1 = Person("Juan", "Agudelo")
    # name = "Juan"
    # last_name = "Agudelo"
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    date = (datetime.datetime.now()).strftime("%d/%m/%Y")
    doc_externo = open("Proyecto1//templates//index.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"name_person":p1.name, "last_name_person": p1.last_name, "date_now":date, "temas_course":temas})
    documento = plt.render(context=ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta Luego Mundo!!!")

def now_date(request):
    date = datetime.datetime.now()
    return HttpResponse(f"""<html>
                        <body>
                        <h1>Date: {date}</h1>
                        </body>
                        </html>""")
    
def calcule_age(request, age, year):
    period = year - int(datetime.datetime.now().year)
    age_future = age + period
    return HttpResponse(f"""<html>
                        <body>
                        <h2>In Year {year} you wil be {age_future} years old</h2>
                        </body>
                        </html>""")