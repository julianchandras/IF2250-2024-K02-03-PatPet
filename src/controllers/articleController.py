from PyQt5.QtWidgets import QStackedWidget
from models.articleModel import ArticleModel
from boundaries.articleViews.mainArticleView import MainArticleView
from boundaries.articleViews.detailArticleView import DetailArticleView


class ArticleController:
    def __init__(self, stacked_widget : QStackedWidget, article_model : ArticleModel) :
        self.stacked_widget = stacked_widget
        self.article_model = article_model

        self.main_article_view : MainArticleView= self.stacked_widget.widget(1)  # Main article view index 1
        self.detail_article_view : DetailArticleView = self.stacked_widget.widget(2)

        self.main_article_view.view_article_signal.connect(self.navigate_to_detail)

        self.load_articles()

    def load_articles(self):
        articles = self.article_model.get_all_articles()
        self.main_article_view.set_articles(articles)

    def navigate_to_detail(self, article_id):
        article = self.article_model.get_specific_article(article_id)
        self.detail_article_view.set_article_details(article)
        self.stacked_widget.setCurrentIndex(2)