import logging
import os
import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

MOCK_API_URL = os.getenv("MOCK_API_URL")


def buscar_agendamentos():
    try:
        response = requests.get(MOCK_API_URL, timeout=5)

        if response.status_code != 200:
            logger.error("API respondeu com status %s", response.status_code)
            return [], "Erro ao consultar a API."

        try:
            dados = response.json()
        except ValueError:
            logger.error("Resposta não contém JSON válido.")
            return [], "Resposta inválida da API."

        if not isinstance(dados, list):
            logger.error("Resposta não é uma lista.")
            return [], "Formato de resposta inválido."

        # Campos obrigatórios
        campos = {
            "paciente",
            "cpf",
            "medico",
            "especialidade",
            "data",
            "horario",
            "convenio",
            "status",
        }

        # Valida cada item
        for i, item in enumerate(dados):
            if not isinstance(item, dict):
                logger.error("Item %s não é um dicionário.", i)
                return [], "Dados inválidos."

            faltando = campos - item.keys()

            if faltando:
                logger.error("Item %s está sem os campos %s", i, faltando)
                return [], "Dados incompletos."

        return dados, None

    except requests.exceptions.Timeout:
        logger.error("Timeout ao acessar a API.")
        return [], "A API demorou para responder."

    except requests.exceptions.ConnectionError:
        logger.error("Não foi possível conectar à API.")
        return [], "A API está indisponível no momento."

    except requests.exceptions.RequestException as e:
        logger.error("Erro HTTP: %s", e)
        return [], "Erro ao acessar a API."
