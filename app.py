import pandas as pd
import streamlit as st
import base64

def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

    """
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'



st.header('Bem vindos à InvestSP Prospect Advisor - Sua ferramenta de apoio para detecção de novos clientes (Prospects)')

st.header('Usando Algoritmos de Clusterização, com base na pesquisa PIESP, mapeamos 4 Perfis/segmentos')

st.header('Abaixo temos a consulta consolidada e mais abaixo a consulta detalhada de acordo com seu perfil')
# Aplicação no Streamlit
dfClustersFinal = pd.read_csv('dfClustersFinal2.csv')
dfClustersFinal2 = dfClustersFinal[['Empresa alvo do investimento','Empresa(s) investidora(s)','Real (em milhões)','Período','Descrição do investimento','SetorNome','Região','Município','klusterK3D']]
#st.write(dfClustersFinal)
# Group by do total de investimentos por ano e trimestre
Tot3DKmeans = dfClustersFinal.groupby(['klusterK3D','SetorNome','FaixaValorNome','Região']).agg({'Real (em milhões)': ['sum','count']})
Tot3DKmeans = Tot3DKmeans.reset_index()

#st.write(Tot3DKmeans)
# imagem do Seade  
st.image('Piesp.png')

# texto sobre propósito (artigo medium)

st.header('Propósito dessa aplicação')
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
st.write('Nessa figura temos o gráfico dos 4 Clusters gerados com K-Means')
# criação das variáveis dataframe de acordo com o perfil do usuário/persona
TotC1 = Tot3DKmeans[ Tot3DKmeans['klusterK3D'] == 0 ]	
TotC2 = Tot3DKmeans[ Tot3DKmeans['klusterK3D'] == 1 ]
TotC3 = Tot3DKmeans[ Tot3DKmeans['klusterK3D'] == 2 ]
TotC4 = Tot3DKmeans[ Tot3DKmeans['klusterK3D'] == 3 ]
Tot1 = dfClustersFinal2[ dfClustersFinal2['klusterK3D'] == 0 ]
Tot2 = dfClustersFinal2[ dfClustersFinal2['klusterK3D'] == 1 ]
Tot3 = dfClustersFinal2[ dfClustersFinal2['klusterK3D'] == 2 ]
Tot4 = dfClustersFinal2[ dfClustersFinal2['klusterK3D'] == 3 ]

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

#botao = st.button(label='Exportar Dados')
if st.button('Exportar Dados'):
    if persona == 'Perfil 1: Empresas/Fornecedores com interesse em investimentos P e M para os Setores Infra, Outros e Serviços':
       # Tot1.to_excel('ClusterPerfil1.xlsx')
        tmp_download_link = download_link(Tot1, 'ClusterPerfil1.csv', 'Clique aqui para fazer o download do arquivo ClusterPerfil1.csv')
        st.markdown(tmp_download_link, unsafe_allow_html=True)

    elif persona ==  'Perfil 2: Empresas/Fornecedores com interesse em investimentos G e GG para os Setores Infra, Outros e Serviços' :
        #Tot2.to_excel('ClusterPerfil2.xlsx')
        tmp_download_link = download_link(Tot2, 'ClusterPerfil2.csv', 'Clique aqui para fazer o download do arquivo ClusterPerfil2.csv')
        st.markdown(tmp_download_link, unsafe_allow_html=True)
    elif persona ==  'Perfil 3: Empresas/Fornecedores com interesse em investimentos P e M para os Setores Comércio e Indústria' :
        #Tot3.to_excel('ClusterPerfil3.xlsx')
        tmp_download_link = download_link(Tot3, 'ClusterPerfil3.csv', 'Clique aqui para fazer o download do arquivo ClusterPerfil3.csv')
        st.markdown(tmp_download_link, unsafe_allow_html=True)
    else:
        #Tot4.to_excel('ClusterPerfil4.xlsx')
        tmp_download_link = download_link(Tot4, 'ClusterPerfil4.csv', 'Clique aqui para fazer o download do arquivo ClusterPerfil4.csv')
        st.markdown(tmp_download_link, unsafe_allow_html=True)
    #st.write("Excel Exportado!")

st.header('Agradecemos sua visita e desejamos sucesso no seu processo de prospecção de novos clientes!')
st.write("Veja nosso artigo sobre esse estudo de clusterização no Medium:","https://augustocamargos.medium.com/an%C3%A1lise-de-neg%C3%B3cios-e-conclus%C3%B5es-dos-clusters-gerados-investsp-prospect-advisor-bc498dc0f085")
#st.write("https://augustocamargos.medium.com/an%C3%A1lise-de-neg%C3%B3cios-e-conclus%C3%B5es-dos-clusters-gerados-investsp-prospect-advisor-bc498dc0f085")

