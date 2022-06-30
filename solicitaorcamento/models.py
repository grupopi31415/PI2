from django.db import models
from users.models import Usuario


class Orc(models.Model):

    status_choices = (('P', 'Pendente'),
                     ('F', 'Finalizado'))

    finalidade_choices = (('L', 'Lazer'),
                       ('N', 'Negócios'),
                       ('E', 'Estudos'),
                       ('O', 'Outros'))

    passagem_choices = (('A', 'Aérea'),
                      ('T', 'Terrestre'),
                      ('M', 'Matítima'))


    pensao_choices = (('CM', 'Café da manhã'),
                      ('MP', 'Meia pensão'),
                      ('PC', 'Pensão Completa'),
                      ('AI', 'All Inclusive'))

    hotel_choices = (('1', '1 estrela'),
                      ('2', '2 estrela'),
                      ('3', '3 estrelas'),
                      ('4', '4 estrelas'),
                      ('5', '5 estrelas'))


    dt_ida = models.DateField()
    dt_volta = models.DateField()
    destino = models.CharField(max_length=100, null=True, blank=False)
    finalidade = models.CharField(max_length=50, choices=finalidade_choices, default='')
    tipo_passagem = models.CharField(max_length=50, choices=passagem_choices, default='')
    nome = models.CharField(max_length=50, null=False, default='')
    email = models.EmailField(max_length=50, null=False, default='')
    orcamento = models.CharField(max_length=15, null=True, blank=True, default='R$ ')
    observacoes = models.CharField(max_length=300, null=True, blank=True)
    classificacao_hotel = models.CharField(max_length=12,choices=hotel_choices, default=3)
    tipo_pensao = models.CharField(max_length=50, choices=pensao_choices, default='')
    qtde_0_6 = models.IntegerField(default=0)
    qtde_7_12 = models.IntegerField(default=0)
    qtde_adultos = models.IntegerField(default=0)
    qtde_melhor_idade = models.IntegerField(default=0)
    transfer = models.BooleanField(default=False)
    seguro_viagem = models.BooleanField(default=False)
    passeios = models.BooleanField(default=False)
    ingressos = models.BooleanField(default=False)






