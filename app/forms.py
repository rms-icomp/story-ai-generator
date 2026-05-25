from django import forms

class InformacaoForm(forms.Form):
    apresentacao = forms.CharField(label="Apresentação do Produto", max_length=255)
    user_nome = forms.CharField(label="Nome", max_length=255)
    user_descricao = forms.CharField(label="Descrição", max_length=255)
    user_acoes = forms.CharField(label="Ações", max_length=255)
    requisitos = forms.CharField(label="Requisitos Funcionais", max_length=255)