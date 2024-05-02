from django.shortcuts import render, redirect
from django.http import HttpResponse
from firewall_apply_app.forms import FirewallApplyForm
from firewall_apply_app.models import FirewallApply
import datetime
from django.views.generic import ListView

#def home(request):
#    return render(
#        request,
#        'firewall_apply_app/home.html'
#    )

class HomeListView(ListView):
    model = FirewallApply

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def apply(request):
    return render(
        request,
        'firewall_apply_app/apply.html'
    )

def applying(request):
    form = FirewallApplyForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            apply = form.save(commit=False)
            apply.status = 1
            apply.apply_date = datetime.datetime.now()
            apply.save()
            return redirect("home")
        else:
            return render(
                request,
                'firewall_apply_app/apply.html',
                {"form":form}
            )
    else:
        return render(
            request,
            'firewall_apply_app/apply.html',
            {"form":form}
        )
    