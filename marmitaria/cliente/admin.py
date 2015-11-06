from django.contrib import admin
from marmitaria.core.models import Vendas
from marmitaria.cliente.models import Clientes
from marmitaria.produto.models import Produtos
from marmitaria.financeiro.models import Financeiro

class VendasAdmin(admin.ModelAdmin):
    list_display = ('data', 'descricao', 'cliente', 'produto', 'tipo', 'entrada', 'saida', 'somartotal')
    date_hierarchy = 'criado'
    search_fields = ('data', 'descricao', 'cliente', 'produto', 'tipo', 'entrada', 'saida')
    list_filter = ['criado']
    list_editable = ('data', 'descricao', 'cliente', 'produto', 'tipo', 'entrada', 'saida')

class ClientesAdmin(admin.ModelAdmin):
    pass

class ProdutosAdmin(admin.ModelAdmin):
    pass

class FinanceiroAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vendas, VendasAdmin)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Financeiro, FinanceiroAdmin)
