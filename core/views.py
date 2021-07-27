from django.shortcuts import render
from django.views import View
from .forms import CoreForm
from .models import Core


class CoreView(View):
    template_name = "core/core.html"
    form_class = CoreForm

    def get(self, request):
        form = self.form_class()
        queryset = Core.objects.all()
        context = {"form": form, "query": queryset}

        return render(self.request, self.template_name, context)
