
from flask.ext.wtf import Form

# Import needed HTML and HTML5 form input field types
from wtforms import StringField, RadioField, SubmitField

# Import form data validators
from wtforms.validators import DataRequired



class SearchForm(Form):
    #mode_radio_fld = RadioField('Search Mode: ', default='name', choices=[('name', 'Name'), ('isbn', 'ISBN')])
    query_fld = StringField('Find: ')
    submit_btn = SubmitField('Search')    


class RecordUpdateForm(Form):

    #units_fld = StringField('Units on Hand')
    submit_btn = SubmitField('Update')    
