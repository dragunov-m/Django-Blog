from blog.services.comments.service import CommentsService


class GetCommentUseCase:
    def __init__(self):
        self.comment_service = CommentsService()

    def execute(self, post_id: int, author_id: int, content: str):
        return self.comment_service.get_comment(post_id, author_id, content)


class GetCommentsFromPostUseCase:
    def __init__(self):
        self.comment_service = CommentsService()

    def execute(self, post_id: int):
        return self.comment_service.get_comments_from_post(post_id)


class CreateCommentUseCase:
    def __init__(self):
        self.comment_service = CommentsService()

    def execute(self, post_id: int, author_id: int, content: str):
        return self.comment_service.create_comment(post_id, author_id, content)


class DeleteCommentUseCase:
    def __init__(self):
        self.comment_service = CommentsService()

    def execute(self, post_id: int, author_id: int, content: str):
        return self.comment_service.delete_comment(post_id, author_id, content)
