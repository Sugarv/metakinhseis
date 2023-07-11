from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
# from django.contrib.admin import DateFieldListFilter
from rangefilter.filters import DateRangeFilterBuilder, NumericRangeFilterBuilder
from django_admin_listfilter_dropdown.filters import DropdownFilter
from django.contrib.auth.models import User
from import_export.widgets import ForeignKeyWidget

# Register your models here.
from .models import Metakinhsh


class MetakinhshResource(resources.ModelResource):
    # used to declare foreign key @ field person
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(User, field='id'))
    
    class Meta:
        model = Metakinhsh


class MetakinhshAdmin(ImportExportModelAdmin):
    resource_class = MetakinhshResource
    list_display = ('id','person', 'metak_to', 'date_from', 'aitiologia','egkrish','pragmat')
    list_filter = [
        ("date_from", DateRangeFilterBuilder()),
        ("km", NumericRangeFilterBuilder()),
        ("person__last_name", DropdownFilter)
    ]
    search_fields = ['metak_to']
    list_per_page=25

admin.site.register(Metakinhsh, MetakinhshAdmin)