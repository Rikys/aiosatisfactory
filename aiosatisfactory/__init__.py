import aiohttp
from .lightweight import LightweightAPI
from .https import HttpsAPI


class SatisfactoryServer:
    def __init__(self, session: aiohttp.ClientSession, host: str, port: int = 7777, self_signed_certificate: bool = True, api_token: str = ""):
        self._lightweight = LightweightAPI(host, port)
        self._https = HttpsAPI(self_signed_certificate, host, port, session, api_token)

    @property
    def lightweight(self) -> LightweightAPI:
        return self._lightweight
    
    @property
    def https(self) -> HttpsAPI:
        return self._https

