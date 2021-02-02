from django.shortcuts import render, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.http import Http404
from django.views.generic import(
    ListView,
    UpdateView,
    DetailView
)


# class PeopleListView(ListView):
#     template_name = "people.html"
#     queryset = Person.objects.all()
class PersonDetailView(DetailView):
    template_name = "person.html"
    queryset = Person.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Person, id=id_)

def people_list_view(request):
    queryset = Person.objects.all()
    context = {
        'object': queryset
    }
    return render(request, 'people.html', context)
# Create your views here.

def create_person_view(request, *args, **kwargs):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonForm()
    context = {
        'form': form
    }
    return render(request, "add_person.html", context)
