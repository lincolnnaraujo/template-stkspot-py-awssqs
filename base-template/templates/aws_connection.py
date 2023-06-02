import os

import boto3

from exceptions import AwsSessionIsNotOpened


class AwsSession:
    DEFAULT_HTTP_PROXY = "{{http_proxy}}"
    DEFAULT_HTTPS_PROXY = "{{https_proxy}}"
    HTTP_PROXY_ENV_VAR = "HTTP_PROXY"
    HTTPS_PROXY_ENV_VAR = "HTTPS_PROXY"

    def __init__(self, profile: str, region: str, http_proxy: str = DEFAULT_HTTP_PROXY,
                 https_proxy: str = DEFAULT_HTTPS_PROXY):
        self._profile = profile
        self._region = region
        self._http_proxy = http_proxy
        self._https_proxy = https_proxy
        self._aws_session = None

    def open_session(self) -> boto3.Session:
        if self._aws_session is None:
            self._setup_environment()
            self._aws_session = boto3.Session(profile_name=self._profile, region_name=self._region)

        return self._aws_session

    def get_sqs_client(self):
        self._raise_exception_if_session_not_opened()
        return self._aws_session.client('sqs')

    def _setup_environment(self):
        os.environ[self.HTTP_PROXY_ENV_VAR] = self._http_proxy
        os.environ[self.HTTPS_PROXY_ENV_VAR] = self._https_proxy

    def _raise_exception_if_session_not_opened(self):
        if self._aws_session is None:
            raise AwsSessionIsNotOpened("a sessao com a AWS ainda não foi feita")
