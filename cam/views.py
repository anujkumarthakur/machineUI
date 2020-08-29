from django.shortcuts import render
import os
 
def Index(request):
    engine_no = request.POST
    print(engine_no)
    return render(request, 'index.html', {"engine_no": engine_no})
