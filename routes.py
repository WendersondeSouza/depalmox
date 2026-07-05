from flask import Flask, render_template, request, redirect, url_for
from database import criar_produtos, excluir_produto, listar_produtos, qntd_increase
def route_register(app):
        
    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @app.route("/register", methods=["GET", "POST"])
    def registrar():
        if request.method == "POST":
            nome = request.form["nome"]
            referencia = request.form["ref"]
            quantidade = request.form["qntd"]

            criar_produtos(nome, referencia, quantidade)

        produtos = listar_produtos()

        return render_template(
            "register.html",
            produtos=produtos
        )
    
    @app.route("/delete_item/<int:ref>", methods=["POST"])
    def delete(ref):
        excluir_produto(ref)
        return redirect(url_for("registrar"))
    
    # scanner route for qr code reader
    @app.route("/scanner", methods=["GET"])
    def scanner():
        produtos = listar_produtos()

        return render_template(
            "scanner.html",
            produtos=produtos
        )

    @app.route("/scanner/read", methods=["POST"])
   
    def scanner_read():
        if request.method == "POST":
            dados = request.get_json()

            ref = dados["ref"]

            sucesso = qntd_increase(ref)

            if sucesso:
                return {
                    "status": "ok"
                }

            return {
                "status": "erro",
                "mensagem": "pProduto não encontrado"
            }
