
## {{project_name}}

#### inputs
    - {{aws_profile}}
    - {{aws_region}}
    - {{http_proxy}}
    - {{https_proxy}}
    - {{aws_sqs_queue_name}}
    - {{aws_sqs_queue_arn}}
    - {{aws_sqs_queue_url}}

#### Necessário importar pacotes na config Python interpreter:
    - boto3

![Screenshot](docs/boto3-pkg-settings.png)

### Como usar ?
Basta adicionar o seu payload json no arquivo 'data.json' e executar 'main.py' :D

### Obs1: Lembrar de atualizar as suas credenciais antes de executar o script
![Screenshot](docs/conf-credentials-aws.png)
