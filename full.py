from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/ThinkPad/Documents/CURSO DE PYTHON COMPLETO/Python con MYSQL y SQLITE/FLASK/database/libreria.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# DEFINICION DE MODELO
class Libros (db.Model):
    rowid = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100), unique =True, nullable =False)
    actor = db.Column(db.String(100))
    precio = db.Column(db.Integer)


    def __init__(self, titulo, actor, precio):
        super().__init__()
        self.titulo = titulo
        self.actor = actor
        self.precio = precio


    def __str__(self):
        return "\n titulo: {}. actor: {}. precio: {}.".format(
            self.titulo,
            self.actor,
            self.precio
        )
    
    def serialize(self):
        return{
            "rowid" : self.rowid,
            "titulo" : self.titulo,
            "actor" : self.actor,
            "precio" : self.precio
        }


# AQUI EMPIEZAN LAS RUTAS
@app.route("/")
def home ():
    return render_template("index.html")
    return "<h1> bienvenido a python </h1>"

@app.route("/books")
def buy():
    return render_template("search_libros.html")


@app.route("/buying", methods = ["GET"])

def libro():
    #read = Libros.query.all()
    #print(read)
    try:
        readbook = Libros.query.all()
        toback = [lect.serialize() for lect in readbook]
        return jsonify(toback), 200
    except Exception:
        exception("[SERVER]: error =")
        return jsonify({"msg": "ha ocurrido un error!"}), 500
    
    return "<h1> success </h1>"


# ENCONTRAR VALORES

@app.route("/app/libros/", methods = ["GET"])

def character():
    try:
        fields = {}
        if "titulo" in request.args:
            fields["titulo"] = request.args["titulo"]

        if "actor" in request.args:
            fields["actor"] = request.args["actor"]

        if "titulo" in request.args:
            fields["precio"] = request.args["precio"]

        readings = Libros.query.filter_by(**fields).first()
        if not readings:
            return jsonify({"msg:":"no existe el mensaje"}), 200
        else:
            return jsonify(readings.serialize()), 200
        
    except Exception:
        exception("[SERVER]: error")
        return jsonify({"msg:": "ha ocurrido un error"}),500
    


# REGISTRAR E INICIAR SESION EN HTML
@app.route("/app/addCustomers", methods= ["POST"])

def Custom():
    try:
        titulo = request.form["titulo"]
        actor = request.form["actor"]
        precio = request.form["precio"]

        lexico = Libros(titulo, actor, precio)
        db.session.add(lexico)
        db.session.commit()

        return jsonify(lexico.serialize()), 200
    except Exception:
        exception("\n[SERVER] error en ruta: /app/addCustomers. log: \n.")
        return jsonify({"msg" : "algo ha salido mal"}), 500
    

@app.route("/app/buying", methods = ["POST"])

def interest():
    try:
        nombreTitulo = request.form["titulo"]
        readings = Libros.query.filter(Libros.titulo.like(f"%{nombreTitulo}%")).first()
        if not readings:
            return jsonify({"msg:":"no existe el mensaje"}), 200
        else:
            return jsonify(readings.serialize()), 200
        
    except Exception:
        exception("[SERVER]: error")
        return jsonify({"msg:": "ha ocurrido un error"}),500
        

if __name__ == "__main__":
    app.run (debug= True)