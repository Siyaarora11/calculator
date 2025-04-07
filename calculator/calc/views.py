from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def calc(request):
    result = None
    error = None
    
    if request.method == "POST":
    
     try:
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        operator = request.POST.get("operator")

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator =="*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                error = " error! divisor by zero"
            else:
                result = num1/num2
        else:
            "Invalid operator!"
     except ValueError:
          error = "please enter valid number!"

        
        
    return render(request,'calc.html',{'result':result,'error':error})
