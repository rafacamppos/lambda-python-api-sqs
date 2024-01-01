import json
import logging
import requests
from dotenv import load_dotenv
from fastapi import HTTPException
import os


logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


load_dotenv('.env')


def get_(
        contrato: str,
        idCorrelation: str):
    try:
        logger.info("Iniciando get ...")
        response = requests.get(
            "http://google.com"
        )
        # response = requests.post(
        #   "http://localhost:8080/aditamento/altera-quantidade-parcelas",
        #  data=json.dumps(contrato),
        #  headers=get_headers_aditamento_post(idCorrelation))
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=500, detail="Erro ao executar a API de aditamento")

    if response.status_code != 200:
        logger.info("Erro ao executar a API de aditamento, parametros inválidos")
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())

    logger.info("Sucesso ao executar o get")
    return {"resultado": "sucesso"}


def get_headers_aditamento_post(id_correlation: str):
    return {"Content-Type": "application/json",
            "itau-pos-venda-teste": id_correlation}
