from django.db import models
from django.urls import reverse


class Pharmacy(models.Model):
    """Model representing a Pharmacy."""
    shop_name = models.CharField(max_length=300)
    address = models.TextField()
    owner_name = models.CharField(max_length=300)
    phone_no = models.DecimalField(max_digits=11, decimal_places=0, null=True)


class Medicine(models.Model):
    """Model representing a Medicine."""
    code = models.DecimalField(max_digits=5, decimal_places=0)
    name = models.CharField(max_length=200)
    stock = models.DecimalField(max_digits=6, decimal_places=0)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('medicine-detail', args=[str(self.id)])


class Price(models.Model):
    """Model representing a Medicine's Price"""
    medicine = models.ForeignKey('Medicine',on_delete=models.CASCADE)
    dealer = models.ForeignKey('Dealer',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)


class Dealer(models.Model):
    """Model representing a Dealer."""
    name = models.CharField(max_length=300)
    address = models.TextField()
    phone_no = models.DecimalField(max_digits=11, decimal_places=0)
    email = models.EmailField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dealer-detail', args=[str(self.id)])


class Employee(models.Model):
    """Model representing a Employee"""
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_no = models.DecimalField(max_digits=11, decimal_places=0)
    email = models.EmailField()
    PROOF = (
        ('a', 'Aadhar'),
        ('b', 'Driving License'),
        ('c', 'Ration Card'),
        ('d', 'PAN Card'),
        ('e', 'Passport'),
    )
    id_proof = models.CharField(
        max_length=1,
        choices=PROOF,
        blank=False,
        default='a',
        help_text='Enter Vote',
    )
    proof_unique_no = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee-detail', args=[str(self.id)])


class TODO(models.Model):
    """Model representing a TODO"""
    title = models.CharField(max_length=200)
    date = models.DateField()
    employees = models.ManyToManyField('Employee', blank=True)
    description = models.TextField(max_length=1000)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo-detail', args=[str(self.id)])


class Customer(models.Model):
    """Model representing a Customer"""
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_no = models.DecimalField(max_digits=11, decimal_places=0)
    email = models.EmailField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])


class Bill(models.Model):
    """Model representing a Bill"""
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField()
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.customer.name

    def get_absolute_url(self):
        return reverse('bill-detail', args=[str(self.id)])


class Attendance(models.Model):
    """Model representing a Attendance"""
    date = models.DateField()
    employees = models.ManyToManyField('Employee', blank=True)

    class Meta:
        ordering = ['date']

    def get_absolute_url(self):
        return reverse('attendance-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.date)
