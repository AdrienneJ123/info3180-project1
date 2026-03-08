from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired


class PropertyForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])

    bedrooms = IntegerField('Bedrooms', validators=[DataRequired()])
    bathrooms = IntegerField('Bathrooms', validators=[DataRequired()])

    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])

    property_type = SelectField(
        'Type',
        choices=[('House','House'),('Apartment','Apartment')],
        validators=[DataRequired()]
    )

    photo = FileField(
    "Property Photo",
    validators=[
        FileRequired(message="Please upload a property image."),
        FileAllowed(['jpg', 'jpeg', 'png'], "Only JPG, JPEG, and PNG images are allowed.")
    ]
)
    submit = SubmitField('Add Property')
