from abc import ABC, abstractmethod
from typing import List
import requests

class RequestInfo:
    url: str = None
    method: str = None
    params: dict = None
    headers: dict = None
    content = None
    timeout: tuple = None

    def __init__(self, url: str, method: str, params:dict = None, headers: dict = None, content = None, timeout: tuple = (10, 10)):
        self.url = url
        self.method = method
        self.params = params
        self.headers = headers
        self.content = content
        self.timeout = timeout

class IClient(ABC):

    @abstractmethod
    def add(self, name: str, requestInfo: RequestInfo):
        pass
    
    @abstractmethod
    def request(self, name: str) -> requests.Response:
        pass

class Client(IClient):
    __requests: dict = None

    def __init__(self, pingRequest: RequestInfo = None):
        if pingRequest is not None:
            self.__requests = {"ping" : pingRequest}

    def add(self, name: str, requestInfo: RequestInfo):
        if self.__requests is None:
            self.__requests = {name : requestInfo}
        else:
            self.__requests.update((name, requestInfo))
        
    def request(self, name: str = "ping") -> requests.Response:
        if name in self.__requests:
            requestInfo = self.__requests[name]
            
            return requests.request(
                    method = requestInfo.method, 
                    url = requestInfo.url,
                    params = requestInfo.params,
                    headers = requestInfo.headers,
                    data = requestInfo.content,
                    timeout = requestInfo.timeout
            )

    def signleRequest(self, requestInfo: RequestInfo):

        return requests.request(
            method = requestInfo.method,
            url = requestInfo.url,
            params = requestInfo.params,
            headers = requestInfo.headers,
            data = requestInfo.content,
        )

if __name__ == "__main__":
    client = Client()

    result = client.signleRequest(
        RequestInfo(
            url =  "https://api-fns.ru/api/search",
            method = "GET",
            
        )
    )