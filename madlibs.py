"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = sample(AWESOMENESS,3)
    # if wants_compliments:
    #     nice_things = sample(COMPLIMENTS, 3)
    # else:
    #     nice_things = []
    # return render_template("compliments.html",
    #                        compliments=nice_things, name=player)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliment)

@app.route('/game')
def show_madlib_form():
    """ Play game with user"""

    is_playing = request.args.get("yes-or-no")

    if is_playing == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():
    """Shows you your madlib"""
    person = request.args.get("person")
    noun = request.args.get("noun")
    # color = (request.args.get("color"))
    adjective = request.args.get("adjective")
    list_colors = []
    list_colors.extend(request.args.get("color"))

    return render_template("madlib.html",person=person, noun=noun, colors = list_colors, adjective=adjective)

# 3. Write a new function, show_madlib(), which is routed to by the URL 
# path /madlib. It should render the template madlib.html, which should fill 
# the person, color, noun, and adjective provided by the user into a 
# MadLibs-style story.


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
