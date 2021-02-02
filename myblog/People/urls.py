from django.urls import path
from .views import(
 people_list_view,
create_person_view,
 PersonDetailView
)

app_name = 'people'
urlpatterns = [
    path('', people_list_view, name="people-view"),
    path('add_person/', create_person_view, name="create"),

    path('<int:id>', PersonDetailView.as_view(), name="detail")
]