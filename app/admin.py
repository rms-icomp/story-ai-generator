from django.contrib import admin

from app.models import HistoriaUsuario, Produto, Usuario

class UsuarioInline(admin.TabularInline):  # ou StackedInline se preferir
    model = Usuario
    extra = 1
    search_fields = ("usuario_papel",)


class HistoriaUsuarioInline(admin.TabularInline):
    model = HistoriaUsuario
    extra = 1
    search_fields = ("titulo", "como",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "apresentacao_produto_resumo")
    search_fields = ("apresentacao_produto",)
    inlines = [UsuarioInline, HistoriaUsuarioInline]

    def apresentacao_produto_resumo(self, obj):
        return obj.apresentacao_produto[:60]
    apresentacao_produto_resumo.short_description = "Apresentação"


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("usuario_papel", "produto", "descricao_resumo")
    search_fields = ("usuario_papel", "descricao_usuario", "acoes_usuario")
    list_filter = ("produto",)

    def descricao_resumo(self, obj):
        return obj.descricao_usuario[:50]
    descricao_resumo.short_description = "Descrição do Usuário"


@admin.register(HistoriaUsuario)
class HistoriaUsuarioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "como", "produto", "resumo_historia")
    search_fields = ("titulo", "como", "eu_quero", "para_que")
    #list_filter = ("produto",)

    def resumo_historia(self, obj):
        return f"Eu quero {obj.eu_quero[:40]}..."
    resumo_historia.short_description = "Resumo"
