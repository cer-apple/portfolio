from django import template
from django.urls import translate_url as _translate_url

register = template.Library()


@register.simple_tag
def translate_url(url, lang_code):
    """Translate the given URL to the target language.

    Works for any URL pattern, including those with captured arguments
    (e.g. /projects/<slug>/), unlike `{% url url_name %}` which requires
    each argument to be passed explicitly.
    """
    return _translate_url(url, lang_code)
