import requests
from requests.adapters import HTTPAdapter, Retry


class WebService:
    MAX_RETRIES = 50
    BACKOFF_FACTOR = .5
    STATUS_RETRY_LIST = [429, 495, 500, 502, 503, 504]

    def __init__(self):
        self.session = None

    def _get_session(self):
        if self.session is None:
            self.session = requests.Session()
            retries = Retry(total=self.MAX_RETRIES, backoff_factor=self.BACKOFF_FACTOR,
                            status_forcelist=self.STATUS_RETRY_LIST)
            self.session.mount('https://', HTTPAdapter(max_retries=retries))
        return self.session

    def call_get(self, url, params=None, headers=None, retry=True):
        if not headers:
            headers = {}
        headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
        if retry:
            return self._get_session().get(url=url, params=params, headers=headers)
        else:
            return requests.get(url=url, params=params, headers=headers)

