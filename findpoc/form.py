#!/usr/bin/python
# coding:utf-8
# another:blue-bird
from django import forms
from .models import Poc, Audit
from .field import LayuiField, LayuiWidget


class SearchForm(forms.Form):
    q = forms.CharField(max_length=40, label=None, widget=forms.TextInput(attrs={'class': 'layui-input',
                                                                                       'autocomplete': 'off',
                                                                                       'style': 'width: 70%;float: left;',
                                                                                       'lay-verify': 'required'}))


class UploadForm(forms.ModelForm):
    class Meta:
        model = Audit
        fields = '__all__'
        desc = forms.Textarea()

        labels = {
            'bugtype': '漏洞类型',
            'version': '版本',
            'place':'漏洞文件',
            'another': '作者',
            'email': '邮箱',
            'desc': "漏洞详情",
            'package': "影响组件"

        }



