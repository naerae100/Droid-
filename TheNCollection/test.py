from django.test import TestCase, Client
from django.urls import reverse

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

        
            

