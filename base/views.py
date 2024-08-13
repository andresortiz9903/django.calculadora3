from django.shortcuts import render #importa los modulos

from django.http import HttpResponse

 
def main(request): #define y main llama a la aplicacion 
    context={}
    return render(request,'base/calculator.html',context) #return devuelvce la ruta al navegador 
#rende devuelve una respiusta http y rquest recibido por el navegador y main llama la aplicacion 
def calculate(request):
    if request.method == 'POST': #if toma la decison 
        number_one = request.POST.get("number_one")
        number_two = request.POST.get("number_two")
        operation = request.POST.get("operation")
    if operation == "add":
        result = float(number_one) + float(number_two)
        context={'result':result}
        return render(request,"base/calculator.html",context)


    elif operation == "subtract":
         result = float(number_one) - float(number_two)
         context={'result' :result}
         return render(request,"base/calculator.html",context)
     
     
     
    elif operation == "multiply":
         result = float(number_one) / float(number_two)
         context={'result' :result}
         return render(request,"base/calculator.html",context)
     
     
     
    elif operation == "divide":
         result = float(number_one) * float(number_two)
         context={'result' :result}
         return render(request,"base/calculator.html",context)
     
    else:
        return HttpResponse("calculator.html")