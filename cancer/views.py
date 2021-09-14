import joblib
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return render(request, "pages/cancerForm.html",)


@csrf_exempt
def cancer_pre(request):
    template = loader.get_template('pages/cancerForm.html')
    concave_points_mean = request.POST.get("concave_points_mean")
    area_mean = request.POST.get("area_mean")
    radius_mean = request.POST.get("radius_mean")
    perimeter_mean = request.POST.get("perimeter_mean")
    concavity_mean = request.POST.get("concavity_mean")

    diabetes_data = [
        [concave_points_mean, area_mean, radius_mean, perimeter_mean, concavity_mean]]
    diabetes_model = joblib.load(r'breast_canser.pkl')
    # diabetes_model = pd.read_pickle('r',"diabetes_model.pickle")
    prediction = diabetes_model.predict(
        [[concave_points_mean, area_mean, radius_mean, perimeter_mean, concavity_mean]])
    outcome = prediction


    if outcome == 1:
        result = "afflicted with breast cancer"
    elif outcome == 0:
        result = "Does not have breast cancer"


    return HttpResponse(template.render({'result':result}))
