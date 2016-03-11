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

        # else:
        #     print "INVALID FORM DATA!!!!!"
        #     return redirect(url_for('index'))

    return render_template('index.html', searchform = form)



@app.route('/results/<mode>/<query>', methods=['GET','POST'])
def results(mode="name", query=""):


    if request.method == 'GET':
        print "HERE"
        form = RecordUpdateForm()
        items=None
        data = load_data()
        pattern = '%'+'%'.join(query.split())+'%'
        print pattern

        if mode == 'name' or mode == 'isbn':

            items = db_ops.ret_like(db_ops.Record,
                field=mode, pattern=pattern)

        # elif mode == 'isbn':
        #     items = db_ops.ret_all_val(db_ops.Record,
        #         dict(isbn=query))

        return render_template('results.html', items=items, record_update_form=form)


    # elif request.method == 'POST':

    #     form = request.form
    #     print form

    #     # item_id = 
    #     # isbn = 
    #     # name = 
    #     param_dict = {'item_id':1, 'isbn':3, 'name':2}

    #     #db_ops.update_row(db_ops.Record, dict('rec_id':...), param_dict)


@app.route('/update', methods=['POST'])
def update():

    form = request.form
    print form['hidden_fld']
    for element in form.iterkeys():
        if element.startswith('_units_'):
            value = form.get(element)
            item_id = int(element[element.rfind('_')+1:])
            param_dict = {
                'rec_id': item_id,
                'units':value,
                }            
            db_ops.update_row(db_ops.Record, dict(rec_id=item_id), param_dict)
            flash("Updated!")

    return redirect(url_for('index'))



def load_data():

    all_data = db_ops.ret_all(db_ops.Record)    

    return all_data