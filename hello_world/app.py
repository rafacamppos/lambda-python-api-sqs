from __future__ import annotations
from fastapi import FastAPI
import logging
from rest import Client as client
from sqs import Sqs as sqs

app = FastAPI()

logger = logging.getLogger(__name__)


def get_headers_aditamento_post(id_correlation: str):
    return {"Content-Type": "application/json",
            "itau-pos-venda-teste": id_correlation}


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def lambda_handler(event, context):
    print(event)
    logger.info(f' Evento recebido com sucesso, body={event["body"]}, correlationId={event["correlationId"]}')
    response = client.get_(event["body"], event["correlationId"])
    sqs.enviar_mensagem_sqs(str(response))
    return {
        "statusCode": 200,
        "body": "sucesso"
    }
