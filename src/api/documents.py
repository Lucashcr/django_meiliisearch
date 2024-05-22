from django_meilisearch.documents import Document

from api.models import Post


class PostIndex(Document):
    name = "posts"

    class Django:
        model = Post
        primary_key_field = "id"
        searchable_fields = ["title", "content"]
