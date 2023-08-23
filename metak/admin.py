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

# resource for import export plugin
class MetakinhshResource(resources.ModelResource):
    # used to declare foreign key @ field person
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(User, field='id'))
    
    class Meta:
        model = Metakinhsh
        exclude = ('id',)
    
    # use dehydrate to display full name instead of person id
    def dehydrate_person(self, metakinhsh):
        full_name = getattr(metakinhsh.person, 'last_name') + ' ' + getattr(metakinhsh.person, 'first_name')
        return '%s' % full_name


class MetakinhshAdmin(ImportExportModelAdmin):
    resource_class = MetakinhshResource
    list_display = ('id','get_user', 'metak_to', 'date_from', 'egkrish','pragmat','km','handler')
    list_display_links = ('id','get_user')
    list_filter = [
        ("date_from", DateRangeFilterBuilder()),
        ("km", NumericRangeFilterBuilder()),
        ("person__last_name", DropdownFilter)
    ]
    search_fields = ['metak_to']
    list_per_page=25

    # construct get_user column to display full name
    def get_user(self, obj):
        return f'{obj.person.last_name} {obj.person.first_name}'
    get_user.short_description = 'Χρήστης'
    get_user.admin_order_field = 'person__last_name'

    # make person a readonly field for manager
    manager_readonly = ('person',)

    def get_readonly_fields(self, request, obj=None):
        if obj and request.user.groups.filter(name='managers').exists():
            return self.manager_readonly
        else:
            return super(MetakinhshAdmin, self).get_readonly_fields(request, obj=obj)

admin.site.register(Metakinhsh, MetakinhshAdmin)