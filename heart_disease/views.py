import joblib
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import hyperlink


# Create your views here.


def index(request):
    return render(request, "pages/heartDiseaseForm.html",)


@csrf_exempt
def heart_pre(request):
    template = loader.get_template('pages/heartDiseaseForm.html')
    age = request.POST.get("age")
    cp = request.POST.get("cp")
    trestbps = request.POST.get("trestbps")
    chol = request.POST.get("chol")
    fbs = request.POST.get("fbs")
    restecg = request.POST.get("restecg")
    thalach = request.POST.get("thalach")
    exang = request.POST.get("exang")
    diabetes_data = [
        [age, cp,trestbps,chol, fbs, restecg , thalach , exang]]
    diabetes_model = joblib.load(r'heart_disease.pkl')
    # diabetes_model = pd.read_pickle('r',"diabetes_model.pickle")
    prediction = diabetes_model.predict(
        [[age, cp, trestbps ,chol, fbs, restecg , thalach , exang]])
    outcome = prediction


    if outcome == 1:
        result = "We are sorry, but it seems that you have the disease, please go to the nearest hospital from here"
    elif outcome == 0:
        result = "Congratulations, you are not ill"


    return HttpResponse(template.render({'result':result}))

