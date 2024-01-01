import boto3
import botocore
import logging


logger = logging.getLogger(__name__)


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

sqs = boto3.client('sqs',
                   endpoint_url='http://host.docker.internal:4566',
                   aws_access_key_id="foo",
                   aws_secret_access_key="bar",
                   region_name="sa-east-1"
                   )


def enviar_mensagem_sqs(obj):
    try:
        resp = sqs.send_message(
            QueueUrl="http://host.docker.internal:4566/000000000000/upload-file-event-sqs",
            MessageBody=(
                obj
            )
        )
        logger.info(f' Mensagem {obj} enviada com sucesso, response {resp}')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InternalError':
            logger.info('Error Message: {}'.format(e.response['Error']['Message']))
            logger.info('Request ID: {}'.format(e.response['ResponseMetadata']['RequestId']))
            logger.info('Http code: {}'.format(e.response['ResponseMetadata']['HTTPStatusCode']))
        else:
            logger.info('Error Message: {}'.format(e.response['Error']['Message']))
            raise e
