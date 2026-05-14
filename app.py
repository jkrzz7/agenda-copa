"""
App Flask - Copa do Mundo 2026
"""

from flask import Flask, render_template, request, redirect, url_for
from seunome import config

app = Flask(__name__)

dados = [[config['username']]]
lista = []


@app.get("/")
def home():
    return render_template(
        "base.html",
        lista_front=lista,
        lista_dados=dados
    )


@app.post("/add")
def add():
    selecao = request.form.get("selecao")
    continente = request.form.get("continente")
    numero_copas = request.form.get("numero_copas")

    time = []

    if (
        selecao != '' and
        continente != '' and
        numero_copas != ''
    ):

        time.append(selecao.strip())
        time.append(continente.strip())
        time.append(numero_copas.strip())

        lista.append(time)

        print(f'Seleção adicionada: {lista}')

    else:
        print("Preencha todos os campos")

    return redirect(url_for("home"))


@app.post("/sort")
def sort():

    if lista != []:
        print("Ordenando seleções")
        lista.sort()

    return redirect(url_for("home"))


@app.post("/reverse")
def reverse():

    global lista

    if lista != []:
        print("Invertendo ordem")

        lista = sorted(
            lista,
            reverse=True,
            key=lambda x: x[0]
        )

    return redirect(url_for("home"))


@app.post("/clear")
def clear():

    global lista

    print("Apagando lista")

    lista = []

    return redirect(url_for("home"))


@app.get("/delete/<nome_selecao>")
def delete(nome_selecao):

    for i in range(len(lista)):
        if nome_selecao in lista[i]:
            del lista[i]
            break

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
