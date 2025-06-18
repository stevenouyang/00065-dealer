from .models import Product
from miscpage.models import MiscPage
from news.models import News
from content.models import ContentSetting


c
    """
    Context processor to add all products to the template context.
    """
    ctx_products = Product.objects.all()
    return {'ctx_products': ctx_products}

def page_context_processor(request):
    """
    Context processor to pages link
    """
    ctx_misc_pages = MiscPage.objects.filter(is_show=True)
    return {'ctx_misc_pages': ctx_misc_pages}


def content_setting_context_processor(request):
    """
    Context processor to retrieve the first ContentSetting object.
    """
    ctx_content_setting = ContentSetting.objects.first()
    return {'ctx_content_setting': ctx_content_setting}


def latest_news_context_processor(request):
    """
    Context processor to add the latest 5 news items to the template context.
    """
    ctx_latest_news = News.objects.order_by('-created_at')[:5]
    return {'ctx_latest_news': ctx_latest_news}
