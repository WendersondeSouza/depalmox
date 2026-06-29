from flask import Flask
from routes import route_register
from database import criar_db

app = Flask(__name__)

criar_db()
route_register(app)

if __name__ == "__main__":
    criar_db()
    app.run(debug=True)



#         connection = sqlite3.connect("estoque.db")
#         cursor = connection.cursor()
#         cursor.execute(
#             "INSERT INTO produtos (nome, ref, quantidade) VALUES (?, ?, ?)", (nome, referencia, quantidade)
#         )

#         connection.commit()
#         connection.close()

#         print("PRODUTO CADASTRADO")

    
#     connection = sqlite3.connect("estoque.db")
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM produtos")
#     produtos = cursor.fetchall()

#     connection.close()

#     return render_template("register.html", produtos=produtos)

# # delete item
# @app.route("/delete_item/<int:ref>", methods=["POST"])
# def delete(ref):
#     connection = sqlite3.connect("estoque.db")
#     cursor = connection.cursor()

#     cursor.execute("DELETE FROM produtos WHERE ref = ?", 
#     (ref,)
#     )

#     connection.commit()
#     connection.close()
#     return redirect(url_for("registrar"))

# # @app.route("/scanner", methods=["POST"])
# # def escanear():




