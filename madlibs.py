"""A madlib game that compliments its users."""

from random import choice

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

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

Make a function called show_madlib_form() and have the URL /game route to it. In this function, get the user’s response to the yes-or-no question on the “would you like to play a game?” form.

If they said no, return a rendered template, goodbye.html, that tells them goodbye and that they’ll be missed (or something else appropriate).

# 2. Make a function called show_madlib_form() and have the URL /game 
# route to it. In this function, get the user’s response to the yes-or-no 
# question on the “would you like to play a game?” form.

# If they said no, return a rendered template, goodbye.html, that tells them 
# goodbye and that they’ll be missed (or something else appropriate).

# If they said yes, render a different template, game.html. 
# The template game.html should have a simple form that asks for a person,
#  a color, a noun, and an adjective. How you choose to implement those 
# inputs is up to you, but you should feel free to mix and match. (Hint: it 
# might be fun to try one as a drop-down menu of choices). This new form 
# should have the action of /madlib.


# 3. Write a new function, show_madlib(), which is routed to by the URL 
# path /madlib. It should render the template madlib.html, which should fill 
# the person, color, noun, and adjective provided by the user into a 
# MadLibs-style story.


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
