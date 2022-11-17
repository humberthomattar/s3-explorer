from s3_explorer.forms import AccountForm
from s3_explorer import db, models
from flask_login import login_required, current_user
from flask import Blueprint, render_template, redirect, url_for, request, flash


account = Blueprint(
    'account', 
    __name__,
    template_folder='templates'
    )

@login_required
@account.route('/list')
def list():
    accounts = models.Account.query.filter_by(user_id=current_user.id).all()
    return render_template('account.html', accounts=accounts)

@login_required
@account.route('/add')
def add():
    form = AccountForm()    
    return render_template('account_add.html', form=form)


@login_required
@account.route('/add', methods=['POST'])
def add_post():
    form = AccountForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        endpoint = request.form.get('endpoint')
        access_key_id = request.form.get('access_key_id')
        secret_access_key = request.form.get('access_key_id')
        
        new_account = models.Account(name=name,
                                    endpoint=endpoint,
                                    access_key_id=access_key_id,
                                    secret_access_key=secret_access_key,
                                    user_id=current_user.id
                                    )

        db.session.add(new_account)
        db.session.commit()
        flash('Conta cadastrada com sucesso!')
        
    return redirect(url_for('account.list'))


@login_required
@account.route('/edit')
def edit():
    return ''

@login_required
@account.route('/del/<account_delete>')
def delete(account_delete):
    account = models.Account.query.filter_by(id=account_delete).one()
    db.session.delete(account)
    db.session.commit()
    flash('Conta excluida com sucesso!')
    
    return redirect(url_for('account.list'))




