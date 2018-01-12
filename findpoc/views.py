from django.shortcuts import render
from .models import Poc, ExchangeCode, Audit, Links
from .form import SearchForm, UploadForm
from django.template import RequestContext
from django.utils.timezone import now
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required


def audit(request, code, free):
    _ = Audit.objects.filter(id=code)[0]
    poc = Poc(code=now().strftime('%Y%m%H%S%d%M'),bugtype=_.bugtype, version=_.version, another=_.another,
              email=_.email, package=_.package, desc=_.desc, free=bool(free), place=_.place)
    poc.save()
    link = Links(description=_.desc, free=bool(free), title='{cms}-{version}-{bugtype}'.format(
        cms=_.package, version=_.version, bugtype=_.bugtype),url=poc.get_url())
    link.save()
    _.review = 1
    _.save()
    return render_to_response(
        "/admin/audit/",
        {},
        RequestContext(request, {}),
    )


audit = staff_member_required(audit)


# Create your views here.
def index(request):
    data = Poc.objects.order_by('frequency')
    if len(data) > 5:
        data = data[:4]

    context = {'search': data}
    return render(request, 'index.html', context)


def search(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form = SearchForm()
        else:
            keyword = form.cleaned_data['keyword']
            Poc.objects.filter()
    else:
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form = SearchForm()

        # if a GET (or any other method) we'll create a blank for
    return render(request, 'search.html', {'form': form})


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            render(request, 'prompt.html', {'msg': '提交失败', 'url': 'http://127.0.0.1'})
        form.save()
        render(request, 'upload.html')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})


def seepoc(request, code):
    if request.method == 'POST':
        poc = ExchangeCode.objects.filter(code=code)[0]
        if poc.effective:
            poc.effective = False
            poc.pocnumber = code
            poc.frequency += 1
            poc.save()
            poc = Poc.objects.filter(code=code)[0]
            return render(request, 'poc.html', {'poc': poc})
        elif poc.pocnumber == code:
            poc = Poc.objects.filter(code=code)[0]
            poc.frequency += 1
            poc.save()
            return render(request, 'poc.html', {'poc': poc})
        else:
            return render(request, 'error.html', {'code': code})
    else:
        poc = Poc.objects.filter(code=code)[0]
        if poc.free:
            poc.frequency += 1
            poc.save()
            return render(request, 'poc.html', {'poc': poc})
        else:
            return render(request, 'error.html', {'code': code})
