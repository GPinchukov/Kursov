from django import forms


class FindGroup(forms.Form):
    group = forms.CharField(label='Группа', max_length=10, required=False)


class FindProj(forms.Form):
    project_name = forms.CharField(label='Дипломный проект', max_length=50, required=False)


class FindStud(forms.Form):
    stfio = forms.CharField(label='ФИО Студента', max_length=50, required=False)


class FindLid(forms.Form):
    leaders_fio = forms.CharField(label='ФИО руководителя', max_length=50, required=False)


class FindRev(forms.Form):
    reviewers_fio = forms.CharField(label='ФИО Рецензента', max_length=50, required=False)