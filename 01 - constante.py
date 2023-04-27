"""
CONSTANTE = "Variaveis" que não mudam de valor
muitas condições no mesmo if (Ruim)
  <-- Contagem de complexidade (Ruim)

"""

velocidade = 61 # km/h (constante) velocidade atual do carro
local_carro = 101 # km/h (constante) Local em que o carro esta na estrada em km 


RADAR_1 = 60 # km/h (constante) Limite de velocidade
LOCAL_1 = 100 # km/h (constante) Local do radar 1
RADAR_RANGE = 1 # km/h (constante) Alcance do radar

# armazenando o resultado da condição em uma variavel
pos_carro = local_carro >= (LOCAL_1 - RADAR_1)
rang_carro = local_carro  <= (LOCAL_1 + RADAR_RANGE)
vel_carro_pass_radar_1 = velocidade > RADAR_1
dif_vel = velocidade > RADAR_1

carro_passou_radar_1 = pos_carro and rang_carro and dif_vel
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade do carro Passou do radar 1')

if carro_passou_radar_1:
    print('Carro Passou do radar 1')



if carro_multado_radar_1:
      print('Multado')


 









