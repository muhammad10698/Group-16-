from django.test import TestCase

from django.core.checks import messages
from django.test import RequestFactory,TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import Client
from Contact.models import Contact
import unittest

class ContactTest1(TestCase):
    def setUp(self):
        Contact.objects.create(name="A")
    def test_Contact_model(self):
        a=Contact.objects.get(name='A')
        self.assertEqual(a == None,False)


class ContactTest2(TestCase):
    def setUp(self):
        Contact.objects.create(email="Random@example.com")
    def test_Contact_model(self):
        b=Contact.objects.get(email='Random@example.com')
        self.assertEqual(b == None,False)


class ContactTest3(TestCase):
    def setUp(self):
        Contact.objects.create(subject="A")
    def test_Contact_model(self):
        c=Contact.objects.get(subject='A')
        self.assertEqual(c == None,False)

class ContactTest4(TestCase):
    def setUp(self):
        Contact.objects.create(message="A")
    def test_Contact_model(self):
        d=Contact.objects.get(message='A')
        self.assertEqual(d == None,False)


class ContactTest5(TestCase):
    def setUp(self):
        Contact.objects.create(business_owner="A")
    def test_Contact_model(self):
        d=Contact.objects.get(business_owner='A')
        self.assertEqual(d == None,False)




