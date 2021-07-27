from django.shortcuts import render
from django.views import View
from .forms import CoreForm
from .models import Core
from rest_framework import generics
from .serializers import CoreSerializer

class CoreView(View):
    template_name = "core/core.html"
    form_class = CoreForm

    def get(self, request):
        form = self.form_class()
        queryset = Core.objects.all()
        context = {"form": form, "query": queryset}

        return render(self.request, self.template_name, context)

    
class CoreApiView(generics.ListCreateAPIView):
    serializer_class = CoreSerializer
    queryset = Core.objects.all().order_by("-id")
