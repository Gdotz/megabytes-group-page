from flask import Flask, Blueprint, redirect, render_template, url_for, request
from .models import overview
from . import db

feature = Blueprint("feature", __name__)

@feature.route("/")
def home():
    return render_template("home.html")
    