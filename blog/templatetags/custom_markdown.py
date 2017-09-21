#!/usr/bin/env python
# -*- coding: utf-8 -*-


import houdini as h
import misaka as m
from django import template
from pygments import highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from pygments.lexers import get_lexer_by_name
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter(is_safe=True)
@stringfilter
class HighlighterRenderer(m.HtmlRenderer):
    def blockcode(self, text, lang):
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            lexer = None

        if lexer:
            formatter = HtmlFormatter()
            return highlight(text, lexer, formatter)
        # default
        return '\n<pre><code>{}</code></pre>\n'.format(
                            h.escape_html(text.strip()))


@register.filter
def custom_markdown(value):

    renderer = HighlighterRenderer()
    md = m.Markdown(renderer, extensions=('fenced-code','tables','highlight'))
    return md(value)
