from django.shortcuts import render
from .models import Medicine, Employee, Dealer, Price, Pharmacy, TODO, Attendance, Bill, Customer
from django.views import generic
from django.urls import reverse_lazy
from django_filters import views
from .filters import MedicineFilter, DealerFilter, EmployeeFilter, TodoFilter, AttendanceFilter, BillFilter, CustomerFilter


def show_index(request):
    context = {
        'No_Of_Medicine': Medicine.objects.all().count(),
        'No_Of_Bill': Bill.objects.all().count(),
        'No_Of_Customer': Customer.objects.all().count(),
        'No_Of_Dealer': Dealer.objects.all().count(),
        'No_Of_Employee': Employee.objects.all().count(),
        'No_Of_TODO': TODO.objects.all().count(),
    }
    return render(request, 'pharmacyapp/index.html', context)


class MedicineListView(views.FilterView):
    filterset_class = MedicineFilter
    paginate_by = 10
    template_name = 'pharmacyapp/medicine_list.html'


class MedicineCreateView(generic.CreateView):
    model = Medicine
    fields = ['code', 'name', 'stock', 'description']
    success_url = reverse_lazy('medicine-list')


class MedicineDeleteView(generic.DeleteView):
    model = Medicine
    success_url = reverse_lazy('medicine-list')


class MedicineUpdateView(generic.UpdateView):
    model = Medicine
    fields = ['code', 'name', 'stock', 'description']
    success_url = reverse_lazy('medicine-list')


class MedicineDetailView(generic.DetailView):
    model = Medicine


class PriceCreateView(generic.CreateView):
    model = Price
    fields = ['dealer','price']

    def form_valid(self, form):
        form.instance.medicine = Medicine.objects.get(pk=self.kwargs['pk1'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('medicine-detail', kwargs={'pk':self.kwargs['pk1']})


class PriceUpdateView(generic.UpdateView):
    model = Price
    fields = ['dealer', 'price']

    def get_success_url(self):
        return reverse_lazy('medicine-detail', kwargs={'pk':self.kwargs['pk1']})


class PriceDeleteView(generic.DeleteView):
    model = Price

    def get_success_url(self):
        return reverse_lazy('medicine-detail', kwargs={'pk':self.kwargs['pk1']})


class DealerDetailView(generic.DetailView):
    model = Dealer


class DealerListView(views.FilterView):
    filterset_class = DealerFilter
    paginate_by = 10
    template_name = 'pharmacyapp/dealer_list.html'


class DealerCreateView(generic.CreateView):
    model = Dealer
    fields = ['name', 'address', 'phone_no', 'email']
    success_url = reverse_lazy('dealer-list')


class DealerUpdateView(generic.UpdateView):
    model = Dealer
    fields = ['name', 'address', 'phone_no', 'email']
    success_url = reverse_lazy('dealer-list')


class DealerDeleteView(generic.DeleteView):
    model = Dealer
    success_url = reverse_lazy('dealer-list')


class EmployeeDetailView(generic.DetailView):
    model = Employee


class EmployeeListView(views.FilterView):
    filterset_class = EmployeeFilter
    paginate_by = 10
    template_name = 'pharmacyapp/employee_list.html'


class EmployeeCreateView(generic.CreateView):
    model = Employee
    fields = ['name', 'address', 'phone_no', 'email', 'id_proof', 'proof_unique_no']
    success_url = reverse_lazy('employee-list')


class EmployeeUpdateView(generic.UpdateView):
    model = Employee
    fields = ['name', 'address', 'phone_no', 'email', 'id_proof', 'proof_unique_no']
    success_url = reverse_lazy('employee-list')


class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    success_url = reverse_lazy('employee-list')


class TodoListView(views.FilterView):
    filterset_class = TodoFilter
    paginate_by = 10
    template_name = 'pharmacyapp/todo_list.html'


class TodoCreateView(generic.CreateView):
    model = TODO
    fields = ['title', 'date', 'employees', 'description']
    success_url = reverse_lazy('todo-list')


class TodoDeleteView(generic.DeleteView):
    model = TODO
    success_url = reverse_lazy('todo-list')


class TodoUpdateView(generic.UpdateView):
    model = TODO
    fields = ['title', 'date', 'employees', 'description']
    success_url = reverse_lazy('todo-list')


class TodoDetailView(generic.DetailView):
    model = TODO


class PharmacyUpdateView(generic.UpdateView):
    model = Pharmacy
    fields = ['shop_name', 'address', 'owner_name', 'phone_no']
    success_url = reverse_lazy('index')


class AttendanceListView(views.FilterView):
    filterset_class = AttendanceFilter
    paginate_by = 10
    template_name = 'pharmacyapp/attendance_list.html'


class AttendanceCreateView(generic.CreateView):
    model = Attendance
    fields = ['date', 'employees']
    success_url = reverse_lazy('attendance-list')


class AttendanceDeleteView(generic.DeleteView):
    model = Attendance
    success_url = reverse_lazy('attendance-list')


class AttendanceUpdateView(generic.UpdateView):
    model = Attendance
    fields = ['date', 'employees']
    success_url = reverse_lazy('attendance-list')


class AttendanceDetailView(generic.DetailView):
    model = Attendance


class BillListView(views.FilterView):
    filterset_class = BillFilter
    paginate_by = 10
    template_name = 'pharmacyapp/bill_list.html'


class BillCreateView(generic.CreateView):
    model = Bill
    fields = ['customer', 'amount', 'date', 'employee']
    success_url = reverse_lazy('bill-list')


class BillDeleteView(generic.DeleteView):
    model = Bill
    success_url = reverse_lazy('bill-list')


class BillUpdateView(generic.UpdateView):
    model = Bill
    fields = ['customer', 'amount', 'date', 'employee']
    success_url = reverse_lazy('bill-list')


class BillDetailView(generic.DetailView):
    model = Bill


class CustomerListView(views.FilterView):
    filterset_class = CustomerFilter
    paginate_by = 10
    template_name = 'pharmacyapp/customer_list.html'


class CustomerCreateView(generic.CreateView):
    model = Customer
    fields = ['name', 'address', 'phone_no', 'email']
    success_url = reverse_lazy('customer-list')


class CustomerDeleteView(generic.DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')


class CustomerUpdateView(generic.UpdateView):
    model = Customer
    fields = ['name', 'address', 'phone_no', 'email']
    success_url = reverse_lazy('customer-list')


class CustomerDetailView(generic.DetailView):
    model = Customer
