from django.test import TestCase
from django.urls import reverse
from .models import Pharmacy, Medicine, Price, Dealer, Employee, TODO, Customer, Bill, Attendance


class PharmacyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Pharmacy.objects.create(shop_name="ABC", address="Chennai", owner_name="XYZ", phone_no=1234567890)

    def test_shop_name_label(self):
        pharmacy = Pharmacy.objects.get(id=1)
        field_label = pharmacy._meta.get_field('shop_name').verbose_name
        self.assertEqual(field_label, 'shop name')

    def test_address_label(self):
        pharmacy = Pharmacy.objects.get(id=1)
        field_label = pharmacy._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_owner_name_label(self):
        pharmacy = Pharmacy.objects.get(id=1)
        field_label = pharmacy._meta.get_field('owner_name').verbose_name
        self.assertEqual(field_label, 'owner name')

    def test_phone_no_label(self):
        pharmacy = Pharmacy.objects.get(id=1)
        field_label = pharmacy._meta.get_field('phone_no').verbose_name
        self.assertEqual(field_label, 'phone no')


class MedicineModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Medicine.objects.create(code=12345, name='Crocin', stock=100, description='Good medicine')

    def test_code_label(self):
        medicine = Medicine.objects.get(id=1)
        field_label = medicine._meta.get_field('code').verbose_name
        self.assertEqual(field_label, 'code')

    def test_name_label(self):
        medicine = Medicine.objects.get(id=1)
        field_label = medicine._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_stock_label(self):
        medicine = Medicine.objects.get(id=1)
        field_label = medicine._meta.get_field('stock').verbose_name
        self.assertEqual(field_label, 'stock')

    def test_description_label(self):
        medicine = Medicine.objects.get(id=1)
        field_label = medicine._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_get_absolute_url(self):
        medicine = Medicine.objects.get(id=1)
        self.assertEqual(medicine.get_absolute_url(), '/pharmacy/medicine/detail/1')

    def test_str(self):
        medicine = Medicine.objects.get(id=1)
        self.assertEqual(str(medicine), 'Crocin')


class DealerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Dealer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_name_label(self):
        dealer = Dealer.objects.get(id=1)
        field_label = dealer._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_address_label(self):
        dealer = Dealer.objects.get(id=1)
        field_label = dealer._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_phone_no_label(self):
        dealer = Dealer.objects.get(id=1)
        field_label = dealer._meta.get_field('phone_no').verbose_name
        self.assertEqual(field_label, 'phone no')

    def test_email_description_label(self):
        dealer = Dealer.objects.get(id=1)
        field_label = dealer._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_get_absolute_url(self):
        dealer = Dealer.objects.get(id=1)
        self.assertEqual(dealer.get_absolute_url(), '/pharmacy/dealer/detail/1')

    def test_str(self):
        dealer = Dealer.objects.get(id=1)
        self.assertEqual(str(dealer), 'ABC')


class PriceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Medicine.objects.create(code=12345, name='Crocin', stock=100, description='Good medicine')
        Dealer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')
        Price.objects.create(medicine=Medicine.objects.get(id=1), dealer=Dealer.objects.get(id=1) , price=100)

    def test_medicine_label(self):
        price = Price.objects.get(id=1)
        field_label = price._meta.get_field('medicine').verbose_name
        self.assertEqual(field_label, 'medicine')

    def test_dealer_label(self):
        price = Price.objects.get(id=1)
        field_label = price._meta.get_field('dealer').verbose_name
        self.assertEqual(field_label, 'dealer')

    def test_price_label(self):
        price = Price.objects.get(id=1)
        field_label = price._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')


class EmployeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')

    def test_name_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_address_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_phone_no_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('phone_no').verbose_name
        self.assertEqual(field_label, 'phone no')

    def test_email_description_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_id_proof_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('id_proof').verbose_name
        self.assertEqual(field_label, 'id proof')

    def test_proof_unique_no_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('proof_unique_no').verbose_name
        self.assertEqual(field_label, 'proof unique no')

    def test_get_absolute_url(self):
        employee = Employee.objects.get(id=1)
        self.assertEqual(employee.get_absolute_url(), '/pharmacy/employee/detail/1')

    def test_str(self):
        employee = Employee.objects.get(id=1)
        self.assertEqual(str(employee), 'ABC')


class TODOModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')
        todo = TODO.objects.create(title='Attendance', date='2021-05-30', description='Take attendance tomorrow')
        todo.employees.add(Employee.objects.get(id=1))

    def test_title_label(self):
        todo = TODO.objects.get(id=1)
        field_label = todo._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_date_label(self):
        todo = TODO.objects.get(id=1)
        field_label = todo._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_employees_label(self):
        todo = TODO.objects.get(id=1)
        field_label = todo._meta.get_field('employees').verbose_name
        self.assertEqual(field_label, 'employees')

    def test_description_label(self):
        todo = TODO.objects.get(id=1)
        field_label = todo._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_get_absolute_url(self):
        todo = TODO.objects.get(id=1)
        self.assertEqual(todo.get_absolute_url(), '/pharmacy/todo/detail/1')

    def test_str(self):
        bill = TODO.objects.get(id=1)
        self.assertEqual(str(bill), 'Attendance')


class CustomerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_name_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_address_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_phone_no_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('phone_no').verbose_name
        self.assertEqual(field_label, 'phone no')

    def test_email_description_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_get_absolute_url(self):
        customer = Customer.objects.get(id=1)
        self.assertEqual(customer.get_absolute_url(), '/pharmacy/customer/detail/1')

    def test_str(self):
        customer = Customer.objects.get(id=1)
        self.assertEqual(str(customer), 'ABC')


class BillModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')
        Bill.objects.create(customer=Customer.objects.get(id=1), employee=Employee.objects.get(id=1), amount=100, date='2021-05-23')

    def test_customer_label(self):
        bill = Bill.objects.get(id=1)
        field_label = bill._meta.get_field('customer').verbose_name
        self.assertEqual(field_label, 'customer')

    def test_employee_label(self):
        bill = Bill.objects.get(id=1)
        field_label = bill._meta.get_field('employee').verbose_name
        self.assertEqual(field_label, 'employee')

    def test_amount_label(self):
        bill = Bill.objects.get(id=1)
        field_label = bill._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

    def test_date_label(self):
        bill = Bill.objects.get(id=1)
        field_label = bill._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_get_absolute_url(self):
        bill = Bill.objects.get(id=1)
        self.assertEqual(bill.get_absolute_url(), '/pharmacy/bill/detail/1')

    def test_str(self):
        bill = Bill.objects.get(id=1)
        self.assertEqual(str(bill), 'ABC')


class AttendanceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')
        attendance = Attendance.objects.create(date='2021-05-30')
        attendance.employees.add(Employee.objects.get(id=1))

    def test_date_label(self):
        attendance = Attendance.objects.get(id=1)
        field_label = attendance._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_employees_label(self):
        attendance = Attendance.objects.get(id=1)
        field_label = attendance._meta.get_field('employees').verbose_name
        self.assertEqual(field_label, 'employees')

    def test_get_absolute_url(self):
        attendance = Attendance.objects.get(id=1)
        self.assertEqual(attendance.get_absolute_url(), '/pharmacy/attendance/detail/1')

    def test_str(self):
        attendance = Attendance.objects.get(id=1)
        self.assertEqual(str(attendance), '2021-05-30')


class IndexViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/index.html')


class MedicineListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_medicines = 13

        for medicine_id in range(number_of_medicines):
            Medicine.objects.create(code=medicine_id, name='Crocin', stock=100, description='Good medicine')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/medicine/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('medicine-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('medicine-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/medicine_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('medicine-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['medicine_list']), 10)

    def test_lists_all_medicine(self):
        response = self.client.get(reverse('medicine-list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['medicine_list']), 3)


class MedicineDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Medicine.objects.create(code=1234, name='Crocin', stock=100, description='Good medicine')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/medicine/detail/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('medicine-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('medicine-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/medicine_detail.html')


class MedicineDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Medicine.objects.create(code=1234, name='Crocin', stock=100, description='Good medicine')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/medicine/delete/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('medicine-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('medicine-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/medicine_confirm_delete.html')


class MedicineUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Medicine.objects.create(code=1234, name='Crocin', stock=100, description='Good medicine')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/medicine/update/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('medicine-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('medicine-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/medicine_form.html')


class MedicineCreateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Medicine.objects.create(code=1234, name='Crocin', stock=100, description='Good medicine')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/medicine/create')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('medicine-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('medicine-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/medicine_form.html')


class DealerListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_dealers = 13

        for dealer_id in range(number_of_dealers):
            Dealer.objects.create(name=str(dealer_id), address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/dealer/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('dealer-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('dealer-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/dealer_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('dealer-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['dealer_list']), 10)

    def test_lists_all_dealers(self):
        response = self.client.get(reverse('dealer-list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['dealer_list']), 3)


class DealerDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Dealer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/dealer/detail/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('dealer-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('dealer-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/dealer_detail.html')


class DealerDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Dealer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/dealer/delete/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('dealer-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('dealer-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/dealer_confirm_delete.html')


class DealerUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Dealer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/dealer/update/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('dealer-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('dealer-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/dealer_form.html')


class DealerCreateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Dealer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/dealer/create')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('dealer-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('dealer-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/dealer_form.html')


class PharmacyUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Pharmacy.objects.create(shop_name="ABC", address="Chennai", owner_name="XYZ", phone_no=1234567890)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/pharmacy/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('pharmacy', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('pharmacy', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/pharmacy_form.html')


class PriceDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Medicine.objects.create(code=12345, name='Crocin', stock=100, description='Good medicine')
        Dealer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')
        Price.objects.create(medicine=Medicine.objects.get(id=1), dealer=Dealer.objects.get(id=1), price=100)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/medicine/price/delete/1/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('medicine-price-delete', kwargs={'pk': 1, 'pk1': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('medicine-price-delete', kwargs={'pk': 1, 'pk1': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/price_confirm_delete.html')


class PriceUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Medicine.objects.create(code=12345, name='Crocin', stock=100, description='Good medicine')
        Dealer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')
        Price.objects.create(medicine=Medicine.objects.get(id=1), dealer=Dealer.objects.get(id=1), price=100)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/medicine/price/update/1/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('medicine-price-update', kwargs={'pk': 1, 'pk1': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('medicine-price-update', kwargs={'pk': 1, 'pk1': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/price_form.html')


class PriceCreateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Medicine.objects.create(code=12345, name='Crocin', stock=100, description='Good medicine')
        Dealer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')
        Price.objects.create(medicine=Medicine.objects.get(id=1), dealer=Dealer.objects.get(id=1), price=100)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/medicine/price/create/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('medicine-price-create', kwargs={'pk1': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('medicine-price-create', kwargs={'pk1': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/price_form.html')


class CustomerListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_customers = 13

        for customer_id in range(number_of_customers):
            Customer.objects.create(name=str(customer_id), address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/customer/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('customer-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('customer-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/customer_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('customer-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['customer_list']), 10)

    def test_lists_all_customers(self):
        response = self.client.get(reverse('customer-list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['customer_list']), 3)


class CustomerDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/customer/detail/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('customer-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('customer-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/customer_detail.html')


class CustomerDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/customer/delete/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('customer-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('customer-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/customer_confirm_delete.html')


class CustomerUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/customer/update/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('customer-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('customer-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/customer_form.html')


class CustomerCreateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/customer/create')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('customer-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('customer-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/customer_form.html')


class EmployeeListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_employees = 13

        for employee_id in range(number_of_employees):
            Employee.objects.create(name=str(employee_id), address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no='1234567890135794')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/employee/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/employee_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['employee_list']), 10)

    def test_lists_all_employee(self):
        response = self.client.get(reverse('employee-list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['employee_list']), 3)


class EmployeeDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/employee/detail/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('employee-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('employee-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/employee_detail.html')


class EmployeeDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/employee/delete/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('employee-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('employee-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/employee_confirm_delete.html')


class EmployeeUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/employee/update/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('employee-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('employee-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/employee_form.html')


class EmployeeCreateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/employee/create')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('employee-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('employee-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/employee_form.html')


class TODOListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_todos = 13

        for todo_id in range(number_of_todos):
            Employee.objects.create(name=str(todo_id), address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no='1234567890135794')
            todo = TODO.objects.create(title=str(todo_id), date='2021-05-30', description='Take attendance tomorrow')
            todo.employees.add(Employee.objects.get(id=(todo_id+1)))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/todo/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/todo_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['todo_list']), 10)

    def test_lists_all_todo(self):
        response = self.client.get(reverse('todo-list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['todo_list']), 3)


class TODODetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no='1234567890135794')
        todo = TODO.objects.create(title='Attendance', date='2021-05-30', description='Take attendance tomorrow')
        todo.employees.add(Employee.objects.get(id=1))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/todo/detail/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('todo-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('todo-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/todo_detail.html')


class TODODeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no='1234567890135794')
        todo = TODO.objects.create(title='Attendance', date='2021-05-30', description='Take attendance tomorrow')
        todo.employees.add(Employee.objects.get(id=1))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/todo/delete/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('todo-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('todo-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/todo_confirm_delete.html')


class TODOUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no='1234567890135794')
        todo = TODO.objects.create(title='Attendance', date='2021-05-30', description='Take attendance tomorrow')
        todo.employees.add(Employee.objects.get(id=1))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/todo/update/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('todo-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('todo-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/todo_form.html')


class TODOCreateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no='1234567890135794')
        todo = TODO.objects.create(title='Attendance', date='2021-05-30', description='Take attendance tomorrow')
        todo.employees.add(Employee.objects.get(id=1))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/todo/create')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('todo-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('todo-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/todo_form.html')


class BillListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_bills = 13

        for bill_id in range(number_of_bills):
            Customer.objects.create(name=str(bill_id+1), address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')
            Employee.objects.create(name=str(bill_id+1), address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no='1234567890135794')
            Bill.objects.create(customer=Customer.objects.get(id=(bill_id+1)), employee=Employee.objects.get(id=(bill_id+1)), amount=(bill_id+1), date='2021-05-23')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/bill/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bill-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bill-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/bill_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('bill-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['bill_list']), 10)

    def test_lists_all_bill(self):
        response = self.client.get(reverse('bill-list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['bill_list']), 3)


class BillDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no='1234567890135794')
        Bill.objects.create(customer=Customer.objects.get(id=1), employee=Employee.objects.get(id=1), amount=100, date='2021-05-23')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/bill/detail/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bill-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bill-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/bill_detail.html')


class BillDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')
        Bill.objects.create(customer=Customer.objects.get(id=1), employee=Employee.objects.get(id=1), amount=100, date='2021-05-23')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/bill/delete/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bill-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bill-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/bill_confirm_delete.html')


class BillUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')
        Bill.objects.create(customer=Customer.objects.get(id=1), employee=Employee.objects.get(id=1), amount=100, date='2021-05-23')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/bill/update/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bill-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bill-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/bill_form.html')


class BillCreateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com')
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')
        Bill.objects.create(customer=Customer.objects.get(id=1), employee=Employee.objects.get(id=1), amount=100, date='2021-05-23')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/bill/create')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bill-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bill-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/bill_form.html')


class AttendanceListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_attendance = 13

        for attendance_id in range(number_of_attendance):
            Employee.objects.create(name=str(attendance_id+1), address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')
            attendance = Attendance.objects.create(date='2021-05-30')
            attendance.employees.add(Employee.objects.get(id=(attendance_id+1)))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/attendance/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('attendance-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('attendance-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/attendance_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('attendance-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['attendance_list']), 10)

    def test_lists_all_attendance(self):
        response = self.client.get(reverse('attendance-list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['attendance_list']), 3)


class AttendanceDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')
        attendance = Attendance.objects.create(date='2021-05-30')
        attendance.employees.add(Employee.objects.get(id=1))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/attendance/detail/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('attendance-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('attendance-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/attendance_detail.html')


class AttendanceDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')
        attendance = Attendance.objects.create(date='2021-05-30')
        attendance.employees.add(Employee.objects.get(id=1))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/attendance/delete/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('attendance-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('attendance-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/attendance_confirm_delete.html')


class AttendanceUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')
        attendance = Attendance.objects.create(date='2021-05-30')
        attendance.employees.add(Employee.objects.get(id=1))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/attendance/update/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('attendance-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('attendance-update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/attendance_form.html')


class AttendanceCreateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='ABC', address="Chennai", phone_no=1234567890, email='xyzabc1234567@gmail.com', id_proof='a', proof_unique_no= '1234567890135794')
        attendance = Attendance.objects.create(date='2021-05-30')
        attendance.employees.add(Employee.objects.get(id=1))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/pharmacy/attendance/create')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('attendance-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('attendance-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pharmacyapp/attendance_form.html')
