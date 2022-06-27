from django.urls import path
from . import views

urlpatterns = [
    #path("register-staff/", views.reg_staff),
    path("register-customer/", views.reg_cust),
    path("", views.home),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("product/<str:name>/", views.product),
    path("product/<str:name>/order", views.order),
    path("login/<str:loc>", views.login_redir),
    path("login/product/<str:loc>", views.login_redir_product),
    path("orders/", views.view_orders),
    path("contact/", views.contact_page),
    path("Feedback/", views.feedback_page),
    path("Service/", views.Service_page),
]
