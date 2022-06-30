from django.forms import ModelForm
from solicitaorcamento.models import Orc

class OrcForm(ModelForm):
    class Meta:
        model = Orc
        fields = ['dt_ida','dt_volta', 'destino', 'finalidade', 'tipo_passagem', 'nome',
                  'email','orcamento','observacoes','classificacao_hotel','tipo_pensao',
                  'qtde_0_6','qtde_7_12','qtde_adultos','qtde_melhor_idade','transfer','seguro_viagem','passeios',
                  'ingressos']
