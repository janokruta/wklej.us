from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from links.forms import LinkCreateForm
from links.models import Link


def add_link(request):
    if request.method == 'POST':
        form = LinkCreateForm(request.POST)
        if form.is_valid():
            link_obj = form.save(commit=False)
            link_obj.timestamp = timezone.now()
            link_obj.save()
            return redirect(link_obj.get_absolute_url())
    else:
        form = LinkCreateForm()
        return render(request, 'links/add_link.html', {'form': form})


def link_view(request, slug):
    link_obj = get_object_or_404(Link, slug=slug)
    context = {
        'text': link_obj.text,
        'timestamp': link_obj.timestamp
    }
    return render(request, 'link_page.html', context)
