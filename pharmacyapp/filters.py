import django_filters
from .models import Medicine, Employee, Dealer, Price, Pharmacy, TODO, Attendance, Bill, Customer


class MedicineFilter(django_filters.FilterSet):
    code = django_filters.NumberFilter(lookup_expr='icontains', label='Code')
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')

    class Meta:
        model = Medicine
        fields = ['code', 'name']


class DealerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')

    class Meta:
        model = Dealer
        fields = ['name', 'email', 'phone_no']


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')

    class Meta:
        model = Employee
        fields = ['name', 'proof_unique_no', 'email', 'phone_no']


class TodoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')

    class Meta:
        model = TODO
        fields = ['title', 'date', 'employees']


class AttendanceFilter(django_filters.FilterSet):

    class Meta:
        model = Attendance
        fields = ['date', 'employees']


class BillFilter(django_filters.FilterSet):

    class Meta:
        model = Bill
        fields = ['customer', 'date', 'employee']


class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')

    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_no']
