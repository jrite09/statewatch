from django.urls import path
from . import views

# neccessary for template tagging
app_name = "tracker"
urlpatterns = [
    path("", views.index, name="index"),
    path("states", views.category_of_states, name="states"),
    path("states/<str:state>/", views.bills_by_state, name="bill_state"),
    path("states/<str:state>/<str:code>/", views.bill_page, name="bill_page"),
    path("favorites", views.user_favorites, name="favorites"),
    path("results", views.results, name="search_results"),
]