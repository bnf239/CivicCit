from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

#required login authentication
@login_required(login_url="/login/")
def pages(request):
    context = {}
    
    try:

        loadTemplate = request.path.split('/')[-1]

        if loadTemplate == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = loadTemplate

        htmlTemplate = loader.get_template('home/' + loadTemplate)
        return HttpResponse(htmlTemplate.render(context, request))

    except template.TemplateDoesNotExist:
        # if the template doesn't exist show 404 page
        htmlTemplate = loader.get_template('home/404page.html')
        return HttpResponse(htmlTemplate.render(context, request))

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    htmlTemplate = loader.get_template('home/index.html')
    return HttpResponse(htmlTemplate.render(context, request))
