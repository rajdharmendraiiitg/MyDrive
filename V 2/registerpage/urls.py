
from django.conf.urls import url
from . import views

urlpatterns = [
    # home/
    url(r'^$', views.home, name="homepage"),

    # home2
    url(r'^home2/$', views.home2, name="loghome"),
    # home/register/
    url(r'^register/$', views.register, name="reg"),

    # home/login
    url(r'^login/$', views.login_user, name="log"),

    #home/logh1
    url(r'^login1/$', views.login_user1, name="logh1"),

    # home/logout
    url(r'^logout/$', views.logout_user, name='out'),

    # home/cars
    url(r'^vehicles/$', views.showcar, name='caaar'),

    # home/rent
    url(r'^rent/$', views.create_rentdata, name='rnt'),

    #home/add
    url(r'^add/$', views.create_adddata, name='add'),

    # home/confirmation
    url(r'^confirm/$', views.confirmation, name='conf'),

    # home/faq
    url(r'^faq/$', views.faq, name='fq'),

    url(r'^history/$', views.history, name='history'),

    url(r'^formpage/$', views.fb, name='feedback')

]
