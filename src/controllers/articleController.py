
class ArticleController:
    def __init__(self):
        pass
    
    def getArticle(self, articleId):
        return self.articleService.getArticle(articleId)