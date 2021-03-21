from django.urls import path
from django.views.decorators.cache import never_cache

from . import views

urlpatterns = [
    path('', never_cache(views.index), name='ardfin'),
    path('delwelcomecodes/', never_cache(views.delwelcome), name='delwelc'),
    path('weathr/', never_cache(views.weathr)),
    path('nfcodes/', never_cache(views.nfcodes)),
    path('links/', never_cache(views.links)),
    path('arcustomtext/', never_cache(views.arcustomtext)),
    path('modes/', never_cache(views.modes)),
    path('editcustomtext/', never_cache(views.editcustomtext), name='editcustomtext'),
    path('temperature/', never_cache(views.temperature)),

]
