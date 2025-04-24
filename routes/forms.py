from flask import Blueprint, render_template

forms_route = Blueprint('forms', __name__)

@forms_route.route('/')
def forms():
    return render_template('tela-nova-transacao.html')