from django.utils import timezone
from django.views.generic import ListView

from .models import Portfolio


class Home(ListView):
    template_name = 'portfolio/home.html'
    model = Portfolio
    context_object_name = 'Portfolio'
