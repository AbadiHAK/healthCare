import joblib
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return render(request, "pages/liverForm.html",)


@csrf_exempt
def liver_pre(request):
    template = loader.get_template('pages/liverForm.html')
    Total_Bilirubin = request.POST.get("Total_Bilirubin")
    Direct_Bilirubin = request.POST.get("Direct_Bilirubin")
    Alkaline_Phosphotase = request.POST.get("Alkaline_Phosphotase")
    Alamine_Aminotransferase = request.POST.get("Alamine_Aminotransferase")
    Total_Protiens = request.POST.get("Total_Protiens")
    Albumin = request.POST.get("Albumin")
    Albumin_and_Globulin_Ratio = request.POST.get("Albumin_and_Globulin_Ratio")
    diabetes_data = [
        [Total_Bilirubin, Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase, Total_Protiens, Albumin , Albumin_and_Globulin_Ratio]]
    diabetes_model = joblib.load(r'liver.pkl')
    # diabetes_model = pd.read_pickle('r',"diabetes_model.pickle")
    prediction = diabetes_model.predict(
        [[Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase ,Alamine_Aminotransferase, Total_Protiens, Albumin , Albumin_and_Globulin_Ratio ]])
    outcome = prediction


    if outcome == 1:
        result = "You are ill"
    else:
        result = "Does not have anything"


    return HttpResponse(template.render({'result':result}))

