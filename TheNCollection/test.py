from django.test import TestCase, Client
from django.urls import reverse
from userlogin.forms import LoginForm
from django.contrib.auth.models import User

class Test (TestCase):
    def setUp(self):
        self.client=Client()
        self.user_login=reverse('nemo:login_user')
    def test_login_access_page(self):
        response = self.client.get(self.user_login)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'userlogin/login.html')
    
#register url was tested    
    def test_register_page(self):
        response = self.client.get( reverse('nemo:register'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'userlogin/register.html')

    def test_home_page(self):
        response = self.client.get( reverse('nemo:home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'userlogin/homepage.html')

    
    def create_user(self, username="naerae100", password="@GTFo@2025"):
        return User.objects.create(username=username, password=password)
    def test_valid_form(self):
        w = User.objects.create(username='Foo', password='Bar')
        data = {'username':w.username,'password':w.password}
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = User.objects.create(username='Foo', password='')
        data = {'username':w.username,'password':w.password}
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())
        

        
            

