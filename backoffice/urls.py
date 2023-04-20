from django.urls import path

from backoffice.views import HomePageView, SearchResultsView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]