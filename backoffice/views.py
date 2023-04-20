from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from backoffice.models import Adherent


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Adherent
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Adherent.objects.filter(Q(nom__icontains=query) | Q(prenom__icontains=query))
        return object_list
