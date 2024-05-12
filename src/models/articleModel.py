from models.baseModel import BaseModel
from seeds.article_seeds import DEFAULT_ARTICLES
class ArticleModel(BaseModel):
    def __init__(self, db_name):
        super().__init__(db_name)  # Call the BaseModel constructor
        self.create_tables()  # Ensure tables are created
        self.insert_default_articles()  # Insert default articles if there are none

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS articles (
                article_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
            """
        )
        self.commit()  # Commit table creation
    
    def get_all_articles(self):
        self.cursor.execute("SELECT * FROM articles")
        rows = self.cursor.fetchall()
        return rows

    def get_specific_article(self, article_id):
        self.cursor.execute("SELECT * FROM articles WHERE article_id = ?", (article_id,))
        row = self.cursor.fetchone()
        return row

    def add_article(self, title, content):
        self.cursor.execute(
            "INSERT INTO articles (title, content) VALUES (?, ?)",
            (title, content),
        )
        self.commit()

    def insert_default_articles(self):
        current_articles = self.get_all_articles()
        if not current_articles:  # If there are no articles, insert default ones
            for article in DEFAULT_ARTICLES:
                self.add_article(
                    article["title"],
                    article["content"]
                )