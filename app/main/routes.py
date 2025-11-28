from flask import Blueprint, render_template, request, redirect
from datetime import datetime
from app import db
from app.models import Professor


@main.route('/')
def index():
    aluno = "Amanda Maciel"
    prontuario = "PT3032591"
    data_hora = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template('index.html', aluno=aluno, prontuario=prontuario, data_hora=data_hora)


@main.route('/professores', methods=['GET', 'POST'])
def professores():

    if request.method == 'POST':
        nome = request.form['nome']
        disciplina = request.form['disciplina']

        novo_prof = Professor(nome=nome, disciplina=disciplina)
        db.session.add(novo_prof)
        db.session.commit()

        return redirect('/professores')

    lista = Professor.query.all()
    return render_template('professores.html', lista=lista)



@main.route('/disciplinas')
@main.route('/alunos')
@main.route('/cursos')
@main.route('/ocorrencias')
def nao_disponivel():
    return render_template('nao_disponivel.html')
