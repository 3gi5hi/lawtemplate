from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class Index (View):
    template_name = 'home.html'

    def get(self, request):

        return render(request, self.template_name)

    def post(self, request):
        pass

class AddTemplates (View):
    template_name = 'addtemplates.html'

    def get(self, request):

        return render(request, self.template_name)

    def post(self, request):
        pass
