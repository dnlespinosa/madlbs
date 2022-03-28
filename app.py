from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/home')
def click_home():
    return render_template('home.html')

@app.route('/story')
def story():
    place = request.args['PLACE']
    noun = request.args['NOUN']
    verb = request.args['VERB']
    adj = request.args['ADJECTIVE']
    plural_noun = request.args['PLURAL_NOUN']
    mad_dictionary = {
        'place': place, 
        'noun': noun, 
        'verb': verb, 
        'adj': adj, 
        'plural_noun': plural_noun
    }
    story = Story(
    mad_dictionary,
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )
    stories = story.generate(mad_dictionary)
    return render_template('story.html', story = stories)