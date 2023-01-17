import unittest
from articles_main import AddArticle

from wikipedia_service import WikipediaService
from models import article_model as AM

class TestFilterArticles(unittest.TestCase):
    def test_filter_articles(self):
        actual = AddArticle(WikipediaService, AM).filter_article(
            {'id':23235,
            'title':'Pakistan War',
            'excerpt':'text in this article correctly about war. <span class=\"searchmatch\">Pakistan</span> (Urdu: پاکِستان [<span class=\"searchmatch\">ˈpaːkɪstaːn</span>]), officially the Islamic Republic of <span class=\"searchmatch\">Pakistan</span> (اِسلامی جمہوریہ پاکِستان), is a',
            'matched_title':None,
            'description':'Country in South Asia',
            'thumbnail':{'mimetype':'image/svg+xml','size':None,'width':60,'height':40,"duration":None,
            'url':'//upload.wikimedia.org/wikipedia/commons/thumb/3/32/Flag_of_Pakistan.svg/60px-Flag_of_Pakistan.svg.png'}
            }
        )
        expected = None
        self.assertEqual(actual, expected)