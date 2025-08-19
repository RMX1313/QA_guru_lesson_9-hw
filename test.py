import os
import sys
import pytest
from selene import browser, be, have
from pages.registration_page import RegistrationPage
from users import User


def test_form_submission():
    registration_page = RegistrationPage()
    alex = User(first_name='Александр',
                 last_name='Евдошенко',
                 email='remix-92@mail.ru',
                 gender="Male",
                 phone_number='8800200100',
                 birthday=('May', '1992', '13'),
                 first_subject='Computer Science',
                 hobby="Sports",
                 file_name='file.txt',
                 address='Sports',
                 user_location=('NCR', 'Delhi')
                 )

    registration_page.open()
    registration_page.register(alex)
    registration_page.should_have_registered(alex)
    print('test finished')