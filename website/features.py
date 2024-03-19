from flask import Flask, Blueprint, redirect, render_template, url_for, request
from .models import Overview
from . import db

feature = Blueprint("feature", __name__)

@feature.route("/")
def home():
    overview = Overview.query.all()
    print(overview)
    return render_template("home.html")

@feature.route("/mon")
def mon():
    overview = Overview.query.all()
    print(overview)
    return render_template("mon.html")


    
