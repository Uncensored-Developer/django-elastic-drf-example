from rest_framework.routers import SimpleRouter
from .apiviews import ArticleViewSet

app_name = 'articles'

router = SimpleRouter()
router.register(
    prefix=r'',
    base_name='articles',
    viewset=ArticleViewSet
)
urlpatterns = router.urls