from flask import Blueprint, url_for, redirect, render_template, request
from .ReconSys import reconSys

views = Blueprint('views',__name__)
reconSystem = reconSys()


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/workout-splits')
def workoutSplits():
    return render_template("workoutSplits.html")

@views.route('/muscle-groups')
def muscleGroups():
    return render_template("muscleGroups.html")

@views.route('/recom-sys', methods = ["POST","GET"])
def recommendationSystem():
    if request.method == "POST":
        #information to be sent from this web page to another
        workout = request.form['work']
        return redirect(url_for("views.exerciseFilter", exercise = workout))
        #redirect to webpage with workout as a key for the following page - redirect is a form that is sent to a webpage
    else:
        #print(reconSystem.toHTML())
        return render_template("exerciseRecom.html", options = reconSystem.toHTML())

@views.route('/exerciseFilter', methods = ["POST","GET"])
def exerciseFilter():
    #Retrieve information from recom-sys page. 
    exercise = request.args.get('exercise')
    return render_template("exerciseFilter.html", data = reconSystem.exerciseRecommend(exercise,5).to_html(index = False, classes ='table table-hover', justify = 'center'), name = exercise)