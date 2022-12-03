# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    user_status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'admin'


class CartProduct(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING)
    user_id_c = models.ForeignKey('Customer', models.DO_NOTHING, db_column='user_id_c')
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart_product'


class Category(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING)
    label = models.ForeignKey('Label', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'category'


class Customer(models.Model):
    user_id_c = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    account = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    id_number = models.CharField(unique=True, max_length=10)
    user_status = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'customer'


class Label(models.Model):
    label_id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'label'


class ManageT(models.Model):
    user = models.ForeignKey(Admin, models.DO_NOTHING)
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'manage_t'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    total_price = models.FloatField()
    order_time = models.DateTimeField()
    address = models.CharField(max_length=255)
    status = models.IntegerField()
    user_id_c = models.ForeignKey(Customer, models.DO_NOTHING, db_column='user_id_c')
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_product'


class Product(models.Model):
    user_id_s = models.ForeignKey('Seller', models.DO_NOTHING, db_column='user_id_s')
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    publish_date = models.DateTimeField()
    status = models.TextField()  # This field type is a guess.
    total_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product'


class SalesReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    sales_results = models.CharField(max_length=255)
    sales_score = models.IntegerField()
    user_id_s = models.ForeignKey('Seller', models.DO_NOTHING, db_column='user_id_s')

    class Meta:
        managed = False
        db_table = 'sales_report'


class Seller(models.Model):
    user_id_s = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    id_number = models.CharField(max_length=10)
    user_status = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'seller'


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    effective_date = models.DateTimeField()
    amount = models.CharField(max_length=255)
    discount = models.CharField(max_length=255)
    user_id_s = models.ForeignKey(Seller, models.DO_NOTHING, db_column='user_id_s')

    class Meta:
        managed = False
        db_table = 'ticket'


class ToDoThing(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_content = models.CharField(max_length=255, blank=True, null=True)
    event_state = models.TextField()  # This field type is a guess.
    user = models.ForeignKey(Admin, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'to_do_thing'