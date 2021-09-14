import joblib
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return render(request , 'pages/diabetesForm.html')





@csrf_exempt
def diabetes_pre(request):
    template = loader.get_template('pages/diabetesForm.html')
    pregnancies = request.POST.get("Pregnancies")
    glucose = request.POST.get("Glucose")
    bloodpressure = request.POST.get("BloodPressure")
    BMI = request.POST.get("BMI")
    DiabetesPedigreeFunction = request.POST.get("DiabetesPedigreeFunction")
    age = request.POST.get("Age")

    diabetes_data = [
        [pregnancies, glucose, bloodpressure, BMI, DiabetesPedigreeFunction, age]]
    diabetes_model = joblib.load(r'diabetes.pkl')
    # diabetes_model = pd.read_pickle('r',"diabetes_model.pickle")
    prediction = diabetes_model.predict(
        [[pregnancies, glucose, bloodpressure, BMI, DiabetesPedigreeFunction, age]])
    outcome = prediction


    if outcome == 1:
        result = "Diabetic"
    elif outcome == 0:
        result = "Not Diabetic"


    return HttpResponse(template.render({'result':result}))
