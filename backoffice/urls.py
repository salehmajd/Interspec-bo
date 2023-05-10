from django.urls import path

from backoffice.views import HomePageView, SearchResultsView, detail

urlpatterns = [
    path("", HomePageView, name="home"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("detail/<int:emprunt_id>/", detail, name="detail")
]