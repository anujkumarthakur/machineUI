from django.shortcuts import render
import os
 
def Index(request):
    engine_no = request.POST
    print(engine_no)
    try:
        os.mkdir(os.path.join('/home/appventurez/Desktop/webcam/Data/', str(engine_no)))
    except:
        pass
    return render(request, 'index.html', {"engine_no": engine_no})
