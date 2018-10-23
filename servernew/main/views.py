from django.shortcuts import render
from django.template import Template , Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse

def main(request):
    template = get_template('main/index.html')
    context = {
        'name': 'Jhon',
        'title': 'TITILE',
        'subtitle': 'SUBTITLE'
    }
    response_string = template.render(context)

    return HttpResponse(response_string)

def contacts(request):
    context = {
        'contacts': [
            ' Contact1',
            'Contact2',
            'Contact3'
        ]
    }
    response_string = render_to_string('main/contacts.html', context)

    return HttpResponse(response_string)

def about(request):
    context = {
        'name': 'Jhon',
        'text': '123'
    }
    response_string = render_to_string('main/about.html', context)

    return render(request, 'main/about.html', context)