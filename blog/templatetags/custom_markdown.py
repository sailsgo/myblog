#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import template
import markdown


register = template.Library()

config = {
    'codehilite': {
        'use_pygments': False,
        'css_class': 'prettyprint linenums',
    }
}
@register.filter
def custom_markdown(value):
    content_html = markdown.markdown(value, extensions=['codehilite','extra','tables','nl2br'], extension_configs=config)

    #md=m.Markdown(renderer,
     #  extensions=m.EXT_FENCED_CODE | m.EXT_NO_INTRA_EMPHASIS)
    #mdp = mistune.Markdown(escape=True, renderer=renderer)
    return content_html
