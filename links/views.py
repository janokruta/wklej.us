from django.shortcuts import render, redirect
from django.utils import timezone

from links.forms import LinkCreateForm


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
