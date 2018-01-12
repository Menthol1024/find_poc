#!/usr/bin/python
# coding:utf-8
# another:blue-bird
from django import template
from django.template.context import Context

register = template.Library()


@register.inclusion_tag('admin/auditline.html', takes_context=True)
def auditline(context):

    change = context['change']

    url = '/admin/{0}'.format(context['request'].path.split('/')[-3])

    is_popup = context['is_popup']
    save_as = context['save_as']
    show_save = context.get('show_save', True)
    show_save_and_continue = context.get('show_save_and_continue', True)
    ctx = Context(context)
    ctx.update({
        'url':url,
        'show_delete_link': (
                not is_popup and context['has_delete_permission'] and
                change and context.get('show_delete', True)
        ),
        'show_save_and_add_another': (
                context['has_add_permission'] and not is_popup and
                (not save_as or context['add'])
        ),
        'show_save_and_continue': not is_popup and context['has_change_permission'] and show_save_and_continue,
        'show_save_as_new': show_save,
    })
    return ctx

