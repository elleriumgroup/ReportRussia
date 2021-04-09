myear_tp   = input('Введите год расчета (последние 2 цифры): ')
mperiod    = input('Введите месяц расчета: ')
myear_appg = int(myear_tp) - 1

# Области ==============================================================================================================
# Россия области - текущий период (раздел / строка / графа)
sql_russia_tp = f'''
    select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,2),0)   as 'zar_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,3,1,2),0)   as 'zar_slob_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,2,1,2),0)   as 'zar_slneob_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,17),0)  as 'ras_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,3,1,5),0)   as 'ras_slob_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,2,1,5),0)   as 'ras_slneob_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,38) +
               get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,39) +
               get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,40),0)  as 'neras_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,3,1,10),0)  as 'neras_slob_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,2,1,10),0)  as 'neras_slneob_tp'
    from
        oblast t
    where
        t.code not in (1109,1106,9502);
'''

# Россия области - предыдущий период
sql_russia_appg = f'''
    select
        t.id as 'region',
        t.name as 'oblast_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,2),0)  as 'zar_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,3,1,2),0)  as 'zar_slob_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,2,1,2),0)  as 'zar_slneob_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,17),0)  as 'ras_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,3,1,5),0)  as 'ras_slob_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,2,1,5),0)  as 'ras_slneob_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,38) +
               get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,39) +
               get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,40),0) as 'neras_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,3,1,10),0)  as 'neras_slob_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,2,1,10),0)  as 'neras_slneob_appg'
    from
        oblast t
    where
        t.code not in (1109,1106,9502);
'''

# Россия области тяжкие составы - текущий период
sql_russiatg_tp = f'''
    select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,2)     +
               get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,2),0)  as 'zartg_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,17),0)  +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,17),0)  as 'rastg_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,38),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,39),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,40),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,38),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,39),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,40),0) as 'nerastg_tp'
    from
        oblast t
    where
        t.code not in (1109, 1106, 9502);
'''

# Россия области тяжкие составы - предыдущий период
sql_russiatg_appg = f'''
    select
        t.id as 'region',
        t.name as 'oblast_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,2)     +
               get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,2),0)  as 'zartg_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,17),0)  +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,17),0)  as 'rastg_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,38),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,39),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,40),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,38),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,39),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,40),0) as 'nerastg_appg'
    from
        oblast t
    where
        t.code not in (1109, 1106, 9502);
'''

# Россия области мошенничества - текущий период
sql_russia_mosh_tp = f'''
    select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,2,47,4),0)  as 'zar_mosh_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,1),0)  as 'ras_mosh_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,24) + 
               get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,26) +
               get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,27),0) as 'neras_mosh_tp'
    from
        oblast t
    where
        t.code not in (1109,1106,9502);
'''

# Россия области мошенничества - предыдущий период
sql_russia_mosh_appg = f'''
    select
        t.id as 'region',
        t.name as 'oblast_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,2,47,4),0)  as 'zar_mosh_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,3,47,1),0)  as 'ras_mosh_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,3,47,24) + 
               get_mvalue(t.code,{myear_appg},{mperiod},494,3,39,26) +
               get_mvalue(t.code,{myear_appg},{mperiod},494,3,39,27),0) as 'neras_mosh_appg'
    from
        oblast t
    where
        t.code not in (1109,1106,9502);
'''

# Россия области НОН - текущий период
sql_russia_non_tp = f'''
    select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,2),0)   as 'zar_non_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,17),0)  as 'ras_non_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,38) + 
               get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,39) +
               get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,40),0)  as 'neras_non_tp'
    from
        oblast t
    where
        t.code not in (1109,1106,9502);
'''

# Россия области НОН - предыдущий период
sql_russia_non_appg = f'''
    select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,2),0)   as 'zar_non_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,17),0)  as 'ras_non_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,38) + 
               get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,39) +
               get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,40),0)  as 'neras_non_appg'
    from
        oblast t
    where
        t.code not in (1109,1106,9502);
'''

# Россия области 15803Г - ТП
sql_russia_15803_tp = f'''
    select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,2,43,4),0)  as 'zar_15803_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,3,43,1),0)  as 'ras_15803_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,3,43,24) + 
               get_mvalue(t.code,{myear_tp},{mperiod},494,3,43,26) +
               get_mvalue(t.code,{myear_tp},{mperiod},494,3,43,27),0) as 'neras_15803_tp'
    from
        oblast t
    where
        t.code not in (1109,1106,9502);
'''

# Россия области 15803Г - АППГ
sql_russia_15803_appg = f'''
    select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,2,43,4),0)  as 'zar_15803_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,3,43,1),0)  as 'ras_15803_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,3,43,24) + 
               get_mvalue(t.code,{myear_appg},{mperiod},494,3,43,26) +
               get_mvalue(t.code,{myear_appg},{mperiod},494,3,43,27),0) as 'neras_15803_appg'
    from
        oblast t
    where
        t.code not in (1109,1106,9502);
'''

# Федеральные округа ===================================================================================================
# Федеральные округа - текущий период
sql_fo_tp = f'''
    select 
        t.id as 'region',
        (select okrug.name from okrug where okrug.id = t.oid) as 'oblast_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,2),0))  as 'zar_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,3,1,2),0))  as 'zar_slob_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,2,1,2),0))  as 'zar_slneob_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,17),0))  as 'ras_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,3,1,5),0))  as 'ras_slob_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,2,1,5),0))  as 'ras_slneob_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,38) + 
                   get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,39) +
                   get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,40),0)) as 'neras_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,3,1,10),0))  as 'neras_slob_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,2,1,10),0))  as 'neras_slneob_fo_tp'
    from
        oblast t
    where
        t.oid > 0 and t.code not in (1109,1106,9502)
    group by t.oid;
'''

# Федеральные округа - предыдущий период
sql_fo_appg = f'''
    select 
        t.id as 'region',
        (select okrug.name from okrug where okrug.id = t.oid) as 'oblast_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,2),0))  as 'zar_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,3,1,2),0))  as 'zar_slob_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,2,1,2),0))  as 'zar_slneob_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,17),0))  as 'ras_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,3,1,5),0))  as 'ras_slob_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,2,1,5),0))  as 'ras_slneob_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,38) + 
                   get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,39) +
                   get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,40),0)) as 'neras_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,3,1,10),0))  as 'neras_slob_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,2,1,10),0))  as 'neras_slneob_fo_appg'
    from
        oblast t
    where
        t.oid > 0 and t.code not in (1109,1106,9502)
    group by t.oid;
'''

# Федеральные округа тяжкие составы - текущий период
sql_fotg_tp = f'''
    select
        t.id as 'region', 
        (select okrug.name from okrug where okrug.id = t.oid) as 'oblast_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,2),0))  +
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,2),0))  as 'zartg_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,17),0))  +
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,17),0))  as 'rastg_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,38),0)) +
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,39),0)) +
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,40),0))  +
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,38),0)) +
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,39),0)) +
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,40),0)) as 'nerastg_fo_tp'
    from
        oblast t
    where
        t.oid > 0 and t.code not in (1109,1106,9502)
    group by t.oid;
'''

# Федеральные округа тяжкие составы - предыдущий период
sql_fotg_appg = f'''
    select
        t.id as 'region', 
        (select okrug.name from okrug where okrug.id = t.oid) as 'oblast_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,2),0))  +
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,2),0))  as 'zartg_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,17),0))  +
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,17),0))  as 'rastg_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,38),0)) +
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,39),0)) +
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,40),0))  +
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,38),0)) +
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,39),0)) +
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,40),0)) as 'nerastg_fo_appg'
        from
            oblast t
        where
            t.oid > 0 and t.code not in (1109,1106,9502)
        group by t.oid;
    '''
# Федеральные округа мошенничества - текущий период
sql_fomosh_tp = f'''
    select
        t.id as 'region',
        (select okrug.name from okrug where okrug.id = t.oid) as 'oblast_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,2,47,4),0)) as 'zar_mosh_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,1),0)) as 'ras_mosh_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,24) + 
                   get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,26) +
                   get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,27),0)) as 'neras_mosh_fo_tp'
    from
        oblast t
    where
        t.oid > 0 and t.code not in (1109,1106,9502)
    group by t.oid;
'''

# Федеральные округа мошенничества - предыдущий период
sql_fomosh_appg = f'''
        select
        t.id as 'region',
        (select okrug.name from okrug where okrug.id = t.oid) as 'oblast_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,2,47,4),0)) as 'zar_mosh_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,3,47,1),0)) as 'ras_mosh_fo_appg',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,3,47,24) + 
                   get_mvalue(t.code,{myear_appg},{mperiod},494,3,47,26) +
                   get_mvalue(t.code,{myear_appg},{mperiod},494,3,47,27),0)) as 'neras_mosh_fo_appg'               
        from
            oblast t
        where
            t.oid > 0 and t.code not in (1109,1106,9502)
        group by t.oid;
'''

# ФО НОН - текущий период
sql_fo_non_tp = f'''
    select
        t.id as 'region',
        (select okrug.name from okrug where okrug.id = t.oid)              as 'oblast_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,2),0))  as 'zar_non_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,17),0)) as 'ras_non_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,38) + 
                   get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,39) +
                   get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,40),0)) as 'neras_non_fo_tp'
    from
        oblast t
    where
        t.oid > 0 and t.code not in (1109,1106,9502)
    group by t.oid;
'''

# ФО НОН - предыдущий период
sql_fo_non_appg = f'''
    select
        t.id as 'region',
        (select okrug.name from okrug where okrug.id = t.oid) as 'oblast_tp',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,2),0))  as 'zar_non_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,17),0)) as 'ras_non_fo_tp',
        sum(ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,38) + 
                   get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,39) +
                   get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,40),0)) as 'neras_non_fo_tp'
    from
        oblast t
    where
        t.oid > 0 and t.code not in (1109,1106,9502)
    group by t.oid;
'''

# Северо-Запад =========================================================================================================
# Области Северо-Запада - текущий период
sql_sz_tp = f'''
        select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,2),0)  as 'zar_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,3,1,2),0)  as 'zar_slob_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,2,1,2),0)  as 'zar_slneob_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,17),0)  as 'ras_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,3,1,5),0)  as 'ras_slob_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,2,1,5),0)  as 'ras_slneob_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,38),0) + 
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,39),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,1,40),0) as 'neras_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,3,1,10),0)  as 'neras_slob_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},451,2,1,10),0)  as 'neras_slneob_sz_tp'
        from
            oblast t
        where
            t.oid = 2;
'''

# Области Северо-Запада - предыдущий период
sql_sz_appg = f'''
        select
        t.id as 'region',
        t.name as 'oblast_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,2),0)  as 'zar_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,3,1,2),0)  as 'zar_slob_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,2,1,2),0)  as 'zar_slneob_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,17),0)  as 'ras_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,3,1,5),0)  as 'ras_slob_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,2,1,5),0)  as 'ras_slneob_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,38),0) + 
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,39),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,1,40),0) as 'neras_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,3,1,10),0)  as 'neras_slob_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},451,2,1,10),0)  as 'neras_slneob_sz_appg'
        from
            oblast t
        where
            t.oid = 2;
'''

# Области Северо-Запада тяжкие составы - текущий период
sql_sztg_tp = f'''
        select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,2),0)  +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,2),0)  as 'zartg_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,17),0)  +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,17),0)  as 'rastg_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,38),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,38),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,2,40),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,38),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,39),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,3,40),0) as 'nerastg_sz_tp'
        from
            oblast t
        where
        t.oid = 2;
    '''

# Области Северо-Запада тяжкие составы - предыдущий период
sql_sztg_appg = f'''
        select
        t.id as 'region',
        t.name as 'oblast_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,2),0)  +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,2),0)  as 'zartg_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,17),0)  +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,17),0)  as 'rastg_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,38),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,39),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,2,40),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,38),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,39),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,3,40),0) as 'nerastg_sz_appg'
        from
            oblast t
        where
        t.oid = 2;
'''

# Области Северо-Запада мошенничество - текущий период
sql_mosh_sz_tp = f'''
        select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,2,47,4),0)  as 'zar_mosh_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,1),0)  as 'ras_mosh_sz_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,24),0) + 
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,26),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,3,47,27),0) as 'neras_mosh_sz_tp'
        from 
            oblast t
        where
        t.oid = 2;
'''

# Области Северо-Запада мошенничество - предыдущий период
sql_mosh_sz_appg = f'''
        select
        t.id as 'region',
        t.name as 'oblast_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,2,47,4),0)  as 'zar_mosh_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,3,47,1),0)  as 'ras_mosh_sz_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,3,47,24),0) + 
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,3,47,26),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,3,47,27),0) as 'neras_mosh_sz_appg'
        from 
            oblast t
        where
        t.oid = 2;
'''

# С-З НОН ТП
sql_sz_non_tp = f'''
        select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,2),0)   as 'zar_sz_non_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,17),0)  as 'ras_sz_non_tp',
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,38),0) + 
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,39),0) +
        ifnull(get_mvalue(t.code,{myear_tp},{mperiod},494,1,23,40),0) as 'neras_sz_non_tp'
        from 
            oblast t
        where
        t.oid = 2;
'''

# С-З НОН АППГ
sql_sz_non_appg = f'''
        select
        t.id as 'region',
        t.name as 'oblast_tp',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,2),0)   as 'zar_sz_non_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,17),0)  as 'ras_sz_non_appg',
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,38),0) + 
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,39),0) +
        ifnull(get_mvalue(t.code,{myear_appg},{mperiod},494,1,23,40),0) as 'neras_sz_non_appg'
        from 
            oblast t
        where
        t.oid = 2;
'''
# добавить инфу по, ИКТ, 15803Г