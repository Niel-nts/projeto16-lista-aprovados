'''Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. O arquivo deve ter a seguinte estrutura:

aluno: Nome do aluno;
nota_1: Primeira nota;
nota_2: Segunda nota;
faltas: Número de faltas;

O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média das duas notas do aluno.
A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa deverá salvar esse novo
dataframe com o nome “alunos_situacao.csv”.

Por fim, o programa deverá mostrar na tela:
- o maior número de faltas;
- a média geral das notas dos alunos;
- e a maior média.'''

import pandas as pd


df=pd.read_csv("planilha_alunos.csv")
media = (df['nota_1']+df['nota_2'])/2
df.insert(loc=4, column='media', value=media)
df.loc[(df['media'] >=7) & (df['faltas'] <=5), 'situação'] = 'Aprovado'
df.loc[(df['media'] <7) | (df['faltas'] > 5), 'situação'] = 'Reprovado'
falta_maior=media_geral=maior_media=cont=0
for c in df['faltas']:
    if c > falta_maior:
        falta_maior=c
for c in df['media']:
    media_geral+=c
    cont+=1
    if c > maior_media:
        maior_media=c
media_geral/=cont
print(f'A maior quantidade de faltas foi: {falta_maior}\nA média geral foi: {media_geral}\nE a maior média: {maior_media}')
df.to_csv("alunos_situacao.csv", index=False)


