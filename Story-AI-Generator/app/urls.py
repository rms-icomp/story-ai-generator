from django.urls import path
from .views import executar_prompt, formulario_view, exportar_historias_excel

urlpatterns = [
    path('executar-prompt/', executar_prompt, name="executar_prompt"),
    path('exportar/historias/', exportar_historias_excel, name='exportar_clientes'),
    path('', formulario_view, name="formulario"),
]