# O DATASUS
Departamento de Informatica do SUS é um orgçao da secretaria executiva do ministerio da saude que tem como responsabilidade: Fomentar, regulamentar e avaliar as ações de informatização do SUS alem de coletar, processar e disseminar informações de saude.

# Bases
Encontrei 12 bases:
* Base Populacional IBGE
* Base Territorial
* CIH - Comunicação de Internação Hospitalar
* CIHA - Comunicação de Informção Hospitalar e Ambulatorial
* CMD - Conjunto Minimo de Dados (da Atenção à Saude)
* CNES - Cadastro Nacional de Estabelecimentos do SUS
* SIASUS - Sistema de Informações Ambulatoriais do SUS
* SIH - Sistema de Informações Hospitalares
* SIM - Sistema de Informações de Mortalidade
* SINAN - Sistema de Informação de Agravos de Notificação
* SINASC - Sistema de Informações de Nascidos Vivos
* SISPRENATAL - Sistema de Acompanhamento da Gestante

## Base Populacional IBGE
	.dbf dBase / .csv / .xml

|Campo|Descrição|
|----:|:--------|
|MUNIC_RES|Codigo do municipio 6 digitos|
|ANO|Ano dos dados 4 digitos|
|Sexo| 1: Masculino / 2:Feminino|
|Situacao|Situacao do dominicilio 1:Urbano, 2:Rural, 3:Não levantado|
|FXEtaria|Faixa etaria 4 digitos, 0000: < 1 ano, 0101, 0202, 1919|
|Populacao| Populacao residente para o municipio, ano, sexo, situacao e fxetaria|

## Base Territorial
	.txt / .csv / .xml
	
### TB_MUNICP
Municipio

|Campo|Tipo|Tamanho|Descrição|
|:---:|:-------:|:----:|:----|
|CO_MUNICIP|Caractere|6|Codigo IBGE do municipio: uuNNNN / UU: UF / NNNN:Codigo|
|CO_MUNICDV|Caractere|7|Codigo IBGE do municipio com digito de controle: uuNNNNd|
|CO_STATUS|Caractere|6|Situacao do municipio: ATIVO, EXTINT, TRANSF, IGNOR|
|CO_TIPO|Caractere|6|Tipo de unidade: MUNIC, DISFED, DISEST, TERRIT, IGNOR|
|DS_NOME|Caractere|42|Nome do municipio|
|DS_NOMEPAD|Caractere|42|Nome do municipio padronizado (Sanitizado)|
|DS_OBSERV|Caractere|42|Observações, nome antigo, situacao...|
|CO_ALTER|Caractere|28|Codigos alternativos.
|CO_ALTERDV|Caractere|32|Idem anterior, sem digito verificador|
|CO_REGIAO|Caractere|1|Codigo da região|
|CO_UF|Caractere|2|Codigo da UF|
|IN_CAPITAL|Caractere|1|Indica se é capital federal (F), estadual (E) ou não é (N)|
|IN_AMAZLEF|Caractere|1|Indica se faz parte da amazonia legal (S/N)|
|IN_SEMIAR|Caractere|1|Indica se faz parte da regiao semiarido (S/N)|
|IN_FRONTFX|Caractere|1|Indica se faz parte de faixa de fronteira (S/N)|
|IN_FRONTZN|Caractere|1|Indica se faz parte de zona de fronteira (S/N)|
|IN_POBREZA|Caractere|1|Indica se faz parte relação de municipios de extrema pobreza (S/N)|
|DT_INSTAL|Caractere|4|Ano de instalação do municipio(nem todos tem)|
|DT_EXTIN|Caractere|4|Ano de extinção ou transferencia do municipio|
|CO_SUCESS|Caractere|7|Codigo de municipio sucessor ao municipio extinto ou transferido|
|NU_ORDEM|Caractere|1|Ordem em o municipio devera aparecer nos arquivos de conversão. 1:ativo, 6:extinto,7:transferido, 8:Ignorado|
|NU_ORDMAP|Caractere|1|Ordem em que o municipio deverá aparecer nos arquivos de conversão para mapas. 1:Normal,2:Após|
|NU_LATITUD|Numerico|10,5|Latitude da sede do municipio|
|NU_LONGIT|Numerico|10,5|Longitude da sede do municipio|
|NU_ALTITUD|Numerico|6|Altitude em metros da sede do municipio|
|NU_AREA|Numerico|12,3|Area em quilometros quadrados do municipio|

### TB_UF
Unidades da federação

|Campo|Tipo|Tamanho|Descrição|
|:---:|:-------:|:----:|:----|
|CO_UF|Caractere|2|Codigo IBGE da UF|
|DS_SIGLA|Caractere|2|Sigla da UF|
|CO_STATUS|Caractere|6|Situacao da UF: ATIVO, EXTINT, IGNOR| 
|DS_NOME|Caractere|42|Nome da UF|
|DS_NOMEPAD|Caractere|42|Nome da UF (sanitizado)|
|CO_SUCESS|Caractere|2|Codigo da UF sucessora a UF extinta|
|CO_ALTER|Caractere|Codigos alternativos para UF|
|CO_ALTER|Caractere|3|Codigos alternativos|
|CO_REGIAO|Caractere|1|Codigo da regiao|
|NU_AREA|Numerico|12,3|Area da UF. |
|NU_ORDEM|Caractere|1|Ordem em que a UF deverá aparecer. 1:Ativa, 6:Extinta, 8:Ignorada|

### TB_REGIAO
Regiões geograficas (Norte, Sul, Centro-Oeste, Nordeste e Sudeste)

|Campo|Tipo|Tamanho|Descrição|
|:---:|:-------:|:----:|:----|
|CO_REGIAO|Caractere|1|Codigo IBGE da regiao|
|CO_STATUS|Caractere|6|Situacao da regiao. ATIVO, IGNOR|
|DS_NOME|Caractere|42|Nome da regiao|
|DS_NOMEPAD|Caractere|50|Nome da regiao (sanitizado)|
|DS_ABREV|Caractere|24|Nome abreviado da regiao|
|NU_ORDEM|Caractere|1|Ordem em que a regiao deve aparecer. 1:Ativa,8:Ignorada|

### TB_REGSAUDE
Região de saude, agrupamento de municipios limitrofes delimitado por identidades culturais, economicas e sociais.

|Campo|Tipo|Tamanho|Descrição|
|:---:|:-------:|:----:|:----|
|CO_REGSAUD|Caractere|5|Codigo da regiao de saude: uuNNN|
|CO_STATUS|Caractere|6|Situacao da regiao de saude. ATIVO, TRANSF, IGNOR|
|DS_NOME|Caractere|42|Nome da regiao de saude|
|DS_NOMEPAD|Caractere|50|Nome da regiao de saude (sanitizado)|
|DS_ABREV|Caractere|24|Nome abreviado da regiao de saude|
|NU_ORDEM|Caractere|1|Ordem em que a regiao de saude deve aparecer. 1:Ativa,7:Transferidas,8:Ignorada|


### TB_MACSAUDE
Macrorregiões de Saude, agrupamento de regiões de saude.

|Campo|Tipo|Tamanho|Descrição|
|:---:|:-------:|:----:|:----|
|CO_MACSAUD|Caractere|4|Codigo da macrorregiao de saude: uuNN|
|CO_STATUS|Caractere|6|Situacao da regiao de saude. ATIVO, OUTROS,TRANSF, IGNOR|
|DS_NOME|Caractere|42|Nome da macrorregiao de saude|
|DS_NOMEPAD|Caractere|42|Nome da macrorregiao de saude (sanitizado)|
|DS_ABREV|Caractere|24|Nome abreviado da macrorregiao de saude|
|NU_ORDEM|Caractere|1|Ordem em que a macrorregiao de saude deve aparecer. 1:Ativa,5:Nao definida,7:Transferidas,8:Ignorada|

### TB_DIVADM
Divisões administrativas regionais, podem ou não corresponder as regiões de saude.

|Campo|Tipo|Tamanho|Descrição|
|:---:|:-------:|:----:|:----|
|CO_DIVADM|Caractere|4|Codigo da divisão administrativa estaudal de saude: uuNN|
|CO_STATUS|Caractere|6|Situacao da divisão administrativa estaudal. ATIVO, OUTROS,TRANSF, IGNOR|
|DS_NOME|Caractere|42|Nome da divisão administrativa estaudal|
|DS_NOMEPAD|Caractere|42|Nome da divisão administrativa estaudal (sanitizado)|
|DS_ABREV|Caractere|24|Nome abreviado da divisão administrativa estaudal|
|NU_ORDEM|Caractere|1|Ordem em que a divisão administrativa estaudal deve aparecer. 1:Ativa,5:Nao definida,7:Transferidas,8:Ignorada|


### TB_MICIBGE
Microrregiões do IBGE

|Campo|Tipo|Tamanho|Descrição|
|:---:|:-------:|:----:|:----|
|CO_MICIBGE|Caractere|5|Codigo da microrregiao do IBGE: uuNNN|
|CO_STATUS|Caractere|6|Situacao da microrregiao do IBGE. ATIVO, TRANSF, IGNOR|
|DS_NOME|Caractere|42|Nome da microrregiao do IBGE|
|DS_NOMEPAD|Caractere|42|Nome da microrregiao do IBGE (sanitizado)|
|DS_ABREV|Caractere|24|Nome abreviado da microrregiao do IBGE|
|NU_ORDEM|Caractere|1|Ordem em que a microrregiao do IBGE deve aparecer. 1:Ativa,7:Transferidas,8:Ignorada|

### TB_REGMETR
Regiões metropolitanas, agrupamentos de municipios limitrofes.

|Campo|Tipo|Tamanho|Descrição|
|:---:|:-------:|:----:|:----|
|CO_REGMETR|Caractere|5|Codigo da região metropolitana: uuNNNs|
|CO_STATUS|Caractere|6|Situacao da região metropolitana. ATIVO, OUTROS, TRANSF, IGNOR|
|CO_TIPO|Caractere|6|Tipo de região metropolitana. RMETR, SRMETR,RIDE,AGLURB,OUTROS,TRANSF,IGNOR|
|DS_NOME|Caractere|42|Nome da região metropolitana|
|DS_NOMEPAD|Caractere|42|Nome da região metropolitana (sanitizado)|
|DS_ABREV|Caractere|24|Nome abreviado da região metropolitana|
|NU_ORDEM|Caractere|1|Ordem em que a região metropolitana deve aparecer. 1:Ativa,7:Transferidas,8:Ignorada|

### TB_TERRCID
Territorios da cidadania

|Campo|Tipo|Tamanho|Descrição|
|:---:|:-------:|:----:|:----|
|CO_TERRCID|Caractere|3|Codigo do territorio da Cidadania: nnn|
|DS_NOME|Caractere|42|Nome do territorio da Cidadania|
|DS_NOMEPAD|Caractere|42|Nome do territorio da Cidadania (sanitizado)|
|CO_STATUS|Caractere|6|Situacao do territorio da Cidadania. ATIVO, OUTROS|
|NU_ORDMAP|Caractere|1|Ordem em que o territorio da Cidadania deve aparecer. 1:Ativo,5:Outros|

### TB_PNDR
Mesorregiões da Politica Nacional de Desenvolvimento Regional.

|Campo|Tipo|Tamanho|Descrição|
|:---:|:-------:|:----:|:----|
|CO_PNDR|Caractere|3|Codigo da mesorregião da PNDR: nnn|
|DS_NOME|Caractere|42|Nome da mesorregião da PNDR|
|DS_NOMEPAD|Caractere|42|Nome da mesorregião da PNDR (sanitizado)|
|CO_STATUS|Caractere|6|Situacao da mesorregião da PNDR. ATIVO, OUTROS|
|NU_ORDMAP|Caractere|1|Ordem em que a mesorregião da PNDR deve aparecer. 1:Ativo,5:Outros|

### TB_DSEI
Distrito Sanitario Especial Indigena

|Campo|Tipo|Tamanho|Descrição|
|:---:|:-------:|:----:|:----|
|CO_DSEI|Caractere|3|Codigo do Distrito Sanitario Especial Indigena: nnn|
|DS_NOME|Caractere|42|Nome do Distrito Sanitario Especial Indigena|
|DS_NOMEPAD|Caractere|42|Nome do Distrito Sanitario Especial Indigena (sanitizado)|
|CO_SEDE|Caractere|6|Codigo do municipio sede do DSEI|

## CIH - Comunicação de Internação Hospitalar

.txt 

### tb_procedimento

|Coluna|Tamanho|Inicio|Fim|Tipo|
|:---:|:-------:|:----:|:----|
|CO_PROCEDIMENTO|10|1|10|VARCHAR2|
|NO_PROCEDIMENTO|250|11|260|VARCHAR2|
|TP_COMPLEXIDADE|1|261|261|VARCHAR2|
|TP_SEXO|1|262|262|VARCHAR2|
|QT_MAXIMA_EXECUCAO|4|263|266|NUMBER|
|QT_DIAS_PERMANENCIA|4|267|270|NUMBER|
|QT_PONTOS|4|271|274|NUMBER|
|VL_IDADE_MINIMA|4|275|278|NUMBER|
|VL_IDADE_MAXIMA|4|279|282|NUMBER|
|VL_SH|10|283|292|NUMBER|
|VL_SA|10|293|302|NUMBER|
|VL_SP|10|303|312|NUMBER|
|CO_FINANCIAMENTO|2|313|314|VARCHAR2|
|CO_RUBRICA|6|315|320|VARCHAR2|
|DT_COMPETENCIA|6|321|326|DATE|


### tb_procedimento_nsus

|Coluna|Tamanho|Inicio|Fim|Tipo|
|:---:|:-------:|:----:|:----|
|CO_PROCEDIMENTO|10|1|10|VARCHAR2|
|NO_PROCEDIMENTO|250|11|260|VARCHAR2|

### tb_cid

|Coluna|Tamanho|Inicio|Fim|Tipo|
|:---:|:-------:|:----:|:----|
|CO_CID|4|1|4|VARCHAR2|
|NO_CID|100|5|104|VARCHAR2|
|TP_AGRAVO|1|105|105|CHAR|
|TP_SEXO|1|106|106|CHAR|
|TP_ESTADIO|1|107|107|CHAR|
|VL_CAMPOS_IRRADIADOS|4|108|111|NUMBER|


## CIHA - Comunicação de Informção Hospitalar e Ambulatorial
	.dbf
|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
|ano_cmpt  |char(4)|Ano de competencia CIH, formato AA|
|mes_cmpt  |char(2)|Mês de competencia da CIH, formato MM|
|espec     |char(2)|Vazio|
|cgc_hosp  |char(14)|CNPJ do Estabelecimento de Saude|
|munic_res |char(6)|Municipio de residencia|
|nasc      |char(8)|Data de nascimento do paciente|
|sexo      |char(1)|Sexo do paciente|
|uti_mes_to|char(3)|(Zerado)|
|uti_int_to|char(3)|Total de dias de utei intermediaria|
|proc_rea  |char(10)|Procedimento realizado|
|qt_proc   |char(6)|Quantidade de procedimento|
|dt_atend  |char(8)|Data de atendimento, AAAAMMDD|
|dt_saida  |char(8)|Data de saida, AAAAMMDD|
|diag_princ|char(4)|Diagnostico principal|
|diag_secun|char(4)|Diagnostico secundario|
|cobranca  |char(2)|Motivo da cobrança|
|natureza  |char(2)|Natureza da relação do hospital com o SUS|
|gestao    |char(1)|Indica o tipo de gestão do hospital|
|munic_mov |char(6)|Codigo do municipio em que se localizao hospital|
|cod_idade |char(1)|Unidade de medida da idade. 0:Ignorada,2:Dias,3:Meses,4:Anos,5:Mais de 100|
|idade     |char(2)|Idade|
|dias_perm |char(5)|Dias de permanencia|
|morte     |char(1)|Indica se o paciente teve saida com morte (0:Não, 1:Sim)|
|nacional  |char(3)|(Vazio)|
|car_int   |char(2)|(Vazio)|
|homonimo  |char(1)|(Vazio)|
|cnes      |char(7)|Codigo CNES do estabelecimento|
|fonte     |char(2)|Fonte da remuneração|
|modalidade|char(2)|Modalidade do atendimento|

## CIHA - Comunicação de Informção Hospitalar e Ambulatorial
