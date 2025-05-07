from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.select_card, name="select_card"),
    path("home/", views.home, name="home"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("update_message/", views.update_message, name="update_message"),
    path('logout/', views.logout_view, name='logout'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('instructions/', views.instructions, name='instructions')
]

# urlpatterns=[
#     path("home", views.home, name="home"),
#     path("join", views.join, name="join"),
#     path("make", views.make, name="make"),
#     path("show", views.show, name="show"),
#     path("si", views.si, name="si"),
#     path("sign", views.sign, name="sign")
    
# ] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)