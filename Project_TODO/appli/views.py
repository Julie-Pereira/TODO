from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def vue_index(request):

    context = {
        'date' : ""
    }
    return render(request, "index.html", context)
