# Imports
import json
from botocore.exceptions import ProxyConnectionError
import AwsSqsEvents as events
from aws_connection import AwsSession

# Configs de ambiente #
HTTP_PROXY = "{{http_proxy}}"
HTTPS_PROXY = "{{https_proxy}}"
AWS_PROFILE = "{{aws_profile}}"
REGION = "{{aws_region}}"


def execute_publish_data_aws_sqs():
    print("Iniciando o processamento")

    # Arquivo json
    listaDataFile = open('data.json')

    # Load arquivo
    listaItem = json.load(listaDataFile)

    print("Abrindo sessão com a conta AWS")
    awssession = AwsSession(profile=AWS_PROFILE, region=REGION)
    awssession.open_session()
    sqs_enviar = events.PublishSQSEvent(aws_session=awssession)

    # Iterar lista
    for i in listaItem['data']:
        try:
            handle_json_data(i, sqs_enviar)
            print("Sucesso ao enviar mensagem:", i)
        except ProxyConnectionError:
            print("Erro de proxy: " + json.dumps(i))

    # Fechar arquivo
    listaDataFile.close()


def handle_json_data(data_event: dict, sqs: events.PublishSQSEvent):
    sqs_payload = json.dumps(data_event)
    sqs.send_message(payload=sqs_payload)
