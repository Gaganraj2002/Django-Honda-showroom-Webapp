from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.db.models import Model as M
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
# Create your views here.


@login_required(login_url='login')
def reg_staff(request):
    staff_regestration = False
    if request.session.has_key("type"):
        if request.session["type"] == "staff":
            staff_regestration = True
        else:
            staff_regestration = False
    print(request)
    if request.method == "POST":
        form = forms.StaffForm(request.POST)
        print(request, form.is_valid())
        if form.is_valid():
            obj = form.save()
            obj = forms.StaffForm()
            print(form.cleaned_data)
            return HttpResponseRedirect("/home")
    form = forms.StaffForm()
    extra_data = {"form": form, "regstaff": staff_regestration}
    return render(request, "register_staff.html", extra_data)


def reg_cust(request):
    staff_regestration = False
    if request.session.has_key("type"):
        if request.session["type"] == "staff":
            staff_regestration = True
        else:
            staff_regestration = False
    if request.method == "POST":
        form = forms.CustomerForm(request.POST)
        print(request, form.is_valid())
        if form.is_valid():
            obj = form.save()
            obj = forms.CustomerForm()
            print(form.cleaned_data)
            return HttpResponseRedirect("/login")
    form = forms.CustomerForm()
    extra_data = {"form": form, "regstaff": staff_regestration}
    return render(request, "register_cust.html", extra_data)


def home(request):
    login_logout = None
    staff_regestration = False
    if request.session.has_key("mail"):
        login_logout = "logout"
    else:
        login_logout = "login"
    staff_regestration = False
    if request.session.has_key("type"):
        if request.session["type"] == "staff":
            staff_regestration = True
        else:
            staff_regestration = False
    vehicles = models.VehicleDetails.objects.all()
    print(vehicles)
    extra_data = {"regstaff": staff_regestration,
                  "login": login_logout, "product": vehicles}
    return render(request, "home.html", extra_data)


def login(request):
    CUST = STAFF = False
    if request.session.has_key("mail") and request.session.has_key("type"):
        print(request.session["mail"], request.session["type"])
        return HttpResponseRedirect("/")
    if (not request.session.has_key("mail")) and (not request.session.has_key("type")):
        if request.method == "POST":
            mail = request.POST["mail"]
            pwd = request.POST["pwd"]
            print(mail, pwd)
            form = forms.LoginForm(request.POST)
            try:
                customers = models.Customer.objects.get(mail=mail)
                CUST = True
                print(customers)
            except:
                try:
                    staff = models.Staff.objects.get(mail=mail)
                    STAFF = True
                    print(staff)
                except:
                    extra_data = {"details": "Details Not Found"}
                    return render(request, "login.html", extra_data)
            if form.is_valid():
                username = mail
                request.session['mail'] = username
                if CUST:
                    request.session['type'] = "cust"
                    print(CUST)
                elif STAFF:
                    request.session['type'] = "staff"
                    print(STAFF)
                return HttpResponseRedirect("/")
        form = forms.LoginForm()
        extra_data = {"form": form}
        return render(request, "login.html", extra_data)

    else:
        form = forms.LoginForm()
        extra_data = {"form": form}
        return render(request, "login.html", extra_data)


def login_redir(request, loc):
    CUST = STAFF = False
    print(loc)
    if request.session.has_key("mail") and request.session.has_key("type"):
        print(request.session["mail"], request.session["type"])
        return HttpResponseRedirect("/")
    if (not request.session.has_key("mail")) and (not request.session.has_key("type")):
        if request.method == "POST":
            mail = request.POST["mail"]
            pwd = request.POST["pwd"]
            print(mail, pwd)
            form = forms.LoginForm(request.POST)
            try:
                customers = models.Customer.objects.get(mail=mail)
                CUST = True
                print(customers)
            except:
                try:
                    staff = models.Staff.objects.get(mail=mail)
                    STAFF = True
                    print(staff)
                except:
                    print("")
                    return HttpResponse("details not found")
            if form.is_valid():
                username = mail
                request.session['mail'] = username
                if CUST:
                    request.session['type'] = "cust"
                    print(CUST)
                elif STAFF:
                    request.session['type'] = "staff"
                    print(STAFF)
                return HttpResponseRedirect("/"+loc)
        form = forms.LoginForm()
        extra_data = {"form": form}
        return render(request, "login.html", extra_data)

    else:
        form = forms.LoginForm()
        extra_data = {"form": form}
        return render(request, "login.html", extra_data)


def login_redir_product(request, loc):
    CUST = STAFF = False
    print(loc)
    if request.session.has_key("mail") and request.session.has_key("type"):
        print(request.session["mail"], request.session["type"])
        return HttpResponseRedirect("/")
    if (not request.session.has_key("mail")) and (not request.session.has_key("type")):
        if request.method == "POST":
            mail = request.POST["mail"]
            pwd = request.POST["pwd"]
            print(mail, pwd)
            form = forms.LoginForm(request.POST)
            try:
                customers = models.Customer.objects.get(mail=mail)
                CUST = True
                print(customers)
            except:
                try:
                    staff = models.Staff.objects.get(mail=mail)
                    STAFF = True
                    print(staff)
                except:
                    print("")
                    return HttpResponse("details not found")
            if form.is_valid():
                username = mail
                request.session['mail'] = username
                if CUST:
                    request.session['type'] = "cust"
                    print(CUST)
                elif STAFF:
                    request.session['type'] = "staff"
                    print(STAFF)
                return HttpResponseRedirect("/product/"+loc)
        form = forms.LoginForm()
        extra_data = {"form": form}
        return render(request, "login.html", extra_data)

    else:
        form = forms.LoginForm()
        extra_data = {"form": form}
        return render(request, "login.html", extra_data)


def logout(request):
    try:
        del request.session['mail']
        del request.session['type']
        request.session.modified = True
        return render(request, "logout.html")
    except Exception as e:
        print(e, "logout")
        return HttpResponseRedirect("/")


def product(request, name):
    login_logout = None
    staff_regestration = False
    if request.session.has_key("mail"):
        login_logout = "logout"
    else:
        login_logout = "login"
        return HttpResponseRedirect("/login/product/{}".format(name))
    staff_regestration = False
    if request.session.has_key("type"):
        if request.session["type"] == "staff":
            staff_regestration = True
        else:
            staff_regestration = False
    vehicles = models.VehicleDetails.objects.get(VehicleName=name)
    stocks = models.Stock.objects.get(VehicleNo=vehicles.VehicleNo)
    extra_data = {"regstaff": staff_regestration,
                  "login": login_logout, "vehicle": vehicles,
                  "stock": stocks}
    return render(request, "product_page.html", extra_data)


def order(request, name):
    login_logout = None
    staff_regestration = False
    order_status = None
    if request.session.has_key("mail"):
        login_logout = "logout"
    else:
        login_logout = "login"
        return HttpResponseRedirect("/login/product/"+name)
    staff_regestration = None
    if request.session.has_key("type"):
        if request.session["type"] == "staff":
            staff_regestration = True
        else:
            staff_regestration = False
    vehicle = models.VehicleDetails.objects.get(VehicleName=name)
    booking = None
    address = None
    if staff_regestration:
        booking = models.Bookingbystaff()
        staf = models.Staff.objects.get(mail=request.session["mail"])
        stock = models.Stock.objects.get(VehicleNo=vehicle.VehicleNo)
        if stock.Stock > 0:
            stock.Stock -= 1
            stock.save()
            booking.Stockid = stock
            booking.Staffid = staf
            address = staf.Address
            booking.save()
            booking = models.Bookingbystaff.objects.filter(
                Staffid=staf).filter(Stockid=stock).order_by("-Bookingid")[0]
            order_status = True
        else:
            order_status = False
    else:
        booking = models.Bookingbycustomer()
        cust = models.Customer.objects.get(mail=request.session["mail"])
        stock = models.Stock.objects.get(VehicleNo=vehicle.VehicleNo)
        if stock.Stock > 0:
            stock.Stock -= 1
            stock.save()
            booking.Stockid = stock
            booking.Custid = cust
            address = cust.Address
            booking.save()
            booking = models.Bookingbycustomer.objects.filter(
                Custid=cust).filter(Stockid=stock).order_by("-Bookingid")[0]
            order_status = True
        else:
            order_status = False
    print(booking)
    extra_data = {"regstaff": staff_regestration, "login": login_logout,
                  "vehicle": vehicle, "order": booking, "address": address, "status": order_status}
    return render(request, "order.html", extra_data)


def view_orders(request):
    login_logout = None
    staff_regestration = False
    ret_orders = None
    order_status = None
    if request.session.has_key("mail"):
        login_logout = "logout"
    else:
        login_logout = "login"
        return HttpResponseRedirect("/login")
    staff_regestration = None
    if request.session.has_key("type"):
        if request.session["type"] == "staff":
            staff_regestration = True
        else:
            staff_regestration = False
    if staff_regestration:
        staf = models.Staff.objects.get(mail=request.session["mail"])
        total_orders = models.Bookingbystaff.objects.filter(Staffid=staf)
        ret_orders = []
        for i in total_orders:
            x = models.VehicleDetails.objects.get(
                VehicleNo=i.Stockid.VehicleNo)
            new_lst = [i, x]
            ret_orders.append(new_lst)
    else:
        cust = models.Customer.objects.get(mail=request.session["mail"])
        total_orders = models.Bookingbycustomer.objects.filter(Custid=cust)
        print(total_orders)
        ret_orders = []
        for i in total_orders:
            x = models.VehicleDetails.objects.get(
                VehicleNo=i.Stockid.VehicleNo)
            new_lst = [i, x]
            ret_orders.append(new_lst)
    extra_data = {"regstaff": staff_regestration, "login": login_logout,
                  "orders": ret_orders, "status": order_status}
    return render(request, "show_orders.html", extra_data)


def contact_page(request):
    login_logout = None
    staff_regestration = False
    if request.session.has_key("mail"):
        login_logout = "logout"
    else:
        login_logout = "login"
    staff_regestration = False
    if request.session.has_key("type"):
        if request.session["type"] == "staff":
            staff_regestration = True
        else:
            staff_regestration = False
    extra_data = {"regstaff": staff_regestration,
                  "login": login_logout}

    return render(request, "contact.html", extra_data)


def Service_page(request):
    login_logout = None
    staff_regestration = False
    if request.session.has_key("mail"):
        login_logout = "logout"
    else:
        login_logout = "login"
    staff_regestration = False
    if request.session.has_key("type"):
        if request.session["type"] == "staff":
            staff_regestration = True
        else:
            staff_regestration = False
    extra_data = {"regstaff": staff_regestration,
                  "login": login_logout}
    return render(request, "Service.html", extra_data)


def feedback_page(request):
    login_logout = None
    staff_regestration = False
    if request.session.has_key("mail"):
        login_logout = "logout"
    else:
        login_logout = "login"
    staff_regestration = False
    if request.session.has_key("type"):
        if request.session["type"] == "staff":
            staff_regestration = True
        else:
            staff_regestration = False
    if request.method == "POST":
        form = forms.Feedback_form(request.POST)
        print(request, form.is_valid())
        if form.is_valid():
            obj = form.save()
            obj = forms.Feedback_form()
            return HttpResponseRedirect("/")
    form = forms.Feedback_form()
    extra_data = {"regstaff": staff_regestration,
                  "login": login_logout, "form": form}
    return render(request, "feedback.html", extra_data)
