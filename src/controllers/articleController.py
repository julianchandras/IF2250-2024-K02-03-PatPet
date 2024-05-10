from PyQt5.QtWidgets import QStackedWidget
from models.articleModel import ArticleModel
class ArticleController:
    def __init__(self, stacked_widget : QStackedWidget, article_model : ArticleModel) :
        pass
    
    def getArticle(self, articleId):
        return self.articleService.getArticle(articleId)