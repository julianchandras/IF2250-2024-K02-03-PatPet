from models.articleModel import ArticleModel
from seeds.article_seeds import DEFAULT_ARTICLES

article_model = ArticleModel("database/pet_management.db")
article_model.cursor.execute("DROP TABLE articles")
# length = len(DEFAULT_ARTICLES)
# for i in range(0, length):
#     article_model.add_article(DEFAULT_ARTICLES[i]['title'], DEFAULT_ARTICLES[i]['content'])