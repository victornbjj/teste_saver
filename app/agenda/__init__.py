from flask import Blueprint

agenda_bp = Blueprint(
    "agenda",
    __name__,
    template_folder="../templates"
)

from app.agenda import routes