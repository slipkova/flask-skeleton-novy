"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template
from .forms import LogUserForm, secti, masoform, obdelnik
from ..data.database import db
from ..data.models import LogUser
from ..data.models.stonks import Stonks
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/secti', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/secti.tmpl', form=form)

@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

@blueprint.route('/rect', methods=['GET','POST'])
def Rect():
    form = obdelnik()
    if form.validate_on_submit():
        if form.type.data == "1":
            return str(pow(form.a.data, 2))
    return render_template("public/obd.tmpl", form=form)


@blueprint.route("/simple_chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('public/chart.tmpl', values=values, labels=labels, legend=legend)

@blueprint.route('/add_row')
def add():
    new = Stonks(company = "Auto", short = "A", value = "20", last_value  = "50")
    db.session.add(new)
    db.session.commit()
    return "ok"

@blueprint.route('/output')
def out():
    pole = db.session.query(Stonks).all()
    return render_template('public/data.tmpl', pole = pole)