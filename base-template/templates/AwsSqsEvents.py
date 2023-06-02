from aws_connection import AwsSession


class PublishSQSEvent:

    def __init__(self, aws_session: AwsSession):
        self.name = "{{aws_sqs_queue_name}}"
        self.arn = "{{aws_sqs_queue_arn}}"
        self.url = "{{aws_sqs_queue_url}}"
        self._sqs = aws_session.get_sqs_client()

    def send_message(self, payload: str, msg_attributes=None):
        if msg_attributes is None:
            msg_attributes = {}

        return self._sqs.send_message(QueueUrl=self.url, MessageBody=payload, MessageAttributes=msg_attributes)

