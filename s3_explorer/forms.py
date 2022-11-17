from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length

class AccountForm(FlaskForm):
    name = StringField('Nome da conta', validators=[InputRequired(), Length(min=2, max=100)])
    endpoint = StringField('Endereço', validators=[InputRequired(), Length(max=200)])
    access_key_id = StringField('Access Key', validators=[InputRequired(), Length(max=200)])
    secret_access_key = StringField('Secret Access Key', validators=[InputRequired(), Length(max=200)])