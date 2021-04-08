from django.shortcuts import render
from django.http import HttpResponse
from tracker.models import State, Legislature, Bills

# Create your views here.
def index(request):
    return render(request, "tracker/index.html")

def category_of_states(request):
    list_of_states = State.objects.order_by('state')
    list_of_bills = Bills.objects.order_by('legBody')
    states_with_bills = []
    for state in list_of_states:
        # print("state " + str(state.state))
        for bill in list_of_bills:
            if state.state == bill.legBody.state.state:
                states_with_bills.append(state)
                break
    # print(states_with_bills)
    return render(request, "tracker/states.html", {'states':states_with_bills})

def bills_by_state(request, state):
    list_of_bills = Bills.objects.order_by('code').filter(legBody__state__state=state)
    return render(request, "tracker/state_bills.html", {'bills':list_of_bills, 'state':state})

def bill_page(request, state, code):
    bill = Bills.objects.get(code=code)
    return render(request, "tracker/bill.html", {'bill':bill, 'state':bill.legBody.state, 'code':code})

def results(request):

    return render(request, "tracker/results.html")