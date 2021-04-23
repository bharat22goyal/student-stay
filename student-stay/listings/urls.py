from django.urls import path,re_path
from .views import ListingsView, ListingView, SearchView,CollegeView

urlpatterns = [
    path('', ListingsView.as_view()),
    path('search', SearchView.as_view()),
    re_path('^college/(?P<college>.+)/$', CollegeView.as_view()),
    path('<slug>', ListingView.as_view()),
]
