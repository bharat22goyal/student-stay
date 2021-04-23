from django.urls import path
from .views import OwnerListView, OwnerView

urlpatterns = [
    path('', OwnerListView.as_view()),
    path('<pk>', OwnerView.as_view()),
]
