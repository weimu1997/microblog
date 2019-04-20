from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired()])
    remember_me = BooleanField("自动登录")
    submit = SubmitField("登录")


class RegistrationForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired()])
    email = StringField("邮箱", validators=[DataRequired(), Email()])
    password = PasswordField("输入密码", validators=[DataRequired()])
    password2 = PasswordField("再次输入密码", validators=[
                              DataRequired(), EqualTo("password")])
    submit = SubmitField("注册")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("该用户名已被使用")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("该邮箱已被使用")


class EditProfileForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired()])
    about_me = TextAreaField("个性签名", validators=[Length(min=0, max=140)])
    submit = SubmitField("更新")


class PostForm(FlaskForm):
    post = TextAreaField(
        "内容", validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField("发表")
