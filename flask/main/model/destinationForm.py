from wtforms import Form,StringField,SelectField, SubmitField

class DestinationForm(Form):
    # age = StringField()
    # weather = StringField()
    destionation_string = StringField('')
    city_choices = ['seoul','sejong','busan','daegu','incheon']
    city_select = SelectField('search for city',choices=city_choices)
    si_goon_goo_choices = ['sahagu','haewoondaegu','gijanggu']
    si_goon_goo_select = SelectField('search for sigoongu',choices= si_goon_goo_choices)
    submit = SubmitField("search")