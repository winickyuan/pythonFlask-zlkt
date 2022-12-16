import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired

from models import EmailCaptchaMode, UserModel


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=3, max=20, message='username format is error ')])
    email = wtforms.StringField(validators=[Email(message='email format is error ')])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4)])
    password = wtforms.StringField(validators=[Length(min=6, max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    def validate_email(self, field):
        email = field.data
        user_model = UserModel.query.filter_by(email=email).first()
        if user_model:
            raise wtforms.ValidationError("eamil is already existed")

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaMode.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError('邮箱验证码错误')


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message='email format is error ')])
    password = wtforms.StringField(validators=[Length(min=6, max=20)])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message='title format is error')])
    content = wtforms.StringField(validators=[Length(min=3, message='content format is error')])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message='content format is error')])
    question_id = wtforms.StringField(validators=[InputRequired(message='question id is required')])

