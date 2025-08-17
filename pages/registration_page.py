from selene import browser, have, be, by
import os

class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_birthday(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.all('.react-datepicker__month-select option').element_by(have.exact_text(month)).click()
        browser.all('.react-datepicker__year-select option').element_by(have.exact_text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def set_gender(self, value):
        browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
        return self

    def fill_phone_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def set_subject_by_enter(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self



    def set_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
        return self

    def upload_picture(self, value):
        file_path = os.path.join(os.path.dirname(__file__), 'file.txt')
        browser.element('#uploadPicture').send_keys(file_path)
        return self

    def fill_current_address(self, value):
        browser.element('[id="currentAddress"]').set_value(value)
        return self

    def choose_location(self, state, city):
        browser.element('#state input').type(state).press_enter()
        browser.element('#city input').type(city).press_enter()
        return self

    def submit_form(self):
        browser.element('[id="submit"]').click()
        return self

    def should_have_registered_user_with(self,
                                   full_name,
                                   email,
                                   gender,
                                   phone_number,
                                   birthday,
                                   subjects,
                                   hobby,
                                   file_name,
                                   address,
                                   state_city):
        (browser.all('.table-responsive td:nth-child(2)')
        .should(have.exact_texts(
            full_name,
            email,
            gender,
            phone_number,
            birthday,
            subjects,
            hobby,
            file_name,
            address,
            state_city
        )))
        return self