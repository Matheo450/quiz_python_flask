# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
))


# lista pytań
DANE = [{
    'pytanie': 'Polecenie "print" oznacza:',  # pytanie
    'odpowiedzi': ['kończy pętlę if', 'wyświetla coś na konsoli', 'oblicza równanie'],  # możliwe odpowiedzi
    'odpok': 'wyświetla coś na konsoli'},  # poprawna odpowiedź
    {
    'pytanie': 'Numpy, matplotlib ... to: :',
    'odpowiedzi': ['biblioteki', 'funkcje', 'interpretory'],
    'odpok': 'biblioteki'},
    {
    'pytanie': 'Jeżeli polecenie jest następujące: "for i in range(0,9) print(i)" na ekranie zostanie wyświetlone: ',
    'odpowiedzi': ['liczby od 0 do 9', 'liczby od 9 do 0', 'liczby od 1 do 8'],
    'odpok': 'liczby od 0 do 9'},
     {
    'pytanie': 'Operator potęgowania w Python to: ',
    'odpowiedzi': ['**', '@', '!'],
    'odpok': '**'},
     {
     'pytanie': 'Jak może się nazywać funkcja w języku Python?: ',
    'odpowiedzi': ['import', 'global', 'return'],
    'odpok': 'return'},

]

@app.route('/', methods=['GET', 'POST'])

def index():

    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form

        for pnr, odp in odpowiedzi.items():
            if odp == DANE[int(pnr)]['odpok']:
                punkty += 1

        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(punkty))
        return redirect(url_for('index'))

    # return 'Cześć, tu Python!'
    return render_template('index.html', pytania=DANE)

if __name__ == '__main__':
    app.run(debug=True)
