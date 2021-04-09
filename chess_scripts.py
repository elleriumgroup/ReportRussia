var_russia = '1100'
var_sz = '9502'
var_obl = '1100, 9502, 0511, 1186, 1187, 0111, 1119, 1140, 1141, 1127, 1147, 1149, 1158'
var_arh = '1100'
var_rkarelia = '1186'
var_rkomi = '1187'
var_nao = '0111'
var_volog = '1119'
var_spb = '1140'
var_len = '1141'
var_kalin = '1127'
var_murm = '1147'
var_novgor = '1149'
var_pskov = '1158'
var_kval = '0000'
myear_tp = input('Введите год расчета (последние 2 цифры): ')
mperiod = input('Введите месяц расчета: ')
myear_appg = int(myear_tp) - 1

# расчет общей части
sql_chess_russia = f'''
select
	t.name as 'oblast',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,1,2),0)  as 'zar_tp',
    ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',1,1,2),0)  as 'zar_appg',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'451',3,1,2),0)  as 'zar_slob_tp',
    ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'451',3,1,2),0)  as 'zar_slob_appg',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'451',2,1,2),0)  as 'zar_slneob_tp',
    ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'451',2,1,2),0)  as 'zar_slneob_appg',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',3,1,1),0)  as 'ras_tp',
    ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',3,1,1),0)  as 'ras_appg',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'451',3,1,5),0)  as 'ras_slob_tp',
	ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'451',3,1,5),0)  as 'ras_slob_appg',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'451',2,1,5),0)  as 'ras_slneob_tp',
    ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'451',2,1,5),0)  as 'ras_slneob_appg',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,1,38) + 
	       get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,1,39) +
	       get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,1,40),0) as 'neras_tp',
    ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',1,1,38) + 
	       get_mvalue(t.code,{myear_appg},{mperiod},'494',1,1,39) +
	       get_mvalue(t.code,{myear_appg},{mperiod},'494',1,1,40),0) as 'neras_appg',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'451',3,1,10),0)  as 'neras_slob_tp',
    ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'451',3,1,10),0)  as 'neras_slob_appg',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'451',2,1,10),0)  as 'neras_slneob_tp',
    ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'451',2,1,10),0)  as 'neras_slneob_appg'
from
	oblast t
where
	t.code in ({var_obl})
order by 1;
'''

# расчет тяжких
sql_chess_russia_tg = f'''
select
	t.name                                              as 'oblast',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,2,2)     +
	       get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,3,2),0)  as 'zar_tp',
	ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',1,2,2)     +
	       get_mvalue(t.code,{myear_appg},{mperiod},'494',1,3,2),0)  as 'zar_appg',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,2,17),0)  +
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,3,17),0)  as 'ras_tp',
	ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',1,2,17),0)  +
	ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',1,3,17),0)  as 'ras_appg',
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,2,38),0) +
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,2,39),0) +
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,2,40),0) +
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,3,38),0) +
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,3,39),0) +
	ifnull(get_mvalue(t.code,{myear_tp},  {mperiod},'494',1,3,40),0) as 'neras_tp',
    ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',1,2,38),0) +
	ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',1,2,39),0) +
	ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',1,2,40),0) +
	ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',1,3,38),0) +
	ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',1,3,39),0) +
	ifnull(get_mvalue(t.code,{myear_appg},{mperiod},'494',1,3,40),0) as 'neras_appg'
from
	oblast t
where 
	t.code in ({var_obl})
'''


# расчет квалификационной части
# Квалификационная часть (Россия)
def func_chess(kod_sql, oblast):
    global var_kval
    var_kval = oblast
    if kod_sql == 1:
        sql = f'''select
            '1.Убийства' as 'kval',
	        oblast.name as 'oblast',
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,2,01) as 'zar_tp',
	        get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,2,01) as 'zar_appg',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,2,05) as 'ras_tp',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,2,12) + 
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,2,13) +  
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,2,14) as 'neras_tp'
            from oblast where oblast.code = {var_kval} order by oblast.name;
        '''
    elif kod_sql == 2:
        sql = f'''select
            '2.Тяжкий вред здоровью'  as 'kval',
	        oblast.name as 'oblast',
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,8,01) as 'zap_tp',
	        get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,8,01) as 'zar_appg',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,8,05) as 'ras_tp',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,8,12)  +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,8,13) +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,8,14)  as 'neras_tp'
            from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    elif kod_sql == 3:
        sql = f'''select
            '3.изнасилование' as 'kval',
	        oblast.name as 'oblast',
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,19,01) as 'zar_tp',
	        get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,19,01) as 'zar_appg',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,19,05) as 'ras_tp',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,19,12)  +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,19,13) +
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,19,14) as 'neras_tp'
            from oblast where oblast.code = {var_kval} order by oblast.name;
                '''
    elif kod_sql == 4:
        sql = f'''select
            '4.разбой' as 'kval',
	        oblast.name as 'oblast',
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,48,01) as 'zar_tp',
	        get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,48,01) as 'zar_appg',
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,48,05) as 'ras_tp',
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,48,12) +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,48,13) +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,48,14)  as 'neras_tp'
	        from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    elif kod_sql == 5:
        sql = f'''select
            '5.грабеж' as 'kval',
	        oblast.name as 'oblast',
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,47,01) as 'zar_tp',
	        get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,47,01) as 'zar_appg',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,47,05) as 'ras_tp',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,47,12) +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,47,13) +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,47,14)  as 'neras_tp'
            from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    elif kod_sql == 6:
        sql = f'''select
            '6.кражи' as 'kval',
	        oblast.name as 'oblast',
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,32,01) as 'zar_tp',
	        get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,32,01) as 'zar_appg',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,32,05) as 'ras_tp',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,32,12) +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,32,13) +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,32,14)  as 'neras_tp'
            from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    elif kod_sql == 7:
        sql = f'''select
            '7.мошенничество' as 'kval',
            oblast.name as 'oblast',
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,39,01) as 'zar_tp',
	        get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,39,01) as 'zar_appg',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,39,05) as 'ras_tp',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,39,12)  +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,39,13) +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,39,14) as 'neras_tp'
            from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    elif kod_sql == 8:
        sql = f'''select
            '8.хулиганства' as 'kval',
	        oblast.name as 'oblast',
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,73,01) as 'zar_tp',
	        get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,73,01) as 'zar_appg',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,73,05) as 'ras_tp',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,73,12)  +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,73,13) +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,73,14) as 'neras_tp'
            from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    elif kod_sql == 9:
        sql = f'''select
            '9.экономические' as 'kval',
	        oblast.name as 'oblast',
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,6,02) as 'zar_tp',
	        get_mvalue(oblast.code,{myear_appg},{mperiod},'494',1,6,02) as 'zar_appg',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,6,07) as 'ras_tp',
            get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,6,15)  +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,6,16) +
	        get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,6,17) as 'neras_tp'
            from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    elif kod_sql == 10:
        sql = f'''select
            '10.взяточничество' as 'kval',
	        oblast.name as 'oblast',
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,110,01),0) +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,111,01),0) +
            ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,112,01),0) +
            ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,113,01),0) as 'zar_tp',
            ifnull(get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,110,01),0) +
	        ifnull(get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,111,01),0) +
            ifnull(get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,112,01),0) +
	        ifnull(get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,113,01),0) as 'zar_appg',
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,110,05),0) +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,111,05),0) +
            ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,112,05),0) +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,113,05),0) as 'ras_tp',
            ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,110,11),0) +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,110,12),0) +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,110,13),0) +
            ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,111,11),0) +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,111,12),0) +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,111,13),0) +
            ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,112,11),0) +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,112,12),0) +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,112,13),0) +
            ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,113,11),0) +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,113,12),0) +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,113,13),0) as 'ras_appg'
            from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    elif kod_sql == 11:
        sql = f'''select
            '11.совершены на улицах' as 'kval',
            oblast.name as 'oblast',
            ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',7,1,2),0) as 'zar_tp',
            ifnull(get_mvalue(oblast.code,{myear_tp}_appg,{mperiod},'494',7,1,2),0) as 'zar_appg'
            from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    elif kod_sql == 12:
        sql = f'''select
            '12.связаны с незаконным оборотом наркотиков' as 'kval',
	        oblast.name as 'oblast',
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,18,02),0) as 'zar_tp',
            ifnull(get_mvalue(oblast.code,{myear_appg},{mperiod},'494',1,18,02),0) as 'zar_appg',
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,18,07),0) as 'ras_tp',
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,18,15),0) +
            ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,18,16),0)  +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,18,17),0)  as 'neras_tp'
            from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    elif kod_sql == 13:
        sql = f'''select
            '13.Связанных с незаконным оборотом оружия' as 'kval',
	        oblast.name as 'oblast',
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,19,02),0) as 'zar_tp',
            ifnull(get_mvalue(oblast.code,{myear_appg},{mperiod},'494',1,19,02),0) as 'zar_appg',
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,19,07),0) as 'ras_tp',
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,19,15),0) +
            ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,19,16),0)  +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',1,19,17),0)  as 'neras_tp'
            from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    elif kod_sql == 14:
        sql = f'''select
            '14.Ст. 150 и 151 УК РФ' as 'kval',
	        oblast.name as 'oblast',
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,28,01),0) as 'zar_tp',
            ifnull(get_mvalue(oblast.code,{myear_appg},{mperiod},'494',2,28,01),0) as 'zar_appg',
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,28,05),0) as 'ras_tp',
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,28,12),0) +
            ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,28,13),0)  +
	        ifnull(get_mvalue(oblast.code,{myear_tp},{mperiod},'494',2,28,14),0)  as 'neras_tp'
            from oblast where oblast.code = {var_kval} order by oblast.name;
            '''
    return sql
