from flask import Flask, render_template

from vsearch import search4letters

app = Flask(__name__)


@app.route('/')

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = '検索結果:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the _title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/entry')
def entry_page() -> str:
    return render_template('entry.html', the_title='Web版のsearch4lettersにようこそ！')


app.run(debug=True)
