from django.test import TestCase

from django.core.checks import messages
from django.test import RequestFactory,TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import Client
from blog.models import BlogPost
import unittest


class BlogTest1(TestCase):
    def setUp(self):
        BlogPost.objects.create(title="A")
    def test_blog_model(self):
        a=BlogPost.objects.get(title='A')
        self.assertEqual(a == None,False)


class BlogTest2(TestCase):
    def setUp(self):
        BlogPost.objects.create(content="A")
    def test_blog_model(self):
        b=BlogPost.objects.get(content='A')
        self.assertEqual(b == None,False)


class BlogTest3(TestCase):
    def setUp(self):
        BlogPost.objects.create(address="A")
    def test_blog_model(self):
        c=BlogPost.objects.get(address='A')
        self.assertEqual(c == None,False)


class BlogTest4(TestCase):

    def setUp(self):
        BlogPost.objects.create(capacity="1")
    def test_blog_model(self):
        d=BlogPost.objects.get(capacity='1')
        self.assertEqual(d == 0,False)


class BlogTest5(TestCase):

    def setUp(self):
        BlogPost.objects.create(capacity="2")
        BlogPost.objects.create(population="1")
    def test_blog_model(self):
        v=BlogPost.objects.get(population='1')
        k=BlogPost.objects.get(capacity="2")
        self.assertTrue(v,k)


class BlogTest6(TestCase):
    def setUp(self):
        BlogPost.objects.create(type="A")
    def test_blog_model(self):
        c=BlogPost.objects.get(type='A')
        self.assertEqual(c == None,False)


class register_Login_Test(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    def test_register_view(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
    def test_login_view(self):
            response = self.client.post('/login/',{'username':'User','password':'asd123asd123'},)
            self.assertEqual(response.status_code, 200)
    def test_logout_view(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)





