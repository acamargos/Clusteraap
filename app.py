import pandas as pd
import streamlit as st

st.header('Bem vindos à INVESTSP - Sua ferramenta de apoio para detecção de novos clientes (Prospects)')

# Aplicação no Streamlit
dfClustersFinal = pd.read_csv('dfClustersFinal2.csv')
st.write(dfClustersFinal)
# Group by do total de investimentos por ano e trimestre
Tot3DKmeans = dfClustersFinal.groupby(['klusterK3D','SetorNome','FaixaValorNome','Região']).agg({'Real (em milhões)': ['sum','count']})
Tot3DKmeans = Tot3DKmeans.reset_index()

st.write(Tot3DKmeans)
# imagem do Seade  
st.image('Piesp.png')

# texto sobre propósito (artigo medium)

proposito = """O propósito desse trabalho é servir como ferramenta de apoio aos fornecedores, consultorias e empreendedores 
para a identificação de prospects (clientes compradores de serviços e soluções).
Explicando melhor o contexto de negócios da proposta, trata-se de utilizar a pesquisa realizada pelo instituto SEADE (chamada PIESP), 
que compila os investimentos que serão realizados pelas empresas no estado de São Paulo como fonte de dados para a geração de clusters 
que apoiem os fornecedores de hardware/software entre outros, consultorias, prestadores de serviços na identificação de prospects 
(potenciais novos clientes). Ou seja, através de cada investimento existem sempre oportunidades de contratações, demandas por serviços 
e afins gerando dessa forma espaço para novos negócios."""

st.write(proposito)

# imagem 4 clusters 
st.image('ClusterK(Persona).PNG')

# criação das variáveis dataframe de acordo com o perfil do usuário/persona
TotC1 = Tot3DKmeans[ Tot3DKmeans['klusterK3D'] == 0 ]	
TotC2 = Tot3DKmeans[ Tot3DKmeans['klusterK3D'] == 1 ]
TotC3 = Tot3DKmeans[ Tot3DKmeans['klusterK3D'] == 2 ]
TotC4 = Tot3DKmeans[ Tot3DKmeans['klusterK3D'] == 3 ]
Tot1 = dfClustersFinal[ dfClustersFinal['klusterK3D'] == 0 ]
Tot2 = dfClustersFinal[ dfClustersFinal['klusterK3D'] == 1 ]
Tot3 = dfClustersFinal[ dfClustersFinal['klusterK3D'] == 2 ]
Tot4 = dfClustersFinal[ dfClustersFinal['klusterK3D'] == 3 ]

# list box (Visão Consolidada- group by):
personaC = st.radio("Prezado fornecedor/consultor, por favor selecione seu perfil: (Consulta Consolidada)",
    ('Perfil 1: Empresas/Fornecedores com interesse em investimentos P e M para os Setores Infra, Outros e Serviços', 
'Perfil 2: Empresas/Fornecedores com interesse em investimentos G e GG para os Setores Infra, Outros e Serviços', 
'Perfil 3: Empresas/Fornecedores com interesse em investimentos P e M para os Setores Comércio e Indústria', 
'Perfil 4: Empresas/Fornecedores com interesse em investimentos G e GG para os Setores Comércio e Indústria'),
key = 'radio_consolidado')
if personaC == 'Perfil 1: Empresas/Fornecedores com interesse em investimentos P e M para os Setores Infra, Outros e Serviços':
	st.write(TotC1)
elif personaC ==  'Perfil 2: Empresas/Fornecedores com interesse em investimentos G e GG para os Setores Infra, Outros e Serviços' :
	st.write(TotC2)
elif personaC ==  'Perfil 3: Empresas/Fornecedores com interesse em investimentos P e M para os Setores Comércio e Indústria' :
	st.write(TotC3)
else:
    st.write(TotC4)


# list box (Visão Detalhada do Dataframe Clusterizado):
persona = st.radio("Prezado fornecedor/consultor, por favor selecione seu perfil: (Consulta Detalhada)",
    ('Perfil 1: Empresas/Fornecedores com interesse em investimentos P e M para os Setores Infra, Outros e Serviços', 
'Perfil 2: Empresas/Fornecedores com interesse em investimentos G e GG para os Setores Infra, Outros e Serviços', 
'Perfil 3: Empresas/Fornecedores com interesse em investimentos P e M para os Setores Comércio e Indústria', 
'Perfil 4: Empresas/Fornecedores com interesse em investimentos G e GG para os Setores Comércio e Indústria'),
key = 'radio_total')
if persona == 'Perfil 1: Empresas/Fornecedores com interesse em investimentos P e M para os Setores Infra, Outros e Serviços':
	st.write(Tot1)
elif persona ==  'Perfil 2: Empresas/Fornecedores com interesse em investimentos G e GG para os Setores Infra, Outros e Serviços' :
	st.write(Tot2)
elif persona ==  'Perfil 3: Empresas/Fornecedores com interesse em investimentos P e M para os Setores Comércio e Indústria' :
	st.write(Tot3)
else:
    st.write(Tot4)
