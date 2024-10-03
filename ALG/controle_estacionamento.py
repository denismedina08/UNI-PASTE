"""
# O trabalho consiste em desenvolver um sistema para controle de estacionamento que contém 3 setores (A, B e C) com 5
vagas para cada setor.

O sistema deverá ter as seguintes funcionalidades:
1) ocupar vaga no estacionamento: lembrando que, o mesmo veículo não pode ocupar duas vagas. Sendo assim, se o veículo
encontra-se estacionado, o sistema não permite a inclusão de um outro veículo com a mesma placa; A entrada no
estacionamento ocorre pela registro da placa. A escolha da vaga será de modo aleatório dentre as vagas disponíveis
livres. Para isto utilize a função random que simula a escolha da vaga pelo motorista. Outro ponto importante, verificar
a disponbilidade de vaga, antes de liberar o estacionamento;
2) liberar vaga: nesta funcionalidade, certifique-se de que o veículo encontra-se estabcionado. O sistema permite a
saída de veículos que tem registro de entrada;
3) exibir as vagas disponíveis no estacionamento, informando por setor as vagas disponíveis;
4) consultar veículo estacionado

A estrutura de dados para o controle das vagas será o array da biblioteca numpy. Pode ser três array's, um para cada
setor do estacionamento.
Todo o sistema precisa ser codificado em blocos (funções), desta forma trará clareza no código.
"""
import numpy as np

def ocupar_estacionamento():
    vehiculo = True