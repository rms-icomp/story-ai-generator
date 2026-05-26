from django.db import models

class Produto(models.Model):
    apresentacao_produto = models.TextField(
        verbose_name="Apresentação do Produto"
    )

    informacoes_adicionais = models.TextField(
        verbose_name="Informações Adicionais do Produto",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.apresentacao_produto[:60]


class Usuario(models.Model):
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name="usuarios"
    )
    usuario_papel = models.CharField(
        max_length=150,
        verbose_name="Usuário (Função ou Papel)"
    )
    descricao_usuario = models.TextField(
        verbose_name="Descrição do Usuário"
    )
    acoes_usuario = models.TextField(
        verbose_name="Ações do Usuário",
        help_text="O que o usuário faz dentro do sistema?"
    )

    def __str__(self):
        return f"{self.usuario_papel} → {self.produto}"


class HistoriaUsuario(models.Model):
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name="historias"
    )

    titulo = models.CharField(
        max_length=200,
        verbose_name="Título da História"
    )
    como = models.CharField(
        max_length=200,
        verbose_name="Como (Persona/Usuário)"
    )
    eu_quero = models.CharField(
        max_length=300,
        verbose_name="Eu quero (Ação desejada)"
    )
    para_que = models.CharField(
        max_length=300,
        verbose_name="Para que (Motivo / Benefício)"
    )

    def __str__(self):
        return f"{self.titulo} (Como {self.como})"
