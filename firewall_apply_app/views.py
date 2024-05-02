from django.shortcuts import render, redirect
from django.http import HttpResponse
from firewall_apply_app.forms import FirewallApplyForm
from firewall_apply_app.models import FirewallApply
import datetime
from django.views.generic import ListView

import tweepy

consumer_key = '6mPcUdxIP75ArYmI8TGTS7lpA'
consumer_secret = 'jibTKlgvXNolKPC49WI7vIDHY2MMgA3FHSTVpAfiaUuAVlzVpd'
access_token = '1785183665242443776-1cGdHjQx4vaEJhKaWy67QMWYTVzMa2'
access_token_secret = 'RV3lCEoErZsGA6YVPQYOYm3WN7e7V1bUUZgIgsUun6fv1'

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

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

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
    