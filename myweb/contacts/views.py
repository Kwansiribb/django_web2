from django.http import HttpResponse
from django.template import loader

def contacts(request):
  template = loader.get_template('contacts.html')
  return HttpResponse(template.render())