from django.urls import path
from . import views

# neccessary for template tagging
app_name = "tracker"
urlpatterns = [
    path("", views.index, name="index"),
    path("states", views.category_of_states, name="states"),
    path("states/<str:state>/", views.bills_by_state, name="billState"),
    path("states/<str:state>/<str:code>/", views.bill_page, name="bill_page")
]