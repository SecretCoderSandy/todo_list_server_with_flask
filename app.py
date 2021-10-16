print("This is my first flask app")
# from ProdBuilder import PageProdBuilder
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# pd = PageProdBuilder("../client/templates/app.html", "../client/templates/index.html")
app = Flask(__name__, static_url_path='', static_folder='../client',template_folder='../client/templates')
db_path = "../db/MyTodoApp.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class MyTodo(db.Model):
    todo_sno = db.Column(db.Integer, primary_key=True)
    todo_title = db.Column(db.String(200), nullable=False)
    todo_desc = db.Column(db.String(200), nullable=False)
    todo_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.todo_sno} - {self.todo_title}"

# pd.build()
@app.route('/')
def home():
    all_todo = MyTodo.query.all()
    return render_template('app.html', all_todo=all_todo)

@app.route('/add_todo', methods =["GET"])
def get_todo():
    if request.method == "GET":
        get_todo_title = request.args.get("title")
        get_todo_description = request.args.get("description")
        set_todo = MyTodo(todo_title=get_todo_title, todo_desc=get_todo_description)
        db.session.add(set_todo)
        db.session.commit()
        
        all_todo = MyTodo.query.all()
        
    return render_template('app.html', all_todo=all_todo)

if __name__ == "__main__":
    app.run(debug=True,port=80)