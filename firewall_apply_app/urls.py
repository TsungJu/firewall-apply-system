from re import template
from django.urls import path
from firewall_apply_app import views
from firewall_apply_app.models import FirewallApply

home_list_view = views.HomeListView.as_view(
    queryset=FirewallApply.objects.order_by("-apply_date")[:5],
    context_object_name="apply_list",
    template_name="firewall_apply_app/home.html"
)

urlpatterns = [
    path('',home_list_view,name="home"),
    path('apply/',views.apply,name="apply"),
    path('applying/',views.applying,name="applying")
]
