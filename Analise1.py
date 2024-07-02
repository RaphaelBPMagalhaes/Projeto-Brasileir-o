import pandas as pd 
from datetime import datetime, timedelta
from matplotlib.pyplot as plt
import os

#SUBIR O DADOS EM CSV PARA 
cartoes_doc = 'C:/Users/lucia/OneDrive/Área de Trabalho/Projeto Analista de Dados/Brasileirão/campeonato-brasileiro-cartoes.csv'
#esse relatório contém o dados de cartões recebidos por jogadores e times. As colunas são: "partida_id","rodata","clube","cartao","atleta","num_camisa","posicao","minuto" / e os dados são a partir de 2014. 

partidas_doc = 'C:/Users/lucia/OneDrive/Área de Trabalho/Projeto Analista de Dados/Brasileirão/campeonato-brasileiro-estatisticas-full.csv'
#esse rela´torio possui essas colunas: "partida_id","rodata","clube","chutes","chutes_no_alvo","posse_de_bola","passes","precisao_passes","faltas","cartao_amarelo","cartao_vermelho","impedimentos","escanteios"
#entretanto os dados efetivamente só começam a partir do ano de 2015. Antes disso fica inviavel a analise por falta de dados preenchidos. ?
brasileirao_doc = 'C:/Users/lucia/OneDrive/Área de Trabalho/Projeto Analista de Dados/Brasileirão/campeonato-brasileiro-full.csv'
#esse relatório contém os dados de todas as partidas desde 2013 do campeonato brasileiro contendo essas informações nas colunas: "ID","rodata","data","hora","mandante","visitante","formacao_mandante","formacao_visitante","tecnico_mandante","tecnico_visitante","vencedor","arena","mandante_Placar","visitante_Placar","mandante_Estado","visitante_Estado"
#entretanto o dado de "tecnico_mandante","tecnico_visitante" só começou a partir de 2014 e os dados de "formacao_mandante","formacao_visitante" a partir de 2015. Então até a data o ano de 2013 não há informações completas.

gols_doc = 'C:/Users/lucia/OneDrive/Área de Trabalho/Projeto Analista de Dados/Brasileirão/campeonato-brasileiro-gols.csv'
#esse relatório contem os gols por jogador a partir do ano de 2014, contendo essas colunas: "partida_id","rodata","clube","atleta","minuto","tipo_de_gol"

cartoes_df = pd.read_csv(cartoes_doc, index_col='partida_id')
partidas_df = pd.read_csv(partidas_doc, index_col='partida_id' )
brasileirao_df = pd.read_csv(brasileirao_doc, index_col='ID')
brasileirao_data = pd.read_csv(brasileirao_doc, index_col='data')
gols_df = pd.read_csv(gols_doc, index_col='partida_id')


print(cartoes_df.head(5))
print(partidas_df.head(5))
print(brasileirao_df.head(5))
print(gols_df.head(5))

print(cartoes_df.columns)
print(partidas_df.columns)
print(brasileirao_df.columns)
print(gols_df.columns)

print(cartoes_df.dtypes)
print(partidas_df.dtypes)
print(brasileirao_df.dtypes)
print(gols_df.dtypes)

#CLASSIFICAÇÃO DOS DADOS. Transformando cada coluna no tipo ideal inicialmente. (Objc é uma classificação geral das variaveis mas na realidade )
            #CARTOES DF
            #no relatório de cartões trataremos todos os dados como string. Dados númericos como partida, minuto, num_camisa, são apenas para categorizar, não tendo funções matematicas aplicadas. 
            cartoes_df.index = cartoes_df.index.astype(str)
            cartoes_df['rodata'] = cartoes_df['rodata'].astype(str)
            cartoes_df['clube'] = cartoes_df['clube'].astype(str)
            cartoes_df['cartao'] = cartoes_df['cartao'].astype(str)
            cartoes_df['atleta'] = cartoes_df['atleta'].astype(str)
            cartoes_df['num_camisa'] = cartoes_df['num_camisa'].astype(str)
            cartoes_df['posicao'] = cartoes_df['posicao'].astype(str)
            cartoes_df['minuto'] = cartoes_df['minuto'].astype(str)

            print(cartoes_df.dtypes)
            

            #PARTIDAS DF
            #no relatorio de partidas, dados estatisticos e por isso são variaveis numéricas com aplicações matematicas possiveis. 
            partidas_df['partida_id'] = partidas_df['partida_id'].astype(str)
            partidas_df['rodata'] = partidas_df['rodata'].astype(str)
            partidas_df['clube'] = partidas_df['clube'].astype(str)
            partidas_df['chutes'] = partidas_df['chutes'].astype('int64')
            partidas_df['chutes_no_alvo'] = partidas_df['chutes_no_alvo'].astype('int64')
            #como temos algumas variaveis de proporção preciso transformar as str em Floats, pra isso preciso tirar o "%" do dado:
            partidas_df['posse_de_bola'] = partidas_df['posse_de_bola'].str.rstrip('%').astype('float') / 100.0
            partidas_df['precisao_passes'] = partidas_df['precisao_passes'].str.rstrip('%').astype('float') / 100.0
            partidas_df['faltas'] = partidas_df['faltas'].astype('int64')
            #partidas_df['cartao_amarelo '] = partidas_df['cartao_amarelo '].astype('int64')
            #partidas_df['cartao_vermelho'] = partidas_df['cartao_vermelho '].astype('int64')
            partidas_df['impedimentos'] = partidas_df['impedimentos'].astype('int64')
            partidas_df['escanteios'] = partidas_df['escanteios'].astype('int64')

            print(partidas_df.dtypes)


            #BRASILEIRAO DF

            brasileirao_df.index = brasileirao_df.index.astype(str)
            brasileirao_df['rodata'] = brasileirao_df['rodata'].astype(str)
            brasileirao_df['data'] = brasileirao_df['data'].astype(str)
            brasileirao_df['data'] = pd.to_datetime(brasileirao_df['data'], format='%d/%m/%Y')

                brasileirao_df['hora'] = pd.to_datetime(brasileirao_df['hora'], format='%H:%M', dayfirst= False)

       #brasileirao_df['hora'] = pd.to_datetime(brasileirao_df['hora'], format='%H:%M').dt.time
            #converti a data para uma variavel de tempo para ficar mais facil de utilizar mas a variavel de hora e minuto estava dando erro, acredito que por conta da falta de dados. 
            print(brasileirao_df.dtypes)


            #GOLS DF
            gols_df['partida_id'] = gols_df['partida_id'].astype(str)
            gols_df['rodata'] = gols_df['rodata'].astype(str)
            gols_df['tipo_de_gol'] = gols_df['tipo_de_gol'].astype(str)
            print(gols_df.dtypes)
            #verificar o artilheiro de cada ano
            #a planilha de gols tem dados apartir do campeonato de 2014 até o de 2023 - não possuido registros anteriores 
            #gols.atleta e tipo_de_gol



#   MAIOR ATILHEIRO DE PENALTIS NOS ULTIMOS 10 ANOS
        gols_penalty = gols_df[gols_df['tipo_de_gol']=='Penalty']
        atleta_contagem_penalty = gols_penalty['atleta'].value_counts()
        atleta_contagem_penalty_df = atleta_contagem_penalty.reset_index()
        atleta_contagem_penalty_df.columns = ['atleta', 'frequencia']
        # Classificar do maior para o menor
        atleta_contagem_penalty_df = atleta_contagem_penalty_df.sort_values(by='frequencia', ascending=False)
        # Exibir o resultado
        print(atleta_contagem_penalty_df)


#MARCADORES DE GOLS CONTRA
        gols_contra = gols_df[gols_df['tipo_de_gol'] == 'Gol Contra']
        contagem_gols_contra = gols_contra['atleta'].value_counts()
        gols_contra_df = contagem_gols_contra.reset_index()
        gols_contra_df.columns = ['atleta', 'frequencia']
        gols_contra_df = gols_contra_df.sort_values(by='frequencia',ascending = false)
        print(gols_contra_df)

#ARTILHEIROS

        gols_df['tipo_de_gol'] = gols_df['tipo_de_gol'].fillna("")
        filtro_gols = gols_df[(gols_df['tipo_de_gol'] == "nan") | (gols_df['tipo_de_gol'] == "Penalty")]

        # Contar os gols por atleta
        gols_por_atleta = filtro_gols['atleta'].value_counts()
        gols_por_atleta_df = gols_por_atleta.reset_index()
        gols_por_atleta_df.columns = ['atleta', 'frequencia']
        gols_por_atleta_df = gols_por_atleta_df.sort_values(by='frequencia',ascending = False)
        # Identificar o atleta com mais gols
        print(gols_por_atleta_df)


        #contar gols por time
        gols_por_time = filtro_gols['clube'].value_counts()
        gols_por_time_df = gols_por_time.reset_index()
        gols_por_time_df.columns = ['clube', 'frequencia']
        gols_por_time_df = gols_por_time_df.sort_values(by='frequencia', ascending=False)
        print(gols_por_time_df)

        #minuto que mais saiu gol
        gols_minuto = filtro_gols['minuto'].value_counts()
        gols_minuto_df = gols_minuto.reset_index()
        gols_minuto_df.columns = ['minuto', 'frequencia']
        gols_minuto_df = gols_minuto_df.sort_values(by='frequencia', ascending=False)
        print(gols_minuto_df)

#HORA MAIS PROVAVEL DE UM JOGO ONDE O MANDANTE SAIA VENCEDOR
df_vencedor_mandante = brasileirao_df[brasileirao_df['vencedor'] == brasileirao_df['mandante']]

# Analisar a distribuição das horas dos jogos vencedores
hora_vencedor_mandante = df_vencedor_mandante['hora'].value_counts().sort_index()

# Encontrar a hora mais provável
hora_mais_provavel = hora_vencedor_mandante.idxmax()

# Exibir o resultado
print(f"A hora mais provável do mandante sair vencedor é: {hora_mais_provavel}")


#TABELA PARA DETERMINAR QUE HORA É MAIS PROVAVEL DE SAIR UM VENCEDOR 
                brasileirao_df['resultado'] = brasileirao_df.apply(lambda row: 'Vencedor' if row['vencedor'] == row['mandante'] else ('Perdedor' if row['vencedor'] == row['visitante'] else 'Empate'), axis=1)

# Calcular o número total de jogos para cada hora
total_jogos_por_hora = brasileirao_df['hora'].value_counts().sort_index()

# Calcular o número de vitórias, derrotas e empates do mandante para cada hora
vitorias_por_hora = brasileirao_df[brasileirao_df['resultado'] == 'Vencedor']['hora'].value_counts().sort_index()
derrotas_por_hora = brasileirao_df[brasileirao_df['resultado'] == 'Perdedor']['hora'].value_counts().sort_index()
empates_por_hora = brasileirao_df[brasileirao_df['resultado'] == 'Empate']['hora'].value_counts().sort_index()

# Calcular os percentuais de vitórias, derrotas e empates para cada hora
percentual_vitorias = (vitorias_por_hora / total_jogos_por_hora * 100).fillna(0)
percentual_derrotas = (derrotas_por_hora / total_jogos_por_hora * 100).fillna(0)
percentual_empates = (empates_por_hora / total_jogos_por_hora * 100).fillna(0)

# Criar uma tabela com esses percentuais
tabela_percentuais = pd.DataFrame({
    'Percentual_Vitorias': percentual_vitorias,
    'Percentual_Derrotas': percentual_derrotas,
    'Percentual_Empates': percentual_empates
}).fillna(0)

# Exibir a tabela
tbl_percents = tabela_percentuais.resample('1H').agg({'Percentual_Derrotas':'mean', 'Percentual_Empates':'mean', 'Percentual_Vitorias':'mean'})
print(tbl_percents.sort_values(by='hora', ascending = True))

# Criar o gráfico de barras
plt.figure(figsize=(12, 6))
percentual_vitorias.plot(kind='bar', color='skyblue')
plt.title('Percentual de Vitórias do Mandante por Hora')
plt.xlabel('Hora')
plt.ylabel('Percentual de Vitórias (%)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Exibir o gráfico
plt.show()



#time que mais venceu jogos desde 2003:
        vitorias_por_time = brasileirao_df['vencedor'].value_counts()

        # Criar um novo DataFrame a partir dessa contagem
        df_vitorias = vitorias_por_time.reset_index()

        # Renomear as colunas para algo mais significativo
        df_vitorias.columns = ['Time', 'Numero_de_Vitorias']

        # Ordenar o DataFrame do maior para o menor número de vitórias
        df_vitorias = df_vitorias.sort_values(by='Numero_de_Vitorias', ascending=False)

        # Exibir o DataFrame resultante
        print(df_vitorias)








#junção de data frame. Todos os data frames tem um parametro em comum, o partida_id ou ID. Primeiro alterar o nome da coluna para deixar todos com o mesmo nome. Isso ira me ajudar na hora de consolidar os dados
brasileirao_df.rename(columns={'ID':'partida_id'}, inplace=True) 
#print(brasileirao_df.columns)

#os primeiros dados que vou juntar é o das partidas com os dados do brasileirao, pois ambas tem dados a partir de 2003 e isso vai aumentar as informações validas nos tipos de dados. 

#brasileirao_completo_df = pd.merge(brasileirao_df,partidas_df, on="partida_id", how='inner')
brasileirao_completo_df = pd.merge(partidas_df,brasileirao_df, on="partida_id", how='inner')
print(brasileirao_completo_df)

os.getcwd()