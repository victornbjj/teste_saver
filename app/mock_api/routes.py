from flask import Blueprint, jsonify, request



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
    },
    {
        "paciente": "Ana Pereira",
        "cpf": "111.222.333-44",
        "medico": "Dr. Roberto Almeida",
        "especialidade": "Pediatria",
        "data": "18/08/2026",
        "horario": "08:30",
        "convenio": "Amil",
        "status": "Agendado"
    },
    {
        "paciente": "Carlos Mendes",
        "cpf": "555.666.777-88",
        "medico": "Dra. Beatriz Costa",
        "especialidade": "Ginecologia",
        "data": "18/08/2026",
        "horario": "10:00",
        "convenio": "NotreDame Intermédica",
        "status": "Confirmado"
    },
    {
        "paciente": "Juliana Rocha",
        "cpf": "999.888.777-66",
        "medico": "Dr. Eduardo Martins",
        "especialidade": "Neurologia",
        "data": "19/08/2026",
        "horario": "13:45",
        "convenio": "Hapvida",
        "status": "Agendado"
    },
    {
        "paciente": "Rafael Nunes",
        "cpf": "333.444.555-22",
        "medico": "Dra. Mariana Lopes",
        "especialidade": "Oftalmologia",
        "data": "19/08/2026",
        "horario": "15:15",
        "convenio": "São Rafael",
        "status": "Confirmado"
    },
    {
        "paciente": "Larissa Teixeira",
        "cpf": "777.888.999-00",
        "medico": "Dr. Felipe Souza",
        "especialidade": "Endocrinologia",
        "data": "20/08/2026",
        "horario": "09:45",
        "convenio": "Unimed",
        "status": "Cancelado"
    },
    {
        "paciente": "Bruno Castro",
        "cpf": "221.334.445-66",
        "medico": "Dra. Camila Dias",
        "especialidade": "Clínica Geral",
        "data": "20/08/2026",
        "horario": "16:00",
        "convenio": "Bradesco Saúde",
        "status": "Agendado"
    },
    {
        "paciente": "Patrícia Lima",
        "cpf": "664.775.886-99",
        "medico": "Dr. Gabriel Azevedo",
        "especialidade": "Urologia",
        "data": "21/08/2026",
        "horario": "10:30",
        "convenio": "SulAmérica",
        "status": "Confirmado"
    },
    {
        "paciente": "Diego Martins",
        "cpf": "112.233.445-56",
        "medico": "Dra. Renata Farias",
        "especialidade": "Psiquiatria",
        "data": "21/08/2026",
        "horario": "12:00",
        "convenio": "Amil",
        "status": "Agendado"
    },
    {
        "paciente": "Sofia Barbosa",
        "cpf": "998.877.665-54",
        "medico": "Dr. Leonardo Torres",
        "especialidade": "Gastroenterologia",
        "data": "22/08/2026",
        "horario": "14:00",
        "convenio": "Hapvida",
        "status": "Confirmado"
    }]),200 


