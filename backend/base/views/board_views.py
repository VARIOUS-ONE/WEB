from django.shortcuts import render
from base.models import Blacklist
def board_list(request):
    queryset = Blacklist.objects.all()
    print(queryset)
    return render(request, "board_list.html", {"boards": queryset})