from PyQt5.QtWidgets import QStackedWidget
from models.activityModel import ActivityModel

class ActivityController:
    def __init__(self, QStackedWidget : QStackedWidget,  activity_model : ActivityModel):
        pass
    
    def getArticle(self, articleId):
        return self.articleService.getArticle(articleId)