from selene import browser, be, have

from pages.registration_page import RegistrationPage


def test_fill_form():
    registration_page = RegistrationPage()
    registration_page.open()
    (
        registration_page
        .fill_first_name('Александр')
        .fill_last_name('Евдошенко')
        .fill_email('remix-92@mail.ru')
        .set_gender("Male")
        .fill_phone_number('8800200100')
        .fill_birthday('May', '1992', '13')
        .set_subject_by_enter('Computer Science')
        .set_hobby("Sports")
        .upload_picture('file.txt')
        .fill_current_address('ул.Жилая, 1')
        .choose_location('NCR', 'Delhi')
        .submit_form()
    )

    registration_page.should_have_registered_user_with(
            'Александр Евдошенко',
            'remix-92@mail.ru',
            'Male',
            '8800200100',
            '13 May,1992',
            'Computer Science',
            'Sports',
            'file.txt',
            'ул.Жилая, 1',
            'NCR Delhi'
                                                 )
    print('Тест пройден')


