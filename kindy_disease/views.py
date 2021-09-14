import joblib
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return render(request, "pages/kindyForm.html",)


@csrf_exempt
def kindy_pre(request):
    template = loader.get_template('pages/kindyForm.html')
    bp = request.POST.get("bp")
    sg = request.POST.get("sg")
    al = request.POST.get("al")
    su = request.POST.get("su")
    rbc = request.POST.get("rbc")
    pc = request.POST.get("pc")
    pcc = request.POST.get("pcc")
    diabetes_data = [
        [bp, sg,al,su, rbc, pc , pcc]]
    diabetes_model = joblib.load(r'kindy.pkl')
    # diabetes_model = pd.read_pickle('r',"diabetes_model.pickle")
    prediction = diabetes_model.predict(
        [[bp, sg, al ,su, rbc, pc , pcc ]])
    outcome = prediction


    if outcome == 1:
        result = "chronic kidney disease"
    elif outcome == 0:
        result = "Does not have chronic kidney disease"


    return HttpResponse(template.render({'result':result}))

