from flask import Blueprint, jsonify





mock_api_bp = Blueprint("mock_api", __name__)


@mock_api_bp.route("/agendamentos", methods=["GET"])
def get_mock():
    return  jsonify ([{  
        "paciente": "João da Silva",
        "cpf": "123.456.789-00",
        "medico": "Dra. Ana Souza",
        "especialidade": "Cardiologia",
        "data": "15/08/2026",
        "horario": "09:00",
        "convenio": "Unimed",
        "status": "Agendado"
    },
    {
        "paciente": "Maria Oliveira",
        "cpf": "987.654.321-00",
        "medico": "Dr. Carlos Pereira",
        "especialidade": "Dermatologia",
        "data": "16/08/2026",
        "horario": "14:30",
        "convenio": "Bradesco Saúde",
        "status": "Confirmado"
    },
    {
        "paciente": "Pedro Santos",
        "cpf": "456.789.123-11",
        "medico": "Dra. Fernanda Lima",
        "especialidade": "Ortopedia",
        "data": "17/08/2026",
        "horario": "11:15",
        "convenio": "SulAmérica",
        "status": "Cancelado"
    }]),200 