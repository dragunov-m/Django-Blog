from blog.services.comments.dao import CommentsDAO


class CommentsService:

    def __init__(self):
        self.comment_dao = CommentsDAO()

    def get_comment(self, post_id: int, author_id: int, content: str):
        return self.comment_dao.get_comment(post_id, author_id, content)

    def get_comments_from_post(self, post_id: int):
        return self.comment_dao.get_comments_from_post(post_id)

    def create_comment(self, post_id: int, author_id: int, content: str):
        return self.comment_dao.create_comment(post_id, author_id, content)

    def delete_comment(self, post_id: int, author_id: int, content: str):
        return self.comment_dao.delete_comment(post_id, author_id, content)
