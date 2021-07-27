from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import View
from .models import FibNum


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


class FibboApiView(View):
    def get(self, request, num):
        FibNum.objects.create(
            num = num
        )
        
        print("DB Num-->", FibNum.objects.all())

        result = [i for i in fib(num)] 
        print(result)

        return JsonResponse({"message": result}, safe=False)
