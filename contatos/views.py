from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

def index(request):
	
    contatos = Contato.objects.all()
    return render (request, 'contatos/index.html', {
        'contatos': contatos
    })
	


def ver_contato(request, contato_id):
	#contato = Contato.objects.get(id=contato_id)
	contato = get_object_or_404(Contato, id=contato_id)


	return render(request, 'contatos/ver_contato.html',{
		'contato': contato
	
	})



