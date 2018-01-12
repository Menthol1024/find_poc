#!/usr/bin/python
# coding:utf-8
# another:blue-bird
from django.forms import  Field, TextInput
from django.utils.html import format_html


class LayuiField(Field):
    """
    预先设置layui 表单 css
    """
    def __init__(self, *args, **kwargs):
        super(LayuiField, self).__init__(*args, **kwargs, widget=TextInput(attrs={'class': 'layui-input',
                                                                                  'autocomplete': 'off',
                                                                                  'style': 'width: 70%;float: left;',
                                                                                  'lay-verify': 'required'})
                                         )
    def clean(self, value):
        if not value is None:
            return value
        else:
            raise ValueError


class LayuiWidget(TextInput):
    """
    预先设置layui表单css
    """
    def __init__(self, name='', type='text', attr=None):
        super(LayuiWidget, self).__init__()
        self.name = name
        self.type = type

    def render(self, name, value, attrs=None, renderer=None):
        if value is None: value = ''
        return format_html('<div class="layui-form-item">' \
                           '<label class="layui-form-label">{name}</label>' \
                           '<div class="layui-input-block">' \
                           '<input type="{type}" name="title" required  lay-verify="required" placeholder="请输入标题" autocomplete="off" class="layui-input">' \
                           '</div>' \
                           '</div>', name=self.name, type=self.type)
