import os
import sys
import pytest
root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir + '/src')
from src.models.articleModel import ArticleModel
from src.seeds.article_seeds import DEFAULT_ARTICLES

class TestArticleModel:
    @pytest.fixture
    def article_model(self):
        model = ArticleModel('database/test.db')
        # Ketika create, ada juga input DEFAULT_ARTICLES
        
        yield model
        
        model.cursor.execute("DROP TABLE articles")
        model.commit()
        model.close()

    def test_get_all_articles(self, article_model: ArticleModel):
        dummy_articles = [
            ("Judul Pertama", "Konten paragraf dari artikel 1"),
            ("Judul Kedua", "Konten paragraf dari artikel 2"),
            ("Judul Ketiga", "Konten paragraf dari artikel 3")
        ]
        for article in dummy_articles:
            article_model.add_article(article[0], article[1])

        articles = article_model.get_all_articles()

        assert len(articles) - + len(DEFAULT_ARTICLES) == 3

        for i in range(len(articles) - len(DEFAULT_ARTICLES)):
            assert articles[i+ len(DEFAULT_ARTICLES)][1] == dummy_articles[i][0]
            assert articles[i+ len(DEFAULT_ARTICLES)][2] == dummy_articles[i][1]

    def test_get_specific_article(self, article_model:ArticleModel):
        dummy_articles = [
            ("Cara Merawat Anjing", "Jangan lupa dimandiin."),
            ("Minuman Favorit Kucing", "Kucing sangat suka meminum susu sapi."),
            ("Rahasia Umur Panjang Anjing Kecintaan!", "Dikasih makan Steak")
        ]

        for article in dummy_articles:
            article_model.add_article(article[0], article[1])

        specific_article_row = article_model.get_specific_article(2 + + len(DEFAULT_ARTICLES))

        assert specific_article_row[0] == 2 + + len(DEFAULT_ARTICLES)
        assert specific_article_row[1] == "Minuman Favorit Kucing"
        assert specific_article_row[2] == "Kucing sangat suka meminum susu sapi."

    def test_add_article(self, article_model:ArticleModel):
        article_model.add_article("Legenda Hewan Peliharaan: Tom dan Jerry", "Mereka sebenarnya teman baik")
        articles = article_model.get_all_articles()
        
        assert len(articles) - len(DEFAULT_ARTICLES) == 1
        assert articles[0 + len(DEFAULT_ARTICLES)][1] == "Legenda Hewan Peliharaan: Tom dan Jerry"
        assert articles[0 + len(DEFAULT_ARTICLES)][2] == "Mereka sebenarnya teman baik"


    def test_insert_default_articles(self, article_model:ArticleModel):
        articles = article_model.get_all_articles()
        assert len(articles) == len(DEFAULT_ARTICLES)
        
        for i, article in enumerate(articles):
            assert article[1] == DEFAULT_ARTICLES[i]["title"]
            assert article[2] == DEFAULT_ARTICLES[i]["content"]