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

    return render_template("hello.html")


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = sample(AWESOMENESS,3)

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
    person = [str(request.args.get("person1")), 
                str(request.args.get("person2")), 
                str(request.args.get("person3"))]
    
    people = []
    for personX in person:
        if personX != 'None':
            people.append(personX)
    if len(people) > 2:
        people_out = f"{people[0]}, {people[1]}, and {people[2]}"
    elif len(people) == 2:
        people_out = f"{people[0]} and {people[1]}"
    elif len(people) == 1:
        people_out = str(people[0])

    noun = [str(request.args.get("noun1")), 
                str(request.args.get("noun2")), 
                str(request.args.get("noun3"))]

    nouns = []
    for nounX in noun:
        if nounX != 'None':
            nouns.append(nounX)
    if len(nouns) > 2:
        nouns_out = f"{nouns[0]}, {nouns[1]}, and {nouns[2]}"
    elif len(nouns) == 2:
        nouns_out = f"{nouns[0]} and {nouns[1]}"
    elif len(nouns) == 1:
        nouns_out = str(nouns[0])
    print(nouns_out)

    color = (request.args.get("color"))
    adjective = request.args.get("adjective")
    list_colors = []
    list_colors.append(request.args.get("color"))
    
    print(f"noun={noun},colors={color},adj={adjective},people={people_out}")
    
    return render_template("madlib.html", 
                            people_out=people_out, 
                            nouns_out=nouns_out,
                            color = color, 
                            adjective=adjective)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
