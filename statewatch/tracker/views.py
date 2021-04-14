from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from tracker.models import State, Legislature, Bills, Favorites

# GET and POST constants because I'm lazy
CONSTPOST = "POST"
CONSTGET = "GET"

# Create your views here.
def index(request):
    return render(request, "tracker/index.html")

def category_of_states(request):
    list_of_states = State.objects.order_by('state')
    list_of_bills = Bills.objects.order_by('legislature')
    states_with_bills = []
    for state in list_of_states:
        # print("state " + str(state.state))
        for bill in list_of_bills:
            if state.state == bill.legislature.state.state:
                states_with_bills.append(state)
                break
    # print(states_with_bills)
    return render(request, "tracker/states.html", {'states':states_with_bills})

def bills_by_state(request, state):
    list_of_bills = Bills.objects.order_by('code').filter(legislature__state__state=state)
    return render(request, "tracker/state_bills.html", {'bills':list_of_bills, 'state':state})

def bill_page(request, state, code):
    bill = Bills.objects.get(code=code)
    
    # check if the bill is already saved by the user
    if Favorites.objects.filter(user=request.user, saved_bill=bill).exists():
        is_saved = True
    else:
        is_saved = False

    # run if the user clicked the "save" button
    if request.method == CONSTPOST:
        if request.POST.get("save"):
            Favorites.objects.get_or_create(user=request.user, saved_bill=bill)
            return redirect(reverse("tracker:bill_page", args=[state, code]))
        elif request.POST.get("unsave"):
            Favorites.objects.get(user=request.user, saved_bill=bill).delete()
            return redirect(reverse("tracker:bill_page", args=[state, code]))

    return render(request, "tracker/bill.html", {'bill':bill, 'state':bill.legislature.state, 'code':code, 'saved':is_saved})

def results(request):
    return render(request, "tracker/results.html")

def user_favorites(request):
    list_of_favorites = Favorites.objects.order_by('saved_bill').filter(user__username=request.user.username)
    return render(request, "tracker/user_favorites.html", {'favorites':list_of_favorites})