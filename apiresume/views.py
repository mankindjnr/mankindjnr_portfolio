from django.shortcuts import render
import requests

def index(request):
    apiresp = requests.get("https://njoroge-resumeapi.onrender.com/")
    apioutput = apiresp.json()
    #print(apioutput)
    summary = (apioutput["Summary"][0]["summary"])
    education = (apioutput["Education"][0])
    workexperience = (apioutput["WorkExperience"][0])

    print(workexperience)
    return render(request, "apiresume/index.html", {
        "summary": summary,
        "education": education,
    })
