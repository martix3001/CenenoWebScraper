from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/autor')
def autor():
    return render_template('autor.html')

@app.route('/ekstrakcja')
def ekstrakcja():
    return render_template('ekstrakcja.html')

@app.route('/lista_produkt')
def lista_produkt():
    return render_template('lista_produkt.html')

@app.route('/strona_produktu')
def strona_produktu():
    return render_template('strona_produktu.html')

@app.route('/wykresy')
def wykresy():
    return render_template('wykresy.html')