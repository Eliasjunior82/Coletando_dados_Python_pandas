#!/usr/bin/env python
# coding: utf-8

# ### Importando arquivos

# In[21]:


import pandas as pd

funcionario_df = pd.read_csv(r'CadastroFuncionarios.csv', sep=';', decimal=',', encoding='utf-8')
clientes_df = pd.read_csv(r'clientes projeto.csv', sep=';', decimal=',', encoding='utf-8')
prestador_df = pd.read_excel(r'BaseServiçosPrestados.xlsx')

# escluindo colunas desnecessarias
funcionario_df = funcionario_df.drop(['Estado Civil'], axis= 1)
prestador_df = prestador_df.drop(['Unnamed: 4', 'Unnamed: 5'], axis=1)

display(funcionario_df)
display(clientes_df)
display(prestador_df)


# # 1- Soma dos salario mensal 

# In[8]:



gasto_funcionarios = funcionario_df['Salario Base']+funcionario_df['Impostos']+funcionario_df['Beneficios']+funcionario_df['VT']+funcionario_df['VR']
print('O total de gastos com o salario dos funcionarios é de {:,}'.format(gasto_funcionarios.sum()))


# # 2- Faturamento da empresa

# In[9]:


#Faturamento da empresa
faturamento = prestador_df.merge(clientes_df, on='ID Cliente')
faturamento['total'] = faturamento['Tempo Total de Contrato (Meses)'] * faturamento['Valor Contrato Mensal']
print('O faturamento total da empresa foi R$ {:,}'.format(faturamento['total'].sum()))
display(faturamento)


# # 3- % de funcionarios que fecharam contratos

# In[13]:


fechou_contrato = prestador_df.merge(funcionario_df, on='ID Funcionário')
fechou_contrato = fechou_contrato['ID Funcionário'].unique()
total = ((len(funcionario_df['ID Funcionário']) - len(fechou_contrato)) / 114 * 100)
print('A % de funcionarios que fechou contrato é de {:.2f} '.format(100 - total),'%')


# # 4- calculando o total de contrato que cada area da empresa fechou

# In[17]:


area = prestador_df.merge(funcionario_df, on='ID Funcionário')
area = area['Area'].value_counts()
print(area)
area.plot(kind='bar')
        
    


# # 5- total de funcionario por area

# In[18]:


funcionario = funcionario_df['Area'].value_counts()
display(funcionario)
funcionario.plot(kind='bar')


# # 6-calculando o Total do ticket medio da empresa

# In[19]:


ticket_medio_mensal= clientes_df
ticket_medio_mensal = ticket_medio_mensal['Valor Contrato Mensal'].mean()
print('O ticket medio mensal é de R${:,}'.format(ticket_medio_mensal))

