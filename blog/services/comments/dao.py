from blog.models import Comment


class CommentsDAO:

    @classmethod
    def get_comment(cls, post_id: int, author_id: int, content: str):
        return Comment.objects.filter(post=post_id, author=author_id, content=content)

    @classmethod
    def get_comments_from_post(cls, post_id: int):
        return Comment.objects.filter(post=post_id)

    @classmethod
    def create_comment(cls, post_id: int, author_id: int, content: str):
        comment = Comment.objects.create(post=post_id, author=author_id, content=content)
        return comment

    @classmethod
    def delete_comment(cls, post_id: int, author_id: int, content: str):
        comment = Comment.objects.get(post=post_id, author=author_id, content=content)
        comment.delete()
