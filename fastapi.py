from fastapi import FastAPI


app = FastAPI()


@app.get("/get-comments")
def get_comments(db_session, query_params):
    author = query_params.get("author")
    sql = f"SELECT * FROM blog_posts WHERE author = {author}"

    blog_posts = db_session.execute(sql)
    comments = []

    for blog_post in blog_posts:
        sql = f"SELECT * FROM comments WHERE blog_post = {blog_post.id}"
        post_comments = db_session.execute(sql)

        for comment in post_comments:
            comments.append(comment)

    return comments
