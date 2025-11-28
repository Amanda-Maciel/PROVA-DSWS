from flask import render_template, Blueprint
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    aluno = "Amanda Maciel"
    prontuario = "PT3032591"
    data_hora = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template('index.html', aluno=aluno, prontuario=prontuario, data_hora=data_hora)
