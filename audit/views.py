from audit import app

from flask import request, render_template, session,g, redirect, url_for, flash

from forms import SearchForm, RecordUpdateForm

import db_ops


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        form = SearchForm()

    elif request.method == 'POST':
        form = request.form

        return redirect(url_for('results',
            mode=form['mode_radio_fld'],
            query=form['query_fld']))

    count = 0
    all_data = load_data()

    for data in all_data:
        if data.units!=0:
            count+=1

    return render_template('index.html', searchform = form, data_count=count)



@app.route('/results/<mode>/<query>', methods=['GET','POST'])
def results(mode="name", query=""):

    if request.method == 'GET':
        form = RecordUpdateForm()
        items=None
        pattern = '%'+'%'.join(query.split())+'%'

        if mode == 'name' or mode == 'isbn':
            items = db_ops.ret_like(db_ops.Record,
                field=mode, pattern=pattern)


        return render_template('results.html', items=items, record_update_form=form)

@app.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        form = request.form # grab submitted form
        
        updated_flds = form['hidden_fld'].split(',')
        updated_flds.pop()

        # The form is a dictionary mapping field names
        # to their corresponding values
        # So we iterate over the form fields
        #
        # The primary id for each record from the DB has
        # been appended to the name of the field,
        # so we get the id and update the DB accordingly
        for element in form.iterkeys():
            # we're interested in fields whose
            # names begin with the string '_units_'
            if element.startswith('_units_'):
                value = form.get(element) # get the value of the current field
                item_id = int(element[element.rfind('_')+1:]) # ID for storing value in the DB has been appended to the name of current field, get it
                pub = form.get('_pub_'+str(item_id))
                param_dict = {
                    'rec_id': item_id,
                    'units': value,
                    'publisher': pub
                    }            
                db_ops.update_row(db_ops.Record, dict(rec_id=item_id), param_dict)
                flash("Updated!")

    return redirect(url_for('index'))



def load_data():

    all_data = db_ops.ret_all(db_ops.Record)    

    return all_data
