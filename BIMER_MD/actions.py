from DatabaseManager import NewDatabaseManager
import xlrd

dbm = NewDatabaseManager(server_name='localhost', database='ALTERDATA_BIMER', logger_file_name='log_de_conexao.log')


class Actions:
    # Monta a insert com os dados necessários para tabela.
    insert_query = '''INSERT INTO NATUREZALANCAMENTO(IdNaturezaLancamento,
                                                 CdChamada, 
                                                 NmNaturezaLancamento, 
                                                 StBaixaInclusao, 
                                                 StBaixaVencimento, 
                                                 StIntegraContabilInclusao, 
                                                 StIntegraContabilBaixa, 
                                                 CdClassificacao, 
                                                 TpNaturezaLancamento, 
                                                 StCobraTaxaBancaria, 
                                                 StNaoGeraTitulo, 
                                                 StAtivo, 
                                                 StDobraValorDespesaViagem)
                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''


    def insert_table_from_xls():
        dados = dbm.select_data('SET NOCOUNT ON; SELECT * FROM NATUREZALANCAMENTO')
        i = 1
        for data in dados:
            i=int(data[1])+1

        # Importa uma lista de qualquer outra fonte que atenda os requisitos.
        dados = [{'CdClassificacao': '3.02.01.06.09.002', 'NmNaturezaLancamento': 'Natureza Criada com Python'},]

        # Percorre a lista e adiciona os VALUES ordenadamente em outra lista para usar no cursor.execute
        for row in dados:
            values = (dbm.chama_id(), str(i).zfill(6), row['NmNaturezaLancamento'],'N','N','N','N', row['CdClassificacao'], 'A','N','N','N',0)
            dbm.insert_sql_data(insert_query, values)

        print('Registro inserido com sucesso!')
        

    def import_sheet():

        # file_location="C:\pythonprog\xxx.xlsv"
        # workbook=xlrd.open_workbook(file_location)
        workbook = xlrd.open_workbook('NATUREZAS_LANCAMENTO.xlsx')
        sheet = workbook.sheet_by_index(0)

        dados = list()

        for row in range(1, sheet.nrows):
            my_dict = {}
            my_dict['cd_chamada'] = sheet.cell_value(row,1)
            my_dict['nm_natureza'] = sheet.cell_value(row,2)
            my_dict['cd_classificacao'] = sheet.cell_value(row,7)
            my_dict['tp_natureza'] = sheet.cell_value(row,8)
            my_dict['st_ativo'] = sheet.cell_value(row,14)

            dados.append(my_dict)

        # Percorre a lista e adiciona os VALUES ordenadamente em outra lista para usar no cursor.execute
        i = 1
        for row in dados:
            values = (dbm.chama_id(), str(i).zfill(6), row['nm_natureza'], 'N', 'N', 'N', 'N', row['cd_classificacao'], row['tp_natureza'], 'N', 'N', row['st_ativo'], 0)
            dbm.insert_sql_data(insert_query, values)
            i += 1

        print('Registro inserido com sucesso!')


    def insert_table2(nmNatureza, 
                     classificacaoNatureza, 
                     baixaInclusao, 
                     baixaVencimento,
                     integraContabilidadeInclusao,
                     integraContabilidadeBaixa,
                     cobraTaxaBancaria,
                     naoGerarTituloFinanceiro,
                     naturezaAtiva,
                     naturezaAnalitica):

        mlist = [nmNatureza, 
                classificacaoNatureza, 
                baixaInclusao, 
                baixaVencimento,
                integraContabilidadeInclusao,
                integraContabilidadeBaixa,
                cobraTaxaBancaria,
                naoGerarTituloFinanceiro,
                naturezaAtiva,
                naturezaAnalitica]       

        def boostr(x):
            if (type(x) == bool) & (x == True):
                return 'S'
            elif (type(x) == bool) & (x == False):
                return 'N'

            return x

        x = map(boostr, mlist)

        #convert the map into a list, for readability:
        #print(list(x))
        
        
        						 
    def insert_table(nmNatureza, 
                     classificacaoNatureza, 
                     baixaInclusao, 
                     baixaVencimento,
                     integraContabilidadeInclusao,
                     integraContabilidadeBaixa,
                     cobraTaxaBancaria,
                     naoGerarTituloFinanceiro,
                     naturezaAtiva,
                     naturezaAnalitica):

        print(baixaInclusao, '<<<<<<<<<<====================')

        insert_query = '''INSERT INTO NATUREZALANCAMENTO(IdNaturezaLancamento,
                                                 CdChamada, 
                                                 NmNaturezaLancamento, 
                                                 StBaixaInclusao, 
                                                 StBaixaVencimento, 
                                                 StIntegraContabilInclusao, 
                                                 StIntegraContabilBaixa, 
                                                 CdClassificacao, 
                                                 TpNaturezaLancamento, 
                                                 StCobraTaxaBancaria, 
                                                 StNaoGeraTitulo, 
                                                 StAtivo, 
                                                 StDobraValorDespesaViagem)
                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''		
		
        dados = dbm.select_data('SET NOCOUNT ON; SELECT * FROM NATUREZALANCAMENTO')
        i = 1
        for data in dados:
            i=int(data[1])+1
            
        print(insert_query)
         
        # values = (dbm.chama_id(), str(i).zfill(6), row['NmNaturezaLancamento'],'N','N','N','N', row['CdClassificacao'], 'A','N','N','N',0)
        #values = (dbm.chama_id(), str(i).zfill(6), 'VIA FUNCAO','N','N','N','N', '999999', 'A','N','N','N',0)
        values = (dbm.chama_id(), str(i).zfill(6), nmNatureza, 
                                                   baixaInclusao, 
                                                   baixaVencimento,
                                                   integraContabilidadeInclusao,
                                                   integraContabilidadeBaixa, 
                                                   classificacaoNatureza, 
                                                   'A',
                                                   cobraTaxaBancaria,
                                                   naoGerarTituloFinanceiro,
                                                   naturezaAtiva,0)


        dbm.insert_sql_data(insert_query, values)

        print('Registro inserido com sucesso!')    
        

    def delete_table():
        nm_natureza_lancamento = 'Natureza Criada com Python'
        dbm.delete_sql_data("DELETE FROM NATUREZALANCAMENTO WHERE NMNATUREZALANCAMENTO=?", (nm_natureza_lancamento))
        print('Excluídos os registros com descrição = ', (nm_natureza_lancamento), '\n')


    def delete_all_table():
        dbm.delete_all_sql_data("DELETE FROM NATUREZALANCAMENTO")
        print('Excluídos todos os registros da tabela ', '\n')


    def update_table():
        dados = dbm.select_data('SET NOCOUNT ON; SELECT * FROM NATUREZALANCAMENTO')
        i = 0
        for data in list(dados):
            nm_natureza_lancamento = dbm.cap_name(data[2])
            id_natureza_lancamento = data[0]
            if data[8] == 'A':
                dbm.update_sql_data("UPDATE NATUREZALANCAMENTO SET NMNATUREZALANCAMENTO=? WHERE IDNATUREZALANCAMENTO=?", (nm_natureza_lancamento, id_natureza_lancamento))
            else:
                dbm.update_sql_data("UPDATE NATUREZALANCAMENTO SET NMNATUREZALANCAMENTO=? WHERE IDNATUREZALANCAMENTO=?", (nm_natureza_lancamento.upper(), id_natureza_lancamento))
            i+=1
        print('\n')
        print('Atualizados todos os {} registros da tabela.'.format(i))


    def list_table():
        output = dbm.select_data('SET NOCOUNT ON; SELECT * FROM NATUREZALANCAMENTO')
        # print(output)
        return output

