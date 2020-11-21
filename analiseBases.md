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
|:---:|:-------:|:----:|:----|:----|
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
|:---:|:-------:|:----:|:----|:----|
|CO_PROCEDIMENTO|10|1|10|VARCHAR2|
|NO_PROCEDIMENTO|250|11|260|VARCHAR2|

### tb_cid

|Coluna|Tamanho|Inicio|Fim|Tipo|
|:---:|:-------:|:----:|:----|:----|
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


## CMD

Base de dados não estava disponivel

## CNES - Cadastro Nacional de Estabelecimentos do SUS

### Tabela de estabelecimentos (STufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
|cnes|CHAR(7)|      Numero nacional do estabelecimento de saude|
|codufmun|CHAR(6)|  Codigo do municipio do estabelecimento: UF MUNIC (sem diglto)|
|cod_cep|CHAR(8)|   Codigo do CEP do estabelecnmento|
|cpf_cnpj|CHAR(14)| CPF do estabelecimento, caso pessoa fisica ou CNPJ, caso pessoa juridica|
|pf_pj|CHAR(1)|     Indicador de pessoa: I-Fisica 3-Juridica|
|niv_dep|CHAR(1)|   Grau de dependéncia, onde: I -Individual 3-Mantida|
|cnpj_man|CHAR(14)| CNPJ da mantenedora do estabelecimento.|
|cod_ir|CHAR(2)|    Indica o tipo de reteneo de tributos da mantene&ra|
|regsaude|CHAR(4)|  Codigo da região de saude NOAS|
|micr_reg|CHAR(6)|  Codigo da micro-regiao de saude NOAS|
|distrsan|CHAR(4)|  Codigo do distrito sanitario|
|distradm|CHAR(4)|  Inicialmente chamado Distrito Administrativo, atualmente C6digo do Mddulo Assistencial conforme tabela local, em conformidade com o Plano Diretor de Regionalizasao do Estado/Municipio|
|vinc_sus|CHAR(1)|  Vinculo com SUS: I-Sim O-Nao|
|tpgestao|CHAR(1)|  Gestao de saude|
|esfera_a|CHAR(2)|  Codigo da esfera administrativa|
|atividad|CHAR(2)|	Codigo da ativldade de ensino/ pesquisa|
|retencao|CHAR(2)|  Codigo de reteneao de tbutos|
|natureza|CHAR(2)|  Codigo da natureza da organizasao|
|clientel|CHAR(2)|  Codigo de FLUXO da clientela|
|tp_unid|CHAR(2)|   Tipo de unidade (estabelecimento)|
|turno_at|CHAR(2)|  Codigo de turno de atendimento|
|niv_hier|CHAR(2)|  Codigo do nivel de hierarquia|
|tp_prest|CHAR(2)|  Tipo de Prestador|
|co_banco|CHAR(4)|  Codigo do Banco do Estabelecimento|
|co_agenc|CHAR(5)|  Codigo da Agéncia do Estabelec:lmento|
|c_corren|CHAR(14)| Codigo da Conta Corrente do Estabelecimento|
|contratm|CHAR(11)| Numero do contrato/convérno MUNICIPAL do vinculo com o SUS|
|dt_publm|CHAR(8)|  Ano e Més de publicaqao do contrato 'convénio MUNICIPAL (.aAAaNN)|
|contrate|CHAR(11)| Nümero do contrato/convénio ESTADIJAL do vinculo com o SUS|
|dt_puble|CHAR(8)|  Ano e Més de publicaqao do contrato Iconvémo ESTADUAL (.aAaAW*.)|
|alvara|CHAR(25)|   Numero do alvara|
|dt_exped|CHAR(8)| Ano e Més de da expedição do alvará (AAAAMM)|
|orgexped|CHAR(2)| orgao expedidor do alvará, onde:1-SES 2-SMS|
|av_acred|CHAR(1)| Indica se o estabelecumento foi avaliado segundo o Manual de Acreditação Hospitalar do MS, onde:1-Sim 2-Não|
|clasaval|CHAR(1)| Classificação da avaliação do estabelecimento segundo o Manual de acreditação Hospitalar do MS|
|dt_acred|CHAR(6)| Ano e Mes da acreditação (AAAAMM)|
|av_pnass|CHAR(1)| Indica se o estabelecnmento foi avaliado Segundo o Programa Nacional de serviços de Saude - PRASS, onde: 1-Sim 2-Não|
|dt_pnass|CHAR(6)| Ano e Més da avaliação PNASS (AAAAMM)|
|gesprg1e|CHAR(1)| Indicador se a gestao da atividade ATENCAO BASICA do Nivel de Atenção AMBULATORIAL é ESTADUAL, onde: 1-Sim 2-Não|
|gesprg1m|CHAR(1)| Indicador se a gestao da atividade ATENCAO BASICA do Nivel de Atenção AMBULATORIAL é MUNICIPAL, onde:1-Sim 2-Não|
|gesprg2e|CHAR(1)| Indicador se a gestao da atividade MEDIA COMPLEXIDADE do Nivel de Antenção AMBULATORIAL é ESTADUAL, onde: 1-Sim 2-Não|
|gesprg2m|CHAR(1)| Indicador se a gestao da atividade MEDIA COMPLEXIDADE do Nivel de Atenção AMBULATORIAL é MUNICIPAL, onde: 1-Sim 2-Não|
|gesprg4e|CHAR(1)| Indicador se a gestao da atividade ALTA COMPLEXIDADE do Nivel de Atenção AMBULATORIAL é ESTADUAL, onde: 1-Sim 2-Não|
|gesprg4m|CHAR(1)| Indicador se a gestao da atividade ALTA COMPLEXIDADE do Nivel de Atenção é MUNICIPAL, onde: 1-Sim 2-Não|
|nivate_a|CHAR(1)| Indica a exitencia de Nivel de Atenção AMBULATORIAL„ de gestao Municipal/EstaduaI, para este CNES, onde: 1-Sim 2-Não|
|gesprg3e|CHAR(1)| Indicador se a gestao do programa cod. 03 é ESTADUAL, onde: 1-Sim 2-Não|
|gesprg3m|CHAR(1)| Indicador se a gestao do programa cod. 03 é MUNICIPAL, onde: 1-Sim 2-Não|
|gesprg5e|CHAR(1)| Indicador se a gestao da atividade MEDIA COMPLEXIDADE do Nivel de Atenção HOSPITALAR é ESTADUAL, onde:1-Sim 2-Não|
|gesprg5m|CHAR(1)| Indicador se a gestao da atividade MEDIA COMPLEXIDADE do Nivel de Antenção HOSPITALAR é MUNICIPAL, onde:1-Sim 2-Não|
|gesprg6e|CHAR(1)| Indicador se a gestao da atividade ALTA COMPLEXIDADE do Nivel de Atenção HOSPITALAR é ESTADUAL, onde:1-Sim 2-Não|
|gesprg6m|CHAR(1)|    Indicador se a gestão da atividade ALTA COMPLEXIDADE do Hivel de Antenção HOSPITAL-AR é MUNICIPAL, onde:1-Sim 0-Não|
|nivate_h|CHAR(1)|    Indica a existencia de Nivel de Atenção HOSPITALAR, de gestão Municipal/Estadual, para este CNES, onde:1-Sim 0-Não|
|qtleitp1|NUMERIC(4)| Quantidade de leitos tipo I (cirurgico) existentes|
|qtleitp2|NUMERIC(4)| Quantidade de leitos tipo 2 (clinico) existentes|
|qtleitp3|NUMERIC(4)| Quantidade de leftos tipo 3 (complem.) existentes|
|leithosp|CHAR(1)|    Indica a existencia de LEITOS HOSPITALARES-CIRURGICOS, CLINICOS E COMPLEMENTARES para este CNES, onde:1-Sim 0-Não|
|qtinst01|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst02|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst03|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst04|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst05|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst06|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst07|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst08|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst09|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst10|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst11|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst12|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst13|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst14|NUMERIC(3)| Quantidade de salas/consultórios|
|urgemerg|CHAR(1)|    Indica a existencia de INSTALACAO FISICA de URGENCIA/EMERGENCIA para este CNES, onde:1-Sim 0-Não|
|qtinst15|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst16|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst17|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst18|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst19|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst20|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst21|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst22|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst23|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst24|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst25|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst26|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst27|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst28|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst29|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst30|NUMERIC(3)| Quantidade de salas/consultórios|
|atendamb|CHAR(1)|    Indica a existenção de INSTALAÇÃO FISICA de ATENDIMENTO AMBULATORIAL para este CNES, onde: 1-Sim 0-Não|
|qtinst31|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst32|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst33|NUMERIC(3)| Quantidade de salas/consultórios|
|centrcir|CHAR(1)|    Indica a existenção de INSTALAÇÃO Fisca de ATENDIMEUTO HOSPITALAR-CENTRO CIRURGICO para este CNES, onde:1-Sim 0-Não|
|qtinst34|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst35|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst36|NUMERIC(3)| Quantidade de salas/consultórios|
|qtinst37|NUMERIC(3)| Quantidade de salas/consultórios|
|centrobs|CHAR(1)|    Indica a existenção de INSTALAÇÃO Fisca de ATENDIMEUTO HOSPITALAR-CENTRO OBSTETRICO para este CNES, onde:1-Sim 0-Não|
|qtleit05|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit06|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit07|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit08|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit09|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit19|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit20|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit21|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit22|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit23|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit32|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit34|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit38|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit39|NUMERIC(3)| Quantidade de leitos/equipos|
|qtleit40|NUMERIC(3)| Quantidade de leitos/equipos|
|centrneo|CHAR(1)|Indica a existencia de INSTALAÇÃO Fisca de ATENDIMENTO HOSPITALAR-UNIDADE NEONATAL para este CNES, onde: 1-Sim 0-Não|
|atendhos|CHAR(1)|Indica a existencia de INSTALAÇÃO FISICA de ATENDIMENTO HOSPITALAR para este CNES, onde:1-Sim 0-Não|
|serap01p|CHAR(1)|Serviço de apoio S.A.M.E. ou S.P.P. proprio, onde: 1-Sim 0-Não|
|serap01t|CHAR(1)|Serviço de apoio S.A.M.E. ou S.P.P. terceirizado, onde: 1-Sim 0-Não|
|serap02p|CHAR(1)|Serviço de apoio Serviço Social proprio, onde:1-Sim 0-Não|
|serap02t|CHAR(1)|Serviço de apoio Serviço Social terceirizado, onde:1-Sim 0-Não|
|serap03p|CHAR(1)|Serviço de apoio Farmacia proprio, onde:1-Sim 0-Não|
|serap03t|CHAR(1)|Serviço de apoio Farmacia terceirizado, onde:1-Sim 0-Não|
|serap04p|CHAR(1)|Serviço de apoio Esterilização de Materiais proprio, onde:1-Sim 0-Não|
|serap04t|CHAR(1)|Serviço de apoio Esterilização de Materiais terceirizado, onde:1-Sim 0-Não|
|serap05p|CHAR(1)|Serviço de apoio Nutrição/Dietética (S.N.D.) proprio, onde:1-Sim 0-Não|
|serap05t|CHAR(1)|Serviço de apoio Nutrição/Dietética (S.N.D.) terceirizado, onde:1-Sim 0-Não|
|serap06p|CHAR(1)|Serviço de apoio Lactario proprio, onde:1-Sim 0-Não|
|serap06t|CHAR(1)|Serviço de apoio Lactario terceirizado, onde:1-Sim 0-Não|
|serap07p|CHAR(1)|Serviço de apoio Banco De Leite proprio, onde:1-Sim 0-Não|
|serap07t|CHAR(1)|Servlso de apoio Banco De Leite terceirizado, onde:1-Sim 0-Não|
|serap08p|CHAR(1)|Serviço de apoio Lavanderia proprio, onde:1-Sim 0-Não|
|serap08t|CHAR(1)|Serviço de apoio Lavanderia terceirizado, onde:1-Sim 0-Não|
|serap09p|CHAR(1)|Serviço de apoio Manuteneäo de Equnpamento proprio, onde:1-Sim 0-Não|
|serap09t|CHAR(1)|Serviço de apoio Manutenção de Equipamento terceirizado, onde: 1-Sim 0-Não|
|serap10p|CHAR(1)|Serviço de apoio Ambulancia proprio, onde:1-Sim 0-Não|
|serap10t|CHAR(1)|Serviço de apoio Ambulancia terceirizado, onde:1-Sim 0-Não|
|serap11p|CHAR(1)|Serviço de apoio Necroterio proprio, onde: 1-Sim 0-Não|
|serap11t|CHAR(1)|Serviço de apoio Necroterio terceirizado, onde:1-Sim 0-Não|
|serapoio|CHAR(1)|Indica a existencia de algum serviço de apoio para este CNES, onde:1-Sim 0-Não|
|res_biol|CHAR(1)|Existe coleta de residuo biologico, onde:1-Sim 0-Não|
|res_quim|CHAR(1)|Existe coleta de residuo quimico, onde:1-Sim 0-Não|
|res_radi|CHAR(1)|Existe coleta de rejeitos radioativos, onde:1-Sim 0-Não|
|res_comu|CHAR(1)|Existe coleta de residuos comuns, onde:1-Sim 0-Não|
|coletres|CHAR(1)|Indica a existencia de alguma coleta de residuo para este CNES, onde:1-Sim 0-Não|
|comiss01|CHAR(1)|Existe comissao de ETICA MEDICA, onde:1-Sim 0-Não|
|comiss02|CHAR(1)|Existe comissao de ETICA DE ENFERMAGEM, onde:1-Sim 0-Não|
|comiss03|CHAR(1)|Existe comissao de FARMÅCIA E TERAPÉUTICA, onde:1-Sim 0-Não|
|comiss04|CHAR(1)|Existe comissao de CONTROLE DE INFECCÅO HOSPITALAR, onde:1-Sim 0-Não|
|comiss05|CHAR(1)|Existe comissao de APROPRIACÅO DE CUSTOS, onde:1-Sim 0-Não|
|comiss06|CHAR(1)|Existe comissao de CIPA, onde:1-Sim 0-Não|
|comiss07|CHAR(1)|Existe comissao de REV'ISÄO DE PRONTUAR'OS, onde:1-Sim 0-Não|
|comiss08|CHAR(1)|Existe comissao de REVISAO DE DOCUMENTACAO MEDICA E ESTATISTICA, onde:1-Sim 0-Não|
|comiss09|CHAR(1)|Existe comissao de ANALISE DE OBITOS E BIOPISIAS, onde:1-Sim 0-Não|
|comiss10|CHAR(1)|Existe comissao de INVESTIGACAO EPIDEMIOLOGICA, onde:1-Sim 0-Não|
|comiss11|CHAR(1)|Existe comissao de NOTIFICACAO DE DOENCAS, onde:1-Sim 0-Não|
|comiss12|CHAR(1)|Existe comissäo de CONTROLE DE ZOONOSES E VETORES, onde: 1-Sim 0-Não|
|comissao|CHAR(1)|Indica a existencia de alguma comissäo para este CNES, onde:1-Sim 0-Não|
|ap01cv01|CHAR(1)|Atendimento prestado INTERNACAO Convenio SUS, onde: 1-Sim 0-Não|
|ap01cv02|CHAR(1)|Atendimento prestado INTERNACAO Convenio PARTICULAR, onde:1-Sim 0-Não|
|ap01cv05|CHAR(1)|Atendimento prestado INTERNACAO/convenio PLANO de SAUDE PUBLICO, onde:1-Sim 0-Não|
|ap01cv06|CHAR(1)|Atendimento prestado INTERNACAO/convenio PLANO de SAUDE PRVADO, onde:1-Sim 0-Não|
|ap01cv03|CHAR(1)|Atendimento prestado INTERNACAO/convenio PLANO-SEGURO PROPRIO, onde:1-Sim 0-Não|
|ap01cv04|CHAR(1)|Atendimento prestado INTERNACAO/convenio PLANO-SEGURO TERCEIRO, onde:1-Sim 0-Não|
|ap02cv01|CHAR(1)|Atendimento prestado ATENDIMEUTO AMBULATORIAL/convenio SUS, onde:1-Sim 0-Não|
|ap02cv02|CHAR(1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PARTICULAR, onde: 1-Sim 0-Não|
|ap02cv05|CHAR(1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PUBLICO, onde: 1-Sim 0-Não|
|ap02cv06|CHAR(1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PRIVADO, onde: 1-Sim 0-Não|
|ap02cv03|CHAR(1)|Atendimento prestado ATENDIMEUTO AMBULATORIAL/Convenio PLANO-SEGURO PROPRIO, onde: 1-Sim 0-Não|
|ap02cv04|CHAR(1)|Atendimento prestado ATENDIMEUTO AMBULATORIAL/Convenio PLANO-SEGURO TERCEIRO, onde: 1-Sim 0-Não|
|ap03cv01|CHAR(1)|Atendimento prestado SADT/ Convenio SUS, onde:1-Sim 0-Não|
|ap03cv02|CHAR(1)|Atendimento prestado SADT/ Convenio PARTICULAR, onde: 1-Sim 0-Não|
|ap03cv05|CHAR(1)|Atendimento prestado SADT/ Convenio PLANO de SAUDE PUBLICO, onde: 1-Sim 0-Não|
|ap03cv06|CHAR(1)|Atendimento prestado SADT/ Convenio PLANO de SAUDE PRIVADO, onde: 1-Sim 0-Não|
|ap03cv03|CHAR(1)|Atendimento prestado SADT/ Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não|
|ap03cv04|CHAR(1)|Atendimento prestado SADT/ Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não|
|ap04cv01|CHAR(1)|Atendimento prestado URGENCIA/ Convenio SUS, onde: 1-sim 0-não|
|ap04cv02|CHAR(1)|Atendimento prestado URGENCIA/ Convenio PARTICULAR, onde: 1-sim 0-não|
|ap04cv05|CHAR(1)|Atendimento prestado URGENCIA/ Convenio PLANO de SAUDE PUBLICO, onde:1-sim 0-não|
|ap04cv06|CHAR(1)|Atendimento prestado URGENCIA/Convenio PLANO de SAUDE PRIVADO, onde:1-sim 0-não|
|ap04cv03|CHAR(1)|Atendimento prestado URGENCIA/ Convenio PLANO-SEGURO PROPRIO, onde:1-sim 0-não|
|ap04cv04|CHAR(1)|Atendimento prestado URGENCIA/ Convenio PLANO-SEGURO TERCEIRO, onde:1-sim 0-não|
|ap05cv01|CHAR(1)|Atendimento prestado OUTROS/ Convenio SUS,onde: 1-sim 0-não|
|ap05cv02|CHAR(1)|Atendimento prestado OUTROS/Convenio PARTICULAR, onde: 1-sim 0-não|
|ap05cv05|CHAR(1)|Atendimento prestado OUTROS/Convenio PLANO de SAUDE PUBLICO, onde:1-sim 0-não|
|ap05cv06|CHAR(1)|Atendimento prestado OUTROS/Convenio PLANO de SAUDE PRIVADO, onde:1-sim 0-não|
|ap05cv03|CHAR(1)|Atendimento prestado OUTROS/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não|
|ap05cv04|CHAR(1)|Atendimento prestado OUTROS/Convenio PLANO-SEGURO TERCEIRO, onde:1-sim 0-não|
|ap06cv01|CHAR(1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio SUS, onde: 1-sim 0-não|
|ap06cv02|CHAR(1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PARTICULAR, onde:1-sim 0-não|
|ap06cv05|CHAR(1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PUBLICO, onde:1-sim 0-não|
|ap06cv06|CHAR(1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PRIVADO, onde:1-sim 0-não|
|ap06cv03|CHAR(1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO-SEGURO PROPRIO, onde:1-sim 0-não|
|ap06cv04|CHAR(1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO-SEGURO TERCEIRO, onde:1-sim 0-não|
|ap07cv01|CHAR(1)|Atendimento prestado REGULACAO/Convenio SUS, onde: 1-sim 0-não|
|ap07cv02|CHAR(1)|Atendimento prestado REGULACAO/Convenio PARTICULAR, onde: 1-sim 0-não|
|ap07cv05|CHAR(1)|Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PUBLICO, onde:1-sim 0-não|
|ap07cv06|CHAR(1)|Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PRIVADO, onde:1-sim 0-não|
|ap07cv03|CHAR(1)|Atendimento prestado REGULACAO/Convenio PLANO-SEGURO PROPRIO, onde:1-sim 0-não|
|ap07cv04|CHAR(1)|Atendimento prestado REGULACAO/Convenio PLANO-SEGURO TERCEIRO, onde:1-sim 0-não|
|atend_pr|CHAR(1)|Indica a existência de algum atendimento prestado para este CNES, onde: 1-sim / 0-não|
|MOTDESAB|CHAR(2)|Código do Motivo de Desabilitação do Estabelecimento|
|dt_atual|CHAR(6)|Ano e Mês de competência da atualização da informação pelo estabelecimento (AAAAMM)|
|competen|CHAR(6)|Ano e Mês de competência da informação (AAAAMM)|
|nat_jur|CHAR(4)| Natureza Jurídica|

### Tabela de Dados complementares (DCufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
|CNES	 |CHAR (7)|Número nacional do estabelecimento de saúde|
|CODUFMUN|CHAR (7)|Código do município do estabelecimento: UF + MUNIC (sem dígito)|
|CPF_CNPJ|CHAR (14)|CPF do estabelecimento, caso pessoa física ou CNPJ, caso pessoa jurídica|
|PF_PJ	|CHAR (1)|Indicador de pessoa: 1-Física 3-Jurídica|
|NIV_DEP|CHAR (1)|Grau de dependência, onde: 1-Individual 3-Mantida |
|CNPJ_MAN|CHAR (14)|CNPJ da mantenedora do estabelecimento. |
|COD_IR	|CHAR (2)|Indica o tipo de retenção de tributos da mantenedora|
|REGSAUDE|CHAR (4)|Código da região de saúde NOAS |
|MICR_REG|CHAR (6)|Código da micro-região de saúde NOAS |
|DISTRSAN|CHAR (4)|Código do distrito sanitário |
|DISTRADM|CHAR (4)|Inicialmente chamado Distrito Administrativo, atualmente Código do Módulo Assistencial conforme tabela local, em conformidade com o Plano Diretor de Regionalização do Estado/Município. |
|VINC_SUS|CHAR (1)|Vínculo com SUS: 1-Sim 0-Não |
|TPGESTAO|CHAR (1)|Gestão de saúde|
|ESFERA_A|CHAR (2)|Código da esfera administrativa|
|ATIVIDAD|CHAR (2)|Código da atividade de ensino/pesquisa |
|RETENCAO|CHAR (2)|Código de retenção de tributos |
|NATUREZA|CHAR (2)|Código da natureza da organização|
|CLIENTEL|CHAR (2)|Código de FLUXO da clientela |
|TP_UNID|CHAR (2)|Tipo de unidade (estabelecimento) |
|TURNO_AT|CHAR (2)|Código de turno de atendimento |
|NIV_HIER|CHAR (2)|Código do nível de hierarquia|
|TPPREST|CHAR (2)|Tipo de Prestador |
|S_HBSAGP|NUMBER (2)|Quantidade de salas HBsAG+ |
|S_HBsAGN|NUMBER (2)|Quantidade de salas HBsAG- |
|S_DPI	|NUMBER (2)|Quantidade de salas DPI |
|S_DPAC	|NUMBER (2)|Quantidade de salas DPAC|
|S_REAGP|NUMBER (2)|Quantidade de salas de reuso de HBsAG+|
|S_REAGN|NUMBER (2)|Quantidade de salas de reuso de HBsAG-|
|S_REHCV|NUMBER (2)|Quantidade de Salas de reuso de HCV+|
|MAQ_PROP|NUMBER (2)|Quantidade de máquinas de proporção|
|MAQ_OUTR|NUMBER (2)|Quantidade de outras máquinas|
|F_AREIA|CHAR (1)|Indica se faz tratamento de água com filtro de areia, onde: 1-Sim 0-Não |
|F_CARVAO|CHAR (1)|Indica se faz tratamento de água com filtro de carvão, onde: 1-Sim 0-Não |
|ABRANDAD|CHAR (1)|Indica se faz tratamento de água com abrandador, onde: 1-Sim 0-Não |
|DEIONIZA|CHAR (1)|Indica se faz tratamento de água com deionizador, onde:	1-Sim 0-Não |
|OSMOSE_R|CHAR (1)|Indica se faz tratamento de água com máquina de osmose reversa, onde: 1-Sim 0-Não|
|OUT_TRAT|CHAR (1)|Indica se faz tratamento de água com outros tipos de equipamento, onde: 1-Sim 0-Não|
|CNS_NEFR|CHAR (15)|CNS do MÉDICO NEFROLOGISTA RESPONSÀVEL|
|DIALISE|CHAR (1)|Indica a existência de algum REQUISITO DE DIÁLISE para este CNES, onde: 1-Sim 0-Não |
|SIMUL_RD|NUMERIC (2)|Quantidade de salas simulação – (Radioterapia)|
|PLANJ_RD|NUMERIC (2)|Quantidade de salas de Planejamento - (Radioterapia)|
|ARMAZ_FT|NUMERIC (2)|Número de salas de armazenamento de fontes - (Radioterapia) |
|CONF_MAS|NUMERIC (2)|Número de salas confecção masc. - (Radioterapia)|
|SALA_MOL|NUMERIC (2)|Número de salas de salas de molde - (Radioterapia)|
|BLOCOPER|NUMERIC (2)|Número de salas de bloco personalizado - (Radioterapia) |
|S_ARMAZE|NUMERIC (2)|Número de salas de armazenagem|
|S_PREPAR|NUMERIC (2)|Número de salas de preparo|
|S_QCDURA|NUMERIC (2)|Salas/Equipamentos de Quimio Curta duração|
|S_QLDURA|NUMERIC (2)|Salas/Equipamentos de Quimio de Longa Duração |
|S_CPFLUX|NUMERIC (2)|Salas/Equipamentos de Capela Fluxo Laminar|
|S_SIMULA|NUMERIC (2)|Quantidade de Simuladores |
|S_ACELL6|NUMERIC (2)|Quantidade de Acelerador Linear até 6 MeV |
|S_ALSEME|NUMERIC (2)|Quantidade de Acelerador Linear maior 6 MeV sem elétrons|
|S_ALCOME|NUMERIC (2)|Quantidade de acelerador linear maior 6 MeV com elétrons|
|ORTV1050|NUMERIC (2)|Quantidade de Equipamentos de Ortovoltagem 10-50 KV |
|ORV50150|NUMERIC (2)|Quantidade de Equipamentos de Ortovoltagem 50-150 KV|
|OV150500|NUMERIC (2)|Quantidade de Equipamentos de Ortovoltagem 150-500 KV |
|UN_COBAL|NUMERIC (2)|Quantidade de Unidade de Cobalto|
|EQBRBAIX|NUMERIC (2)|Quantidade de Equipamentos de Braquiterapia Baixa |
|EQBRMEDI|NUMERIC (2)|Quantidade de Equipamentos de Braquiterapia Média |
|EQBRALTA|NUMERIC (2)|Quantidade de Equipamentos de Braquiterapia Alta|
|EQ_MAREA|NUMERIC (2)|Quantidade de Monitor de Área |
|EQ_MINDI|NUMERIC (2)|Quantidade de Monitor Individual|
|EQSISPLN|NUMERIC (2)|Quantidade de sistema de Computação para Planejamento |
|EQDOSCLI|NUMERIC (2)|Quantidade de dosímetro clínico |
|EQFONSEL|NUMERIC (2)|Quantidade de fontes seladas|
|CNS_ADM|CHAR (15)|CNS do médico responsável – ADMINISTRADOR OU RESPONSÁVEL TÉCNICO |
|CNS_OPlD|CHAR (15)|CNS do médico responsável - ONCOLOGISTA PEDIÁTRICO|
|CNS_CONC|CHAR (15)|CNS do médico responsável - por CIRURGIA ONCOLÓGICA |
|CNS_OCLI|CHAR (15)|CNS do médico responsável - ONCOLOGISTA CLÍNICO |
|CNS_MRAD|CHAR (15)|CNS do médico responsável - RADIOTERAPEUTA|
|CNS_FNUC|CHAR (15)|CNS do médico responsável - FÍSICO NUCLEAR|
|QUIMRADI|CHAR (1)|Indica a existência de algum REQUISITO DE QUÍMIO/RÁDIO para este CNES, onde:1-Sim 0-Não|
|S_RECEPC|NUMERIC (3)|Número de salas de recepção |
|S_TRIHMT|NUMERIC (3)|Número de salas de triagem hematológica |
|S_TRICLI|NUMERIC (3)|Número de salas de triagem clínica|
|S_COLETA|NUMERIC (3)|Número de salas de coleta |
|S_AFERES|NUMERIC (3)|Número de salas de aférese|
|S_PREEST|NUMERIC (3)|Número de salas de pré-estoque|
|S_PROCES|NUMERIC (3)|Número de salas de processamento|
|S_ESTOQU|NUMERIC (3)|Número de salas de estoque|
|S_DISTRI|NUMERIC (3)|Número de salas de distribuição |
|S_SOROLO|NUMERIC (3)|Número de salas de sorologia|
|S_IMUNOH|NUMERIC (3)|Número de salas de imunohematologia |
|S_PRETRA|NUMERIC (3)|Número de salas pré-transfusionais|
|S_HEMOST|NUMERIC (3)|Número de salas hemostasia|
|S_CONTRQ|NUMERIC (3)|Número de salas de controle de qualidade|
|S_BIOMOL|NUMERIC (3)|Número de salas de biologia molecular |
|S_IMUNFE|NUMERIC (3)|Número de salas de imunofenotipágem |
|S_TRANSF|NUMERIC (3)|Número de salas de transfusão |
|S_SGDOAD|NUMERIC (3)|Número de salas seguimento doador |
|QT_CADRE|NUMERIC (3)|Quantidade de cadeiras reclináveis|
|QT_CENRE|NUMERIC (3)|Quantidade de centrífugas refrigeradas|
|QT_REFSA|NUMERIC (3)|Quantidade de refrigeradores para guarda de sangue|
|QT_CONRA|NUMERIC (3)|Quantidade de congeladores rápidos|
|QT_EXTPL|NUMERIC (3)|Quantidade de extratores automáticos de plasma|
|QT_FRE18|NUMERIC (3)|Quantidade de freezers –18ºC|
|QT_FRE30|NUMERIC (3)|Quantidade de freezers -30ºC|
|QT_AGIPL|NUMERIC (3)|Quantidade de agitadores de plaquetas |
|QT_SELAD|NUMERIC (3)|Quantidade de seladoras |
|QT_IRRHE|NUMERIC (3)|Quantidade de irradiadores de hemocomponentes |
|QT_AGLTN|NUMERIC (3)|Quantidade de aglutinoscópio|
|QT_MAQAF|NUMERIC (3)|Quantidade de máquinas de aférese |
|QT_REFRE|NUMERIC (3)|Quantidade de refrigeradores para guarda de reagentes |
|QT_REFAS|NUMERIC (3)|Quantidade de refrigeradores para guarda de amostras de sangue|
|QT_CAPFL|NUMERIC (3)|Quantidade de capelas fluxo laminar |
|CNS_HMTR|CHAR (15)|CNS do médico responsável - HEMOTERAPEUTA |
|CNS_HMTL|CHAR (15)|CNS do médico responsável - HEMATOLOGISTA |
|CNS_CRES|CHAR (15)|CNS do médico capacitado RESPONSÀVEL|
|CNS_RTEC|CHAR (15)|CNS do responsável TÉCNICO / SOROLOGIA|
|HEMOTERA|CHAR (1)|Indica a existência de algum REQUISITO DE HEMOTERAPIA para este CNES, onde:1-Sim 0-Não |
|AP01CV01|CHAR (1)|Atendimento prestado INTERNAÇÃO/Convenio SUS, onde: 1-Sim 0-Não|
|AP01CV02|CHAR (1)|Atendimento prestado INTERNAÇÃO/Convenio PARTICULAR, onde: 1-Sim 0-Não |
|AP01CV05|CHAR (1)|Atendimento prestado INTERNAÇÃO/Convenio PLANO de SAUDE PUBLICO, onde:1-Sim 0-Não|
|AP01CV06|CHAR (1)|Atendimento prestado INTERNAÇÃO/Convenio PLANO de SAUDE PRIVADO, onde:1-Sim 0-Não|
|AP01CV03|CHAR (1)|Atendimento prestado INTERNAÇÃO/Convenio PLANO-SEGURO PROPRIO, onde:1-Sim 0-Não|
|AP01CV04|CHAR (1)|Atendimento prestado INTERNAÇÃO/Convenio PLANO-SEGURO TERCEIRO, onde:1-Sim 0-Não |
|AP02CV01|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio SUS, onde:1-Sim 0-Não |
|AP02CV02|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PARTICULAR, onde:1-Sim 0-Não|
|AP02CV05|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PUBLICO, onde:1-Sim 0-Não|
|AP02CV06|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PRIVADO, onde:1-Sim 0-Não|
|AP02CV03|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO- SEGURO PROPRIO, onde:1-Sim 0-Não |
|AP02CV04|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO- SEGURO TERCEIRO, onde:1-Sim 0-Não|
|AP03CV01|CHAR (1)|Atendimento prestado SADT/Convenio SUS, onde: 1-Sim 0-Não|
|AP03CV02|CHAR (1)|Atendimento prestado SADT/Convenio PARTICULAR, onde: 1-Sim 0-Não |
|AP03CV05|CHAR (1)|Atendimento prestado SADT/Convenio PLANO de SAUDE PUBLICO, onde: 1-Sim 0-Não |
|AP03CV06|CHAR (1)|Atendimento prestado SADT/Convenio PLANO de SAUDE PRIVADO, onde: 1-Sim 0-Não |
|AP03CV03|CHAR (1)|Atendimento prestado SADT/Convenio PLANO-SEGURO PROPRIO, onde: 1-Sim 0-Não |
|AP03CV04|CHAR (1)|Atendimento prestado SADT/Convenio PLANO-SEGURO TERCEIRO, onde: 1-Sim 0-Não|
|AP04CV01|CHAR (1)|Atendimento prestado URGENCIA/Convenio SUS, onde: 1-Sim 0-Não|
|AP04CV02|CHAR (1)|Atendimento prestado URGENCIA/Convenio PARTICULAR, onde: 1-Sim 0-Não |
|AP04CV05|CHAR (1)|Atendimento prestado URGENCIA/Convenio PLANO de SAUDE PUBLICO, onde:1-Sim 0-Não|
|AP04CV06|CHAR (1)|Atendimento prestado URGENCIA/Convenio PLANO de SAUDE PRIVADO, onde:1-Sim 0-Não|
|AP04CV03|CHAR (1)|Atendimento prestado URGENCIA/Convenio PLANO-SEGURO PROPRIO, onde:1-Sim 0-Não|
|AP04CV04|CHAR (1)|Atendimento prestado URGENCIA/Convenio PLANO-SEGURO TERCEIRO, onde:1-Sim 0-Não |
|AP05CV01|CHAR (1)|Atendimento prestado OUTROS/Convenio SUS, onde: 1-Sim 0-Não|
|AP05CV02|CHAR (1)|Atendimento prestado OUTROS/Convenio PARTICULAR, onde: 1-Sim 0-Não |
|AP05CV05|CHAR (1)|Atendimento prestado OUTROS/Convenio PLANO de SAUDE PUBLICO, onde:1-Sim 0-Não|
|AP05CV06|CHAR (1)|Atendimento prestado OUTROS/Convenio PLANO de SAUDE PRIVADO, onde:1-Sim 0-Não|
|AP05CV03|CHAR (1)|Atendimento prestado OUTROS/Convenio PLANO-SEGURO PROPRIO, onde: 1-Sim 0-Não |
|AP05CV04|CHAR (1)|Atendimento prestado OUTROS/Convenio PLANO-SEGURO TERCEIRO, onde:1-Sim 0-Não |
|AP06CV01|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio SUS, onde: 1-Sim 0-Não |
|AP06CV02|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PARTICULAR, onde:1-Sim 0-Não |
|AP06CV05|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PUBLICO, onde:1-Sim 0-Não |
|AP06CV06|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PRIVADO, onde:1-Sim 0-Não |
|AP06CV03|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO-SEGURO PROPRIO, onde:1-Sim 0-Não |
|AP06CV04|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO-SEGURO TERCEIRO, onde:1-Sim 0-Não|
|AP07CV01|CHAR (1)|Atendimento prestado REGULACAO/Convenio SUS, onde: 1-Sim 0-Não |
|AP07CV02|CHAR (1)|Atendimento prestado REGULACAO/Convenio PARTICULAR, onde: 1-Sim 0-Não|
|AP07CV05|CHAR (1)|Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PUBLICO, onde:1-Sim 0-Não |
|AP07CV06|CHAR (1)|Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PRIVADO, onde:1-Sim 0-Não |
|AP07CV03|CHAR (1)|Atendimento prestado REGULACAO/Convenio PLANO-SEGURO PROPRIO, onde:1-Sim 0-Não |
|AP07CV04|CHAR (1)|Atendimento prestado REGULACAO/Convenio PLANO-SEGURO TERCEIRO, onde:1-Sim 0-Não|
|ATEND_PR|CHAR (1)|Indica a existência de algum atendimento prestado para este CNES, onde: 1-sim / 0-não|
|GESPRG3E|CHAR (1)|Indicador se a gestão do programa é ESTADUAL, onde: 1-sim 0-não|
|GESPRG3M|CHAR (1)|Indicador se a gestão do programa é MUNICIPAL, onde: 1-sim 0-não |
|GESPRG4E|CHAR (1)|Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é ESTADUAL, onde:1-Sim 0-Não |
|GESPRG4M|CHAR (1)|Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é MUNICIPAL, onde:1-Sim 0-Não|
|GESPRG6E|CHAR (1)|Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção HOSPITALAR é ESTADUAL, onde:1-Sim 0-Não |
|GESPRG6M|CHAR (1)|Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção HOSPITALAR é MUNICIPAL, onde:1-Sim 0-Não|
|NIVATE_A|CHAR (1)|Indica a existência de Nível de Atenção AMBULATORIAL, de gestão Municipal/Estadual, para este CNES, onde:1-sim 0-não |
|NIVATE_H|CHAR (1)|Indica a existência de Nível de Atenção HOSPITALAR, de gestão Municipal/Estadual, para este CNES, onde:1-sim 0-não |
|COMPETEN|CHAR (6)|Ano e Mês de competência da informação (AAAAMM)|
|NAT_JUR|CHAR (4)|Natureza Jurídica |


### Tabela de Profissional (PFufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
|CNES|CHAR (7)|Número nacional do estabelecimento de saúde |
|CODUFMUN|CHAR (6)|Código do município do estabelecimento UF+ MUNIC (sem dígito) |
|REGSAUDE|CHAR (4)|Código da região de saúde |
|MICR_REG|CHAR (6)|Código da micro-região de saúde |
|DISTRASAN|CHAR (4)|Código do distrito sanitário|
|DISTRADM|CHAR (4)|Código do distrito administrativo |
|TPGESTAO|CHAR (1)|Gestão de saúde |
|PF_PJ|CHAR (1)|Indicador de pessoa: 1-Física 3-Jurídica|
|CPF_CNPJ|CHAR (14)|CPF do Estabelecimento, caso pessoa física ou CNPJ, caso pessoa jurídica|
|NIV_DEP|CHAR (1)|Grau de dependência, onde: 1-Individual 3-Mantida |
|CNPJ_MAN|CHAR (14)|CNPJ da mantenedora do estabelecimento|
|ESFERA_A|CHAR (2)|Código da esfera administrativa |
|ATIVIDAD|CHAR (2)|Código da atividade de ensino |
|RETENCAO|CHAR (2)|Código de retenção de tributos|
|NATUREZA|CHAR (2)|Código da natureza da organização |
|CLIENTEL|CHAR (2)|Código de fluxo da clientela|
|TP_UNID|CHAR (2)|Tipo de unidade (estabelecimento) |
|TURNO_AT|CHAR (2)|Código de turno de atendimento|
|NIV_HIER|CHAR (2)|Código do nível de hierarquia |
|TERCEIRO|CHAR (2)|O estabelecimento é terceiro: 1-Sim 0-Não 2-não |
|CPF_PROF|CHAR (11)|CPF do Profissional ou caso “99999999999” caso não seja preenchido. |
|CPF_UNICO|CHAR (6)|Contador de CPF ÚNICO do Profissional (O preenchimento deste campo acontece somente uma vez por chave - única- CPF) Nos casos em que o CPF for 99999999999, o CPFUNICO sempre deve ser “1”. |
|CBO|CHAR (6)|Código da especialidade do profissional |
|CBO_UNICO|CHAR (2)|Registro único do Código da especialidade do profissional(este registro acontece somente uma vez por chave única CPF + CBO) |
|NOMEPROF|CHAR (60)|Nome do profissional|
|CNS_PROF|CHAR (15)|CNS do profissional ou “999999999999999” caso não seja preenchido.|
|CONSELHO|CHAR (2)|Código do conselho de classe|
|REGISTRO|CHAR (13)|Número do registro no conselho de classe|
|VINCULAC|CHAR (6)|Vínculo empregatício com o estabelecimento: |
|VINCUL_C|CHAR (1)|Vínculo empregatício com o estabelecimento: Contratado SUS|
|VINCUL_A|CHAR (1)|Vínculo empregatício com o estabelecimento: Autônomo SUS|
|VINCUL_N|CHAR (1)|Vínculo empregatício com o estabelecimento: Vínculo não identificado (registros de profissionais não SUS e outras situações anômalas) |
|PROF_SUS|CHAR (1)|Caracterização do PROFISSIONAL que realiza ATENDIMENTO SUS|
|PROFNSUS|CHAR (1)|Caracterização do PROFISSIONAL que realiza ATENDIMENTO NÃO SUS|
|HORAOUTR|CHAR (3)|Carga horária não ambulatorial, nem hospitalar|
|HORAHOSP|CHAR (3)|Carga horária HOSPITALAR|
|HORA_AMB|CHAR (3)|Carga horária AMBULATORIAL|
|COMPETEN|CHAR (6)|Ano e Mês de competência da informação (AAAAMM) |
|UFMUNRES|CHAR (8)|Código da UF + município de residência do profissional (sem dígito) |
|NAT_JUR|CHAR (4)|Natureza Jurídica |

### Tabela de Leitos (LTufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
|CNES	|CHAR (7)|Número nacional do estabelecimento de saúde |
|CODUFMUN|CHAR (6)|Código do município do estabelecimento UF+ MUNIC (sem dígito)|
|REGSAUDE|CHAR (4)|Código da região de saúde|
|MICR_REG|CHAR (6)|Código da micro-região de saúde|
|DISTRSAN|CHAR (4)|Código do distrito sanitário |
|DISTRADM|CHAR (4)|Código do distrito administrativo|
|TPGESTAO|CHAR (1)|Gestão de saúde|
|PF_PJ	|CHAR (1)|Indicador de pessoa: 1-Física 3-Jurídica|
|CPF_CNPJ|CHAR (14)|CPF do Estabelecimento, caso pessoa física OU CNPJ, caso pessoa jurídica|
|NIV_DEP|	CHAR (1)|Grau de dependência: 1-Individual 3-Mantida|
|CNPJ_MAN|CHAR (14)|CNPJ da mantenedora do Estabelecimento|
|ESFERA_A|CHAR (2)|Código da esfera administrativa|
|ATIVIDAD|CHAR (2)|Código da atividade de ensino|
|RETENCAO|CHAR (2)|Código de retenção de tributos |
|NATUREZA|CHAR (2)|Código da natureza da organização|
|CLIENTEL|CHAR (2)|Código de fluxo da clientela |
|TP_UNID|	CHAR (2)|Tipo de unidade (Estabelecimento)|
|TURNO_AT|CHAR (2)|Código de turno de atendimento |
|NIV_HIER|CHAR (2)|Código do nível de hierarquia|
|TERCEIRO|CHAR (1)|O estabelecimento é terceiro: 1-Sim 0-Não|
|TP_LEITO|CHAR (2)|Tipo do LEITO|
|CODLEITO|CHAR (2)|Especialidade do LEITO |
|QT_EXIST|NUMERIC (4)|Quantidade de leitos existentes |
|QT_CONTR|NUMERIC (4)|Quantidade de leitos contratados|
|QT_SUS	|NUMERIC (4)|Quantidade de leitos para o SUS|
|COMPETEN|CHAR (6)|Ano e Mês de competência da informação (AAAAMM)|

### Tabela de Equipamentos (EQufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
|CNES	|CHAR (7)|Número nacional do estabelecimento de saúde|
|CODUFMUN|CHAR (6)|Código do município do estabelecimento UF+ MUNIC (sem dígito) |
|REGSAUDE|CHAR (4)|Código da região de saúde |
|MICR_REG|CHAR (6)|Código da micro-região de saúde |
|DISTRSAN|CHAR (4)|Código do distrito sanitário|
|DISTRADM|CHAR (4)|Código do distrito administrativo |
|TPGESTAO|CHAR (1)|Gestão de saúde |
|PF_PJ	|CHAR (1)|Indicador de pessoa: 1-Física3-Jurídica|
|CPF_CNPJ|CHAR (14)|CPF, caso pessoa física OU CNPJ, caso pessoa jurídica|
|NIV_DEP|	CHAR (1)|Grau de dependência, onde: 1-Individual 3-Mantida |
|CNPJ_MAN|CHAR (14)|CNPJ da mantenedora do Estabelecimento |
|ESFERA_A|CHAR (2)|Código da esfera administrativa |
|ATIVIDAD|CHAR (2)|Código da atividade de ensino |
|RETENCAO|CHAR (2)|Código de retenção de tributos|
|NATUREZA|CHAR (2)|Código da natureza da organização |
|CLIENTEL|CHAR (2)|Código de fluxo da clientela|
|TP_UNID|	CHAR (2)|Tipo de unidade |
|TURNO_AT|CHAR (2)|Código de turno de atendimento|
|NIV_HIER|CHAR (2)|Código do nível de hierarquia |
|TERCEIRO|CHAR (1)|O estabelecimento é terceiro: 1-Sim 0-Não |
|TIPEQUIP|CHAR (1)|Código do tipo do equipamento |
|CODEQUIP|CHAR (2)|Código do equipamento |
|QT_EXIST|CHAR(3)|	Quantidade existente do equipamento|
|QT_USO	|CHAR(3)|	Quantidade em uso do equipamento |
|IND_SUS|	CHAR(1)|	Indicador de disponibilidade para o SUS, onde: 1 =SIM 0 = NÃO|
|IND_NSUS|CHAR(1)|	Indicador de EQUIPAMENTO NÃO DISPONÍVEL para o SUS, onde: 1 = SIM 0 = NÃO|
|COMPETEN|CHAR (6)|Ano e Mês de competência da informação (AAAAMM) |
|NAT_JUR|CHAR (4)|Natureza Jurídica|

### Tabela de Serviço Especializado (SRufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
|CNES	|CHAR (7)|Número nacional do estabelecimento de saúde|
|CODUFMUN|CHAR (6)|Código do município do estabelecimento UF+ MUNIC (sem dígito) |
|SERV_ESP|CHAR (3)|Código do serviço especializado |
|CLASS_SR|CHAR (3)|Código da classificação do serviço ou ‘999’, caso INEXISTENTE |
|SRVUNICO|CHAR (3)|Código do serviço especializado ÚNICO (O PREENCHIMENTO deste campo acontece somente uma vez por chave única CNES + SERV_ESP)|
|REGSAUDE|CHAR (4)|Código da região de saúde |
|MICR_REG|CHAR (6)|Código da micro-região de saúde |
|DISTRSAN|CHAR (4)|Código do distrito sanitário|
|DISTRADM|CHAR (4)|Código do distrito administrativo |
|TPGESTAO|CHAR (1)|Gestão de saúde |
|PF_PJ	|CHAR (1)|Indicador de pessoa: 1-Física 3-Jurídica |
|CPF_CNPJ|CHAR (14)|CPF do Estabelecimento, caso pessoa física ou CNPJ, caso pessoa jurídica |
|NIV_DEP|CHAR (1)|Grau de dependência, onde: 1-Individual 3-Mantida|
|ESFERA_A|CHAR (2)|Código da esfera administrativa |
|ATIVIDAD|CHAR (2)|Código da atividade de ensino |
|RETENCAO|CHAR (2)|Código de retenção de tributos|
|NATUREZA|CHAR (2)|Código da natureza da organização |
|CLIENTEL|CHAR (2)|Código de fluxo da clientela|
|TP_UNID|CHAR (2)|Tipo de unidade (Estabelecimento)|
|TURNO_AT|CHAR (2)|Código de turno de atendimento|
|NIV_HIER|CHAR (2)|Código do nível de hierarquia |
|TERCEIRO|CHAR (1)|O estabelecimento é terceiro: 1-Sim 0-Não |
|CNPJ_MAN|CHAR (14)|CNPJ da mantenedora do estabelecimento |
|CARACTER|CHAR (1)|Caracterização do serviço |
|AMB_HOSP|CHAR (4)|Indica se o Serviço é Ambulatorial Não SUS / Ambulatorial SUS / Hospitalar Não SUS / Hospitalar SUS, onde: 1 – Sim 0 – Não|
|COMPETEN|CHAR (6)|Ano e Mês de competência da informação (AAAAMM) |
|CONTSRVU|CHAR (1)|INDICADOR de serviço especializado ÚNICO|
|CNESTERC|CHAR (7)|Número nacional do estabelecimento de saúde TERCEIRO|
|NAT_JUR|CHAR (4)|Natureza Jurídica|

### Tabela de Equipe (EPufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
|CNES|CHAR (7)|Número nacional do estabelecimento de saúde |
|CODUFMUN|CHAR (7)|Código do município do estabelecimento: UF + MUNIC (sem dígito) |
|COD_CEP|CHAR (8)|Código do CEP do estabelecimento|
|CPF_CNPJ|CHAR (14)|CPF do estabelecimento, caso pessoa física ou CNPJ, caso pessoa jurídica|
|PF_PJ|CHAR (1)|Indicador de pessoa: 1-Física 3-Jurídica|
|NIV_DEP|CHAR (1)|Grau de dependência, onde: 1-Individual 3-Mantida |
|CNPJ_MAN|CHAR (14)|CNPJ da mantenedora do estabelecimento.|
|COD_IR|CHAR (2)|Indica o tipo de retenção de tributos da mantenedora|
|REGSAUDE|CHAR (4)|Código da região de saúde NOAS |
|MICR_REG|CHAR (6)|Código da micro-região de saúde NOAS |
|DISTRSAN|CHAR (4)|Código do distrito sanitário|
|DISTRADM|CHAR (4)|Inicialmente chamado Distrito Administrativo, atualmente Código do Módulo Assistencial conforme tabela local, em conformidade com o Plano Diretor de Regionalização do Estado/Município.|
|VINC_SUS|CHAR (1)|Vínculo com SUS: 1-Sim 0-Não|
|TPGESTAO|CHAR (1)|Gestão de saúde |
|ESFERA_A|CHAR (2)|Código da esfera administrativa|
|RETENCAO|CHAR (2)|Código de retenção de tributos |
|ATIVIDAD|CHAR (2)|Código da atividade de ensino/pesquisa|
|NATUREZA|CHAR (2)|Código da natureza da organização |
|CLIENTEL|CHAR (2)|Código de FLUXO da clientela|
|TP_UNID|CHAR (2)|Tipo de unidade (estabelecimento)|
|TURNO_AT|CHAR (2)|Código de turno de atendimento |
|NIV_HIER|CHAR (2)|Código do nível de hierarquia|
|TERCEIRO|CHAR (1)|O estabelecimento é terceiro: 1-Sim 0-Não|
|TP_PREST|CHAR (2)|Tipo de Prestador|
|GESPRG1E|CHAR (1)|Indicador se a gestão da atividade ATENÇÃO BÁSICA do Nível de Atenção AMBULATORIAL é ESTADUAL, onde:1-sim 0-não |
|GESPRG1M|CHAR (1)|Indicador se a gestão da atividade ATENÇÃO BÁSICA do Nível de Atenção AMBULATORIAL é MUNICIPAL, onde:1-sim 0-não|
|GESPRG2E|CHAR (1)|Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é ESTADUAL, onde:1-sim 0-não|
|GESPRG2M|CHAR (1)|Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é MUNICIPAL, onde:1-sim 0-não|
|GESPRG4E|CHAR (1)|Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é ESTADUAL, onde:1-sim 0-não |
|GESPRG4M|CHAR (1)|Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é MUNICIPAL, onde:1-sim 0-não|
|NIVATE_A|CHAR (1)|Indica a existência de Nível de Atenção AMBULATORIAL, de gestão Municipal/Estadual, para este CNES, onde:1-sim 0-não|
|GESPRG3E|CHAR (1)|Indicador se a gestão do programa é ESTADUAL, onde: 1-sim 0-não |
|GESPRG3M|CHAR (1)|Indicador se a gestão do programa é MUNICIPAL, onde: 1-sim 0-não|
|GESPRG5E|CHAR (1)|Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção HOSPITALAR é ESTADUAL, onde:1-sim 0-não|
|GESPRG5M|CHAR (1)|Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção HOSPITALAR é MUNICIPAL, onde:1-sim 0-não |
|GESPRG6E|CHAR (1)|Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção HOSPITALAR é ESTADUAL, onde:1-sim 0-não|
|GESPRG6M|CHAR (1)|Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção HOSPITALAR é MUNICIPAL, onde:1-sim 0-não|
|NIVATE_H|CHAR (1)|Indica a existência de Nível de Atenção HOSPITALAR, de gestão Municipal/Estadual, para este CNES, onde:1-sim 0-não |
|AP01CV01|CHAR (1)|Atendimento prestado INTERNAÇÃO/ Convenio SUS, onde:1-sim 0-não |
|AP01CV02|CHAR (1)|Atendimento prestado INTERNAÇÃO/Convenio PARTICULAR, onde: 1-sim 0-não|
|AP01CV05|CHAR (1)|Atendimento prestado INTERNAÇÃO/Convenio PLANO de SAUDE PUBLICO, onde:1-sim 0-não |
|AP01CV06|CHAR (1)|Atendimento prestado INTERNAÇÃO/Convenio PLANO de SAUDE PRIVADO, onde:1-sim 0-não |
|AP01CV03|CHAR (1)|Atendimento prestado INTERNAÇÃO/Convenio PLANO-SEGURO PROPRIO, onde:1-sim 0-não|
|AP01CV04|CHAR (1)|Atendimento prestado INTERNAÇÃO/Convenio PLANO-SEGURO TERCEIRO, onde:1-sim 0-não|
|AP02CV01|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio SUS, onde:1-sim 0-não|
|AP02CV02|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PARTICULAR, onde:1-sim 0-não|
|AP02CV05|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PUBLICO, onde:1-sim 0-não|
|AP02CV06|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PRIVADO, onde:1-sim 0-não|
|AP02CV03|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO- SEGURO PROPRIO, onde:1-sim 0-não|
|AP02CV04|CHAR (1)|Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO- SEGURO TERCEIRO, onde:1-sim 0-não|
|AP03CV01|CHAR (1)|Atendimento prestado SADT/Convenio SUS, onde: 1-sim 0-não |
|AP03CV02|CHAR (1)|Atendimento prestado SADT/Convenio PARTICULAR, onde: 1-sim 0-não|
|AP03CV05|CHAR (1)|Atendimento prestado SADT/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não|
|AP03CV06|CHAR (1)|Atendimento prestado SADT/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não|
|AP03CV03|CHAR (1)|Atendimento prestado SADT/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não|
|AP03CV04|CHAR (1)|Atendimento prestado SADT/Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não |
|AP04CV01|CHAR (1)|Atendimento prestado URGENCIA/Convenio SUS, onde: 1-sim 0-não|
|AP04CV02|CHAR (1)|Atendimento prestado URGENCIA/Convenio PARTICULAR, onde: 1-sim 0-não|
|AP04CV05|CHAR (1)|Atendimento prestado URGENCIA/Convenio PLANO de SAUDE PUBLICO, onde:1-sim 0-não|
|AP04CV06|CHAR (1)|Atendimento prestado URGENCIA/Convenio PLANO de SAUDE PRIVADO, onde:1-sim 0-não|
|AP04CV03|CHAR (1)|Atendimento prestado URGENCIA/Convenio PLANO-SEGURO PROPRIO, onde:1-sim 0-não|
|AP04CV04|CHAR (1)|Atendimento prestado URGENCIA/Convenio PLANO-SEGURO TERCEIRO, onde:1-sim 0-não |
|AP05CV01|CHAR (1)|Atendimento prestado OUTROS/Convenio SUS,onde: 1-sim 0-não|
|AP05CV02|CHAR (1)|Atendimento prestado OUTROS/Convenio PARTICULAR, onde: 1-sim 0-não |
|AP05CV05|CHAR (1)|Atendimento prestado OUTROS/Convenio PLANO de SAUDE PUBLICO, onde:1-sim 0-não|
|AP05CV06|CHAR (1)|Atendimento prestado OUTROS/Convenio PLANO de SAUDE PRIVADO, onde:1-sim 0-não|
|AP05CV03|CHAR (1)|Atendimento prestado OUTROS/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não|
|AP05CV04|CHAR (1)|Atendimento prestado OUTROS/Convenio PLANO-SEGURO TERCEIRO, onde:1-sim 0-não|
|AP06CV01|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio SUS, onde: 1-sim 0-não |
|AP06CV02|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PARTICULAR, onde:1-sim 0-não |
|AP06CV05|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PUBLICO, onde:1-sim 0-não |
|AP06CV06|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PRIVADO, onde:1-sim 0-não |
|AP06CV03|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/ Convenio PLANO-SEGURO PROPRIO, onde:1-sim 0-não|
|AP06CV04|CHAR (1)|Atendimento prestado VIGILANCIA EM SAUDE/ Convenio PLANO-SEGURO TERCEIRO, onde:1-sim 0-não |
|AP07CV01|CHAR (1)|Atendimento prestado REGULACAO/Convenio SUS, onde: 1-sim 0-não|
|AP07CV02|CHAR (1)|Atendimento prestado REGULACAO/Convenio PARTICULAR, onde: 1-sim 0-não |
|AP07CV05|CHAR (1)|Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PUBLICO, onde:1-sim 0-não|
|AP07CV06|CHAR (1)|Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PRIVADO, onde:1-sim 0-não|
|AP07CV03|CHAR (1)|Atendimento prestado REGULACAO/Convenio PLANO-SEGURO PROPRIO, onde:1-sim 0-não |
|AP07CV04|CHAR (1)|Atendimento prestado REGULACAO/Convenio PLANO-SEGURO TERCEIRO, onde:1-sim 0-não|
|ATEND_PR|CHAR (1)|Indica a existência de algum atendimento prestado para este CNES, onde: 1-sim / 0-não|
|ID_EQUIPE|CHAR (18)|Código do Município + Código da Área da Equipe + Seqüencial da Equipe|
|TIPO_EQP|CHAR (2)|Tipo de Equipe|
|NOME_EQP|CHAR (60)|Nome da Equipe |
|AREA_EQP|CHAR (10)|Código da Área da Equipe|
|NOMEAREA|CHAR (60)|Nome da Área|
|ID_SEGM|CHAR (8)|Código do Segmento|
|DESCSEGM|CHAR (60)|Descrição do Segmento|
|TIPOSEGM|CHAR (1)|Tipo do Segmento: 1–Urbano 2–Rural|
|DT_ATIVA|CHAR (6)|Ano e Mês da Data de ATIVAÇÃO da Equipe |
|DT_DESAT|CHAR (6)|Ano e Mês da Data de DESATIVAÇÃO da Equipe |
|QUILOMBO|CHAR (1)|Atende População Assistida Quilombolas: 1-Sim 0-Não |
|ASSENTAD|CHAR (1)|Atende População Assistida Assentados: 1– Sim 0-Não |
|POPGERAL|CHAR (1)|Atende População Assistida Geral: 1-Sim 0-Não |
|ESCOLA|CHAR (1)|Atende População Assistida Escolares: 1-Sim 0-Não|
|INDIGENA|CHAR (1)|Atende População Assistida PRONASCI: 1-Sim 0-Não |
|PRONASCI|CHAR (1)|Atende População Assistida Geral: 1-Sim 0-Não |
|MOTDESAT|CHAR (2)|Código do Motivo de Desativação da Equipe|
|TP_DESAT|CHAR (1)|Código do Tipo de Desativação da Equipe 1 – Temporário 2 - Definitivo |
|COMPETEN|CHAR (6)|Ano e Mês de competência da informação (AAAAMM)|
|NAT_JUR|CHAR (4)|Natureza Jurídica|

### Tabela de Habilitacoes (HBufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| CNES| CHAR (7) | Número nacional do estabelecimento de saúde|
| CODUFMUN| CHAR (6) | Código do município do estabelecimento UF+ MUNIC (sem dígito)|
| REGSAUDE| CHAR (4) | Código da região de saúde|
| MICR_REG | CHAR (6) | Código da micro-região de saúde|
| DISTRSAN| CHAR (4) | Código do distrito sanitário |
| DISTRADM| CHAR (4) | Código do distrito administrativo|
| TPGESTAO| CHAR (1) | Gestão de saúde|
| PF_PJ| CHAR (1) | Indicador de pessoa: 1-Física 3-Jurídica |
| CPF_CNPJ | CHAR (14)| CPF do Estabelecimento, caso pessoa física OU CNPJ, caso pessoa jurídica |
| NIV_DEP| CHAR (1) | Grau de dependência: 1-Individual 3-Mantida|
| CNPJ_MAN | CHAR (14)| CNPJ da mantenedora do Estabelecimento |
| ESFERA_A | CHAR (2) | Código da esfera administrativa|
| ATIVIDAD| CHAR (2) | Código da atividade de ensino|
| RETENCAO| CHAR (2) | Código de retenção de tributos |
| NATUREZA| CHAR (2) | Código da natureza da organização |
| CLIENTEL| CHAR (2) | Código de fluxo da clientela|
| TP_UNID| CHAR (2) | Tipo de unidade (Estabelecimento) |
| TURNO_AT | CHAR (2) | Código de turno de atendimento|
| NIV_HIER | CHAR (2) | Código do nível de hierarquia |
| TERCEIRO| CHAR (1) | O estabelecimento é terceiro: 1-Sim 0-Não 2-não |
| COD_CEP| CHAR (8) | CEP do estabelecimento|
| VINC_SUS | CHAR (2) | Vínculo com SUS: 1-Sim 0-Não|
| TP_PREST | CHAR(2)| Tipo de Prestador |
| SGRUPHAB| CHAR(4)| Código da habilitação |
| CMPT_INI | CHAR(6)| Competência inicial |
| CMPT_FIM | CHAR(6)| Competência final |
| DTPORTAR| CHAR (10)| Data da portaria|
| PORTARIA| CHAR (50)| Portaria|
| MAPORTAR| CHAR (6) | Campo DT_PORTARIA formatado como AAAAMM|
| NULEITOS| NUMERIC (3)| Quantidade de leitos|
| COMPETEN| CHAR (6) | Ano e Mês de competência da informação (AAAAMM) |
| NAT_JUR| CHAR (6) | Natureza Jurídica |

### Tabela de Regras contratuais (RCufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| CNES| CHAR (7) | Número nacional do estabelecimento de saúde|
| CODUFMUN| CHAR (6) | Código do município do estabelecimento UF+ MUNIC (sem dígito)|
| REGSAUDE| CHAR (4) | Código da região de saúde|
| MICR_REG | CHAR (6) | Código da micro-região de saúde|
| DISTRSAN| CHAR (4) | Código do distrito sanitário |
| DISTRADM| CHAR (4) | Código do distrito administrativo|
| TPGESTAO| CHAR (1) | Gestão de saúde|
| PF_PJ| CHAR (1) | Indicador de pessoa: 1-Física 3-Jurídica |
| CPF_CNPJ | CHAR (14)| CPF do Estabelecimento, caso pessoa física OU CNPJ, caso pessoa jurídica |
| NIV_DEP| CHAR (1) | Grau de dependência: 1-Individual 3-Mantida|
| CNPJ_MAN | CHAR (14)| CNPJ da mantenedora do Estabelecimento |
| ESFERA_A | CHAR (2) | Código da esfera administrativa |
| ATIVIDAD| CHAR (2) | Código da atividade de ensino |
| RETENCAO| CHAR (2) | Código de retenção de tributos|
| NATUREZA| CHAR (2) | Código da natureza da organização |
| CLIENTEL| CHAR (2) | Código de fluxo da clientela|
| TP_UNID| CHAR (2) | Tipo de unidade (Estabelecimento) |
| TURNO_AT | CHAR (2) | Código de turno de atendimento|
| NIV_HIER | CHAR (2) | Código do nível de hierarquia |
| TERCEIRO| CHAR (1) | O estabelecimento é terceiro: 1-Sim 0-Não 2-não |
| COD_CEP| CHAR (8) | CEP do estabelecimento|
| VINC_SUS | CHAR (2) | Vínculo com SUS: 1-Sim 0-Não|
| TP_PREST | CHAR(2)| Tipo de Prestador |
| SGRUPHAB| CHAR(4)| Código da habilitação |
| CMPT_INI | CHAR(6)| Competência inicial |
| CMPT_FIM | CHAR(6)| Competência final |
| DTPORTAR| CHAR (10)| Data da portaria|
| PORTARIA| CHAR (50)| Portaria|
| MAPORTAR| CHAR (6) | Campo DT_PORTARIA formatado como AAAAMM|
| COMPETEN| CHAR (6) | Ano e Mês de competência da informação (AAAAMM) |
| NAT_JUR| CHAR (4) | Natureza Jurídica |

### Tabela de Gestão e Metas (GMufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| CNES| CHAR (7) | Número nacional do estabelecimento de saúde |
| CODUFMUN| CHAR (6) | Código do município do estabelecimento UF+ MUNIC (sem dígito) |
| REGSAUDE| CHAR (4) | Código da região de saúde |
| MICR_REG | CHAR (6) | Código da micro-região de saúde |
| DISTRSAN| CHAR (4) | Código do distrito sanitário|
| DISTRADM| CHAR (4) | Código do distrito administrativo |
| TPGESTAO| CHAR (1) | Gestão de saúde |
| PF_PJ| CHAR (1) | Indicador de pessoa: 1-Física 3-Jurídica|
| CPF_CNPJ | CHAR (14)| CPF do Estabelecimento, caso pessoa física OU CNPJ, caso pessoa jurídica |
| NIV_DEP| CHAR (1) | Grau de dependência: 1-Individual 3-Mantida|
| CNPJ_MAN | CHAR (14)| CNPJ da mantenedora do Estabelecimento |
| ESFERA_A | CHAR (2) | Código da esfera administrativa|
| ATIVIDAD| CHAR (2) | Código da atividade de ensino|
| RETENCAO| CHAR (2) | Código de retenção de tributos |
| NATUREZA| CHAR (2) | Código da natureza da organização|
| CLIENTEL| CHAR (2) | Código de fluxo da clientela |
| TP_UNID| CHAR (2) | Tipo de unidade (Estabelecimento)|
| TURNO_AT | CHAR (2) | Código de turno de atendimento |
| NIV_HIER | CHAR (2) | Código do nível de hierarquia|
| TERCEIRO| CHAR (1) | O estabelecimento é terceiro: 1-Sim 0-Não 2-não|
| COD_CEP| CHAR (8) | CEP do estabelecimento |
| VINC_SUS | CHAR (2) | Vínculo com SUS: 1-Sim 0-Não |
| TP_PREST | CHAR(2)| Tipo de Prestador|
| SGRUPHAB| CHAR(4)| Código da habilitação|
| CMPT_INI | CHAR(6)| Competência inicial|
| CMPT_FIM | CHAR(6)| Competência final|
| DTPORTAR| CHAR (10)| Data da portaria |
| PORTARIA| CHAR (50)| Portaria |
| MAPORTAR| CHAR (6) | Campo DT_PORTARIA formatado como AAAAMM |
| COMPETEN| CHAR (6) | Ano e Mês de competência da informação (AAAAMM)|
| NAT_JUR| CHAR (6) | Natureza Jurídica|

### Tabela de Estabelecimento de Ensino (EEufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| CNES| CHAR (7) | Número nacional do estabelecimento de saúde |
| CODUFMUN| CHAR (6) | Código do município do estabelecimento UF+ MUNIC (sem dígito) |
| REGSAUDE| CHAR (4) | Código da região de saúde |
| MICR_REG | CHAR (6) | Código da micro-região de saúde |
| DISTRSAN| CHAR (4) | Código do distrito sanitário|
| DISTRADM| CHAR (4) | Código do distrito administrativo |
| TPGESTAO| CHAR (1) | Gestão de saúde|
| PF_PJ| CHAR (1) | Indicador de pessoa: 1-Física 3-Jurídica |
| CPF_CNPJ | CHAR (14)| CPF do Estabelecimento, caso pessoa física OU CNPJ, caso pessoa jurídica |
| NIV_DEP| CHAR (1) | Grau de dependência: 1-Individual 3-Mantida|
| CNPJ_MAN | CHAR (14)| CNPJ da mantenedora do Estabelecimento |
| ESFERA_A | CHAR (2) | Código da esfera administrativa|
| ATIVIDAD| CHAR (2) | Código da atividade de ensino|
| RETENCAO| CHAR (2) | Código de retenção de tributos |
| NATUREZA| CHAR (2) | Código da natureza da organização|
| CLIENTEL| CHAR (2) | Código de fluxo da clientela |
| TP_UNID| CHAR (2) | Tipo de unidade (Estabelecimento)|
| TURNO_AT | CHAR (2) | Código de turno de atendimento |
| NIV_HIER | CHAR (2) | Código do nível de hierarquia|
| TERCEIRO| CHAR (1) | O estabelecimento é terceiro: 1-Sim 0-Não 2-não|
| COD_CEP| CHAR (8) | CEP do estabelecimento |
| VINC_SUS | CHAR (2) | Vínculo com SUS: 1-Sim 0-Não |
| TP_PREST | CHAR(2)| Tipo de Prestador|
| SGRUPHAB| CHAR(4)| Código da habilitação|
| CMPT_INI | CHAR(6)| Competência inicial|
| CMPT_FIM | CHAR(6)| Competência final|
| DTPORTAR| CHAR (10)| Data da portaria |
| PORTARIA| CHAR (50)| Portaria |
| MAPORTAR| CHAR (6) | Campo DT_PORTARIA formatado como AAAAMM |
| COMPETEN| CHAR (6) | Ano e Mês de competência da informação (AAAAMM)|
| NAT_JUR| CHAR (4) | Natureza Jurídica|

### Tabela de Estabelecimento Filantropico (EFufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| CNES| CHAR (7) | Número nacional do estabelecimento de saúde |
| CODUFMUN| CHAR (6) | Código do município do estabelecimento UF+ MUNIC (sem dígito) |
| REGSAUDE| CHAR (4) | Código da região de saúde |
| MICR_REG | CHAR (6) | Código da micro-região de saúde|
| DISTRSAN| CHAR (4) | Código do distrito sanitário |
| DISTRADM| CHAR (4) | Código do distrito administrativo|
| TPGESTAO| CHAR (1) | Gestão de saúde|
| PF_PJ| CHAR (1) | Indicador de pessoa: 1-Física 3-Jurídica |
| CPF_CNPJ | CHAR (14)| CPF do Estabelecimento, caso pessoa física OU CNPJ, caso pessoa jurídica |
| NIV_DEP| CHAR (1) | Grau de dependência: 1-Individual 3-Mantida|
| CNPJ_MAN | CHAR (14)| CNPJ da mantenedora do Estabelecimento |
| ESFERA_A | CHAR (2) | Código da esfera administrativa|
| ATIVIDAD| CHAR (2) | Código da atividade de ensino|
| RETENCAO| CHAR (2) | Código de retenção de tributos |
| NATUREZA| CHAR (2) | Código da natureza da organização|
| CLIENTEL| CHAR (2) | Código de fluxo da clientela |
| TP_UNID| CHAR (2) | Tipo de unidade (Estabelecimento)|
| TURNO_AT | CHAR (2) | Código de turno de atendimento |
| NIV_HIER | CHAR (2) | Código do nível de hierarquia|
| TERCEIRO| CHAR (1) | O estabelecimento é terceiro: 1-Sim 0-Não 2-não|
| COD_CEP| CHAR (8) | CEP do estabelecimento |
| VINC_SUS | CHAR (2) | Vínculo com SUS: 1-Sim 0-Não |
| TP_PREST | CHAR(2)| Tipo de Prestador|
| SGRUPHAB| CHAR(4)| Código da habilitação|
| CMPT_INI | CHAR(6)| Competência inicial|
| CMPT_FIM | CHAR(6)| Competência final|
| DTPORTAR| CHAR (10)| Data da portaria |
| PORTARIA| CHAR (50)| Portaria |
| MAPORTAR| CHAR (6) | Campo DT_PORTARIA formatado como AAAAMM |
| COMPETEN| CHAR (6) | Ano e Mês de competência da informação (AAAAMM)|
| NAT_JUR| CHAR (6) | Natureza Jurídica|

### Tabela de IntegraSUS (INufAAmm.dbf)

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| CNES| CHAR (7) | Número nacional do estabelecimento de saúde|
| CODUFMUN| CHAR (6) | Código do município do estabelecimento UF+ MUNIC (sem dígito)|
| REGSAUDE| CHAR (4) | Código da região de saúde|
| MICR_REG | CHAR (6) | Código da micro-região de saúde|
| DISTRSAN| CHAR (4) | Código do distrito sanitário |
| DISTRADM| CHAR (4) | Código do distrito administrativo|
| TPGESTAO| CHAR (1) | Gestão de saúde|
| PF_PJ| CHAR (1) | Indicador de pessoa: 1-Física 3-Jurídica |
| CPF_CNPJ | CHAR (14)| CPF do Estabelecimento, caso pessoa física OU CNPJ, caso pessoa jurídica |
| NIV_DEP| CHAR (1) | Grau de dependência: 1-Individual 3-Mantida|
| CNPJ_MAN | CHAR (14)| CNPJ da mantenedora do Estabelecimento |
| ESFERA_A | CHAR (2) | Código da esfera administrativa|
| ATIVIDAD| CHAR (2) | Código da atividade de ensino|
| RETENCAO| CHAR (2) | Código de retenção de tributos |
| NATUREZA| CHAR (2) | Código da natureza da organização|
| CLIENTEL| CHAR (2) | Código de fluxo da clientela |
| TP_UNID| CHAR (2) | Tipo de unidade (Estabelecimento)|
| TURNO_AT | CHAR (2) | Código de turno de atendimento |
| NIV_HIER | CHAR (2) | Código do nível de hierarquia|
| TERCEIRO| CHAR (1) | O estabelecimento é terceiro: 1-Sim 0-Não 2-não|
| COD_CEP| CHAR (8) | CEP do estabelecimento |
| VINC_SUS | CHAR (2) | Vínculo com SUS: 1-Sim 0-Não |
| TP_PREST | CHAR(2)| Tipo de Prestador|
| SGRUPHAB| CHAR(4)| Código da habilitação|
| CMPT_INI | CHAR(6)| Competência inicial|
| CMPT_FIM | CHAR(6)| Competência final|
| DTPORTAR| CHAR (10)| Data da portaria |
| PORTARIA| CHAR (50)| Portaria |
| MAPORTAR| CHAR (6) | Campo DT_PORTARIA formatado como AAAAMM |
| COMPETEN| CHAR (6) | Ano e Mês de competência da informação (AAAAMM)|

## SIASUS - Sistema de Informações Ambulatoriais do SUS

### PRODUÇÃO AMBULATORIAL: PAUFAAMM.DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| PA_CODUNI | CHAR (7) | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde)6|
| PA_GESTAO | CHAR (6) | Código da Unidade da Federação7 (IBGE) + Código do Município (IBGE) do Gestor, ou UF0000 se o estabelecimento estiver sob Gestão Estadual |
| PA_CONDIC | CHAR (2) | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado|
| PA_UFMUN| CHAR (6) | Unidade da Federação + Código do Município onde está localizado o estabelecimento|
| PA_REGCT| CHAR (4) | Código da Regra Contratual |
| PA_INCOUT | CHAR (4) | Incremento Outros|
| PA_INCURG | CHAR (4) | Incremento Urgência|
| PA_TPUPS| CHAR (2) | Tipo de Estabelecimento|
| PA_TIPPRE | CHAR (2) | Tipo de Prestador|
| PA_MN_IND| CHAR (1) | Estabelecimento Mantido / Individual |
| PA_CNPJCPF| CHAR (14)| CNPJ do Estabelecimento executante |
| PA_CNPJMNT| CHAR (14)| CNPJ da Mantenedora do estabelecimento ou zeros, caso não a tenha|
| PA_CNPJ_CC | CHAR (14)| CNPJ do Órgão que recebeu pela produção por cessão de crédito ou zeros, caso não o tenha |
| PA_MVM| CHAR (6) | Data de Processamento / Movimento (AAAAMM) |
| PA_CMP| CHAR (6) | Data da Realização do Procedimento / Competência (AAAAMM)|
| PA_PROC_ID | CHAR (10)| Código do Procedimento Ambulatorial|
| PA_TPFIN| CHAR (2) | Tipo de Financiamento da produção|
| PA_SUBFIN | CHAR (4) | Subtipo de Financiamento da produção |
| PA_NIVCPL | CHAR (1) | Complexidade do Procedimento|
| PA_DOCORIG| CHAR (1) | Instrumento de Registro (conforme explicado na página 2)|
| PA_AUTORIZ| CHAR (13)| Número da APAC ou número de autorização do BPA-I, conforme o caso. No BPA-I, não é obrigatório, portanto, não é criticado. Lei de formação: UFAATsssssssd, onde: UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito|
| PA_CNSMED | CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do profissional de saúde executante|
| PA_CBOCOD | CHAR (6) | Código da Ocupação do profissional na Classificação Brasileira de Ocupações8 (Ministério do Trabalho) |
| PA_MOTSAI | CHAR (2) | Motivo de saída ou zeros, caso não tenha|
| PA_OBITO| CHAR (1) | Indicador de Óbito (APAC) |
| PA_ENCERR | CHAR (1) | Indicador de Encerramento (APAC)|
| PA_PERMAN | CHAR (1) | Indicador de Permanência (APAC) |
| PA_ALTA | CHAR (1) | Indicador de Alta (APAC)|
| PA_TRANSF | CHAR (1) | Indicador de Transferência (APAC) |
| PA_CIDPRI | CHAR (4) | CID9 Principal (APAC ou BPA-I)|
| PA_CIDSEC | CHAR (4) | CID Secundário (APAC) |
| PA_CIDCAS | CHAR (4) | CID Causas Associadas (APAC)|
| PA_CATEND | CHAR (2) | Caráter de Atendimento (APAC ou BPA-I)|
| PA_IDADE| CHAR (3) | Idade do paciente em anos |
| IDADEMIN | CHAR (3) | Idade mínima do paciente para realização do procedimento|
| IDADEMAX | CHAR (3) | Idade máxima do paciente para realização do procedimento|
| PA_FLIDADE| CHAR (1) | Compatibilidade com a faixa de idade do procedimento (SIGTAP – Sistema de Gerenciamento da Tabela de Procedimentos do SUS): 0 = Idade não exigida; 1 = Idade compatível com o SIGTAP; 2 = Idade fora da faixa do SIGTAP; 3 = Idade inexistente; 4 = Idade EM BRANCO |
| PA_SEXO | CHAR (1) | Sexo do paciente|
| PA_RACACOR| CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação |
| PA_MUNPCN | CHAR (6) | Código da Unidade da Federação + Código do Município de residência do paciente ou do estabelecimento, caso não se tenha a identificação do paciente, o que ocorre no (BPA) |
| PA_QTDPRO | NUMERIC (11) | Quantidade Produzida (APRESENTADA)|
| PA_QTDAPR | NUMERIC (11) | Quantidade Aprovada do procedimento |
| PA_VALPRO | NUMERIC (20,2) | Valor Produzido (APRESENTADO) |
| PA_VALAPR | NUMERIC (20,2) | Valor Aprovado do procedimento|
| PA_UFDIF| CHAR (1) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento:0 = mesma UF; 1 = UF diferente |
| PA_MNDIF| CHAR (1) | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento:0 = mesmo município; 1 = município diferente |
| PA_DIF_VAL | NUMERIC (20,2) | Diferença do Valor Unitário do procedimento praticado na Tabela Unificada com Valor Unitário praticado pelo Gestor da Produção, multiplicado pela Quantidade Aprovada|
| NU_VPA_TOT | NUMERIC (20,2) | Valor Unitário do Procedimento da Tabela VPA|
| NU_PA_TOT| NUMERIC (20,2) | Valor Unitário do Procedimento da Tabela SIGTAP |
| PA_INDICA | CHAR (1) | Indicativo de situação da produção produzida: 0 = não aprovado; 5 = aprovado total; 6 = aprovado parcial |
| PA_CODOCO | CHAR (1) | Código de Ocorrência|
| PA_FLQT | CHAR (1) | Indicador de erro de Quantidade Produzida |
| PA_FLER | CHAR (1) | Indicador de erro de corpo da APAC|
| PA_ETNIA| CHAR (4) | Etnia do paciente |
| PA_VL_CF | NUMERIC (20,2) | Valor do Complemento Federal|
| PA_VL_CL | NUMERIC (20,2) | Valor do Complemento Local|
| PA_VL_INC| NUMERIC (20,2) | Valor do Incremento |
| PA_SRC_C | CHAR(6)| Código do Serviço Especializado / Classificação CBO (de acordo com o CNES)|
| PA_INE| CHAR(10),| Código de Identificação Nacional de Equipes10, para registrar a atuação das equipes na execução de ações de saúde |
| PA_NAT_JUR | CHAR(4)| Código da Natureza Juridica11 |

### AUTORIZAÇÕES DE PROCEDIMENTOS AMBULATORIAIS - APAC

#### LAUDOS DIVERSOS: ADUFAAMM.DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| AP_MVM | CHAR (6) | Data de Processamento / Movimento (AAAAMM)|
| AP_CONDIC| CHAR (2) | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado |
| AP_GESTAO| CHAR (6) | Cód. da Unidade de Federação + Cód. Município de Gestão, ou UF0000 se a Unidade está sob Gestão Estadual|
| AP_CODUNI| CHAR (7) | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde)|
| AP_AUTORIZ | CHAR (13)| Número da APAC. Lei de formação: UFAATsssssssd, onde UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito |
| AP_CMP | CHAR (6) | Data de Atendimento ao paciente / Competência (AAAAMM)|
| AP_PRIPAL| CHAR (10)| Procedimento Principal da APAC|
| AP_VL_AP| NUMERIC (20.2) | Valor Total da APAC Aprovado|
| AP_UFMUN | CHAR (6) | Código da Unidade da Federação + Município do Estabelecimento |
| AP_TPUPS | CHAR (2) | Tipo de Estabelecimento |
| AP_TIPPRE| CHAR (2) | Tipo de Prestador |
| AP_MN_IND | CHAR (1) | Estabelecimento Mantido / Individual|
| AP_CNPJCPF | CHAR (14)| CNPJ do Estabelecimento executante|
| AP_CNPJMNT | CHAR (14)| CNPJ da Mantenedora do estabelecimento ou zeros, caso não a tenha |
| AP_CNSPCN| CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do paciente|
| AP_COIDADE | CHAR (1) | Código da Idade do paciente |
| AP_NUIDADE | CHAR (2) | Número da Idade |
| AP_SEXO| CHAR (1) | Sexo do paciente|
| AP_RACACOR | CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação |
| AP_MUNPCN| CHAR (6) | Código da Unidade de Federação + Código Município de Residência do paciente |
| AP_UFNACIO | CHAR (3) | Código da Nacionalidade do paciente |
| AP_CEPPCN| CHAR (8) | CEP do endereço do paciente |
| AP_UFDIF | CHAR (1) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento: 0 = mesma UF; 1 = UF diferente |
| AP_MNDIF | CHAR (1) | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento: 0 = mesmo município; 1 = município diferente |
| AP_DTINIC| CHAR (8) | Data de INÍCIO validade (AAAAMMDD)|
| AP_DTFIM | CHAR (8) | Data de FIM validade (AAAAMMDD) |
| AP_TPATEN| CHAR (2) | Tipo de Atendimento de APAC |
| AP_TPAPAC| CHAR (1) | Indica se a APAC é 1 - inicial, 2 - continuidade, 3 - única |
| AP_MOTSAI| CHAR (2) | Motivo de Saída e Permanência |
| AP_OBITO | CHAR (1) | Indicador de Óbito|
| AP_ENCERR| CHAR (1) | Indicador de Encerramento |
| AP_PERMAN| CHAR (1) | Indicador de Permanência|
| AP_ALTA| CHAR (1) | Indicador de Alta |
| AP_TRANSF| CHAR (1) | Indicador de Transferência|
| AP_DTOCOR| CHAR (8) | Data de Ocorrência que substitui a data de FIM de validade|
| AP_CODEMI| CHAR (10)| Código do Órgão emissor |
| AP_CATEND| CHAR (2) | Caráter do Atendimento|
| AP_APACANT | CHAR (13)| Número APAC Anterior|
| AP_UNISOL| CHAR (7) | Código CNES do Estabelecimento Solicitante|
| AP_DTSOLIC | CHAR(8)| Data da Solicitação (AAAAMMDD)|
| AP_DTAUT | CHAR(8)| Data da Autorização (AAAAMMDD)|
| AP_CIDCAS| CHAR (4) | CID Causas Associadas |
| AP_CIDPRI| CHAR (4) | CID Principal |
| AP_CIDSEC| CHAR (4) | CID Secundário|
| AP_ETNIA | CHAR (4) | Etnia do paciente |

#### APAC DE  MEDICAMENTOS: AMUFAAMM.DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| AP_MVM| CHAR (6) | Data de Processamento / Movimento (AAAAMM)|
| AP_CONDIC | CHAR (2) | Sigla do Tipo de Gestão na qual Estado ou Município está habilitado |
| AP_GESTAO| CHAR (6) | Código da Unidade de Federação + Código do Município de Gestão, ou UF0000 se o estabelecimento está sob Gestão Estadual|
| AP_CODUNI| CHAR (7) | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde)|
| AP_AUTORIZ | CHAR (13)| Número da APAC. Lei de formação: UFAATsssssssd, onde UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito |
| AP_CMP | CHAR (6) | Data de Atendimento ao paciente / Competência (AAAAMM)|
| AP_PRIPAL| CHAR (10)| Procedimento Principal da APAC|
| AP_VL_AP| NUMERIC (12.2) | Valor Total da APAC Aprovado|
| AP_UFMUN | CHAR (6) | Código da Unidade da Federação + Código do Município do Estabelecimento |
| AP_TPUPS | CHAR (2) | Tipo de Estabelecimento |
| AP_TIPPRE| CHAR (2) | Tipo de Prestador |
| AP_MN_IND | CHAR (1) | Estabelecimento Mantido / Individual|
| AP_CNPJCPF | CHAR (14)| CNPJ do Estabelecimento executante|
| AP_CNPJMNT | CHAR (14)| CNPJ Mantenedora|
| AP_CNSPCN| CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do paciente|
| AP_COIDADE | CHAR (1) | Código da Idade do paciente |
| AP_NUIDADE | CHAR (2) | Número da Idade |
| AP_SEXO| CHAR (1) | Sexo do paciente|
| AP_RACACOR | CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação |
| AP_MUNPCN| CHAR (6) | Código Unidade de Federação + Código do Município de Residência do paciente |
| AP_UFNACIO | CHAR (3) | Código da Nacionalidade do paciente |
| AP_CEPPCN| CHAR (8) | CEP do paciente |
| AP_UFDIF | CHAR (2) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento|
| AP_MNDIF | CHAR (2) | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento|
| AP_DTINIC| CHAR (8) | Data de INÍCIO validade |
| AP_DTFIM | CHAR (8) | Data de FIM validade|
| AP_TPATEN| CHAR (2) | Tipo de Atendimento de APAC |
| AP_TPAPAC| CHAR (1) | Indica se a APAC é 1 - inicial, 2 - continuidade, 3 – única |
| AP_MOTSAI| CHAR (2) | Motivo de Saída e Permanência |
| AP_OBITO | CHAR (1) | Indicador de Óbito|
| AP_ENCERR| CHAR (1) | Indicador de Encerramento |
| AP_PERMAN| CHAR (1) | Indicador de Permanência|
| AP_ALTA| CHAR (1) | Indicador de Alta |
| AP_TRANSF| CHAR (1) | Indicador de Transferência|
| AP_DTOCOR| CHAR (8) | Data de Ocorrência que substitui a data de FIM de validade|
| AP_CODEMI| CHAR (10)| Código do Órgão emissor |
| AP_CATEND| CHAR (2) | Caráter do Atendimento|
| AP_APACANT | CHAR (13)| Número APAC Anterior|
| AP_UNISOL| CHAR (7) | Código do Estabelecimento solicitante no CNES (Cadastro Nacional de Estabelecimentos de Saúde)|
| AP_DTSOLIC | CHAR(8)| Data da Solicitação |
| AP_DTAUT | CHAR(8)| Data da Autorização |
| AP_CIDCAS| CHAR (4) | CID Causas Associadas |
| AP_CIDPRI| CHAR (4) | CID Principal |
| AP_CIDSEC| CHAR (4) | CID Secundário|
| AP_ETNIA | CHAR (4) | Etnia do paciente |
| AM_PESO| CHAR (3) | Peso do paciente em kg|
| AM_ALTURA| CHAR (3) | Altura do paciente em cm|
| AM_TRANSPL | CHAR (1) | Indicador se o paciente fez transplante |
| AM_QTDTRAN | CHAR (2) | Quantidade de Transplantes|
| AM_GESTANT | CHAR (1) | Indicador de Gestante (S = Sim; N = Não)|

#### APAC DE  NEFROLOGIA: ANUFAAMM.DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| AP_MVM| CHAR (6) | Data de Processamento / Movimento (AAAAMM) |
| AP_CONDIC | CHAR (2) | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado|
| AP_GESTAO | CHAR (6) | Código da Unidade de Federação + Código Município de Gestão ou UF0000 se a Unidade está sob Gestão Estadual |
| AP_CODUNI| CHAR (7) | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde)|
| AP_AUTORIZ | CHAR (13)| Número da APAC. Lei de formação: UFAATsssssssd, onde UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito |
| AP_CMP | CHAR (6) | Data de Atendimento ao paciente / Competência (AAAAMM)|
| AP_PRIPAL| CHAR (10)| Procedimento Principal da APAC|
| AP_VL_AP| NUMERIC (20.2) | Valor Total da APAC Aprovado|
| AP_UFMUN | CHAR (6) | Código de Unidade da Federação + Código do Município do Estabelecimento |
| AP_TPUPS | CHAR (2) | Tipo de Estabelecimento |
| AP_TIPPRE| CHAR (2) | Tipo de Prestador |
| AP_MN_IND | CHAR (1) | Estabelecimento Mantido / Individual|
| AP_CNPJCPF | CHAR (14)| CNPJ do Estabelecimento executante|
| AP_CNPJMNT | CHAR (14)| CNPJ MANTENEDORA|
| AP_CNSPCN| CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do paciente|
| AP_COIDADE | CHAR (1) | Código da Idade |
| AP_NUIDADE | CHAR (2) | Número da Idade |
| AP_SEXO| CHAR (1) | Sexo do paciente|
| AP_RACACOR | CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação |
| AP_MUNPCN| CHAR (6) | Código da UF + Código do Município de Residência do paciente|
| AP_UFNACIO | CHAR (3) | Nacionalidade do paciente |
| AP_CEPPCN| CHAR (8) | CEP do paciente |
| AP_UFDIF | CHAR (1) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento (N = não, S = sim)|
| AP_MNDIF | CHAR (1) | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento (N = não, S = sim)|
| AP_DTINIC| CHAR (8) | Data de INÍCIO validade |
| AP_DTFIM | CHAR (8) | Data de FIM validade|
| AP_TPATEN| CHAR (2) | Tipo de Atendimento de APAC |
| AP_TPAPAC| CHAR (1) | Indica se a APAC é 1 - inicial, 2 - continuidade, 3 - única |
| AP_MOTSAI| CHAR (2) | Motivo de Saída e Permanência |
| AP_OBITO | CHAR (1) | Indicador de Óbito|
| AP_ENCERR| CHAR (1) | Indicador de Encerramento |
| AP_PERMAN| CHAR (1) | Indicador de Permanência|
| AP_ALTA| CHAR (1) | Indicador de Alta |
| AP_TRANSF| CHAR (1) | Indicador de Transferência|
| AP_DTOCOR| CHAR (8) | Data de Ocorrência que substitui a data de FIM de validade|
| AP_CODEMI| CHAR (10)| Código do Órgão emissor |
| AP_CATEND| CHAR (2) | Caráter do Atendimento|
| AP_APACANT | CHAR (13)| Número APAC Anterior|
| AP_UNISOL| CHAR (7) | Código do Estabelecimento solicitante no CNES (Cadastro Nacional de Estabelecimentos de Saúde)|
| AP_DTSOLIC | CHAR(8)| Data da Solicitação |
| AP_DTAUT | CHAR(8)| Data da Autorização |
| AP_CIDCAS| CHAR (4) | CID Causas Associadas |
| AP_CIDPRI| CHAR (4) | CID Principal |
| AP_CIDSEC| CHAR (4) | CID Secundário|
| AP_ETNIA | CHAR (4) | Etnia do paciente |
| AN_DTPDR | CHAR (8) | Data (AAAAMMDD) da PRIMEIRA diálise realizada |
| AN_ALTURA| CHAR (3) | Altura do paciente em cm|
| AN_PESO| CHAR (3) | Peso do paciente em kg|
| AN_DIURES| CHAR (4) | Diurese em ml |
| AN_GLICOS| CHAR (4) | Glicose em Mg/dl|
| AN_ACEVAS| CHAR (1) | Acesso Vascular (S = Sim; N = Não)|
| AN_ULSOAB| CHAR (1) | Ultrassonografia Abdominal (S = Sim; N = Não) |
| AN_TRU | CHAR (4) | TRU (taxa de redução de ureia)|
| AN_INTFIS| CHAR (2) | Quantidade de intervenção de Fístula|
| AN_CNCDO | CHAR (1) | Inscrito na lista da CNCDO (S = Sim; N = Não) |
| AN_ALBUMI| CHAR (2) | Albumina em g%|
| AN_HCV | CHAR (1) | Indicativo de presença de Anticorpos de HCV (P = Positivo; N = Negativo)|
| AN_HBSAG | CHAR (1) | Indicativo de HBsAg (P = Positivo; N = Negativo)|
| AN_HIV | CHAR (1) | Indicativo de presença de anticorpos de HIV (P = Positivo; N = Negativo) |
| AN_HB| CHAR (2) | HB em g% |

#### APAC DE  QUIMIOTERAPIA: AQUFAAMM.DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| AP_MVM | CHAR (6) | Data de Processamento / Movimento (AAAAMM)|
| AP_CONDIC| CHAR (2) | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado |
| AP_GESTAO| CHAR (6) | Código da Unidade de Federação + Código Município de Gestão ou UF0000 se a Unidade está sob Gestão Estadual|
| AP_CODUNI| CHAR (7) | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde)|
| AP_AUTORIZ | CHAR (13)| Número da APAC. Lei de formação: UFAATsssssssd, onde UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito |
| AP_CMP | CHAR (6) | Data de Atendimento ao paciente / Competência (AAAAMM)|
| AP_PRIPAL| CHAR (10)| Procedimento Principal da APAC|
| AP_VL_AP| NUMERIC (12.2) | Valor Total da APAC Aprovado|
| AP_UFMUN | CHAR (6) | Código da Unidade da Federação + Código do Município do Estabelecimento |
| AP_TPUPS | CHAR (2) | Tipo de Estabelecimento |
| AP_TIPPRE| CHAR (2) | Tipo de Prestador |
| AP_MN_IND | CHAR (1) | Estabelecimento Mantido / Individual|
| AP_CNPJCPF | CHAR (14)| CNPJ do Estabelecimento executante|
| AP_CNPJMNT | CHAR (14)| CNPJ MANTENEDORA|
| AP_CNSPCN| CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do paciente|
| AP_COIDADE | CHAR (1) | Código da Idade |
| AP_NUIDADE | CHAR (2) | Número da Idade |
| AP_SEXO| CHAR (1) | Sexo do paciente|
| AP_RACACOR | CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação |
| AP_MUNPCN| CHAR (6) | Código da UF + Código do Município de Residência do paciente|
| AP_UFNACIO | CHAR (3) | Nacionalidade do paciente |
| AP_CEPPCN| CHAR (8) | CEP do paciente |
| AP_UFDIF | CHAR (1) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento (N = não, S = sim)|
| AP_MNDIF | CHAR (1) | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento (N = não, S = sim)|
| AP_DTINIC| CHAR (8) | Data de INÍCIO validade |
| AP_DTFIM | CHAR (8) | Data de FIM validade|
| AP_TPATEN| CHAR (2) | Tipo de Atendimento de APAC |
| AP_TPAPAC| CHAR (1) | Indica se a APAC é 1 - inicial, 2 - continuidade, 3 - única |
| AP_MOTSAI| CHAR (2) | Motivo de Saída e Permanência |
| AP_OBITO | CHAR (1) | Indicador de Óbito|
| AP_ENCERR| CHAR (1) | Indicador de Encerramento |
| AP_PERMAN| CHAR (1) | Indicador de Permanência|
| AP_ALTA| CHAR (1) | Indicador de Alta |
| AP_TRANSF| CHAR (1) | Indicador de Transferência|
| AP_DTOCOR| CHAR (8) | Data de Ocorrência que substitui a data de FIM de validade|
| AP_CODEMI| CHAR (10)| Código do Órgão emissor |
| AP_CATEND| CHAR (2) | Caráter do Atendimento|
| AP_APACANT | CHAR (13)| Número APAC Anterior|
| AP_UNISOL| CHAR (7) | Código do Estabelecimento solicitante no CNES (Cadastro Nacional de Estabelecimentos de Saúde)|
| AP_DTSOLIC | CHAR(8)| Data da Solicitação |
| AP_DTAUT | CHAR(8)| Data da Autorização |
| AP_CIDCAS| CHAR (4) | CID Causas Associadas |
| AP_CIDPRI| CHAR (4) | CID Principal |
| AP_CIDSEC| CHAR (4) | CID Secundário|
| AP_ETNIA | CHAR (4) | Etnia do paciente |
| AQ_CID10 | CHAR (4) | CID 10 – Topografia |
| AQ_LINFIN| CHAR (1) | Linfonodos regionais invadidos (S = Sim; N = Não; 3 = Não Avaliáveis) |
| AQ_ESTADI| CHAR (1) | Estádio - UICC (0; 1; 2; 3; 4)|
| AQ_GRAHIS | CHAR (2) | Grau Histopatológico|
| AQ_DTIDEN | CHAR (8) | Data da identificação patológica do caso (AAAAMMDD) |
| AQ_TRANTE | CHAR (1) | Tratamentos anteriores (S = Sim; N = Não) |
| AQ_CIDINI1| CHAR (4) | CID 1º Tratamento anterior|
| AQ_DTINI1 | CHAR (8) | Data de início (AAAAMMDD) 1º tratamento anterior|
| AQ_CIDINI2| CHAR (4) | CID 2º Tratamento anterior|
| AQ_DTINI2 | CHAR (8) | Data de início (AAAAMMDD) 2º tratamento anterior|
| AQ_CIDINI3| CHAR (4) | CID 3º Tratamento anterior|
| AQ_DTINI3 | CHAR (8) | Data de início (AAAAMMDD) 3º tratamento anterior|
| AQ_CONTTR | CHAR (1) | Continuidade do tratamento (S = Sim; N = Não) |
| AQ_DTINTR | CHAR (8) | Data de INÍCIO do tratamento solicitado (AAAAMMDD)|
| AQ_ESQU_P1 | CHAR (5) | ESQUEMA (Sigla ou abrev.) - 5 primeiras posições|
| AQ_TOTMPL | CHAR (3) | Total de MESES Planejados |
| AQ_TOTMAU | CHAR (3) | Total de MESES Autorizados|
| AQ_ESQU_P2 | CHAR (10)| ESQUEMA (Sigla ou abrev.) - 10 últimas posições |
| AP_NATJUR | CHAR (4) | Código da Natureza Jurídica |

#### APAC DE  RADIOTERAPIA: ARUFAAMM.DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| AP_MVM | CHAR (6) | Data de Processamento / Movimento (AAAAMM) |
| AP_CONDIC| CHAR (2) | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado|
| AP_GESTAO| CHAR (6) | Código da Unidade de Federação + Código Município de Gestão ou UF0000 se a Unidade está sob Gestão Estadual |
| AP_CODUNI| CHAR (7) | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde) |
| AP_AUTORIZ | CHAR (13)| Número da APAC. Lei de formação: UFAATsssssssd, onde: UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito |
| AP_CMP | CHAR (6) | Data de Atendimento ao paciente / Competência (AAAAMM) |
| AP_PRIPAL| CHAR (10)| Procedimento Principal da APAC |
| AP_VL_AP| NUMERIC (20.2) | Valor Total da APAC Aprovado |
| AP_UFMUN | CHAR (6) | Código da Unidade da Federação + Código do Município do Estabelecimento|
| AP_TPUPS | CHAR (2) | Tipo de Estabelecimento|
| AP_TIPPRE| CHAR (2) | Tipo de Prestador|
| AP_MN_IND | CHAR (1) | Estabelecimento Mantido / Individual |
| AP_CNPJCPF | CHAR (14)| CNPJ do Estabelecimento executante |
| AP_CNPJMNT | CHAR (14)| CNPJ MANTENEDORA |
| AP_CNSPCN| CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do paciente |
| AP_COIDADE | CHAR (1) | Código da Idade|
| AP_NUIDADE | CHAR (2) | Número da Idade|
| AP_SEXO| CHAR (1) | Sexo do paciente |
| AP_RACACOR | CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação|
| AP_MUNPCN| CHAR (6) | Código da UF + Código do Município de Residência do paciente |
| AP_UFNACIO | CHAR (3) | Nacionalidade do paciente|
| AP_CEPPCN| CHAR (8) | CEP do paciente|
| AP_UFDIF | CHAR (2) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento (N = não, S = sim)|
| AP_MNDIF | CHAR (1) | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento (N \= não, S = sim)|
| AP_DTINIC| CHAR (8) | Data de INÍCIO validade|
| AP_DTFIM | CHAR (8) | Data de FIM validade |
| AP_TPATEN| CHAR (2) | Tipo de Atendimento de APAC|
| AP_TPAPAC| CHAR (1) | Indica se a APAC é 1 - inicial, 2 - continuidade, 3 - única|
| AP_MOTSAI| CHAR (2) | Motivo de Saída e Permanência|
| AP_OBITO | CHAR (1) | Indicador de Óbito |
| AP_ENCERR| CHAR (1) | Indicador de Encerramento|
| AP_PERMAN| CHAR (1) | Indicador de Permanência |
| AP_ALTA| CHAR (1) | Indicador de Alta|
| AP_TRANSF| CHAR (1) | Indicador de Transferência |
| AP_DTOCOR| CHAR (8) | Data de Ocorrência que substitui a data de FIM de validade |
| AP_CODEMI| CHAR (10)| Código do Órgão emissor |
| AP_CATEND| CHAR (2) | Caráter do Atendimento|
| AP_APACANT | CHAR (13)| Número APAC Anterior|
| AP_UNISOL| CHAR (7) | Código CNES do Estabelecimento Solicitante|
| AP_DTSOLIC | CHAR (8) | Data da Solicitação |
| AP_DTAUT | CHAR (8) | Data da Autorização |
| AP_CIDCAS| CHAR (4) | CID Causas Associadas |
| AP_CIDPRI| CHAR (4) | CID Principal |
| AP_CIDSEC| CHAR (4) | CID Secundário|
| AP_ETNIA | CHAR (4) | Etnia do paciente |
| AR_SMRD| CHAR (3) | |
| AR_CID10 | CHAR (4) | CID-10 - Topografia |
| AR_LINFIN| CHAR (1) | Linfonodos regionais invadidos (S = Sim; N =Não; 3= Não Avaliáveis) |
| AR_ESTADI| CHAR (1) | Estádio - UICC (0; 1; 2; 3; 4)|
| AR_GRAHIS| CHAR (2) | Grau Histopatológico|
| AR_DTIDEN| CHAR (8) | Data da identificação patológica do caso (AAAAMMDD) |
| AR_TRANTE| CHAR (1) | Tratamentos anteriores (S = Sim; N = Não) |
| AR_CIDINI1 | CHAR (4) | CID 1º Tratamento anterior|
| AR_DTINI1| CHAR (8) | Data de INÍCIO (AAAAMMDD) 1º tratamento anterior|
| AR_CIDINI2 | CHAR (4) | CID 2º Tratamento anterior|
| AR_DTINI2| CHAR (8) | Data de INÍCIO (AAAAMMDD) 2º tratamento anterior|
| AR_CIDINI3 | CHAR (4) | CID 3º Tratamento anterior|
| AR_DTINI3| CHAR (8) | Data de início (AAAAMMDD) 3º tratamento anterior|
| AR_CONTTR| CHAR (1) | Continuidade do tratamento (S = Sim; N = Não) |
| AR_DTINTR| CHAR (8) | Data de INÍCIO do tratamento solicitado (AAAAMMDD)|
| AR_FINALI| CHAR (1) | Finalidade do Tratamento: (1 = RADICAL; 2 = ADJUVANTE; 3 = ANTIÁLGICA; 4 = PALIATIVA; 5 = PRÉVIA; 6 = ANTIHEMORRÁGICA) |
| AR_CIDTR1| CHAR (4) | CID Topográfico 1º|
| AR_CIDTR2| CHAR (4) | CID Topográfico 2º|
| AR_CIDTR3| CHAR (4) | CID Topográfico 3º|
| AR_NUMC1 | CHAR (3) | Nº Campo/Inserções 1º |
| AR_INIAR1| CHAR (8) | Data de INÍCIO 1º (AAAAMMDD)|
| AR_INIAR2| CHAR (8) | Data de INÍCIO 2º (AAAAMMDD)|
| AR_INIAR3| CHAR (8) | Data de INÍCIO 3º (AAAAMMDD)|
| AR_FIMAR1| CHAR (8) | Data de Fim 1º (AAAAMMDD) |
| AR_FIMAR2| CHAR (8) | Data de FIM 2º (AAAAMMDD) |
| AR_FIMAR3| CHAR (8) | Data de Fim 3º (AAAAMMDD) |
| AR_NUMC2 | CHAR (3) | Nº Campo/Inserções 2º |
| AR_NUMC3 | CHAR (3) | Nº Campo/Inserções 3º |
| AP_NATJUR| CHAR (4) | Código da Natureza Jurídica |

#### APAC DE  CIRURGIA BARIÁTRICA: ABUFMM.DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| AP_MVM | CHAR (6) | Data de Processamento / Movimento (AAAAMM) |
| AP_CONDIC| CHAR (2) | Sigla do Tipo de Gestão na qual o Estado ou Município está habilitado|
| AP_GESTAO| CHAR (6) | Código da Unidade de Federação + Código Município de Gestão ou UF0000 se a Unidade está sob Gestão Estadual |
| AP_CODUNI| CHAR (7) | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde) |
| AP_AUTORIZ | CHAR (13)| Número da APAC. Lei de formação: UFAATsssssssd, onde: UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito |
| AP_CMP | CHAR (6) | Data de Atendimento ao paciente / Competência (AAAAMM) |
| AP_PRIPAL| CHAR (10)| Procedimento Principal da APAC |
| AP_VL_AP| NUMERIC (20.2) | Valor Total da APAC Aprovado |
| AP_UFMUN | CHAR (6) | Código da Unidade da Federação + Código do Município do Estabelecimento|
| AP_TPUPS | CHAR (2) | Tipo de Estabelecimento|
| AP_TIPPRE| CHAR (2) | Tipo de Prestador|
| AP_MN_IND | CHAR (1) | Estabelecimento Mantido / Individual |
| AP_CNPJCPF | CHAR (14)| CNPJ do Estabelecimento executante |
| AP_CNPJMNT | CHAR (14)| CNPJ MANTENEDORA |
| AP_CNSPCN| CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do paciente |
| AP_COIDADE | CHAR (1) | Código da Idade|
| AP_NUIDADE | CHAR (2) | Número da Idade|
| AP_SEXO| CHAR (1) | Sexo do paciente |
| AP_RACACOR | CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação |
| AP_MUNPCN| CHAR (6) | Código da UF + Código do Município de Residência do paciente |
| AP_UFNACIO | CHAR (3) | Nacionalidade do paciente|
| AP_CEPPCN| CHAR (8) | CEP do paciente|
| AP_UFDIF | CHAR (1) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento (N=não, S=sim) |
| AP_MNDIF | CHAR (1) | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento (N=não, S=sim) |
| AP_DTINIC| CHAR (8) | Data de INÍCIO validade|
| AP_DTFIM | CHAR (8) | Data de FIM validade |
| AP_TPATEN| CHAR (2) | Tipo de Atendimento de APAC|
| AP_TPAPAC| CHAR (1) | Indica se a APAC é 1 - inicial, 2 - continuidade, 3 - única|
| AP_MOTSAI| CHAR (2) | Motivo de Saída e Permanência|
| AP_OBITO | CHAR (1) | Indicador de Óbito |
| AP_ENCERR| CHAR (1) | Indicador de Encerramento|
| AP_PERMAN| CHAR (1) | Indicador de Permanência |
| AP_ALTA| CHAR (1) | Indicador de Alta|
| AP_TRANSF| CHAR (1) | Indicador de Transferência |
| AP_DTOCOR| CHAR (8) | Data de Ocorrência que substitui a data de FIM de validade |
| AP_CODEMI| CHAR (10)| Código do Órgão emissor|
| AP_CATEND| CHAR (2) | Caráter do Atendimento |
| AP_APACANT | CHAR (13)| Número APAC Anterior |
| AP_UNISOL| CHAR (7) | Código CNES do Estabelecimento Solicitante |
| AP_DTSOLIC | CHAR(8)| Data da Solicitação|
| AP_DTAUT | CHAR(8)| Data da Autorização|
| AP_CIDCAS| CHAR (4) | CID Causas Associadas|
| AP_CIDPRI| CHAR (4) | CID Principal|
| AP_CIDSEC| CHAR (4) | CID Secundário |
| AP_ETNIA | CHAR (4) | Etnia do paciente|
| AB_IMC | CHAR (3) | IMC do paciente|
| AB_PROCAIH | CHAR (10)| Procedimento do AIH|
| AB_DTCIRUR | CHAR (8) | Data da Cirurgia |
| AB_NUMAIH| CHAR (13)| Número da AIH|
| AB_PRCAIH2 | CHAR (10)| Procedimento do AIH|
| AB_PRCAIH3 | CHAR (10)| Procedimento do AIH|
| AB_NUMAIH2 | CHAR (13)| Número da AIH|
| AB_DTCIRG2 | CHAR (8) | Data da Cirurgia |
| AB_MESACOM | CHAR (2) | Número em MESES de Acompanhamento|
| AB_ANOACOM | CHAR (4) | Ano de Acompanhamento|
| AB_PONTBAR | CHAR (1) | Pontuação de Baros12 |
| AB_TABBARR | CHAR (1) | Tabela de Baros|
| AP_NATJUR| CHAR(4)| Código da Natureza Jurídica|

#### APAC DE CONFECÇÃO DE FÍSTULA ARTERIOVENOSA: ACFUFMM.DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| AP_MVM | CHAR (6) | Data de Processamento / Movimento (AAAAMM)|
| AP_CONDIC| CHAR (2) | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado |
| AP_GESTAO| CHAR (6) | Código da Unidade de Federação + Código Município de Gestão ou UF0000 se a Unidade está sob Gestão Estadual|
| AP_CODUNI| CHAR (7) | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde)|
| AP_AUTORIZ | CHAR (13)| Número da APAC. Lei de formação: UFAATsssssssd, onde UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito |
| AP_CMP | CHAR (6) | Data de Atendimento ao paciente / Competência (AAAAMM)|
| AP_PRIPAL| CHAR (10)| Procedimento Principal da APAC|
| AP_VL_AP| NUMERIC (20.2) | Valor Total da APAC Aprovado|
| AP_UFMUN | CHAR (6) | Código da Unidade da Federação + Código do Município do Estabelecimento |
| AP_TPUPS | CHAR (2) | Tipo de Estabelecimento |
| AP_TIPPRE| CHAR (2) | Tipo de Prestador |
| AP_MN_IND | CHAR (1) | Estabelecimento Mantido / Individual|
| AP_CNPJCPF | CHAR (14)| CNPJ do Estabelecimento executante|
| AP_CNPJMNT | CHAR (14)| CNPJ MANTENEDORA|
| AP_CNSPCN| CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do paciente|
| AP_COIDADE | CHAR (1) | Código da Idade |
| AP_NUIDADE | CHAR (2) | Número da Idade |
| AP_SEXO| CHAR (1) | Sexo do paciente|
| AP_RACACOR | CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação |
| AP_MUNPCN| CHAR (6) | Código da UF + Código do Município de Residência do paciente|
| AP_UFNACIO | CHAR (3) | Nacionalidade do paciente |
| AP_CEPPCN| CHAR (8) | CEP do paciente |
| AP_UFDIF | CHAR (1) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento (N = não, S = sim)|
| AP_MNDIF | CHAR (1) | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento (N = não, S = sim)|
| AP_DTINIC| CHAR (8) | Data de INÍCIO validade |
| AP_DTFIM | CHAR (8) | Data de FIM validade|
| AP_TPATEN| CHAR (2) | Tipo de Atendimento de APAC |
| AP_TPAPAC| CHAR (1) | Indica se a APAC é 1 – inicial, 2 – continuidade, 3 – única |
| AP_MOTSAI| CHAR (2) | Motivo de Saída e Permanência |
| AP_OBITO | CHAR (1) | Indicador de Óbito|
| AP_ENCERR| CHAR (1) | Indicador de Encerramento |
| AP_PERMAN| CHAR (1) | Indicador de Permanência|
| AP_ALTA| CHAR (1) | Indicador de Alta |
| AP_TRANSF| CHAR (1) | Indicador de Transferência|
| AP_DTOCOR| CHAR (8) | Data de Ocorrência que substitui a data de FIM de validade|
| AP_CODEMI| CHAR (10)| Código do Órgão emissor |
| AP_CATEND| CHAR (2) | Caráter do Atendimento|
| AP_APACANT | CHAR (13)| Número APAC Anterior|
| AP_UNISOL| CHAR (7) | Código do Estabelecimento Solicitante no CNES (Cadastro Nacional de Estabelecimentos de Saúde)|
| AP_DTSOLIC | CHAR(8)| Data da Solicitação |
| AP_DTAUT | CHAR(8)| Data da Autorização |
| AP_CIDCAS| CHAR (4) | CID Causas Associadas |
| AP_CIDPRI| CHAR (4) | CID Principal |
| AP_CIDSEC| CHAR (4) | CID Secundário|
| AP_ETNIA | CHAR (4) | Etnia do paciente |
| ACF_DUPLEX | CHAR (1) | Duplex prévio (S - Sim, N - Não)|
| ACF_USOCAT | CHAR (1) | Uso do cateter venoso ou outros acessos venosos prévios (S - Sim, N - Não)|
| ACF_PREFAV | CHAR (1) | FAV prévia (S - Sim, N - Não) |
| ACF_FLEBIT | CHAR (1) | Flebites (S - Sim, N - Não) |
| ACF_HEMATO | CHAR (1)| Hematomas (S - Sim, N - Não) |
| ACF_VEIAVI | CHAR (1)| Veia visível (S - Sim, N - Não)|
| ACF_PULSO| CHAR (1)| Presença de pulso (S - Sim, N - Não) |
| ACF_VEIDIA | NUMERIC(4)| Diâmetro da veia (em mm) |
| ACF_ARTDIA | NUMERIC (4) | Diâmetro da artéria (em mm)|
| ACF_FREMIT | CHAR(1) | Frêmito - Vibração perceptível pelo tato |
| AP_NATJUR| CHAR(4) | Código da Natureza Jurídica|

#### APAC DE  TRATAMENTO DIALÍTICO: ATDUFMM.DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| AP_MVM | CHAR (6) | Data de Processamento / Movimento (AAAAMM)|
| AP_CONDIC| CHAR (2) | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado |
| AP_GESTAO| CHAR (6) | Código da Unidade de Federação + Código Município de Gestão ou UF0000 se a Unidade está sob Gestão Estadual|
| AP_CODUNI| CHAR (7) | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde)|
| AP_AUTORIZ | CHAR (13)| Número da APAC. Lei de formação: UFAATsssssssd, onde UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito |
| AP_CMP | CHAR (6) | Data de Atendimento ao paciente / Competência (AAAAMM)|
| AP_PRIPAL| CHAR (10)| Procedimento Principal da APAC|
| AP_VL_AP| NUMERIC (20.2) | Valor Total da APAC Aprovado|
| AP_UFMUN | CHAR (6) | Código da Unidade da Federação + Código do Município do Estabelecimento |
| AP_TPUPS | CHAR (2) | Tipo de Estabelecimento |
| AP_TIPPRE| CHAR (2) | Tipo de Prestador |
| AP_MN_IND | CHAR (1) | Estabelecimento Mantido / Individual|
| AP_CNPJCPF | CHAR (14)| CNPJ do Estabelecimento executante|
| AP_CNPJMNT | CHAR (14)| CNPJ MANTENEDORA|
| AP_CNSPCN| CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do paciente|
| AP_COIDADE | CHAR (1) | Código da Idade |
| AP_NUIDADE | CHAR (2) | Número da Idade |
| AP_SEXO| CHAR (1) | Sexo do paciente|
| AP_RACACOR | CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação |
| AP_MUNPCN| CHAR (6) | Código da UF + Código do Município de Residência do paciente|
| AP_UFNACIO | CHAR (3) | Nacionalidade do paciente |
| AP_CEPPCN| CHAR (8) | CEP do paciente |
| AP_UFDIF | CHAR (1) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento (N - não, S - sim) |
| AP_MNDIF | CHAR (1) | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento (N - não, S - sim)|
| AP_DTINIC| CHAR (8) | Data de INÍCIO validade |
| AP_DTFIM | CHAR (8) | Data de FIM validade|
| AP_TPATEN| CHAR (2) | Tipo de Atendimento de APAC |
| AP_TPAPAC| CHAR (1) | Indica se a APAC é 1 – inicial, 2 – continuidade, 3 – única |
| AP_MOTSAI| CHAR (2) | Motivo de Saída e Permanência |
| AP_OBITO | CHAR (1) | Indicador de Óbito|
| AP_ENCERR| CHAR (1) | Indicador de Encerramento |
| AP_PERMAN| CHAR (1) | Indicador de Permanência|
| AP_ALTA| CHAR (1) | Indicador de Alta |
| AP_TRANSF| CHAR (1) | Indicador de Transferência|
| AP_DTOCOR| CHAR (8) | Data de Ocorrência que substitui a data de FIM de validade|
| AP_CODEMI| CHAR (10)| Código do Órgão emissor |
| AP_CATEND| CHAR (2) | Caráter do Atendimento|
| AP_APACANT | CHAR (13)| Número APAC Anterior|
| AP_UNISOL| CHAR (7) | Código CNES do Estabelecimento Solicitante|
| AP_DTSOLIC | CHAR(8)| Data da Solicitação |
| AP_DTAUT | CHAR(8)| Data da Autorização |
| AP_CIDCAS| CHAR (4) | CID Causas Associadas |
| AP_CIDPRI| CHAR (4) | CID Principal |
| AP_CIDSEC| CHAR (4) | CID Secundário|
| AP_ETNIA | CHAR (4) | Etnia do paciente |
| ATD_CARACT | CHAR (1) | Característica do tratamento|
| ATD_DTPDR| CHAR (8) | Data (AAAAMMDD) do início da primeira dialise |
| ATD_DTCLI| CHAR (8) | Data (AAAAMMDD) do início da dialise nesta clinica|
| ATD_ACEVAS | CHAR (1) | Acesso Vascular |
| ATD_MAISNE | CHAR (1) | Acompanhado há mais de um ano com nefrologia (S - Sim, N - Não, I - Ignorado) |
| ATD_SITINI | CHAR (1) | Situação Inicial|
| ATD_SITTRA | CHAR (1) | Situação de transplante (1 - Apto, 2 - Inapto, 3 - Recusa, 4 - N/A caso novo, com menos de 90 dias de tratamento) |
| ATD_SEAPTO | CHAR (1) | Se Apto a transplante (1 - Inscrito na CNCDO, 2 - Em processo de avaliação transplantante no centro transplantador, 3 - Sem encaminhamento, 4 - Aguardando agendamento de consulta no centro transplantador) |
| ATD_HB | CHAR (4) | HB (hemoglobina)|
| ATD_FOSFOR | CHAR (4) | Fósforo |
| ATD_KTVSEM | CHAR (4) | Kt/v Semanal|
| ATD_TRU| CHAR (4) | TRU (taxa de redução de ureia)|
| ATD_ALBUMI | CHAR (4) | Albumina|
| ATD_PTH| CHAR (4) | PTH (hormônio da paratireoide)|
| ATD_HIV| CHAR (1) | Indicativo de presença de anticorpos de HIV (P - Positivo; N - Negativo)|
| ATD_HCV| CHAR (1) | Indicativo de presença de anticorpos de HCV (P - Positivo; N - Negativo)|
| ATD_HBSAG| CHAR (1) | Indicativo de HBsAg (P - Positivo; N - Negativo)|
| ATD_INTERC | CHAR (1) | Usuário internado, com data de início no mês vigente, para tratamento de intercorrência clínica? (S – Sim, N - Não, I - Ignorado)|
| ATD_SEPERI | CHAR (1) | Se em Diálise Peritoneal, houve peritonite diagnosticada no mês vigente? (S - Sim, N - Não, I - Ignorado) |
| AP_NATJUR| CHAR (4) | Código da Natureza Jurídica |

### AMBULATORIAIS DE SAÚDE - RAAS

#### ATENÇÃO DOMICILIAR: SAD*. DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| CNES_EXEC | CHAR (7) | Código do SCNES do Estabelecimento de Saúde |
| GESTAO | CHAR (6) | Unidade da Federação + Código do Município do Gestor, ou UF0000 se a Unidade está sob Gestão Estadual |
| CONDIC | CHAR (2) | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado |
| UFMUN| CHAR (6) | Unidade da Federação + município onde está localizado o Estabelecimento |
| TPUPS| CHAR (2) | Tipo de do Estabelecimento|
| MN_IND| CHAR (1) | Estabelecimento Mantido / Individual|
| CNPJCPF| CHAR (14)| CNPJ do Estabelecimento executante|
| CNPJMNT| CHAR (14)| CNPJ da Mantenedora do Estabelecimento ou zeros, caso não a tenha |
| DT_PROCESS| CHAR (6) | Mês de Processamento (AAAAMM) |
| DT_ATEND| CHAR (6) | Mês do Atendimento (AAAAMM) |
| CNS_PAC | CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do paciente (criptografia) |
| DTNASC | CHAR (8) | Data de nascimento do paciente|
| TPIDADEPAC | CHAR (1) | Tipo da Idade do paciente em anos, meses ou dias. Calculado a partir da data de nascimento|
| IDADEPAC | CHAR (2) | Idade do paciente |
| NACION_PAC| CHAR(2)| Nacionalidade do paciente |
| SEXOPAC| CHAR (1) | Sexo do paciente|
| RACACOR| CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação |
| ETNIA| CHAR (4) | Etnia do paciente (Caso seja da Raça/Cor Indígena)|
| MUNPAC | CHAR (6) | Unidade da Federação + município do município de residência do paciente |
| MOT_COB | CHAR (2) | Motivo de Saída/Permanência |
| DT_MOTCOB | CHAR (8) | Data da ocorrência no caso de alta, transferência ou óbito|
| CATEND | CHAR (2) | Caráter de Atendimento|
| CIDPRI | CHAR (4) | CID Principal |
| CIDASSOC | CHAR (4) | CID Causas Associadas |
| ORIGEM_PAC| CHAR (2) | Origem do paciente|
| DT_INÍCIO | CHAR (8) | Data de Início|
| DT_FIM| CHAR (8) | Data de Fim |
| COB_ESF | CHAR (1) | Indica se a região de atendimento do paciente tem cobertura de Estratégia Saúde da Família|
| CNES_ESF| CHAR (7) | Código do SCNES do Estabelecimento de Saúde Unidade da Saúde da Família da região |
| DESTINO_PAC | CHAR (2) | Destino do paciente |
| PA_PROC_ID | CHAR (10)| Código de Procedimento Ambulatorial |
| PA_QTDPRO | NUMERIC (11) | Quantidade Produzida (APRESENTADA)|
| PA_QTDAPR| NUMERIC (11) | Quantidade aprovada do procedimento|
| PA_SRV | CHAR (4) | Serviço Especializado|
| PA_CLAS_S | CHAR (4) | Classificação do Serviço |
| PA_EQUIPE| CHAR (12)| Código da Equipe (somente para o Instrumento de registro RAAS) |
| PA_TP_EQP | CHAR(2)| Tipo de Equipe (somente para o Instrumento de registro RAAS) |
| PA_CID | CHAR (4) | CID do Procedimento|
| DT_INICIO| CHAR (8) | Data de Início do Atendimento (DDMMAAAA) |
| DT_FIM | CHAR (8) | Data de Fim do Atendimento (DDMMAAAA)|
| PERMANENCIA | CHAR (4) | Permanência em Atendimento |
| QTDATE| CHAR (4) | Quantidade de Atendimentos |
| QTDPCN| CHAR (4) | Quantidade de pacientes|

#### PSICOSSOCIAL: PS*.DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| CNES_EXEC | CHAR (7) | Código do SCNES do Estabelecimento de Saúde |
| GESTAO | CHAR (6) | Unidade da Federação + Código do Município do Gestor, ou UF0000 se a Unidade está sob Gestão Estadual |
| CONDIC | CHAR (2) | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado |
| UFMUN| CHAR (6) | Unidade da Federação + município onde está localizado o Estabelecimento |
| TPUPS| CHAR (2) | Tipo de do Estabelecimento|
| TIPPRE | CHAR (2) | Tipo de Prestador |
| MN_IND| CHAR (1) | Estabelecimento Mantido / Individual|
| CNPJCPF| CHAR (14)| CNPJ do Estabelecimento executante|
| CNPJMNT| CHAR (14)| CNPJ da Mantenedora do Estabelecimento ou zeros, caso não a tenha |
| DT_PROCESS| CHAR (14)| Data de Processamento (AAAAMM)|
| DT_ATEND| CHAR (6) | Data do Atendimento (AAAAMM)|
| CNS_PAC | CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do paciente (criptografia) |
| DTNASC | CHAR (8) | Data de nascimento do paciente|
| TPIDADEPAC | CHAR (1) | Tipo da Idade do paciente em anos, meses ou dias. Calculado a partir da data de nascimento|
| IDADEPAC | CHAR (2) | Idade do paciente |
| NACION_PAC| CHAR (2) | Nacionalidade do paciente |
| SEXOPAC| CHAR (1) | Sexo do paciente|
| RACACOR| CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação |
| ETNIA| CHAR (4) | Etnia do paciente (Caso seja da Raça/Cor Indígena)|
| MUNPAC | CHAR (6) | Unidade da Federação + município do município de residência do paciente |
| MOT_COB | CHAR (2) | Motivo de Saída/Permanência |
| DT_MOTCOB | CHAR (8) | Data da ocorrência no caso de alta, transferência ou óbito|
| CATEND | CHAR (2) | Caráter de Atendimento|
| CIDPRI | CHAR (4) | CID Principal |
| CIDASSOC | CHAR (4) | CID Causas Associadas |
| ORIGEM_PAC| CHAR (2) | Origem do paciente|
| DT_INICIO | CHAR (8) | Data de Início|
| DT_FIM| CHAR (8) | Data de Fim |
| COB_ESF | CHAR (1) | Indica se a região de atendimento do paciente tem cobertura de Estratégia Saúde da Família|
| CNES_ESF| CHAR (7) | Código do SCNES do Estabelecimento de Saúde Unidade da Saúde da Família da região |
| DESTINOPAC | CHAR (2) | Destino do paciente |
| PA_PROC_ID | CHAR(10) | Ação Realizada|
| QT_APRES| NUMERIC (11) | Quantidade Apresentada|
| QT_APROV| NUMERIC (11) | Quantidade Aprovada |
| SERV | CHAR (3) | Código do Serviço Especializado |
| CLASS| CHAR (3) | Código da Classificação do Serviço|
| SIT_RUA | CHAR (1) | Situação de Rua (S- SIM, N - NÃO) |
| TP_DROGA| CHAR (3) | TIPO DE DROGA (A - Álcool, C - Crack, O - Outros) |
| LOC_REALIZ| CHAR (1) | Local de Realização (C – CAPS, T - Território)|
| INICIO | CHAR (8) | Data de Início do Atendimento (DDMMAAAA)|
| FIM| CHAR (8) | Data de Fim do Atendimento (DDMMAAAA) |
| PERMANEN | CHAR (4) | Permanência em Atendimento|
| QTDATE | CHAR (4) | Quantidade de Atendimentos|
| QTDPCN | CHAR (4) | Quantidade de pacientes |

### BOLETIM DE PRODUÇÃO AMBULATORIAL INDIVIDUALIZADO – BPA-I

#### DE BPA-I: BIUFAAMM.DBF

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| CODUNI| CHAR (7) | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde) |
| GESTAO| CHAR (6) | Código da Unidade da Federação + Código do Município (IBGE) do Gestor, ou UF0000 se o estabelecimento estiver sob Gestão Estadual |
| CONDIC| CHAR (2) | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado|
| UFMUN | CHAR (6) | Código da Unidade da Federação + Código do Município onde está localizado o estabelecimento|
| TPUPS | CHAR (2) | Tipo de do Estabelecimento |
| TIPPRE| CHAR (2) | Tipo de Prestador|
| MN_IND | CHAR (1) | Estabelecimento Mantido / Individual |
| CNPJCPF | CHAR (14)| CNPJ do Estabelecimento executante |
| CNPJMNT | CHAR (14)| CNPJ da Mantenedora do estabelecimento ou zeros, caso não a tenha|
| CNPJ_CC| CHAR (14)| CNPJ do Órgão que recebeu pela produção por cessão de crédito ou zeros, caso não o tenha |
| DT_PROCESS | CHAR (6) | Ano e mês de Processamento da produção (AAAAMM)|
| DT_ATEND | CHAR (6) | Ano e mês do Atendimento (AAAAMM)|
| PROC_ID| CHAR (10)| Código do Procedimento Ambulatorial|
| TPFIN | CHAR (2) | Tipo de Financiamento da produção|
| SUBFIN| CHAR (4) | Subtipo de Financiamento da produção |
| COMPLEX | CHAR (1) | Complexidade do Procedimento |
| AUTORIZ | CHAR (13)| Número da APAC ou número de autorização do BPA-I, conforme o caso. No BPA-I, não é obrigatório, portanto, não é criticado. Lei de formação: UFAATsssssssd, onde: UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito. |
| CNSPROF | CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do profissional de saúde executante |
| CBOPROF | CHAR (6) | Código da Ocupação do profissional na Classificação Brasileira de Ocupações (Ministério do Trabalho) |
| CIDPRI| CHAR (4) | CID Principal|
| CATEND| CHAR (2) | Caráter de Atendimento |
| CNS_PAC| CHAR (15)| Número do CNS (Cartão Nacional de Saúde) do paciente |
| DTNASC| CHAR (8) | Data de nascimento do Paciente |
| TPIDADEPAC| CHAR (1) | Tipo da Idade do paciente em anos, meses ou dias. Calculado a partir da data de nascimento |
| IDADEPAC| CHAR (2) | Idade do Paciente|
| SEXOPAC | CHAR (1) | Sexo do paciente |
| RACACOR | CHAR (2) | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação|
| MUNPAC| CHAR (6) | Código da Unidade da Federação + Código do Município de residência do paciente ou do estabelecimento, caso não se tenha a identificação do paciente, o que ocorre no (BPA)|
| QT_APRES | NUMERIC (20.0) | Quantidade Produzida (APRESENTADA) |
| QT_APROV | NUMERIC (20.0) | Quantidade Aprovada do procedimento|
| VL_APRES | NUMERIC (20.2) | Valor Produzido (APRESENTADO) |
| VL_APROV | NUMERIC (20.2) | Valor Aprovado do procedimento|
| UFDIF | CHAR (1) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento: 0 = mesma UF; 1 = UF diferente |
| MNDIF | CHAR (1) | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento: 0 = mesmo município; 1 = município diferente |
| ETNIA | CHAR (4) | Conteúdo definido conforme [Portaria SAS Nº 508, de 28 de Setembro de 2010.](http://bvsms.saude.gov.br/bvs/saudelegis/sas/2010/prt0508_28_09_2010.html) Anexo I. Preencher somente se o campo RACACOR for 05 - Indígena. A partir da competência Out/2010. |
| NAT_JUR| CHAR (4) | Código da Natureza Jurídica |

## SIH - Sistema de Informações Hospitalares

### RD*.dbf

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| UF_ZI| char(6)| Município Gestor.|
| ANO_CMPT | char(4)| Ano de processamento da AIH, no formato aaaa.|
| MÊS_CMPT | char(2)| Mês de processamento da AIH, no formato mm.|
| ESPEC | char(2)| Especialidade do Leito |
| CGC_HOSP | char(14) | CNPJ do Estabelecimento. |
| N_AIH| char(13) | Número da AIH. |
| IDENT | char(1)| Identificação do tipo da AIH.|
| CEP | char(8)| CEP do paciente. |
| MUNIC_RES| char(6)| Município de Residência do Paciente|
| NASC| char(8)| Data de nascimento do paciente (aaaammdd). |
| SEXO| char(1)| Sexo do paciente.|
| UTI_MES_IN| numeric(2) | Zerado |
| UTI_MES_AN| numeric(2) | Zerado |
| UTI_MES_AL| numeric(2) | Zerado |
| UTI_MES_TO| numeric(3) | Quantidade de dias de UTI no mês.|
| MARCA_UTI| char(2)| Indica qual o tipo de UTI utilizada pelo paciente. |
| UTI_INT_IN| numeric(2) | Zerado |
| UTI_INT_AN| numeric(2) | Zerado |
| UTI_INT_AL| numeric(2) | Zerado |
| UTI_INT_TO| numeric(3) | Quantidade de diárias em unidade intermediaria.|
| DIAR_ACOM| numeric(3)| Quantidade de diárias de acompanhante.|
| QT_DIARIAS | numeric(3)| Quantidade de diárias.|
| PROC_SOLIC | char(10)| Procedimento solicitado.|
| PROC_REA | char(10)| Procedimento realizado. |
| VAL_SH | numeric(13,2) | Valor de serviços hospitalares. |
| VAL_SP | numeric(13,2) | Valor de serviços profissionais.|
| VAL_SADT | numeric(13,2) | Zerado|
| VAL_RN | numeric(13,2) | Zerado|
| VAL_ACOMP| numeric(13,2) | Zerado|
| VAL_ORTP | numeric(13,2) | Zerado|
| VAL_SANGUE | numeric(13,2) | Zerado|
| VAL_SADTSR | numeric(11,2) | Zerado|
| VAL_TRANSP | numeric(13,2) | Zerado|
| VAL_OBSANG | numeric(11,2) | Zerado|
| VAL_PED1AC | numeric(11,2) | Zerado|
| VAL_TOT| numeric(14,2) | Valor total da AIH. |
| VAL_UTI| numeric(8,2)| Valor de UTI. |
| US_TOT | numeric(10,2) | Valor total, em dólar.|
| DI_INTER | char(8) | Data de internação no formato aaammdd.|
| DT_SAIDA | char(8) | Data de saída, no formato aaaammdd. |
| DIAG_PRINC | char(4) | Código do diagnóstico principal (CID10).|
| DIAG_SECUN | char(4) | Código do diagnostico secundário (CID10). Preenchido com zeros a partir de 201501.|
| COBRANCA| char(2) | Motivo de Saída/Permanência |
| NATUREZA| char(2) | Natureza jurídica do hospital (com conteúdo até maio/12). Era utilizada a classificação de Regime e Natureza. |
| NAT_JUR| char(4) | NaturezajurídicadoEstabelecimento,conformeaComissão Nacional de Classificação - CONCLA|
| DESTAO| char(1) | Indica o tipo de gestão do hospital.|
| RUBRICA | numeric(5)| Zerado|
| IND_VDRL | char(1) | Indica exame VDRL.|
| MUNIC_MOV| char(6) | Município do Estabelecimento. |
| COD_IDADE| char(1) | Unidade de medida da idade. |
| IDADE | numeric(2)| Idade.|
| DIAS_PERM| numeric(5)| Dias de Permanência.|
| MORTE | numeric(1)| Indica Óbito|
| NACIONAL| char(2) | Código da nacionalidade do paciente.|
| NUM_PROC | char(4) | Zerado|
| CAR_INT| char(2) | Caráter da internação.|
| TOT_PT_SP | numeric(6) | Zerado |
| CPF_AUT| char(11) | Zerado |
| HOMONIMO| char(1)| Indicador se o paciente da AIH é homônimo do paciente de outra AIH.|
| NUM_FILHOS | numeric(2) | Número de filhos do paciente.|
| INSTRU| char(1)| Grau de instrução do paciente. |
| CID_NOTIF| char(4)| CID de Notificação.|
| CONTRACEP1| char(2)| Tipo de contraceptivo utilizado. |
| CONTRACEP2| char(2)| Segundo tipo de contraceptivo utilizado. |
| GESTRISCO | char(1)| Indicador se é gestante de risco.|
| INSC_PN| char(12) | Número da gestante no pré-natal. |
| SEQ_AIH5 | char(3)| Sequencial de longa permanência (AIH tipo 5).|
| CBOR| char(3)| Ocupação do paciente, segundo a Classificação Brasileira de Ocupações – CBO. |
| CNAER | char(3)| Código de acidente de trabalho.|
| VINCPREV| char(1)| Vínculo com a Previdência. |
| GESTOR_COD | char(3)| Motivo de autorização da AIH pelo Gestor.|
| GESTOR_TP| char(1)| Tipo de gestor.|
| GESTOR_CPF | char(11) | Número do CPF do Gestor. |
| GESTOR_DT| char(8)| Data da autorização dada pelo Gestor (aaaammdd). |
| CNES| char(7)| Código CNES do hospital. |
| CNPJ_MANT| char(14) | CNPJ da mantenedora. |
| INFEHOSP| char(1)| Status de infecção hospitalar. |
| CID_ASSO | char(4)| CID causa. |
| CID_MORTE| char(4)| CID da morte.|
| COMPLEX | char(2)| Complexidade.|
| FINANC| char(2)| Tipo de financiamento. |
| FAEC_TP| char(6)| Subtipo de financiamento FAEC. |
| REGCT | char(4)| Regra contratual.|
| RACA_COR | char(4)| Raça/Cor do paciente.|
| ETNIA | char(4)| Etnia do paciente, se raça cor for indígena. |
| SEQUENCIA | numeric(9) | Sequencial da AIH na remessa.|
| REMESSA | char(21) | Número da remessa. |
| AUD_JUST | char (50)| Justificativa do auditor para aceitação da AIH sem o número do Cartão Nacional de Saúde.|
| SIS_JUST | char (50)| Justificativa do estabelecimento para aceitação da AIH sem o número do Cartão Nacional de Saúde. |
| VAL_SH_FED| numeric (10, 2) | Valor do complemento federal de serviços hospitalares. Está incluído no valor total da AIH.|
| VAL_SP_FED| numeric (10, 2) | Valor do complemento federal de serviços profissionais. Está incluído no valor total da AIH. |
| VAL_SH_GES| numeric (10, 2) | Valor do complemento do gestor (estadual ou municipal) de serviços hospitalares. Está incluído no valor total da AIH.|
| VAL_SP_GES| numeric (10, 2) | Valor do complemento do gestor (estadual ou municipal) de serviços profissionais. Está incluído no valor total da AIH. |
| VAL_UCI| numeric (10, 2) | Valor de UCI.|
| MARCA_UCI| char (2)| Tipo de UCI utilizada pelo paciente. |
| DIAGSEC1| char (4)| Diagnóstico secundário1. |
| DIAGSEC2| char (4)| Diagnóstico secundário 2.|
| DIAGSEC3| char (4)| Diagnóstico secundário 3.|
| DIAGSEC4| char (4)| Diagnóstico secundário 4.|
| DIAGSEC5| char (4)| Diagnóstico secundário 5.|
| DIAGSEC6| char (4)| Diagnóstico secundário 6.|
| DIAGSEC7| char (4)| Diagnóstico secundário 7.|
| DIAGSEC8| char (4)| Diagnóstico secundário 8.|
| DIAGSEC9| char (4)| Diagnóstico secundário 9.|
| TPDISEC1| char(1) | Tipo de diagnóstico secundário 1.|
| TPDISEC2| char(1) | Tipo de diagnóstico secundário 2.|
| TPDISEC3| char(1) | Tipo de diagnóstico secundário 3.|
| TPDISEC4| char(1) | Tipo de diagnóstico secundário 4.|
| TPDISEC5| char(1) | Tipo de diagnóstico secundário 5.|
| TPDISEC6| char(1) | Tipo de diagnóstico secundário 6.|
| TPDISEC7| char(1) | Tipo de diagnóstico secundário 7.|
| TPDISEC8| char(1) | Tipo de diagnóstico secundário 8.|
| TPDISEC9| char(1) | Tipo de diagnóstico secundário 9.|

### SP*.dbf

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| SP_GESTOR| char(6)| Unidade de Federação + Código Município de Gestão ou UF0000 se o Estabelecimento Executante está sob Gestão Estadual. |
| SP_UF| char (2) | Unidade da Federação. |
| SP_AA| char(4)| Ano da internação.|
| SP_MM| char(2)| Mês da internação.|
| SP_CNES| char(7)| Código do CNES do Estabelecimento de Saúde executante da AIH. |
| SP_NAIH| char(13) | Número da AIH.|
| SP_PROCREA | char (10)| Procedimento principal realizado na AIH.|
| SP_DTINTER | char (8) | Data da internação. |
| SP_DTSAIDA | char (8) | Data de saída. |
| SP_NUM_PR | char (8) | Zerado |
| SP_TIPO| char (2) | Zerado |
| SP_CPFCGC| char (14)| CNES, CPF ou CNPJ do prestador do serviço do ato profissional. |
| SP_ATOPROF | char (10)| Procedimento referente ao ato profissional.|
| SP_TP_ATO | char (2) | Zerado.|
| SP_QTD_ATO| numeric (4)| Quantidade de atos profissionais.|
| SP_PTSP| char (6) | Quantidade de pontos.|
| SP_NF| char (8) | Nota fiscal do material empregado quando órtese/prótese, quando não, o campo representa a data do ato. |
| SP_VALATO| numeric (14,2) | Valor do ato profissional. |
| SP_M_HOSP | char (6) | Município de localização do Estabelecimento Executante da AIH. |
| SP_M_PAC| char (6) | Município de residência do paciente. |
| SP_DES_HOS| char (1) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento.|
| SP_DES_PAC| char (1) | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento.|
| SP_COMPLEX | char (2) | Complexidade do ato profissional.|
| SP_FINANC| char (2) | Tipo de financiamento do ato profissional. |
| SP_CO_FAEC| char (6) | Tipo de financiamento (04-FAEC) + Subtipo de financiamento relacionado ao tipo de financiamento (04-FAEC) do ato profissional. |
| SP_PF_CBO | char (6) | Código de Ocupação Brasileira do Profissional que realizou o ato ou “00000” caso não tenha sido. |
| SP_PF_DOC | char (15)| Documento de pessoa jurídica.|
| SP_PJ_DOC | char (14)| Documento de pessoa física.|
| IN_TP_VAL | char (1) | Tipo de valor: 1 - SP /2 –SH.|
| SEQUENCIA | char (9) | Código sequencial. |
| REMESSA | char (21)| Nome da remessa. |
| SERV_CLA | char (6) | Serviço/Classificação. |
| SP_CIDPRI| char (4) | CID Principal. |
| SP_CIDSEC| char (4) | CID Secundário.|
| SP_QT_PROC| numeric(4) | Quantidade de procedimentos realizados.|
| SP_U_AIH| char(1)| Indicador único da AIH. Contabiliza a AIH sem repetições.|


## SIM - Sistema de Informações de Mortalidade

| **Nome do campo no DBF** | **Tipo** | **Tam** | **Valores válidos** | **Descrição** |
|:------------------------:|:--------:|:-------:|:------------------------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TIPOBITO | Caracter | 1 | 1-Fetal; 2-Não Fetal| Tipo do óbito Óbito fetal: morte antes da expulsão ou da extração completa do corpo da Mãe, independentemente da duração da gravidez. Indica o óbito o fato de o feto, depois da expulsão do corpo materno, não respirar nem apresentar nenhum outrosinal de vida, como batimentos do coração, pulsações do cordão umbilical ou movimentos efetivos dos músculosde contração voluntária |
| DTOBITO| Caracter | 8 | Data no padrão ddmmaaaa | Data em que occoreu o óbito.|
| HORAOBITO| Caracter | 5 | Números (padrão 24 horas 00:00) | Horário do óbito|
| NATURAL| Caracter | 3 | Números | País e Unidade da Federação onde falecido nasceu. Se estrangeiro informar País|
| CODMUNNATU 			 | Caracter | 7 	| Números | Código do município de naturalidade do falecido.|
| DTNASC | Caracter | 8 | Data no padrão ddmmaaaa| Data do nascimento do falecido. Em caso de óbito fetal as datas de óbito e nascimento deverão ser iguais. |
| IDADE| Caracter | 3 | Idade: composto de dois subcampos. \- O primeiro, de 1 dígito, indica a unidade da idade (se 1 = minuto, se 2 = hora, se 3 = mês, se 4 = ano, se\= 5 idade maior que 100anos). \- O segundo, de dois dígitos, indicaa quantidade deunidades: **Idade menor de 1 hora**: subcampo varia de 01 e 59 (minutos); **De 1 a 23 Horas**: subcampo varia de 01 a 23 (horas); **De 24 horas e 29 dias:** subcampo varia de 01 a 29 (dias); **De 1 a menos de 12 meses completos**: subcampo varia de 01 a 11 (meses); **Anos** \- subcampo varia de 00 a 99; \- 9 -ignorado | Idade do falecido em minutos, horas, dias, meses ou anos |
| SEXO | Caracter | 1 | M – masculino; F – feminino; I - ignorado| Sexo do falecido. “Ignorado” selecionada em casos especiais como cadáveres mutilados, em estado avançado de decomposição, genitália indefinida ou hermafroditismo |
| RACACOR| Caracter | 1 | 1 – Branca; 2 – Preta; 3 – Amarela; 4 – Parda; 5 – Indígena | Cor informada pelo responsável pelas informações do falecido |
| ESTCIV | Caracter | 1 | 1 – Solteiro; 2 – Casado; 3 – Viúvo;4 – Separado judicialmente/divorciado; 5 –União estável; 9 – Ignorado| Situação conjugal do falecido informada pelos familiares |
| ESC2010| Caracter | 1 | 0 – Sem escolaridade; 1 – Fundamental I (1ª a 4ª série); 2 – Fundamental II (5ª a 8ª série); 3 – Médio (antigo 2º Grau); 4 – Superior incompleto; 5 – Superior completo; 9 – Ignorado | Escolaridade 2010. Nível da última série concluída pelo falecido|
| SERIESCFAL | Caracter | | Números de 1 a 8 | Última série escolar concluída pelo falecido|
| OCUP | Caracter | 6 | Números| Tipo de trabalho que o falecido desenvolveu na maior parte de sua vida produtiva. Preenchimento de acordo com Classificação Brasileira de Ocupações – CBO 2002 |
| CODMUNRES| Caracter | 7 | Números| Código do município de residência. Em caso de óbito fetal, considerar o município de residência da mãe|
| LOCOCOR| Caracter | 1 | 1 – hospital; 2 – outros estabelecimentos de saúde; 3 – domicílio; 4 – via pública; 5 – outros; 6 - aldeia indígena; 9 – ignorado.| Local de ocorrência do óbito|
| CODMUNOCOR | Caracter | 8 | Números| Código relativo ao município onde ocorreu o óbito|
| IDADEMAE | Caracter | 2 | Números| Idade da mãe|
| ESCMAE2010 | Caracter | 1 | 0 – Sem escolaridade; 1 – Fundamental I (1ª a 4ª série); 2 – Fundamental II (5ª a 8ª série); 3 – Médio (antigo 2º Grau); 4 – Superior incompleto; 5 – Superior completo; 9 – Ignorado | Escolaridade 2010. Nível da última série concluída pela mãe |
| SERIESCMAE | Caracter | 1 | Números de 1 a 8 | Última série escolar concluída pela mãe |
| OCUPMAE| Caracter | 6 || Tipo de trabalho exercido habitualmente pela Mãe, de acordo com Classificação Brasileira de Ocupações – CBO 2002. No caso da mãe do falecido(a) ser “aposentada”, preencher com a ocupação habitual anterior. |
| QTDFILVIVO | Caracter | 2 | Número; 9 - igonorado| Número de filhos vivos|
| QTDFILMORT | Caracter | 2 | Número; 9 - igonorado| Número de filhos mortos. Não incluir a criança cujo óbito se notifica na respectiva DO |
| SEMAGESTAC | Caracter | 3 | Números com dois algarismos; 9 - igonorado| Semanas de gestação com dois algarismos |
| GRAVIDEZ | Caracter | 1 | 1 – única; 2 – dupla; 3 – tripla e mais; 9 – ignorada | Tipo de gravidez|
| PARTO| Caracter | 1 | 1 – vaginal; 2 – cesáreo; 9 – ignorado| Tipo de parto |
| OBITOPARTO | Caracter | 1 | 1 - antes; 2– durante; 3–depois; 9– Ignorado| Momento do óbito em relação ao parto|
| PESO | Caracter | 4 | Número (quatro algarismos) | Peso ao nascer em gramas|
| NUMERODN | Caracter | 8 | Números| Número da Declaração de Nascido Vivo|
| TPMORTEOCO | Caracter | 1 | 1 – na gravidez; 2 – no parto; 3 – no abortamento; 4 – até 42 dias após o término do parto; 5 – de 43 dias a 1 ano após o término da gestação ;8 – não ocorreu nestes períodos; 9– ignorado. | Situação gestacional ou pósgestacional em que ocorreu o óbito |
| ASSISTMED| Caracter | 1 | 1 – sim; 2 – não; 9 – ignorado | Se refere ao atendimento médico continuado que o paciente recebeu, ou não, durante a enfermidade que ocasionou o óbito |
| NECROPSIA| Caracter | 1 | 1 – sim; 2 – não; 9 – ignorado | Refere-se a execução ou não de necropsia para confirmação do diagnóstico|
| LINHAA| Caracter | 20 | Códigos CID 10| CIDs informados na Linha A da DO referente ao diagnóstico na Linha A da DO (**causa terminal -** doença ou estado mórbido que causou diretamente a morte) |
| LINHAB| Caracter | 20 | Códigos CID 10| CIDs informados na Linha B da DO referente ao diagnóstico na Linha B da DO (**causa antecedente ou conseqüencial** \- estado mórbido, se existir, que produziu a causa direta da morte registrada na linha A) |
| LINHAC| Caracter | 20 | Códigos CID 10| CIDs informados na Linha C da DO referente ao diagnóstico na Linha C da DO (**causa antecedente ou conseqüencial** \- estado mórbido, se existir, que produziu a causa direta da morte registrada na linha A) |
| LINHAD| Caracter | 20 | Códigos CID 10| CIDs informados na Linha D da DO referente ao diagnóstico na Linha D da DO **(causa básica** – estado mórbido, se existir, que produziu a causa direta da morte registrada na linha A)|
| LINHAII | Caracter | 45 | Códigos CID 10| CIDs informados na Parte II da DO referente ao diagnóstico na Parte II da DO (**causa contribuinte** \- outras condições significativas que contribuíram para a morte e que não entraram na cadeia definidana Parte I |
| CIRCOBITO | Caracter | 1| 1 – acidente; 2 – suicídio; 3 – homicídio; 4 – outros; 9 – ignorado | Tipo de morte violenta ou circunstâncias em que se deu a morte não natural |
| ACIDTRAB| Caracter | 1| 1 – sim; 2 – não; 9 – ignorado| Indica se o evento que desencadeou o óbito está relacionado ao processo de trabalho|
| FONTE | Caracter | 1| 1 – ocorrência policial; 2 – hospital; 3 – família; 4 – outra; 9 – ignorado | fonte de informação utilizada para o preenchimento dos campos 48 e 49|
| ORIGEM| Caracter | 1 | 1- Oracle; 2 - Banco estadual diponibilizado via FTP; 3 - Banco SEADE; 9 - Ignorado | Origem do registro |
| ESC | Caracter | 1 | 1 – Nenhuma; 2 – de 1 a 3 anos; 3 – de 4 a 7 anos; 4 – de 8 a 11 anos; 5 – 12 anos e mais; 9 – Ignorado. | Escolaridade em anos |
| ESCMAE| Caracter | 1 | 1 – Nenhuma; 2 – de 1 a 3 anos; 3 – de 4 a 7 anos; 4 – de 8 a 11 anos; 5 – 12 anos e mais; 9 – Ignorado| Escolaridade da mãe em anos|
| OBITOGRAV | Caracter | 1 | 1 – sim; 2 – não; 9 – ignorado | Óbito na gravidez|
| OBITOPUERP| Caracter | 1 | 1 – Sim, até 42 dias após o parto; 2 – Sim, de 43 dias a 1 ano; 3 – Não;9 – Ignorado.| Óbito no puerpério |
| EXAME | Caracter | 1 | 1 – sim; 2 – não; 9 – ignorado | Realização de exame|
| CIRURGIA| Caracter | 1 | 1 – sim; 2 – não; 9 – ignorado | Realização de cirurgia |
| CAUSABAS_O | Caracter | 4 | Códigos CID 10 | Causa básica informada antes da resseleção |
| CAUSABAS| Caracter | 4 | Códigos CID 10 | Causa básica da DO |
| NUMEROLOTE| Caracter | 8 | Números| Número do lote |
| DTINVESTIG| Caracter | 8 | Data no padrão ddmmaaaa| Data da investigação do óbito|
| DTCADASTRO| Caracter | 8 | Data no padrão ddmmaaaa| Data do cadastro do óbito|
| STCODIFICA| Caracter | 1 | Se codificadora (valor: S) ou não (valor: N)| Status de instalação |
| CODIFICADO| Caracter | 1 | Se estiver codificado (valor: S) ou não (valor: N)| Informa se formulario foi codificado |
| VERSAOSIST| Caracter | 7 | Números; . | Versão do sistema|
| VERSAOSCB | Caracter | 7 | Números; . | Versão do seletor de causa básica|
| FONTEINV | Caracter | 8| 1 – Comitê de Morte Materna e/ou Infantil; 2 – Visita domiciliar / Entrevista família; 3 – Estabelecimento de Saúde / Prontuário; 4 – Relacionado com outros bancos de dados; 5 – S V O; 6 – I M L; 7 – Outra fonte; 8 – Múltiplas fontes; 9 – Ignorado| Fonte de investigação|
| DTRECEBIM| Caracter | 8| Data no padrão ddmmaaaa| Data do recebimento|
| ATESTADO | Caracter | 70 | Códigos CID 10 | CIDs informados no atestado|
| DTRECORIGA | Caracter | 8| Data no padrão ddmmaaaa| Campo Criado no Tratamento para Data do recebimento original |
| CAUSAMAT | Caracter | 4| Códigos CID 10 | CID da causa externa associada a uma causa materna|
| ESCMAEAGR1 | Caracter | 2| 00 – Sem Escolaridade; 01 – Fundamental I Incompleto; 02 – Fundamental I Completo; 03 – Fundamental II Incompleto; 04 – Fundamental II Completo; 05 – Ensino Médio Incompleto; 06 – Ensino Médio Completo; 07 – Superior Incompleto; 08 – Superior Completo; 09 – Ignorado; 10 – Fundamental I Incompleto ou Inespecífico; 11 – Fundamental II Incompleto ou Inespecífico; 12 – Ensino Médio Incompleto ou Inespecífico | Escolaridade da mãe agregada (formulário a partir de 2010) |
| ESCFALAGR1 | Caracter | 1 | 00 – Sem Escolaridade; 01 – Fundamental I Incompleto; 02 – Fundamental I Completo; 03 – Fundamental II Incompleto; 04 – Fundamental II Completo; 05 – Ensino Médio Incompleto; 06 – Ensino Médio Completo; 07 – Superior Incompleto; 08 – Superior Completo; 09 – Ignorado; 10 – Fundamental I Incompleto ou Inespecífico; 11 – Fundamental II Incompleto ou Inespecífico; 12 – Ensino Médio Incompleto ou Inespecífico | Escolaridade do falecido agregada (formulário a partir de 2010) |
| STDOEPIDEM | Caracter | 1 | 1 - Sim; 0 - Não | Status de DO Epidemiológica |
| STDONOVA | Caracter | 1 | 1 - Sim; 0 - Não | Status de DO Nova |
| DIFDATA| Caracter | 8 | Números| Diferença entre a data de óbito e data do recebimento original da DO (\[DTOBITO\] – \[DTRECORIG\]) |
| NUDIASOBCO | Caracter | 4 | Números| Diferença entre a data óbito e a data conclusão da investigação, em dias. |
| DTCADINV | Caracter | 8 | Data no padrão ddmmaaaa| Data do cadastro de investigação|
| TPOBITOCOR | Caracter | 1 | 1-Durante a gestação, 2- Durante o abortamento, 3- Após o abortamento , 4- No parto ou até 1 hora após o parto, 5- No puerpério - até 42 dias após o parto, 6- Entre 43 dias e até 1 ano após o parto, 7- A investigação não identificou o momento do óbito, 8- Mais de um ano após o parto , 9- O óbito não ocorreu nas circunstancias anteriores, Branco - Não investigado| Momento da ocorrência do óbito|
| DTCONINV | Caracter | 8 | Data no padrão ddmmaaaa| Data da conclusão da investigação|
| FONTES | Caracter | 6 | Letras | Combinado de caracteres conforme o preenchimento dos campos de fontes (FONTENTREV, FONTEAMBUL, FONTEPRONT, FONTESVO, FONTEIML, FONTEPROF): se preenchido caractere “S”, se o campo estiver vazio caractere “X” |
| TPRESGINFO | Caracter | 2 | 01 - Não acrescentou nem corrigiu informação; 02 - Sim, permitiu o resgate de novas informações; 03 - Sim, permitiu a correção de alguma das causas informadas originalmente. | Informa se a investigação permitiu oresgate de alguma causa de óbito não informado, ou a correção de alguma antesinformada |
| TPNIVELINV | Caracter | 1 | E – estadual; R- regional; M- Municipal | Tipo de nível investigador |
| DTCADINF | Caracter | 8 | Data no padrão ddmmaaaa| Quando preenchido indica se a investigação foi realizada |
| MORTEPARTO | Caracter | 1 | 1 - antes; 2– durante; 3–após; 9– Ignorado| Momento do óbito em relação ao parto |
| DTCONCASO| Caracter | 8 | Data no padrão ddmmaaaa| Data de conclusão do caso|
| ALTCAUSA | Caracter | 1 | 1- Sim; 2 – Não| Indica se houve correção ou alteração da causa do óbito após investigação|
| TPPOS| Caracter | 1 | 1 – sim; 2 – não | Óbito investigado|
| GESTACAO | Caracter | 1 | 1 - Menos de 22 semanas; 2 - 22 a 27 semanas; 3 - 28 a 31 semanas; 4 - 32 a 36 semanas; 5 - 37 a41 semanas; 6 - 42 e +semanas | Faixas de semanas de gestação|
| CB_PRE| Caracter | 4 | Código CID 10| Causa básica informada antes da resseleção (localidade)|

## SINAN - Sistema de Informação de Agravos de Notificação

### Botulismo
|Coluna|Tipo|
|:---:|:-------:|
|  nu_notific |char(7)|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  dtatend    |date|
|  nuatend    |char(10)|
|  dtsuspeic  |date|
|  sthospital |char(1)|
|  dtinterna  |date|
|  dtalta     |date|
|  stfebre    |char(1)|
|  stnausea   |char(1)|
|  stvomito   |char(1)|
|  stdiarreia |char(1)|
|  stconstipa |char(1)|
|  stcefaleia |char(1)|
|  sttontura  |char(1)|
|  stvisao    |char(1)|
|  stdiplopia |char(1)|
|  stdisartri |char(1)|
|  stdisfonia |char(1)|
|  stdisfagia |char(1)|
|  stboca     |char(1)|
|  stferiment |char(1)|
|  stflacidez |char(1)|
|  stdispneia |char(1)|
|  strespira  |char(1)|
|  stcardiaca |char(1)|
|  stcoma     |char(1)|
|  stparestes |char(1)|
|  stoutrosin |char(1)|
|  stptose    |char(1)|
|  stoftalmo  |char(1)|
|  stmidriase |char(1)|
|  stfacial   |char(1)|
|  stbulbar   |char(1)|
|  stmeminf   |char(1)|
|  stmemsup   |char(1)|
|  stdescende |char(1)|
|  stsimetric |char(1)|
|  stsensivel |char(1)|
|  tpneuro    |char(1)|
|  stalimento |char(1)|
|  dsalimento |char(30)|
|  stcaseira  |char(1)|
|  stcomercio |char(1)|
|  stexpalim  |char(1)|
|  stdomicili |char(1)|
|  stescola   |char(1)|
|  sttrabalho |char(1)|
|  strestaura |char(1)|
|  stfesta    |char(1)|
|  stoutroloc |char(1)|
|  nuconsome  |char(10)|
|  stsoro     |char(1)|
|  stantibio  |char(1)|
|  stoutrotra |char(1)|
|  dtsoro     |date|
|  stantibotu |char(1)|
|  stsoromat  |char(1)|
|  dtsorocol  |date|
|  stfezesmat |char(1)|
|  dtfezescol |date|
|  steletro   |char(1)|
|  dteletro   |date|
|  classi_fin |char(1)|
|  agente_out |char(30)|
|  criterio   |char(1)|
|  tpbotulism |char(1)|
|  stclinica  |char(1)|
|  stbromato  |char(1)|
|  tpclinica  |char(1)|
|  tpbromato  |char(1)|
|  dscausalim |char(30)|
|  doenca_tra |char(1)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  dt_encerra |date|
|  dt_digita  |date|
|  stventila  |char(1)|
|  uf_hosp    |char(2)|
|  mun_hosp   |char(6)|
|  ds_pares   |char(30)|
|  ds_outrosi |char(30)|
|  ds_indus   |char(30)|
|  ds_ingest  |char(4)|
|  ds_ini_ges |char(4)|
|  ds_fim_ges |char(4)|
|  ds_outr_lo |char(30)|
|  uf_ing     |char(2)|
|  mun_ing    |char(6)|
|  ds_trat    |char(30)|
|  stsorores  |char(1)|
|  tpsorotox  |char(1)|
|  stfezesres |char(1)|
|  tpfezestox |char(1)|
|  st_ali1col |char(1)|
|  ds_ali1out |char(30)|
|  dt_ali1col |date|
|  resalim1   |char(1)|
|  tp_ali1tox |char(1)|
|  st_ali2col |char(1)|
|  ds_ali2out |char(30)|
|  dt_ali2col |date|
|  st_ali2res |char(1)|
|  tp_ali2to  |char(1)|
|  tp_colout  |char(1)|
|  ds_outro   |char(30)|
|  dt_colout  |date|
|  resalimout |char(1)|
|  tp_toxoutr |char(1)|
|  tp_liquor  |char(1)|
|  nu_celula  |char(5)|
|  nu_protei  |char(5)|
|  dt_liquor  |date|
|  tp_sensiti |char(1)|
|  tp_motora  |char(1)|
|  tp_repete  |char(1)|
|  ds_ali1    |char(30)|
|  ds_ali2    |char(30)|
|  ds_local1  |char(30)|
|  ds_local2  |char(30)|

### Doença de Chagas

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  nduplic_n  |char(1)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  ant_uf_1   |char(2)|
|  mun_1      |char(6)|
|  ant_uf_2   |char(2)|
|  mun_2      |char(6)|
|  ant_uf_3   |char(2)|
|  mun_3      |char(6)|
|  presenca   |char(1)|
|  parasito   |date|
|  historia   |char(1)|
|  controle   |char(1)|
|  manipula   |char(1)|
|  maechaga   |char(1)|
|  oral       |char(1)|
|  assintoma  |char(1)|
|  edema      |char(1)|
|  meningoe   |char(1)|
|  poliadeno  |char(1)|
|  febre      |char(1)|
|  hepatome   |char(1)|
|  sinais_icc |char(1)|
|  arritmias  |char(1)|
|  astenia    |char(1)|
|  esplenom   |char(1)|
|  chagoma    |char(1)|
|  outro_sin  |char(1)|
|  outro_esp  |char(30)|
|  dt_col_dir |date|
|  exame      |char(1)|
|  micro_hema |char(1)|
|  outro      |char(1)|
|  dt_col_ind |date|
|  xenodiag   |char(1)|
|  hemocult   |char(1)|
|  dt_col_s1  |date|
|  dt_col_s2  |date|
|  eli_igm_s1 |char(1)|
|  eli_igg_s1 |char(1)|
|  eli_igm_s2 |char(1)|
|  eli_igg_s2 |char(1)|
|  hem_igm_s1 |char(1)|
|  hem_igg_s1 |char(1)|
|  hem_igm_s2 |char(1)|
|  hem_igg_s2 |char(1)|
|  imu_igm_s1 |char(1)|
|  tit_igm_s1 |char(5)|
|  imu_igm_s2 |char(1)|
|  tit_igm_s2 |char(5)|
|  imu_igg_s1 |char(1)|
|  tit_igg_s1 |char(5)|
|  imu_igg_s2 |char(1)|
|  tit_igg_s2 |char(5)|
|  resul_his  |date|
|  res_hist   |char(1)|
|  especifico |char(1)|
|  sintomatic |char(1)|
|  droga      |char(1)|
|  tempo      |numeric(3)|
|  con_triat  |char(1)|
|  biosseg    |char(1)|
|  fiscaliza  |char(1)|
|  med_outro  |char(1)|
|  outro_des  |char(30)|
|  classi_fin |char(1)|
|  criterio   |char(1)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  con_provav |char(1)|
|  con_outra  |char(30)|
|  con_local  |char(1)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  doenca_tra |char(1)|
|  dt_encerra |date|

### Colera

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  fc_contato |char(1)|
|  fc_cont_de |char(30)|
|  vinculo    |char(1)|
|  out_vincul |char(30)|
|  cs_assinto |char(1)|
|  cs_diarre  |char(1)|
|  cs_caimbra |char(1)|
|  cs_febre   |char(1)|
|  cs_vomitos |char(1)|
|  cs_dor     |char(1)|
|  cs_choque  |char(1)|
|  cs_desit   |char(1)|
|  tip_diarre |char(1)|
|  cs_frequen |char(1)|
|  cs_sangue  |char(1)|
|  cs_muco    |char(1)|
|  cs_tipo    |char(1)|
|  dt_atendim |date|
|  dt_interna |date|
|  uf_hospita |char(2)|
|  nm_munic_h |char(6)|
|  cs_materia |char(1)|
|  cs_vomito  |char(1)|
|  dt_coleta  |date|
|  cs_antib   |char(1)|
|  nm_antibio |char(30)|
|  cs_resulta |char(1)|
|  cs_positiv |char(1)|
|  cs_neg_esp |char(30)|
|  cs_reidrat |char(1)|
|  cs_antib_t |char(1)|
|  antib_des  |char(30)|
|  classi_fin |char(1)|
|  criterio   |char(1)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  codisinf   |char(9)|
|  doenca_tra |char(1)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  dt_encerra |date|
|  dt_digita  |date|
|  dt_desc1   |date|
|  dt_desc2   |date|
|  dt_desc3   |date|
|  co_uf_des1 |char(2)|
|  co_uf_des2 |char(2)|
|  co_uf_des3 |char(2)|
|  mun_des1   |char(6)|
|  mun_des2   |char(6)|
|  mun_des3   |char(6)|
|  pa_des1    |numeric(4)|
|  pa_des2    |numeric(4)|
|  pa_des3    |numeric(4)|
|  ds_trans1  |char(30)|
|  ds_trans2  |char(30)|
|  ds_trans3  |char(30)|

### Conqueluche

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  nduplic_n  |char(1)|
|  cs_flxret  |char(1)|
|  flxrecebi  |char(1)|
|  migrado_w  |char(1)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  ant_sentin |char(1)|
|  fc_contato |char(1)|
|  out_contat |char(30)|
|  cs_vac_n   |char(1)|
|  dt_ult_dos |date|
|  dt_catarra |date|
|  cs_tosse_e |char(1)|
|  cs_tosse_p |char(1)|
|  cs_crise   |char(1)|
|  cs_cianose |char(1)|
|  cs_vomitos |char(1)|
|  cs_apneia  |char(1)|
|  cs_temp37  |char(1)|
|  cs_temp_38 |char(1)|
|  cs_out_sin |char(1)|
|  nm_out_sin |char(30)|
|  cs_pneumon |char(1)|
|  cs_encefal |char(1)|
|  cs_desitra |char(1)|
|  cs_otite   |char(1)|
|  cs_desnutr |char(1)|
|  cs_out_com |char(1)|
|  nm_out_com |char(30)|
|  cs_hospita |char(1)|
|  dt_interna |date|
|  cod_uf_hos |char(2)|
|  cod_mun_ho |char(6)|
|  cs_antibio |char(1)|
|  dt_adm_ant |date|
|  cs_coleta  |char(1)|
|  dt_coleta  |date|
|  cs_cultura |char(1)|
|  med_iden_c |char(1)|
|  med_quan_c |numeric(4)|
|  med_caso_s |char(1)|
|  colet_comu |char(1)|
|  quan_comun |numeric(4)|
|  quan_posit |numeric(4)|
|  med_bloque |char(1)|
|  classi_fin |char(1)|
|  criterio   |char(1)|
|  doenca_tra |char(1)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  dt_encerra |date|

### Dengue

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(5)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  febre      |char(1)|
|  mialgia    |char(1)|
|  cefaleia   |char(1)|
|  exantema   |char(1)|
|  vomito     |char(1)|
|  nausea     |char(1)|
|  dor_costas |char(1)|
|  conjuntvit |char(1)|
|  artrite    |char(1)|
|  artralgia  |char(1)|
|  petequia_n |char(1)|
|  leucopenia |char(1)|
|  laco       |char(1)|
|  dor_retro  |char(1)|
|  diabetes   |char(1)|
|  hematolog  |char(1)|
|  hepatopat  |char(1)|
|  renal      |char(1)|
|  hipertensa |char(1)|
|  acido_pept |char(1)|
|  auto_imune |char(1)|
|  dt_chik_s1 |date|
|  dt_chik_s2 |date|
|  dt_prnt    |date|
|  res_chiks1 |char(1)|
|  res_chiks2 |char(1)|
|  resul_prnt |char(1)|
|  dt_soro    |date|
|  resul_soro |char(1)|
|  dt_ns1     |date|
|  resul_ns1  |char(1)|
|  dt_viral   |date|
|  resul_vi_n |char(1)|
|  dt_pcr     |date|
|  resul_pcr_ |char(1)|
|  sorotipo   |char(1)|
|  histopa_n  |char(1)|
|  imunoh_n   |char(1)|
|  hospitaliz |char(1)|
|  dt_interna |date|
|  uf         |char(2)|
|  municipio  |char(6)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  classi_fin |char(2)|
|  criterio   |char(1)|
|  doenca_tra |char(1)|
|  clinc_chik |char(1)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  dt_encerra |date|
|  alrm_hipot |char(1)|
|  alrm_plaq  |char(1)|
|  alrm_vom   |char(1)|
|  alrm_sang  |char(1)|
|  alrm_hemat |char(1)|
|  alrm_abdom |char(1)|
|  alrm_letar |char(1)|
|  alrm_hepat |char(1)|
|  alrm_liq   |char(1)|
|  dt_alrm    |date|
|  grav_pulso |char(1)|
|  grav_conv  |char(1)|
|  grav_ench  |char(1)|
|  grav_insuf |char(1)|
|  grav_taqui |char(1)|
|  grav_extre |char(1)|
|  grav_hipot |char(1)|
|  grav_hemat |char(1)|
|  grav_melen |char(1)|
|  grav_metro |char(1)|
|  grav_sang  |char(1)|
|  grav_ast   |char(1)|
|  grav_mioc  |char(1)|
|  grav_consc |char(1)|
|  grav_orgao |char(1)|
|  dt_grav    |date|
|  mani_hemor |char(1)|
|  epistaxe   |char(1)|
|  gengivo    |char(1)|
|  metro      |char(1)|
|  petequias  |char(1)|
|  hematura   |char(1)|
|  sangram    |char(1)|
|  laco_n     |char(1)|
|  plasmatico |char(1)|
|  evidencia  |char(1)|
|  plaq_menor |char(7)|
|  con_fhd    |char(1)|
|  complica   |char(1)|
|  tp_sistema |char(1)|
|  nduplic_n  |char(1)|
|  cs_flxret  |char(1)|
|  flxrecebi  |char(7)|

### Difteria

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  cs_zona    |char(1)|
|  id_pais    |char(4)|
|  nduplic_n  |char(1)|
|  cs_flxret  |char(1)|
|  flxrecebi  |char(1)|
|  migrado_w  |char(1)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  ant_tipoco |char(1)|
|  ant_outros |char(30)|
|  ant_dos_n  |char(1)|
|  ant_ulti_d |date|
|  cli_edemag |char(1)|
|  cli_pescoc |char(1)|
|  cli_febre  |char(1)|
|  cli_prostr |char(1)|
|  cli_pseudo |char(1)|
|  cli_palide |char(1)|
|  cli_temper |numeric(3)|
|  cli_cavida |char(1)|
|  cli_amigda |char(1)|
|  cli_cordao |char(1)|
|  cli_faring |char(1)|
|  cli_laring |char(1)|
|  cli_orgaos |char(1)|
|  cli_palato |char(1)|
|  cli_condut |char(1)|
|  cli_traque |char(1)|
|  cli_pele   |char(1)|
|  cli_conjun |char(1)|
|  cli_miocar |char(1)|
|  cli_nefrit |char(1)|
|  cli_paralb |char(1)|
|  cli_paralp |char(1)|
|  cli_arritm |char(1)|
|  cli_paralm |char(1)|
|  cli_outras |char(1)|
|  cli_especi |char(30)|
|  ate_hospit |char(1)|
|  ate_intern |date|
|  ate_uf_int |char(2)|
|  ate_munici |char(6)|
|  lab_mate_n |char(1)|
|  lab_data_c |date|
|  lab_cultur |char(1)|
|  lab_provas |char(1)|
|  tra_data_s |date|
|  tra_antibi |char(1)|
|  tra_data_a |date|
|  med_iden_c |char(1)|
|  med_quan_c |numeric(3)|
|  med_caso_s |char(1)|
|  med_materi |char(1)|
|  med_quan_m |numeric(3)|
|  med_quan_p |numeric(3)|
|  med_preven |char(1)|
|  classi_fin |char(1)|
|  criterio   |char(1)|
|  doenca_tra |char(1)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  dt_encerra |date|

### Esquistossomose

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  dt_copro   |date|
|  an_quant   |numeric(6)|
|  outros     |char(1)|
|  tratam     |char(1)|
|  tratanao   |char(1)|
|  stcura1    |char(1)|
|  stcura2    |char(1)|
|  stcura3    |char(1)|
|  forma      |char(1)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  nopropin   |char(100)|
|  nocolinf   |char(100)|
|  doenca_tra |char(1)|
|  evolucao   |char(1)|
|  dt_encerra |date|
|  dt_obito   |date|
|  ds_forma   |char(30)|
|  an_quali   |char(1)|
|  dttrat     |date|
|  dt_resu3   |date|
|  outro_ex   |char(40)|

### Febre Amarela

|Coluna|Tipo|
|:---:|:-------:|
|  nu_notific |char(7)|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  localidade |char(100)|
|  id_pais    |char(4)|
|  nduplic_n  |char(1)|
|  dt_info_1  |date|
|  dt_info_2  |date|
|  dt_info_3  |date|
|  co_uf_obs1 |char(2)|
|  co_uf_obs2 |char(2)|
|  co_uf_obs3 |char(2)|
|  co_mun_1   |char(6)|
|  co_mun_2   |char(6)|
|  co_mun_3   |char(6)|
|  co_pais_1  |char(3)|
|  co_pais_2  |char(3)|
|  co_pais_3  |char(3)|
|  ds_trans_1 |char(30)|
|  ds_trans_2 |char(30)|
|  ds_trans_3 |char(30)|
|  cs_flxret  |char(1)|
|  flxrecebi  |char(1)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  epizootias |char(1)|
|  isol_vir_n |char(1)|
|  vetor_a    |char(1)|
|  vacinado   |char(1)|
|  dt_vacina  |date|
|  uf_vac     |char(2)|
|  munci_vac  |char(6)|
|  unid_vac   |char(7)|
|  dor_abdo_n |char(1)|
|  sint_hem_n |char(1)|
|  faget      |char(1)|
|  excr_rena_ |char(1)|
|  hospitaliz |char(1)|
|  dt_interna |date|
|  uf         |char(2)|
|  municipio  |char(6)|
|  bt         |char(6)|
|  ast        |char(5)|
|  bd         |char(6)|
|  alt        |char(5)|
|  dt_col_1   |date|
|  s1_igm     |char(1)|
|  dt_col_2   |date|
|  s2_igm     |char(1)|
|  mat_coleta |char(1)|
|  dt_coleta  |date|
|  res_isolam |char(1)|
|  histopa    |char(1)|
|  imunoh     |char(1)|
|  dt_ptpcr   |date|
|  res_ptpcr  |char(1)|
|  classi_fin |char(2)|
|  clasfin_es |char(30)|
|  criterio   |char(2)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  doenca_tra |char(1)|
|  con_ativid |char(1)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  dt_encerra |date|
|  nu_lote_i  |char(7)|

### Febre Maculosa

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  febre      |char(1)|
|  cefaleia   |char(1)|
|  abdominal  |char(1)|
|  mialgia    |char(1)|
|  nausea     |char(1)|
|  exantema   |char(1)|
|  diarreia   |char(1)|
|  ictericia  |char(1)|
|  hiperemia  |char(1)|
|  hepatome   |char(1)|
|  petequias  |char(1)|
|  hemorrag   |char(1)|
|  linfadeno  |char(1)|
|  convulsao  |char(1)|
|  necrose    |char(1)|
|  prostacao  |char(1)|
|  choque     |char(1)|
|  coma       |char(1)|
|  hemorragi  |char(1)|
|  respirato  |char(1)|
|  oliguria   |char(1)|
|  outros     |char(1)|
|  outro_esp  |char(30)|
|  carrapato  |char(1)|
|  capivara   |char(1)|
|  cao_gato   |char(1)|
|  bovino     |char(1)|
|  equinos    |char(1)|
|  outroani   |char(1)|
|  anim_esp   |char(30)|
|  foi_mata   |char(1)|
|  hospital   |char(1)|
|  dtinterna  |date|
|  dtalta     |date|
|  coufhosp   |char(2)|
|  comunhosp  |char(6)|
|  diagno_lab |char(1)|
|  dts1       |date|
|  dts2       |date|
|  igm_s1     |char(1)|
|  tit_igm_s1 |numeric(5)|
|  igg_s1     |char(1)|
|  tit_igg_s1 |numeric(5)|
|  igm_s2     |char(1)|
|  tit_igm_s2 |numeric(5)|
|  igg_s2     |char(1)|
|  tit_igg_s2 |numeric(5)|
|  dt_coleta  |date|
|  dt_digita  |date|
|  isolamento |char(1)|
|  agente     |char(30)|
|  histopato  |char(1)|
|  imunohist  |char(1)|
|  classi_fin |char(2)|
|  criterio   |char(1)|
|  diag_desca |char(30)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  ambiente   |char(1)|
|  doenca_tra |char(1)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  dt_encerra |date|

### Febre Tifoide

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  contato    |char(1)|
|  cont_out   |char(30)|
|  suge_vincu |char(1)|
|  vinc_out   |char(30)|
|  assintomat |char(1)|
|  febre      |char(1)|
|  cefaleia   |char(1)|
|  diarreia   |char(1)|
|  constipa   |char(1)|
|  astenia    |char(1)|
|  tosse      |char(1)|
|  espleno    |char(1)|
|  tifica     |char(1)|
|  nauseas    |char(1)|
|  vomitos    |char(1)|
|  dor        |char(1)|
|  pulso      |char(1)|
|  entero     |char(1)|
|  perfura    |char(1)|
|  comp_out   |char(1)|
|  comp_out_d |char(30)|
|  atendiment |char(1)|
|  dt_atende  |date|
|  uf         |char(2)|
|  municipio  |char(6)|
|  sangue     |char(1)|
|  fezes      |char(1)|
|  urina      |char(1)|
|  antibiotic |char(1)|
|  dt_hemo1   |date|
|  hemo_r1    |char(1)|
|  hemo_d_1   |char(30)|
|  dt_hemo2   |date|
|  hemo_r2    |char(1)|
|  hemo_d_2   |char(30)|
|  dt_hemo3   |date|
|  hemo_r3    |char(1)|
|  hemo_d_3   |char(30)|
|  dt_uro     |date|
|  uro_r1     |char(1)|
|  uro_d      |char(30)|
|  dt_uro2    |date|
|  uro_r2     |char(1)|
|  uro_d_2    |char(30)|
|  dt_uro3    |date|
|  uro_r3     |char(1)|
|  uro_d_3    |char(30)|
|  dt_copro1  |date|
|  copro_r1   |char(1)|
|  copro_d_1  |char(30)|
|  dt_copro2  |date|
|  copro_r2   |char(1)|
|  copro_d_2  |char(30)|
|  dt_copro3  |date|
|  copro_r3   |char(1)|
|  copro_d_3  |char(30)|
|  dt_outr1   |date|
|  outr_r1    |char(1)|
|  outr_d1    |char(30)|
|  dt_outr2   |date|
|  outr_r2    |char(1)|
|  outr_d2    |char(30)|
|  dt_outr3   |date|
|  outr_r3    |char(1)|
|  outr_d3    |char(30)|
|  clorafen   |char(1)|
|  ampicilina |char(1)|
|  sulfa      |char(1)|
|  quinolona  |char(1)|
|  ant_outr   |char(1)|
|  ant_out_d  |char(30)|
|  dias       |char(2)|
|  classi_fin |char(2)|
|  criterio   |char(2)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  doenca_tra |char(1)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  dt_encerra |date|
|  dt_desc1   |date|
|  dt_desc2   |date|
|  dt_desc3   |date|
|  co_uf_des1 |char(2)|
|  co_uf_des2 |char(2)|
|  co_uf_des3 |char(2)|
|  mun_des1   |char(6)|
|  mun_des2   |char(6)|
|  mun_des3   |char(6)|
|  pa_des1    |numeric(4)|
|  pa_des2    |numeric(4)|
|  pa_des3    |numeric(4)|
|  ds_trans1  |char(30)|
|  ds_trans2  |char(30)|
|  ds_trans3  |char(30)|

### Hanseníase

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_diag    |date|
|  sem_diag   |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  nduplic_n  |char(1)|
|  dt_digita  |date|
|  cs_flxret  |char(1)|
|  flxrecebi  |char(1)|
|  migrado_w  |char(1)|
|  id_ocupa_n |char(6)|
|  nu_lesoes  |numeric(2)|
|  formaclini |char(1)|
|  avalia_n   |char(1)|
|  classopera |char(1)|
|  modoentr   |char(1)|
|  mododetect |char(1)|
|  baciloscop |char(1)|
|  dtinictrat |date|
|  esq_ini_n  |char(1)|
|  contreg    |numeric(2)|
|  nervosafet |numeric(2)|
|  ufatual    |char(2)|
|  id_muni_at |char(6)|
|  dt_noti_at |date|
|  id_unid_at |char(7)|
|  ufresat    |char(2)|
|  muniresat  |char(6)|
|  dtultcomp  |date|
|  classatual |char(1)|
|  aval_atu_n |char(1)|
|  esq_atu_n  |char(1)|
|  dose_receb |numeric(2)|
|  epis_racio |char(1)|
|  dtmudesq   |date|
|  contexam   |numeric(2)|
|  dtalta_n   |date|
|  tpalta_n   |char(1)|
|  in_vincula |char(1)|

### Hantaviroses

|Coluna|Tipo|
|:---:|:-------:|
|  nu_notific |char(7)|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  cs_suspeit |char(1)|
|  in_aids    |char(1)|
|  cs_mening  |char(1)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(7)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dtdiasinac |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(7)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  dt_invest  |date|
|  id_ocupa_n |char(5)|
|  treina_mil |char(1)|
|  desmata_n  |char(1)|
|  expo_n     |char(1)|
|  moagem_n   |char(1)|
|  dormiu_n   |char(1)|
|  transpo_n  |char(1)|
|  pescou_n   |char(1)|
|  roedor_n   |char(1)|
|  outra_ativ |char(1)|
|  outr_ati_d |char(40)|
|  cli_dt_ate |date|
|  cli_febre  |char(1)|
|  cli_tosse  |char(1)|
|  cli_dispne |char(1)|
|  cli_respi  |char(1)|
|  cli_cefale |char(1)|
|  cli_mial_g |char(1)|
|  cli_lombar |char(1)|
|  cli_abdomi |char(1)|
|  cli_hipote |char(1)|
|  cli_choque |char(1)|
|  cli_vomito |char(1)|
|  cli_diarre |char(1)|
|  cli_toraci |char(1)|
|  cli_tontur |char(1)|
|  cli_cardia |char(1)|
|  cli_renal  |char(1)|
|  cli_neurol |char(1)|
|  cli_asteni |char(1)|
|  cli_petequ |char(1)|
|  cli_hemo   |char(1)|
|  cli_h_desc |char(30)|
|  cli_outros |char(1)|
|  cli_out_d  |char(30)|
|  am_sangue  |char(1)|
|  lab_hema_n |char(1)|
|  lab_trombo |char(1)|
|  lab_atipic |char(1)|
|  lab_ureia  |char(1)|
|  lab_tgo    |char(1)|
|  lab_tgo_d  |char(30)|
|  lab_tgp    |char(1)|
|  lab_tgp_d  |char(30)|
|  lab_res_b  |char(30)|
|  lab_radiol |char(1)|
|  lab_difuso |char(1)|
|  lab_local  |char(1)|
|  lab_derram |char(1)|
|  lab_colheu |char(1)|
|  dt_col_igm |date|
|  lab_igm_r  |char(1)|
|  lab_imuno  |char(1)|
|  dt_rtpcr   |date|
|  lab_rtpcr  |char(1)|
|  tra_dt_int |date|
|  tra_uf     |char(2)|
|  tra_munici |char(6)|
|  tra_hospit |char(7)|
|  tra_mecani |char(1)|
|  tra_antivi |char(1)|
|  tra_cortic |char(1)|
|  tra_cpap   |char(1)|
|  tra_vasoat |char(1)|
|  tra_antibi |char(1)|
|  tra_tratam |char(1)|
|  tra_especi |char(30)|
|  classi_fin |char(1)|
|  con_forma  |char(1)|
|  criterio   |char(1)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  con_ambien |char(1)|
|  con_amb_de |char(30)|
|  con_locali |char(2)|
|  con_local2 |char(1)|
|  evolucao   |char(1)|
|  dt_evoluc  |date|
|  con_autops |char(1)|
|  doenca_tra |char(1)|
|  dt_encerra |date|
|  dt_digita  |date|
|  dt_transus |date|
|  dt_transdm |date|
|  dt_transsm |date|
|  dt_transrm |date|
|  dt_trnasrs |date|
|  dt_transse |date|
|  nu_lote_v  |char(7)|
|  nu_lote_h  |char(7)|
|  ident_micr |char(50)|

### Leptospirose

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  nduplic_n  |char(1)|
|  dt_digita  |date|
|  cs_flxret  |char(1)|
|  flxrecebi  |char(1)|
|  migrado_w  |char(1)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  ant_cb_lam |char(1)|
|  ant_cb_cri |char(1)|
|  ant_cb_cai |char(1)|
|  ant_cb_fos |char(1)|
|  ant_cb_sin |char(1)|
|  ant_cb_pla |char(1)|
|  ant_cb_cor |char(1)|
|  ant_cb_roe |char(1)|
|  ant_cb_gra |char(1)|
|  ant_cb_ter |char(1)|
|  ant_cb_lix |char(1)|
|  ant_cb_out |char(1)|
|  ant_ou_des |char(30)|
|  ant_humano |char(1)|
|  ant_animai |char(1)|
|  cli_dt_ate |date|
|  cli_febre  |char(1)|
|  cli_mialgi |char(1)|
|  cli_cefale |char(1)|
|  cli_prost  |char(1)|
|  cli_conges |char(1)|
|  cli_pantur |char(1)|
|  cli_vomito |char(1)|
|  cli_diarre |char(1)|
|  cli_icteri |char(1)|
|  cli_renal  |char(1)|
|  cli_respir |char(1)|
|  cli_cardia |char(1)|
|  cli_hemopu |char(1)|
|  cli_hemorr |char(1)|
|  cli_mening |char(1)|
|  cli_outros |char(1)|
|  cli_otrdes |char(30)|
|  ate_dt_int |date|
|  ate_dt_alt |date|
|  ate_uf     |char(2)|
|  ate_munici |char(6)|
|  ate_hosp   |char(1)|
|  lab_dt_1   |date|
|  lab_elis_1 |char(1)|
|  lab_dt_2   |date|
|  lab_elis_2 |char(1)|
|  dtmicro1   |date|
|  micro1_s1  |char(30)|
|  micro1_t_1 |char(4)|
|  micro1_s_2 |char(30)|
|  micro1_t_2 |char(5)|
|  lab_micr_1 |char(1)|
|  dtmicro2   |date|
|  micro2_s1  |char(30)|
|  micro2_t_1 |char(4)|
|  micro2_s_2 |char(30)|
|  micro2_t_2 |char(4)|
|  lab_micr_2 |char(1)|
|  dtisola    |date|
|  res_isol   |char(1)|
|  dtimuno    |date|
|  res_imuno  |char(1)|
|  dt_pcr     |date|
|  res_pcr    |char(1)|
|  classi_fin |char(2)|
|  criterio   |char(2)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  con_area   |char(1)|
|  con_ambien |char(1)|
|  doenca_tra |char(1)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  dt_encerra |date|
|  dt_risco1  |date|
|  dt_risco2  |date|
|  dt_risco3  |date|
|  dt_risco4  |date|
|  co_mun_r1  |char(6)|
|  co_mun_r2  |char(6)|
|  co_mun_r3  |char(6)|
|  co_mun_r4  |char(6)|
|  co_uf_r1   |char(2)|
|  co_uf_r2   |char(2)|
|  co_uf_r3   |char(2)|
|  co_uf_r4   |char(2)|

### Malaria

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  classi_fin |char(2)|
|  at_ativida |char(2)|
|  at_lamina  |char(1)|
|  at_sintoma |char(1)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  loc_inf    |char(60)|
|  dexame     |date|
|  result     |char(2)|
|  pmm        |numeric(8)|
|  pcruz      |char(1)|
|  tra_esquem |char(2)|
|  dstraesque |char(30)|
|  dtrata     |date|
|  dt_encerra |date|

### Meningite

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  cs_mening  |char(1)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  nduplic_n  |char(1)|
|  cs_flxret  |char(1)|
|  flxrecebi  |char(1)|
|  migrado_w  |char(1)|
|  id_ocupa_n |char(6)|
|  ant_ac     |char(1)|
|  ant_dose_3 |char(2)|
|  ant_dtul_3 |date|
|  ant_bc     |char(1)|
|  ant_doses_ |numeric(2)|
|  ant_dtult_ |date|
|  ant_conj_c |char(1)|
|  ant_dose_c |numeric(2)|
|  ant_dtul_c |date|
|  ant_bcg    |char(1)|
|  ant_dose_4 |numeric(2)|
|  ant_dtul_4 |date|
|  ant_tripli |char(1)|
|  ant_dose_5 |numeric(2)|
|  ant_dtul_5 |date|
|  ant_hemo_t |char(1)|
|  ant_dose_t |numeric(2)|
|  ant_dtul_t |date|
|  ant_pneumo |char(1)|
|  ant_dose_7 |numeric(2)|
|  ant_dtul_7 |date|
|  ant_outra  |char(1)|
|  ant_ou_de  |char(30)|
|  ant_dtul_8 |date|
|  ant_aids   |char(1)|
|  ant_imuno  |char(1)|
|  ant_ira    |char(1)|
|  ant_tube   |char(1)|
|  ant_trauma |char(1)|
|  ant_inf_ho |char(1)|
|  ant_outro  |char(1)|
|  ant_outr_d |char(30)|
|  ant_cont_n |char(1)|
|  ant_secund |char(1)|
|  cli_cefale |char(1)|
|  cli_febre  |char(1)|
|  cli_vomito |char(1)|
|  cli_convul |char(1)|
|  cli_rigide |char(1)|
|  cli_kernig |char(1)|
|  cli_abaula |char(1)|
|  cli_coma   |char(1)|
|  cli_petequ |char(1)|
|  cli_outras |char(1)|
|  cli_especi |char(30)|
|  ate_hospit |char(1)|
|  ate_intern |date|
|  ate_uf_hos |char(2)|
|  ate_munici |char(6)|
|  lab_puncao |char(1)|
|  lab_dtpunc |date|
|  lab_aspect |char(1)|
|  lab_ctliqu |char(2)|
|  lab_ctlesa |char(2)|
|  lab_ctsang |char(2)|
|  lab_ctesca |char(2)|
|  lab_bcliqu |char(2)|
|  lab_bclesa |char(2)|
|  lab_bcsang |char(2)|
|  lab_bcesca |char(2)|
|  lab_ciliqu |char(2)|
|  lab_cisang |char(2)|
|  lab_agliqu |char(2)|
|  lab_agsang |char(2)|
|  lab_isliqu |char(2)|
|  lab_isfeze |char(2)|
|  lab_pcliqu |char(2)|
|  lab_pclesa |char(2)|
|  lab_pcsang |char(2)|
|  lab_pcesca |char(2)|
|  classi_fin |char(1)|
|  con_diages |char(2)|
|  cla_me_bac |char(4)|
|  cla_me_ass |char(4)|
|  cla_me_eti |char(4)|
|  criterio   |char(2)|
|  cla_sorogr |numeric(4)|
|  med_nucomu |numeric(2)|
|  med_quimio |char(1)|
|  med_dt_qui |date|
|  doenca_tra |char(1)|
|  evolucao   |char(1)|
|  med_dt_evo |date|
|  dt_encerra |date|
|  lab_hema   |numeric(5)|
|  lab_neutro |numeric(5)|
|  lab_glico  |numeric(5)|
|  lab_leuco  |numeric(5)|
|  lab_eosi   |numeric(5)|
|  lab_prot   |numeric(5)|
|  lab_mono   |numeric(5)|
|  lab_linfo  |numeric(5)|
|  lab_clor   |numeric(5)|

### Peste

|Coluna|Tipo|
|:---:|:-------:|
|  nu_notific |char(7)|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  co_risco   |char(1)|
|  epi_peste  |char(1)|
|  com_pest   |char(1)|
|  sin_gang   |char(1)|
|  sin_pulm   |char(1)|
|  tratado    |char(1)|
|  criterio   |char(1)|
|  classi_fin |char(1)|
|  con_gravid |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  doenca_tra |char(1)|
|  evolucao   |char(1)|
|  dt_encerra |date|
|  con_classi |char(1)|
|  lab_esfr   |char(1)|
|  dt_s1      |date|
|  lab_hemo   |char(1)|
|  dt_s2      |date|
|  elisa1     |char(1)|
|  elisa2     |char(1)|
|  hemo_igm   |char(1)|
|  hemo_igg   |char(1)|
|  igm_t1     |char(2)|
|  igg_t2     |char(2)|
|  co_focal   |char(1)|
|  tpautocto  |char(1)|

### Raiva Humana

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  cs_zona    |char(1)|
|  id_pais    |char(4)|
|  nduplic_n  |char(1)|
|  cs_flxret  |char(1)|
|  flxrecebi  |char(1)|
|  migrado_w  |char(1)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  arranhao   |char(1)|
|  lambedura  |char(1)|
|  mordedura  |char(1)|
|  contato    |char(1)|
|  mucosa     |char(1)|
|  cabeca     |char(1)|
|  maos_n     |char(1)|
|  pes        |char(1)|
|  tronco     |char(1)|
|  superiores |char(1)|
|  inferiores |char(1)|
|  feriment_n |char(1)|
|  profundo   |char(1)|
|  superficia |char(1)|
|  dilacerant |char(1)|
|  dt_expo    |date|
|  antec_pre  |char(1)|
|  antec_pos  |char(1)|
|  num_doses  |numeric(2)|
|  dt_tr_rab  |date|
|  especie_n  |char(1)|
|  esp_out    |char(30)|
|  vacinad    |char(1)|
|  hospitaliz |char(1)|
|  dt_interna |date|
|  uf         |char(2)|
|  municipio  |char(6)|
|  aerofobia  |char(1)|
|  hidrofobi  |char(1)|
|  disfagia   |char(1)|
|  parestesi  |char(1)|
|  agressivi  |char(1)|
|  paralisia  |char(1)|
|  agitacao   |char(1)|
|  febre      |char(1)|
|  outro      |char(1)|
|  outro_des  |char(30)|
|  anti_rab   |char(1)|
|  dt_r_tra   |date|
|  doses_a    |numeric(2)|
|  dt_vac1    |date|
|  dt_vac_ult |date|
|  tra_soro   |char(1)|
|  dt_apli_so |date|
|  quantid    |numeric(3)|
|  infiltra   |char(1)|
|  imuno_dire |char(1)|
|  imuno_indi |char(1)|
|  histolog_n |char(1)|
|  prova_biol |char(1)|
|  varia_vir  |numeric(2)|
|  classi_fin |char(1)|
|  criterio   |char(1)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  doenca_tra |char(1)|
|  dt_obito   |date|
|  dt_encerra |date|
|  dt_digita  |date|

### Tetano acidental

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  tp_causa   |char(1)|
|  tp_causout |char(30)|
|  tp_localle |char(1)|
|  nu_dose    |char(1)|
|  dt_ult_dos |date|
|  tp_profila |char(1)|
|  cs_trismo  |char(1)|
|  cs_riso    |char(1)|
|  cs_opistot |char(1)|
|  cs_nuca    |char(1)|
|  cs_abdomin |char(1)|
|  cs_membros |char(1)|
|  cs_crises  |char(1)|
|  cs_sin_out |char(1)|
|  nm_sin_out |char(30)|
|  tp_origem  |char(1)|
|  cs_hospita |char(1)|
|  dt_interna |date|
|  sg_uf_inte |char(2)|
|  nm_munic_h |char(6)|
|  tp_identfi |char(1)|
|  tp_vacina  |char(1)|
|  tp_analise |char(1)|
|  classi_fin |char(1)|
|  cs_local   |char(1)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  evolucao   |char(1)|
|  dt_encerra |date|
|  dt_obito   |date|
|  dt_digita  |date|

### Tetano Neonatal

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  id_unidade |char(7)|
|  dt_sin_pri |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  num_con_n  |char(1)|
|  cs_vacteta |char(1)|
|  dt_1_dose  |date|
|  dt_2_dose  |date|
|  dt_3_dose  |date|
|  dt_reforco |date|
|  idade_mae  |numeric(3)|
|  nu_gesta   |char(1)|
|  escolmae_n |char(2)|
|  cs_nascido |char(1)|
|  no_ouparto |char(30)|
|  cs_atend_n |char(1)|
|  no_atenout |char(30)|
|  cs_sugou   |char(1)|
|  cs_mamar   |char(1)|
|  cs_trismo  |char(1)|
|  cs_nuca    |char(1)|
|  cs_choro   |char(1)|
|  cs_riso    |char(1)|
|  cs_abdomen |char(1)|
|  cs_inf_cot |char(1)|
|  cs_opistot |char(1)|
|  cs_membros |char(1)|
|  cs_crise   |char(1)|
|  cs_outros  |char(1)|
|  nm_out_sin |char(30)|
|  dt_trismo  |date|
|  cs_origem  |char(1)|
|  cs_hospita |char(1)|
|  cs_cobertu |char(1)|
|  no_coboutr |char(30)|
|  cs_vacinac |char(1)|
|  cs_cadastr |char(1)|
|  cs_divulga |char(1)|
|  cs_buscaat |char(1)|
|  cs_orienta |char(1)|
|  cs_analise |char(1)|
|  cs_outras  |char(1)|
|  no_outras  |char(30)|
|  classi_fin |char(1)|
|  ds_inf_loc |char(1)|
|  ds_inf_out |char(30)|
|  tpautocto  |char(1)|
|  coufinf    |char(2)|
|  copaisinf  |char(4)|
|  comuninf   |char(6)|
|  counidinf  |char(7)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  dt_encerra |date|
|  dt_digita  |date|
|  dt_transdm |date|

### Tuberculose

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  id_regiona |char(8)|
|  dt_diag    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_rg_resi |char(8)|
|  id_pais    |char(4)|
|  nduplic_n  |char(1)|
|  in_vincula |char(1)|
|  migrado_w  |char(1)|
|  id_ocupa_n |char(6)|
|  tratamento |char(1)|
|  institucio |char(1)|
|  raiox_tora |char(1)|
|  teste_tube |char(1)|
|  forma      |char(1)|
|  extrapu1_n |char(2)|
|  extrapu2_n |char(2)|
|  extrapul_o |char(30)|
|  agravaids  |char(1)|
|  agravalcoo |char(1)|
|  agravdiabe |char(1)|
|  agravdoenc |char(1)|
|  agravoutra |char(1)|
|  agravoutde |char(30)|
|  bacilosc_e |char(1)|
|  bacilos_e2 |char(1)|
|  bacilosc_o |char(1)|
|  cultura_es |char(1)|
|  cultura_ou |char(1)|
|  hiv        |char(1)|
|  histopatol |char(1)|
|  dt_inic_tr |date|
|  rifampicin |char(1)|
|  isoniazida |char(1)|
|  etambutol  |char(1)|
|  estreptomi |char(1)|
|  pirazinami |char(1)|
|  etionamida |char(1)|
|  outras     |char(1)|
|  outras_des |char(40)|
|  trat_super |char(1)|
|  nu_contato |numeric(2)|
|  doenca_tra |char(1)|
|  sg_uf_at   |char(2)|
|  id_munic_a |char(6)|
|  dt_noti_at |date|
|  sg_uf_2    |char(2)|
|  id_munic_2 |char(6)|
|  bacilosc_1 |char(1)|
|  bacilosc_2 |char(1)|
|  bacilosc_3 |char(1)|
|  bacilosc_4 |char(1)|
|  bacilosc_5 |char(1)|
|  bacilosc_6 |char(1)|
|  tratsup_at |char(1)|
|  dt_mudanca |date|
|  nu_comu_ex |numeric(7)|
|  situa_9_m  |char(2)|
|  situa_12_m |char(2)|
|  situa_ence |char(2)|
|  dt_encerra |date|
|  tpuninot   |char(2)|
|  pop_liber  |char(1)|
|  pop_rua    |char(1)|
|  pop_saude  |char(1)|
|  pop_imig   |char(1)|
|  benef_gov  |char(1)|
|  agravdroga |char(1)|
|  agravtabac |char(1)|
|  test_molec |char(1)|
|  test_sensi |char(1)|
|  ant_retro  |char(1)|
|  bac_apos_6 |char(1)|
|  transf     |char(1)|
|  uf_transf  |char(2)|
|  mun_transf |char(2)|

### Variola

|Coluna|Tipo|
|:---:|:-------:|
|  tp_not     |char(1)|
|  id_agravo  |char(4)|
|  dt_notific |date|
|  sem_not    |char(6)|
|  nu_ano     |char(4)|
|  sg_uf_not  |char(2)|
|  id_municip |char(6)|
|  tp_uni_ext |numeric(1)|
|  nm_uni_ext |char(254)|
|  co_uni_ext |char(15)|
|  id_unidade |char(7)|
|  id_regiona |char(8)|
|  id_rg_resi |char(8)|
|  dt_ocor    |date|
|  sem_pri    |char(6)|
|  dt_nasc    |date|
|  nu_idade_n |numeric(4)|
|  cs_sexo    |char(1)|
|  cs_gestant |char(1)|
|  cs_raca    |char(1)|
|  cs_escol_n |char(2)|
|  sg_uf      |char(2)|
|  id_mn_resi |char(6)|
|  id_pais    |char(4)|
|  nduplic    |char(1)|
|  dt_invest  |date|
|  id_ocupa_n |char(6)|
|  sit_conjug |char(1)|
|  def_trans  |char(1)|
|  def_fisica |char(1)|
|  def_mental |char(1)|
|  def_visual |char(1)|
|  def_auditi |char(1)|
|  tran_ment  |char(1)|
|  tran_comp  |char(1)|
|  def_out    |char(1)|
|  def_espec  |char(30)|
|  sg_uf_ocor |char(2)|
|  id_mn_ocor |char(6)|
|  hora_ocor  |char(5)|
|  local_ocor |char(2)|
|  local_espe |char(30)|
|  out_vezes  |char(1)|
|  les_autop  |char(1)|
|  viol_fisic |char(1)|
|  viol_psico |char(1)|
|  viol_tort  |char(1)|
|  viol_sexu  |char(1)|
|  viol_traf  |char(1)|
|  viol_finan |char(1)|
|  viol_negli |char(1)|
|  viol_infan |char(1)|
|  viol_legal |char(1)|
|  viol_outr  |char(1)|
|  viol_espec |char(30)|
|  ag_forca   |char(1)|
|  ag_enfor   |char(1)|
|  ag_objeto  |char(1)|
|  ag_corte   |char(1)|
|  ag_quente  |char(1)|
|  ag_enven   |char(1)|
|  ag_fogo    |char(1)|
|  ag_ameaca  |char(1)|
|  ag_outros  |char(1)|
|  ag_espec   |char(30)|
|  sex_assedi |char(1)|
|  sex_estupr |char(1)|
|  sex_pudor  |char(1)|
|  sex_porno  |char(1)|
|  sex_explo  |char(1)|
|  sex_outro  |char(1)|
|  sex_espec  |char(30)|
|  pen_oral   |char(1)|
|  pen_anal   |char(1)|
|  pen_vagina |char(1)|
|  proc_dst   |char(1)|
|  proc_hiv   |char(1)|
|  proc_hepb  |char(1)|
|  proc_sang  |char(1)|
|  proc_semen |char(1)|
|  proc_vagin |char(1)|
|  proc_contr |char(1)|
|  proc_abort |char(1)|
|  cons_abort |char(1)|
|  cons_grav  |char(1)|
|  cons_dst   |char(1)|
|  cons_suic  |char(1)|
|  cons_ment  |char(1)|
|  cons_comp  |char(1)|
|  cons_estre |char(1)|
|  cons_outr  |char(1)|
|  cons_espec |char(30)|
|  lesao_nat  |char(2)|
|  lesao_espe |char(30)|
|  lesao_corp |char(2)|
|  num_envolv |char(1)|
|  rel_sexual |char(1)|
|  rel_pai    |char(1)|
|  rel_mae    |char(1)|
|  rel_pad    |char(1)|
|  rel_conj   |char(1)|
|  rel_excon  |char(1)|
|  rel_namo   |char(1)|
|  rel_exnam  |char(1)|
|  rel_filho  |char(1)|
|  rel_desco  |char(1)|
|  rel_irmao  |char(1)|
|  rel_conhec |char(1)|
|  rel_cuida  |char(1)|
|  rel_patrao |char(1)|
|  rel_inst   |char(1)|
|  rel_pol    |char(1)|
|  rel_propri |char(1)|
|  rel_outros |char(1)|
|  rel_espec  |char(30)|
|  autor_sexo |char(1)|
|  autor_alco |char(1)|
|  enc_saude  |char(1)|
|  enc_tutela |char(1)|
|  enc_vara   |char(1)|
|  enc_abrigo |char(1)|
|  enc_sentin |char(1)|
|  enc_deam   |char(1)|
|  enc_dpca   |char(1)|
|  enc_deleg  |char(1)|
|  enc_mpu    |char(1)|
|  enc_mulher |char(1)|
|  enc_creas  |char(1)|
|  enc_iml    |char(1)|
|  enc_outr   |char(1)|
|  enc_espec  |char(30)|
|  rel_trab   |char(1)|
|  rel_cat    |char(1)|
|  circ_lesao |char(5)|
|  classi_fin |char(1)|
|  evolucao   |char(1)|
|  dt_obito   |date|
|  rel_mad    |char(1)|
|  tpuninot   |char(2)|
|  orient_sex |char(1)|
|  ident_gen  |char(1)|
|  viol_motiv |char(2)|
|  cicl_vid   |char(1)|
|  rede_sau   |char(1)|
|  assist_soc |char(1)|
|  rede_educa |char(1)|
|  atend_mulh |char(1)|
|  cons_tutel |char(1)|
|  cons_ido   |char(1)|
|  deleg_idos |char(1)|
|  dir_human  |char(1)|
|  mpu        |char(1)|
|  deleg_cria |char(1)|
|  deleg_mulh |char(1)|
|  deleg      |char(1)|
|  infan_juv  |char(1)|
|  defen_publ |char(1)|
|  dt_encerra |date|

## SINASC - Sistema de Informações de Nascidos Vivos

|Coluna|Tipo|Descrição|
|:---:|:-------:|:----|
| NUMERODN | C(08)| Número da DN, seqüencial por UF informante e por ano. |
| LOCNASC| C(01)| Local de ocorrência do nascimento, conforme a tabela: 9: Ignorado 1: Hospital 2: Outro Estab Saúde 3: Domicílio 4: Outros|
| CODESTAB | C(07)| Código de estabelecimento de saúde. |
| CODBAINASC | C(08)| Código Bairro nascimento. |
| CODMUNNASC | C(07)| Código do município de ocorrência.|
| IDADEMAE | C(02)| Idade da mãe em anos. |
| ESTCIVMAE| C(01)| Estado civil, conforme a tabela: 1: Solteira 2: Casada 3: Viúva 4: Separado judicialmente/Divorciado 9: Ignorado|
| ESCMAE | C(01)| Escolaridade, anos de estudoconcluídos: 1: Nenhuma 2: 1 a 3anos 3: 4 a 7anos 4: 8 a 11 anos 5: 12 emais 9:Ignorado |
| CODOCUPMAE | C(06)| Ocupação, conforme a Classificação Brasileira de Ocupações (CBO-2002). |
| QTDFILVIVO | C(02)| Número de filhos vivos. |
| QTDFILMORT | C(02)| Número de filhos mortos.|
| CODBAIRES| C(08)| Código bairro residência. |
| CODMUNRES| C(07)| Município de residência da mãe. |
| GESTACAO | C(01)| Semanas de gestação, conforme a tabela: 9: Ignorado 1: Menos de 22 semanas 2: 22 a 27semanas 3: 28 a 31semanas 4: 32 a 36semanas 5: 37 a 41semanas 6: 42 semanas e mais |
| GRAVIDEZ | C(01)| Tipo de gravidez, conforme a tabela: 9: Ignorado 1: Única 2: Dupla 3: Tripla e mais|
| PARTO| C(01)| Tipo de parto, conforme a tabela: 9: Ignorado 1: Vaginal 2: Cesáreo |
| CONSULTAS| C(01)| Número de consultas de pré-natal: 1: Nenhuma 2: de 1 a 3 3: de 4 a 6 4: 7 emais 9: Ignorado|
| DTNASC | C(08) | Data do nascimento, no formato ddmmaaaa|
| HORANASC | C(04) | Hora do nascimento |
| SEXO | C(01) | Sexo, conforme a tabela: 0: Ignorado 1: Masculino 2: Feminino|
| APGAR 1| C(02) | Apgar no primeiro minuto 00 a 10|
| APGAR 5| C(02) | Apgar no quinto minuto 00 a 10|
| RACACOR| C(01) | Raça/Cor: 1:Branca 2:Preta 3:Amarela 4: Parda 5: Indígena |
| PESO | C(04) | Peso ao nascer, em gramas. |
| IDANOMAL | C(01) | Anomalia congênita: 9-Ignorado 1=Sim 2=Não|
| CODANOMAL| (C20) | Código de malformação congênita ou anomalia cromossômica, de acordo com a CID-10. |
| DTCADASTR0 | C(08) | Data de cadastramento no sistema.|
| DTRECEBIM| C(08) | Data de recebimento no nível central, data da última atualização do registro. |
| CODINST| C(18) | Código da Instalação da geração dos Registros. |
| UFINFORM | C(02) | Código da UF que informou o registro.|


## SISPRENATAL - Sistema de Acompanhamento da Gestante

### Pre Natal
|Coluna|Tipo|
|:---:|:-------:|
|nu_ano_ges |char(4)|
|dt_atend   |char(6)|
|co_uf_ibge |char(2)|
|nu_gesta   |char(6)|
|co_gestant |char(12)|
|co_pais    |char(3)|
|nu_cns     |char(15)|
|nu_idade   |char(15)|
|nu_nis     |char(15)|
|nu_nis_rep |char(15)|
|ds_zona    |char(50)|
|qt_ab_ect  |char(3)|
|qt_ab_ger  |char(3)|
|qt_ab_mol  |char(3)|
|qt_mor_aps |char(3)|
|qt_mor_ps  |char(3)|
|qt_nsc_mor |char(3)|
|qt_nsc_viv |char(3)|
|qt_prt_cir |char(3)|
|qt_prt_for |char(3)|
|qt_prt_vag |char(3)|
|st_aux_dsl |char(1)|
|st_gra_ant |char(1)|
|st_gra_pla |char(1)|
|dt_dum     |char(8)|
|dt_dpp     |char(8)|
|co_tpo_gra |char(10)|
|co_esc_gp  |char(2)|
|co_rac_gp  |char(2)|
|co_etn_gp  |char(4)|
|co_stf_gp  |char(2)|
|co_mun_ubs |char(6)|
|qt_cons    |numeric(3)|
|qt_consult |char(3)|
|st_gestac  |char(1)|
|dt_inc     |char(8)|