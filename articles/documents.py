from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer
from .models import Article


article_index = Index('articles')
article_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

html_strip = analyzer(
    'html_strip',
    tokenizer='standard',
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@registry.register_document
class ArticleDocument(Document):

    author = fields.ObjectField(properties={
        'username': fields.TextField(),
        'id': fields.IntegerField()
    })

    class Index:
        name = 'articles'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Article
        fields = ['id', 'title', 'body', 'created', 'modified', 'pub_date']
