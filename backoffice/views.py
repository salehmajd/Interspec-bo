from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from backoffice.models import Adherent, emprunt


# Create your views here.

def HomePageView(request):
    adherents = Adherent.objects.all()
    template_name = 'home.html'
    dernier_emprunt_list = emprunt.objects.all()[:5]
    context = {'adherents': adherents, 'dernier_emprunt_list': dernier_emprunt_list}
    return render(request, template_name, context)

class SearchResultsView(ListView):
    model = Adherent
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Adherent.objects.filter(Q(nom__icontains=query) | Q(prenom__icontains=query))
        return object_list
