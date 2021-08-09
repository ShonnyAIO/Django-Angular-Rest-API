from django.conf.urls import url
from django.urls.resolvers import URLPattern
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r"^department/$", views.departmentApi),
    url(r"^department/([0-9]+)$", views.departmentApi),
    url(r"^employee/$", views.EmployeeApi),
    url(r"^employee/([0-9]+)$", views.EmployeeApi),
    url(r"^saveFile$", views.saveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
