from django.core.exceptions import ObjectDoesNotExist
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Main
from .forms import ArduinoForm, ArdCustomtextedit


# Create your views here.
def index(request):
    if request.method == 'GET':
        if 'temperature' in request.GET and 'mode' in request.GET:
            temperature = request.GET.get('temperature')
            mode = request.GET.get('mode')
            ar1 = Main(temperature=temperature, mode=mode)
            ar1.save()
            return HttpResponse('Okay')
        if 'nfcode' in request.GET:
            nfcode = request.GET.get('nfcode')
            ar2 = Main(activated_codes=nfcode)
            ar2.save()
            return HttpResponse('Okaynfc')

    editcustomtextfrom = ArdCustomtextedit()

    if Main.objects.all().exists():

        try:
            obj = Main.objects.filter(temperature__isnull=False).latest('date')
            obj = Main.objects.filter(mode__isnull=False).latest('date')
        except ObjectDoesNotExist:
            return HttpResponse('<h1>I don`t have temperature or mode. </h1><h6>Я жду эти данные от ардуинки..</h6>')

        obj = Main.objects.filter(temperature__isnull=False).latest('date')
        temperature = obj.temperature
        obj = Main.objects.filter(mode__isnull=False).latest('date')
        mode = obj.mode

        temperature = obj.temperature
        obj = Main.objects.filter(custom_text__isnull=False).latest('date')
        custom_text = obj.custom_text
        obj = Main.objects.filter(links__isnull=False).latest('date')
        links = obj.links
        obj = Main.objects.filter(weather__isnull=False).latest('date')
        weather = obj.weather
        obj = Main.objects.filter(nfc_codes__isnull=False).latest('date')
        nfc_codes = obj.nfc_codes

        pc = 'pc1'
        pc2 = 'pc2'
        text = links
        r1 = text.split(',')
        res = []
        url = 'not found.'
        url2 = 'not found.'
        for e in r1:
            r = e.split('#')
            res.append(r)
        for word in res:
            if pc in word:
                url = word[1]
            if pc2 in word:
                url2 = word[1]
        link_pc1 = url
        link_pc2 = url2

        data = {
            'havestart': True,
            'editcustomtextfrom': editcustomtextfrom,
            'temperature': temperature,
            'custom_text': custom_text,
            'mode': mode,
            'weather': weather,
            'nfc_codes': nfc_codes,
            'link_pc1': link_pc1,
            'link_pc2': link_pc2,
        }
    else:
        if request.method == 'POST':
            form = ArduinoForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('thanks')
        else:
            form = ArduinoForm()
        data = {
            'form': form,
            'havestart': False,
        }

    return render(request, 'temp_arduino/index.html', data)


def editcustomtext(request):
    obj = Main.objects.filter(mode__isnull=False).latest('date')

    if '3' in obj.mode:
        if request.method == 'POST':
            form = ArdCustomtextedit(request.POST)
            if form.is_valid():
                form.save()
                return redirect('ardfin')
        else:
            form = ArdCustomtextedit()
    else:
        return HttpResponse('NOT 3 MODE! Error')


def modes(request):
    obj = Main.objects.filter(mode__isnull=False).latest('date')
    return HttpResponse(obj.mode)


def arcustomtext(request):
    obj = Main.objects.filter(custom_text__isnull=False).latest('date')
    return HttpResponse(obj.custom_text)


def delwelcome(request):
    Main.objects.all().delete()
    return HttpResponse('Successfully Cleaned!')


def weathr(request):
    obj = Main.objects.filter(weather__isnull=False).latest('date')
    return HttpResponse(obj.weather)


def nfcodes(request):
    obj = Main.objects.filter(nfc_codes__isnull=False).latest('date')
    return HttpResponse(obj.nfc_codes)


def links(request):
    obj = Main.objects.filter(links__isnull=False).latest('date')
    return HttpResponse(obj.links)


def temperature(request):
    obj = Main.objects.filter(temperature__isnull=False).latest('date')
    return HttpResponse(obj.temperature)
