from django.urls import path
from .views import AddDatatype,AddFormField,AddForm

urlpatterns = [
    path('AddForm', AddForm.as_view()),
    path('AddDatatype', AddDatatype.as_view()),
    path('AddFormField', AddFormField.as_view()),

]