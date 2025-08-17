from selene import browser, be, have

from pages.registration_page import RegistrationPage

MIDDLE
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
# def test_form():
#     file_path = os.path.join(os.path.dirname(__file__), 'file.txt')
#     browser.open('https://demoqa.com/automation-practice-form')
#     browser.element('#firstName').should(be.visible).type('Александр')
#     browser.element('#lastName').should(be.visible).type("Евдошенко")
#     browser.element('#userEmail').should(be.blank).type('remix-92@mail.ru')
#     browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
#     browser.element('#userNumber').should(be.blank).type('8800200100')
#     browser.element('#dateOfBirthInput').click()
#     browser.element('.react-datepicker__month-select').type('May')
#     browser.element('.react-datepicker__year-select').type('1992')
#     browser.element('.react-datepicker__day--013').click()
#     browser.element('#subjectsInput').type('Computer Science').press_enter()
#     browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
#     browser.element('#uploadPicture').send_keys(file_path)
#     browser.element('#currentAddress').type('ул.Жилая, 1')
#     browser.element('#state').click()
#     browser.element('#react-select-3-option-0').click()
#     browser.element('#city').click()
#     browser.element('#react-select-4-option-0').click()
#     browser.element('#submit').press_enter()
#     browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
#     browser.all('.table-responsive td:nth-child(2)').should(have.texts(
#         'Александр Евдошенко',
#         'remix-92@mail.ru',
#         'Male',
#         '8800200100',
#         '13 May,1992',
#         'Computer Science',
#         'Sports',
#         'file.txt',
#         'ул.Жилая, 1',
#         'NCR Delhi'
#     ))


