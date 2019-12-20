from sqlalchemy import create_engine

class DbUtils:
    db_string = "postgresql+psycopg2://postgres:banco@postgres:5432/postgres"
    db_query = " "

    def newUser(self, username, email, password):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO tb_users(username, email, password) VALUES (%s, %s, %s)", username, email, password)
            return True
        except:
            return False

    def authUser(self, email, password):
        db = create_engine(self.db_string)
        try:
            res = db.execute("SELECT email, password FROM tb_users WHERE email = %s and password = %s", email, password)
            return res
        except:
            return False

    # def getPosts(self):
    #     db = create_engine(self.db_string)
    #     try:
    #         res = db.execute("SELECT * FROM tb_posts")
    #         return res
    #     except:
    #         return False

    # def registerPost(self, user_id, title, date_posted, content):
    #     db = create_engine(self.db_string)
    #     try:
    #         res = db.execute("INSERT INTO tb_posts(user_id, title, date_posted, content) VALUES (%s, %s, %s, %s)", user_id, title, date_posted, content)
    #         return True
    #     except:
    #         return False

    # def deletePosts(self, id):
    #     db = create_engine(self.db_string)
    #     try:
    #         res = db.execute("DELETE FROM tb_posts WHERE id = %s", id)
    #         return True
    #     except:
    #         return False

    # def updatePosts(self, id, title, content):
    #     db = create_engine(self.db_string)
    #     try:
    #         res = db.execute("UPDATE tb_posts SET title = %s, content = %s, WHERE id = %s", title, content, id)
    #         return True
    #     except:
    #         return False
