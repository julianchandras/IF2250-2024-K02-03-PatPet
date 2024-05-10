from models.baseModel import BaseModel

class ArticleModel(BaseModel):
    def __init__(self, db_name):
        super().__init__(db_name)  # Call the BaseModel constructor
        self.create_tables()  # Ensure tables are created

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
