from flask import render_template
from app.auth.jwt_utils import jwt_required

from app.agenda import agenda_bp
from app.agenda.client import buscar_agendamentos



@agenda_bp.route("/agenda", methods=["GET"])
@jwt_required
def agenda_page():
    dados, erro = buscar_agendamentos()
    return render_template(
        "agenda_page.html",
        agendamentos = dados,
        erro = erro
    )
