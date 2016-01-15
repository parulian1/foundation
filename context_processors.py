from django.conf import settings

def media_url(request):
    """
    Returns context variables containing search form: 
        - ADMIN_MEDIA_PREFIX
    """
    return {
        'media_url_prefix': settings.MEDIA_URL,
    }


def static_url(request):
    """
    Returns context variables containing search form: 
        - ADMIN_MEDIA_PREFIX
    """
    return {
        'static_url_prefix': settings.STATIC_URL,
    }


def blog_media_url(request):
    """
    Returns context variables containing search form: 
        - ADMIN_MEDIA_PREFIX
    """
    return {
        'blog_media_url_prefix': settings.BLOG_MEDIA_URL,
    }