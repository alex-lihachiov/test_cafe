from django.shortcuts import render
from django.views import View

from .models import Cafe


class CafeView(View):
    """Список кафешек"""
    def get(self,request):
        cafe = Cafe.objects.all()
        return render(request, "cafe/cafe.html", {"cafe_list": cafe})
