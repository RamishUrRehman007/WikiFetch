from json import JSONDecodeError
from typing import List

class WikipediaService:
    URL = 'https://en.wikipedia.org/w/rest.php/v1/search/page'
    HEADERS = {'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://www.mediawiki.org/wiki/API_talk:REST_API)'}
    QUERY = 'Pakistan'
    TOP = 25

    def __init__(self, time_keeper, web_service):
        self.time_keeper = time_keeper
        self.web_service = web_service

    def get_articles(self) -> List[dict]:
        """Get the top 50 Artciles against Pakistan"""
        self.time_keeper.start()

        params = {
            'q': self.QUERY,
            'limit': self.TOP
        }

        response = self.web_service.call_get(self.URL, params=params, headers=self.HEADERS)
        response_json = self._get_response_json(response)
        articles = response_json['pages']

        self.time_keeper.end()
        print(f'PERFORMANCE: It took {self.time_keeper.get_elapsed_time_in_sec()} seconds to retrieve '
              f'the articles: {articles} against Pakistan')

        return articles

    def _get_response_json(self, response):
        try:
            return response.json()
        except JSONDecodeError:
            error_msg = f'There was an error decoding JSON for the response. ' \
                        f'Status code: {response.status_code} ' \
                        f'Content text: {response.text} ' \
                        f'URL: {response.url} ' \
                        f'Headers: {response.headers}'
            print(error_msg)