from django import template
from sape.sape_client import sape_manager

register = template.Library()

@register.inclusion_tag('sape/links.html', takes_context=True)
def sape_links(context, title=None):
    request = context['request']
    if request:
        query_string = request.META.get('QUERY_STRING', '')

        uri = ''.join([request.META["PATH_INFO"],
                        len(query_string) and '?' or '',
                        query_string])
        links = sape_manager.get_links(uri)
        if links:
            return {'links': links, 'block_title': title}
        return {'empty_block': True}
