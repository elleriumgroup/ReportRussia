# импортируем библиотеки
import pymysql as mysql
import pandas as pd
from datetime import datetime
import matrix_scripts as ms

# подключаем БД (mysql)
con = mysql.connect('localhost', 'root', '3151020', 'matrix_giz')
# объявляем пользовательские переменные
xls_file   = 'RUSSIA_MATRIX.xlsx'
log_name   = 'RUSSIA_MATRIX.log'
deep_log=1

# запись лога===========================================================================================================
def logwrite(string):
    datetimeobj = datetime.now()
    timestampstr = datetimeobj.strftime("%Y-%m-%d %H:%M:%S.%f")
    f = open(log_name, 'a')
    try:
        f.writelines(timestampstr + ' REPORT_RUSSIA_MATRIX: ' + string + '\n')
    finally:
        f.close
# ======================================================================================================================
# основные скрипты
# ======================================================================================================================
logwrite(f'===========================================================================')
logwrite(f'Начало обработки отчета. Год расчета: {ms.myear_tp}. Период расчета: {ms.mperiod}')
# ======================================================================================================================
# Преобразование данных для дальнейшей работы
logwrite('Преобразование данных для дальнейшей работы')
# ======================================================================================================================
# Россия-области-ТП
russia_oblast_tp                                 = pd.read_sql(ms.sql_russia_tp, con, index_col = 'region')
russia_oblast_tp['zar_tp']                       = pd.to_numeric(russia_oblast_tp['zar_tp'])
russia_oblast_tp['zar_slob_tp']                  = pd.to_numeric(russia_oblast_tp['zar_slob_tp'])
russia_oblast_tp['zar_slneob_tp']                = pd.to_numeric(russia_oblast_tp['zar_slneob_tp'])
russia_oblast_tp['ras_tp']                       = pd.to_numeric(russia_oblast_tp['ras_tp'])
russia_oblast_tp['ras_slob_tp']                  = pd.to_numeric(russia_oblast_tp['ras_slob_tp'])
russia_oblast_tp['ras_slneob_tp']                = pd.to_numeric(russia_oblast_tp['ras_slneob_tp'])
russia_oblast_tp['neras_tp']                     = pd.to_numeric(russia_oblast_tp['neras_tp'])
russia_oblast_tp['neras_slob_tp']                = pd.to_numeric(russia_oblast_tp['neras_slob_tp'])
russia_oblast_tp['neras_slneob_tp']              = pd.to_numeric(russia_oblast_tp['neras_slneob_tp'])
russia_oblast_tp['rask_tp']                      = russia_oblast_tp['ras_tp'] / (russia_oblast_tp['ras_tp'] + russia_oblast_tp['neras_tp']) * 100
russia_oblast_tp['rask_slob_tp']                 = russia_oblast_tp['ras_slob_tp'] / (russia_oblast_tp['ras_slob_tp'] + russia_oblast_tp['neras_slob_tp']) * 100
russia_oblast_tp['rask_slneob_tp']               = russia_oblast_tp['ras_slneob_tp'] / (russia_oblast_tp['ras_slneob_tp'] + russia_oblast_tp['neras_slneob_tp']) * 100
# Россия-области-АППГ
russia_oblast_appg                               = pd.read_sql(ms.sql_russia_appg, con, index_col = 'region')
russia_oblast_appg['zar_appg']                   = pd.to_numeric(russia_oblast_appg['zar_appg'])
russia_oblast_appg['zar_slob_appg']              = pd.to_numeric(russia_oblast_appg['zar_slob_appg'])
russia_oblast_appg['zar_slneob_appg']            = pd.to_numeric(russia_oblast_appg['zar_slneob_appg'])
russia_oblast_appg['ras_appg']                   = pd.to_numeric(russia_oblast_appg['ras_appg'])
russia_oblast_appg['ras_slob_appg']              = pd.to_numeric(russia_oblast_appg['ras_slob_appg'])
russia_oblast_appg['ras_slneob_appg']            = pd.to_numeric(russia_oblast_appg['ras_slneob_appg'])
russia_oblast_appg['neras_appg']                 = pd.to_numeric(russia_oblast_appg['neras_appg'])
russia_oblast_appg['neras_slob_appg']            = pd.to_numeric(russia_oblast_appg['neras_slob_appg'])
russia_oblast_appg['neras_slneob_appg']          = pd.to_numeric(russia_oblast_appg['neras_slneob_appg'])
russia_oblast_appg['rask_appg']                  = russia_oblast_appg['ras_appg'] / (russia_oblast_appg['ras_appg'] + russia_oblast_appg['neras_appg']) * 100
russia_oblast_appg['rask_slob_appg']             = russia_oblast_appg['ras_slob_appg'] / (russia_oblast_appg['ras_slob_appg'] + russia_oblast_appg['neras_slob_appg']) * 100
russia_oblast_appg['rask_slneob_appg']           = russia_oblast_appg['ras_slneob_appg'] / (russia_oblast_appg['ras_slneob_appg'] + russia_oblast_appg['neras_slneob_appg']) * 100
# Россия-области-тяжкие составы-ТГ
russia_oblast_tg_tp                              = pd.read_sql(ms.sql_russiatg_tp, con, index_col = 'region')
russia_oblast_tg_tp['zartg_tp']                  = pd.to_numeric(russia_oblast_tg_tp['zartg_tp'])
russia_oblast_tg_tp['rastg_tp']                  = pd.to_numeric(russia_oblast_tg_tp['rastg_tp'])
russia_oblast_tg_tp['nerastg_tp']                = pd.to_numeric(russia_oblast_tg_tp['nerastg_tp'])
russia_oblast_tg_tp['rasktg_tp']                 = russia_oblast_tg_tp['rastg_tp'] / (russia_oblast_tg_tp['rastg_tp'] + russia_oblast_tg_tp['nerastg_tp']) * 100
# Россия-области-тяжкие составы-АППГ
russia_oblast_tg_appg                            = pd.read_sql(ms.sql_russiatg_appg, con, index_col = 'region')
russia_oblast_tg_appg['zartg_appg']              = pd.to_numeric(russia_oblast_tg_appg['zartg_appg'])
russia_oblast_tg_appg['rastg_appg']              = pd.to_numeric(russia_oblast_tg_appg['rastg_appg'])
russia_oblast_tg_appg['nerastg_appg']            = pd.to_numeric(russia_oblast_tg_appg['nerastg_appg'])
russia_oblast_tg_appg['rasktg_appg']             = russia_oblast_tg_appg['rastg_appg'] / (russia_oblast_tg_appg['rastg_appg'] + russia_oblast_tg_appg['nerastg_appg']) * 100
# Россия-области-мошенничества-ТП
russia_oblast_mosh_tp                            = pd.read_sql(ms.sql_russia_mosh_tp, con, index_col = 'region')
russia_oblast_mosh_tp['zar_mosh_tp']             = pd.to_numeric(russia_oblast_mosh_tp['zar_mosh_tp'])
russia_oblast_mosh_tp['ras_mosh_tp']             = pd.to_numeric(russia_oblast_mosh_tp['ras_mosh_tp'])
russia_oblast_mosh_tp['neras_mosh_tp']           = pd.to_numeric(russia_oblast_mosh_tp['neras_mosh_tp'])
russia_oblast_mosh_tp['rask_mosh_tp']            = russia_oblast_mosh_tp['ras_mosh_tp'] / (russia_oblast_mosh_tp['ras_mosh_tp'] + russia_oblast_mosh_tp['neras_mosh_tp']) * 100
# Россия-области-мошенничества-АППГ
russia_oblast_mosh_appg                          = pd.read_sql(ms.sql_russia_mosh_appg, con, index_col = 'region')
russia_oblast_mosh_appg['zar_mosh_appg']         = pd.to_numeric(russia_oblast_mosh_appg['zar_mosh_appg'])
russia_oblast_mosh_appg['ras_mosh_appg']         = pd.to_numeric(russia_oblast_mosh_appg['ras_mosh_appg'])
russia_oblast_mosh_appg['neras_mosh_appg']       = pd.to_numeric(russia_oblast_mosh_appg['neras_mosh_appg'])
russia_oblast_mosh_appg['rask_mosh_appg']        = russia_oblast_mosh_appg['ras_mosh_appg'] / (russia_oblast_mosh_appg['ras_mosh_appg'] + russia_oblast_mosh_appg['neras_mosh_appg']) * 100
# Федеральные-округа-ТП
russia_oblast_fo_tp                              = pd.read_sql(ms.sql_fo_tp, con, index_col='region')
russia_oblast_fo_tp['zar_fo_tp']                 = pd.to_numeric(russia_oblast_fo_tp['zar_fo_tp'])
russia_oblast_fo_tp['zar_slob_fo_tp']            = pd.to_numeric(russia_oblast_fo_tp['zar_slob_fo_tp'])
russia_oblast_fo_tp['zar_slneob_fo_tp']          = pd.to_numeric(russia_oblast_fo_tp['zar_slneob_fo_tp'])
russia_oblast_fo_tp['ras_fo_tp']                 = pd.to_numeric(russia_oblast_fo_tp['ras_fo_tp'])
russia_oblast_fo_tp['ras_slob_fo_tp']            = pd.to_numeric(russia_oblast_fo_tp['ras_slob_fo_tp'])
russia_oblast_fo_tp['ras_slneob_fo_tp']          = pd.to_numeric(russia_oblast_fo_tp['ras_slneob_fo_tp'])
russia_oblast_fo_tp['neras_fo_tp']               = pd.to_numeric(russia_oblast_fo_tp['neras_fo_tp'])
russia_oblast_fo_tp['neras_slob_fo_tp']          = pd.to_numeric(russia_oblast_fo_tp['neras_slob_fo_tp'])
russia_oblast_fo_tp['neras_slneob_fo_tp']        = pd.to_numeric(russia_oblast_fo_tp['neras_slneob_fo_tp'])
russia_oblast_fo_tp['rask_fo_tp']                = russia_oblast_fo_tp['ras_fo_tp'] / (russia_oblast_fo_tp['ras_fo_tp'] + russia_oblast_fo_tp['neras_fo_tp']) * 100
russia_oblast_fo_tp['rask_slob_fo_tp']           = russia_oblast_fo_tp['ras_slob_fo_tp'] / (russia_oblast_fo_tp['ras_slob_fo_tp'] + russia_oblast_fo_tp['neras_slob_fo_tp']) * 100
russia_oblast_fo_tp['rask_slneob_fo_tp']         = russia_oblast_fo_tp['ras_slneob_fo_tp'] / (russia_oblast_fo_tp['ras_slneob_fo_tp'] + russia_oblast_fo_tp['neras_slneob_fo_tp']) * 100
# Федеральные-округа-АППГ
russia_oblast_fo_appg                            = pd.read_sql(ms.sql_fo_appg, con, index_col='region')
russia_oblast_fo_appg['zar_fo_appg']             = pd.to_numeric(russia_oblast_fo_appg['zar_fo_appg'])
russia_oblast_fo_appg['zar_slob_fo_appg']        = pd.to_numeric(russia_oblast_fo_appg['zar_slob_fo_appg'])
russia_oblast_fo_appg['zar_slneob_fo_appg']      = pd.to_numeric(russia_oblast_fo_appg['zar_slneob_fo_appg'])
russia_oblast_fo_appg['ras_fo_appg']             = pd.to_numeric(russia_oblast_fo_appg['ras_fo_appg'])
russia_oblast_fo_appg['ras_slob_fo_appg']        = pd.to_numeric(russia_oblast_fo_appg['ras_slob_fo_appg'])
russia_oblast_fo_appg['ras_slneob_fo_appg']      = pd.to_numeric(russia_oblast_fo_appg['ras_slneob_fo_appg'])
russia_oblast_fo_appg['neras_fo_appg']           = pd.to_numeric(russia_oblast_fo_appg['neras_fo_appg'])
russia_oblast_fo_appg['neras_slob_fo_appg']      = pd.to_numeric(russia_oblast_fo_appg['neras_slob_fo_appg'])
russia_oblast_fo_appg['neras_slneob_fo_appg']    = pd.to_numeric(russia_oblast_fo_appg['neras_slneob_fo_appg'])
russia_oblast_fo_appg['rask_fo_appg']            = russia_oblast_fo_appg['ras_fo_appg'] / (russia_oblast_fo_appg['ras_fo_appg'] + russia_oblast_fo_appg['neras_fo_appg']) * 100
russia_oblast_fo_appg['rask_slob_fo_appg']       = russia_oblast_fo_appg['ras_slob_fo_appg'] / (russia_oblast_fo_appg['ras_slob_fo_appg'] + russia_oblast_fo_appg['neras_slob_fo_appg']) * 100
russia_oblast_fo_appg['rask_slneob_fo_appg']     = russia_oblast_fo_appg['ras_slneob_fo_appg'] / (russia_oblast_fo_appg['ras_slneob_fo_appg'] + russia_oblast_fo_appg['neras_slneob_fo_appg']) * 100
# Федеральные-округа-тяжкие-составы-ТП
russia_oblast_tg_fo_tp                           = pd.read_sql(ms.sql_fotg_tp, con, index_col='region')
russia_oblast_tg_fo_tp['zartg_fo_tp']            = pd.to_numeric(russia_oblast_tg_fo_tp['zartg_fo_tp'])
russia_oblast_tg_fo_tp['rastg_fo_tp']            = pd.to_numeric(russia_oblast_tg_fo_tp['rastg_fo_tp'])
russia_oblast_tg_fo_tp['nerastg_fo_tp']          = pd.to_numeric(russia_oblast_tg_fo_tp['nerastg_fo_tp'])
russia_oblast_tg_fo_tp['rasktg_fo_tp']           = russia_oblast_tg_fo_tp['rastg_fo_tp'] / (russia_oblast_tg_fo_tp['rastg_fo_tp'] + russia_oblast_tg_fo_tp['nerastg_fo_tp']) * 100
# Федеральные-округа-тяжкие-составы-АППГ
russia_oblast_tg_fo_appg                         = pd.read_sql(ms.sql_fotg_appg, con, index_col='region')
russia_oblast_tg_fo_appg['zartg_fo_appg']        = pd.to_numeric(russia_oblast_tg_fo_appg['zartg_fo_appg'])
russia_oblast_tg_fo_appg['rastg_fo_appg']        = pd.to_numeric(russia_oblast_tg_fo_appg['rastg_fo_appg'])
russia_oblast_tg_fo_appg['nerastg_fo_appg']      = pd.to_numeric(russia_oblast_tg_fo_appg['nerastg_fo_appg'])
russia_oblast_tg_fo_appg['rasktg_fo_appg']       = russia_oblast_tg_fo_appg['rastg_fo_appg'] / (russia_oblast_tg_fo_appg['rastg_fo_appg'] + russia_oblast_tg_fo_appg['nerastg_fo_appg']) * 100
# Федеральные-округа-мошенничества-ТП
russia_oblast_mosh_fo_tp                         = pd.read_sql(ms.sql_fomosh_tp, con, index_col='region')
russia_oblast_mosh_fo_tp['zar_mosh_fo_tp']       = pd.to_numeric(russia_oblast_mosh_fo_tp['zar_mosh_fo_tp'])
russia_oblast_mosh_fo_tp['ras_mosh_fo_tp']       = pd.to_numeric(russia_oblast_mosh_fo_tp['ras_mosh_fo_tp'])
russia_oblast_mosh_fo_tp['neras_mosh_fo_tp']     = pd.to_numeric(russia_oblast_mosh_fo_tp['neras_mosh_fo_tp'])
russia_oblast_mosh_fo_tp['rask_mosh_fo_tp']      = russia_oblast_mosh_fo_tp['ras_mosh_fo_tp'] / (russia_oblast_mosh_fo_tp['ras_mosh_fo_tp'] + russia_oblast_mosh_fo_tp['neras_mosh_fo_tp']) * 100
# Федеральные-округа-мошенничества-АППГ
russia_oblast_mosh_fo_appg                       = pd.read_sql(ms.sql_fomosh_appg, con, index_col='region')
russia_oblast_mosh_fo_appg['zar_mosh_fo_appg']   = pd.to_numeric(russia_oblast_mosh_fo_appg['zar_mosh_fo_appg'])
russia_oblast_mosh_fo_appg['ras_mosh_fo_appg']   = pd.to_numeric(russia_oblast_mosh_fo_appg['ras_mosh_fo_appg'])
russia_oblast_mosh_fo_appg['neras_mosh_fo_appg'] = pd.to_numeric(russia_oblast_mosh_fo_appg['neras_mosh_fo_appg'])
russia_oblast_mosh_fo_appg['rask_mosh_fo_appg']  = russia_oblast_mosh_fo_appg['ras_mosh_fo_appg'] / (russia_oblast_mosh_fo_appg['ras_mosh_fo_appg'] + russia_oblast_mosh_fo_appg['neras_mosh_fo_appg']) * 100
# Северо-Запад-ТП
russia_oblast_sz_tp                              = pd.read_sql(ms.sql_sz_tp, con, index_col='region')
russia_oblast_sz_tp['zar_sz_tp']                 = pd.to_numeric(russia_oblast_sz_tp['zar_sz_tp'])
russia_oblast_sz_tp['zar_slob_sz_tp']            = pd.to_numeric(russia_oblast_sz_tp['zar_slob_sz_tp'])
russia_oblast_sz_tp['zar_slneob_sz_tp']          = pd.to_numeric(russia_oblast_sz_tp['zar_slneob_sz_tp'])
russia_oblast_sz_tp['ras_sz_tp']                 = pd.to_numeric(russia_oblast_sz_tp['ras_sz_tp'])
russia_oblast_sz_tp['ras_slob_sz_tp']            = pd.to_numeric(russia_oblast_sz_tp['ras_slob_sz_tp'])
russia_oblast_sz_tp['ras_slneob_sz_tp']          = pd.to_numeric(russia_oblast_sz_tp['ras_slneob_sz_tp'])
russia_oblast_sz_tp['neras_sz_tp']               = pd.to_numeric(russia_oblast_sz_tp['neras_sz_tp'])
russia_oblast_sz_tp['neras_slob_sz_tp']          = pd.to_numeric(russia_oblast_sz_tp['neras_slob_sz_tp'])
russia_oblast_sz_tp['neras_slneob_sz_tp']        = pd.to_numeric(russia_oblast_sz_tp['neras_slneob_sz_tp'])
russia_oblast_sz_tp['rask_sz_tp']                = russia_oblast_sz_tp['ras_sz_tp'] / (russia_oblast_sz_tp['ras_sz_tp'] + russia_oblast_sz_tp['neras_sz_tp']) * 100
russia_oblast_sz_tp['rask_slob_sz_tp']           = russia_oblast_sz_tp['ras_slob_sz_tp'] / (russia_oblast_sz_tp['ras_slob_sz_tp'] + russia_oblast_sz_tp['neras_slob_sz_tp']) * 100
russia_oblast_sz_tp['rask_slneob_sz_tp']         = russia_oblast_sz_tp['ras_slneob_sz_tp'] / (russia_oblast_sz_tp['ras_slneob_sz_tp'] + russia_oblast_sz_tp['neras_slneob_sz_tp']) * 100
# Северо-Запад-АППГ
russia_oblast_sz_appg                            = pd.read_sql(ms.sql_sz_appg, con, index_col='region')
russia_oblast_sz_appg['zar_sz_appg']             = pd.to_numeric(russia_oblast_sz_appg['zar_sz_appg'])
russia_oblast_sz_appg['zar_slob_sz_appg']        = pd.to_numeric(russia_oblast_sz_appg['zar_slob_sz_appg'])
russia_oblast_sz_appg['zar_slneob_sz_appg']      = pd.to_numeric(russia_oblast_sz_appg['zar_slneob_sz_appg'])
russia_oblast_sz_appg['ras_sz_appg']             = pd.to_numeric(russia_oblast_sz_appg['ras_sz_appg'])
russia_oblast_sz_appg['ras_slob_sz_appg']        = pd.to_numeric(russia_oblast_sz_appg['ras_slob_sz_appg'])
russia_oblast_sz_appg['ras_slneob_sz_appg']      = pd.to_numeric(russia_oblast_sz_appg['ras_slneob_sz_appg'])
russia_oblast_sz_appg['neras_sz_appg']           = pd.to_numeric(russia_oblast_sz_appg['neras_sz_appg'])
russia_oblast_sz_appg['neras_slob_sz_appg']      = pd.to_numeric(russia_oblast_sz_appg['neras_slob_sz_appg'])
russia_oblast_sz_appg['neras_slneob_sz_appg']    = pd.to_numeric(russia_oblast_sz_appg['neras_slneob_sz_appg'])
russia_oblast_sz_appg['rask_sz_appg']            = russia_oblast_sz_appg['ras_sz_appg'] / (russia_oblast_sz_appg['ras_sz_appg'] + russia_oblast_sz_appg['neras_sz_appg']) * 100
russia_oblast_sz_appg['rask_slob_sz_appg']       = russia_oblast_sz_appg['ras_slob_sz_appg'] / (russia_oblast_sz_appg['ras_slob_sz_appg'] + russia_oblast_sz_appg['neras_slob_sz_appg']) * 100
russia_oblast_sz_appg['rask_slneob_sz_appg']     = russia_oblast_sz_appg['ras_slneob_sz_appg'] / (russia_oblast_sz_appg['ras_slneob_sz_appg'] + russia_oblast_sz_appg['neras_slneob_sz_appg']) * 100
# Северо-Запад-тяжкие-составы-ТП
russia_oblast_sztg_tp                            = pd.read_sql(ms.sql_sztg_tp, con, index_col='region')
russia_oblast_sztg_tp['zartg_sz_tp']             = pd.to_numeric(russia_oblast_sztg_tp['zartg_sz_tp'])
russia_oblast_sztg_tp['rastg_sz_tp']             = pd.to_numeric(russia_oblast_sztg_tp['rastg_sz_tp'])
russia_oblast_sztg_tp['nerastg_sz_tp']           = pd.to_numeric(russia_oblast_sztg_tp['nerastg_sz_tp'])
russia_oblast_sztg_tp['rasktg_sz_tp']            = russia_oblast_sztg_tp['rastg_sz_tp'] / (russia_oblast_sztg_tp['rastg_sz_tp'] + russia_oblast_sztg_tp['nerastg_sz_tp']) * 100
# Северо-Запад-тяжкие-составы-АППГ
russia_oblast_sztg_appg                          = pd.read_sql(ms.sql_sztg_appg, con, index_col='region')
russia_oblast_sztg_appg['zartg_sz_appg']         = pd.to_numeric(russia_oblast_sztg_appg['zartg_sz_appg'])
russia_oblast_sztg_appg['rastg_sz_appg']         = pd.to_numeric(russia_oblast_sztg_appg['rastg_sz_appg'])
russia_oblast_sztg_appg['nerastg_sz_appg']       = pd.to_numeric(russia_oblast_sztg_appg['nerastg_sz_appg'])
russia_oblast_sztg_appg['rasktg_sz_appg']        = russia_oblast_sztg_appg['rastg_sz_appg'] / (russia_oblast_sztg_appg['rastg_sz_appg'] + russia_oblast_sztg_appg['nerastg_sz_appg']) * 100
# Северо-Запад-мошенничества-ТП
russia_oblast_mosh_sz_tp                         = pd.read_sql(ms.sql_mosh_sz_tp, con, index_col='region')
russia_oblast_mosh_sz_tp['zar_mosh_sz_tp']       = pd.to_numeric(russia_oblast_mosh_sz_tp['zar_mosh_sz_tp'])
russia_oblast_mosh_sz_tp['ras_mosh_sz_tp']       = pd.to_numeric(russia_oblast_mosh_sz_tp['ras_mosh_sz_tp'])
russia_oblast_mosh_sz_tp['neras_mosh_sz_tp']     = pd.to_numeric(russia_oblast_mosh_sz_tp['neras_mosh_sz_tp'])
russia_oblast_mosh_sz_tp['rask_mosh_sz_tp']      = russia_oblast_mosh_sz_tp['ras_mosh_sz_tp'] / (russia_oblast_mosh_sz_tp['ras_mosh_sz_tp'] + russia_oblast_mosh_sz_tp['neras_mosh_sz_tp']) * 100
# Северо-Запад-мошенничества-АППГ
russia_oblast_mosh_sz_appg                       = pd.read_sql(ms.sql_mosh_sz_appg, con, index_col='region')
russia_oblast_mosh_sz_appg['zar_mosh_sz_appg']   = pd.to_numeric(russia_oblast_mosh_sz_appg['zar_mosh_sz_appg'])
russia_oblast_mosh_sz_appg['ras_mosh_sz_appg']   = pd.to_numeric(russia_oblast_mosh_sz_appg['ras_mosh_sz_appg'])
russia_oblast_mosh_sz_appg['neras_mosh_sz_appg'] = pd.to_numeric(russia_oblast_mosh_sz_appg['neras_mosh_sz_appg'])
russia_oblast_mosh_sz_appg['rask_mosh_sz_appg']  = russia_oblast_mosh_sz_appg['ras_mosh_sz_appg'] / (russia_oblast_mosh_sz_appg['ras_mosh_sz_appg'] + russia_oblast_mosh_sz_appg['neras_mosh_sz_appg']) * 100
# ======================================================================================================================
# Объединение DataFrame для преобразований
logwrite('Объединение DataFrame перед преобразованием')
# ======================================================================================================================
# объединяем Россия-области
russia_oblast  = russia_oblast_tp.join(russia_oblast_appg)
russia_oblast1 = russia_oblast[['oblast_tp',
            'zar_tp',   'zar_appg',   'zar_slob_tp',   'zar_slob_appg',   'zar_slneob_tp',   'zar_slneob_appg',
            'ras_tp',   'ras_appg',   'ras_slob_tp',   'ras_slob_appg',   'ras_slneob_tp',   'ras_slneob_appg',
            'neras_tp', 'neras_appg', 'neras_slob_tp', 'neras_slob_appg', 'neras_slneob_tp', 'neras_slneob_appg',
            'rask_tp',  'rask_appg',  'rask_slob_tp',  'rask_slob_appg',  'rask_slneob_tp',  'rask_slneob_appg']].copy()
# объединяем Россия-области тяжкие
russia_oblast_tg  = russia_oblast_tg_tp.join(russia_oblast_tg_appg)
russia_oblast1_tg = russia_oblast_tg[['oblast_tp',
            'zartg_tp',   'zartg_appg',
            'rastg_tp',   'rastg_appg',
            'nerastg_tp', 'nerastg_appg',
            'rasktg_tp',  'rasktg_appg']] .copy()
# объединяем Россия-области мошенничества
russia_oblast_mosh  = russia_oblast_mosh_tp.join(russia_oblast_mosh_appg)
russia_oblast_mosh1 = russia_oblast_mosh[['oblast_tp',
            'zar_mosh_tp', 'zar_mosh_appg',
            'ras_mosh_tp', 'ras_mosh_appg',
            'neras_mosh_tp', 'neras_mosh_appg',
            'rask_mosh_tp', 'rask_mosh_appg']].copy()
# объединяем Федеральные округа
russia_fo = russia_oblast_fo_tp.join(russia_oblast_fo_appg)
russia_fo1 = russia_fo[['oblast_tp',
            'zar_fo_tp',   'zar_fo_appg',   'zar_slob_fo_tp',   'zar_slob_fo_appg',   'zar_slneob_fo_tp',   'zar_slneob_fo_appg',
            'ras_fo_tp',   'ras_fo_appg',   'ras_slob_fo_tp',   'ras_slob_fo_appg',   'ras_slneob_fo_tp',   'ras_slneob_fo_appg',
            'neras_fo_tp', 'neras_fo_appg', 'neras_slob_fo_tp', 'neras_slob_fo_appg', 'neras_slneob_fo_tp', 'neras_slneob_fo_appg',
            'rask_fo_tp',  'rask_fo_appg',  'rask_slob_fo_tp',  'rask_slob_fo_appg',  'rask_slneob_fo_tp',  'rask_slneob_fo_appg']].copy()
# объединяем Федеральные округа-тяжкие
russia_tg_fo = russia_oblast_tg_fo_tp.join(russia_oblast_tg_fo_appg)
russia_tg_fo1 = russia_tg_fo[['oblast_tp',
            'zartg_fo_tp',   'zartg_fo_appg',
            'rastg_fo_tp',   'rastg_fo_appg',
            'nerastg_fo_tp', 'nerastg_fo_appg',
            'rasktg_fo_tp',  'rasktg_fo_appg']].copy()
# объединяем Федеральные округа-мошенничества
russia_mosh_fo = russia_oblast_mosh_fo_tp.join(russia_oblast_mosh_fo_appg)
russia_mosh_fo1 = russia_mosh_fo[['oblast_tp',
            'zar_mosh_fo_tp',   'zar_mosh_fo_appg',
            'ras_mosh_fo_tp',   'ras_mosh_fo_appg',
            'neras_mosh_fo_tp', 'neras_mosh_fo_appg',
            'rask_mosh_fo_tp',  'rask_mosh_fo_appg']].copy()
# объединяем Северо-Запад
russia_sz = russia_oblast_sz_tp.join(russia_oblast_sz_appg)
russia_sz1 = russia_sz[['oblast_tp',
        'zar_sz_tp',   'zar_sz_appg',   'zar_slob_sz_tp',   'zar_slob_sz_appg',   'zar_slneob_sz_tp',   'zar_slneob_sz_appg',
        'ras_sz_tp',   'ras_sz_appg',   'ras_slob_sz_tp',   'ras_slob_sz_appg',   'ras_slneob_sz_tp',   'ras_slneob_sz_appg',
        'neras_sz_tp', 'neras_sz_appg', 'neras_slob_sz_tp', 'neras_slob_sz_appg', 'neras_slneob_sz_tp', 'neras_slneob_sz_appg',
        'rask_sz_tp',  'rask_sz_appg',  'rask_slob_sz_tp',  'rask_slob_sz_appg',  'rask_slneob_sz_tp',  'rask_slneob_sz_appg']].copy()
# объединяем Северо-Запад-тяжкие
russia_tg_sz = russia_oblast_sztg_tp.join(russia_oblast_sztg_appg)
russia_tg_sz1 = russia_tg_sz[['oblast_tp',
        'zartg_sz_tp',   'zartg_sz_appg',
        'rastg_sz_tp',   'rastg_sz_appg',
        'nerastg_sz_tp', 'nerastg_sz_appg',
        'rasktg_sz_tp',    'rasktg_sz_appg']].copy()
# объединяем Северо-Запад-мошенничества
russia_mosh_sz = russia_oblast_mosh_sz_tp.join(russia_oblast_mosh_sz_appg)
russia_mosh_sz1 = russia_mosh_sz[['oblast_tp',
        'zar_mosh_sz_tp',   'zar_mosh_sz_appg',
        'ras_mosh_sz_tp',   'ras_mosh_sz_appg',
        'neras_mosh_sz_tp', 'neras_mosh_sz_appg',
        'rask_mosh_sz_tp', 'rask_mosh_sz_appg']].copy()
# ======================================================================================================================
logwrite('Добавление вычисляемых полей в матрицы расчетов')
# добавление вычисляемых полей - области
russia_oblast1['rang_tp']          = 0
russia_oblast1['rang_appg']        = 0
russia_oblast1['rang_slob_tp']     = 0
russia_oblast1['rang_slob_appg']   = 0
russia_oblast1['rang_slneob_tp']   = 0
russia_oblast1['rang_slneob_appg'] = 0
russia_oblast1_tg['rang_tp']       = 0
russia_oblast1_tg['rang_appg']     = 0
russia_oblast_mosh1['rang_tp']     = 0
russia_oblast_mosh1['rang_appg']   = 0
# добавление вычисляемых полей - федеральные округа
russia_fo1['rang_tp']              = 0
russia_fo1['rang_appg']            = 0
russia_fo1['rang_slob_tp']         = 0
russia_fo1['rang_slob_appg']       = 0
russia_fo1['rang_slneob_tp']       = 0
russia_fo1['rang_slneob_appg']     = 0
russia_tg_fo1['rang_tp']           = 0
russia_tg_fo1['rang_appg']         = 0
russia_mosh_fo1['rang_tp']         = 0
russia_mosh_fo1['rang_appg']       = 0
# добавление вычисляемых полей - Северо-Запад
russia_sz1['rang_tp']              = 0
russia_sz1['rang_appg']            = 0
russia_sz1['rang_slob_tp']         = 0
russia_sz1['rang_slob_appg']       = 0
russia_sz1['rang_slneob_tp']       = 0
russia_sz1['rang_slneob_appg']     = 0
russia_tg_sz1['rang_tp']           = 0
russia_tg_sz1['rang_appg']         = 0
russia_mosh_sz1['rang_tp']         = 0
russia_mosh_sz1['rang_appg']       = 0
# ======================================================================================================================
# Расчет рангов
logwrite('Расчет рангов')
# ======================================================================================================================
# Функция Расчет рангов
def sortirovka(df, field_name, rang_field_name):
    if deep_log == 1:
        logwrite(f'Расчет рангов по полю: {field_name}')
    df.sort_values([field_name], axis=0, ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    i = 0
    j = 1
    for row in df.iterrows():
        if deep_log == 1:
            logwrite(str(df.loc[i, 'oblast_tp']) + " -- " + str(j))
        if df.loc[i, 'oblast_tp'] != 'Всего по России':
            df.loc[i, rang_field_name] = j
            j = j + 1
        elif df.loc[i, 'oblast_tp'] == 'Всего по России':
            df.loc[i, rang_field_name] = j - .9
            j = j
        i = i + 1
# ======================================================================================================================
# сортировка 1
sortirovka(russia_oblast1, 'rask_tp', 'rang_tp')
sortirovka(russia_oblast1, 'rask_appg', 'rang_appg')
sortirovka(russia_oblast1, 'rask_slob_tp', 'rang_slob_tp')
sortirovka(russia_oblast1, 'rask_slob_appg', 'rang_slob_appg')
sortirovka(russia_oblast1, 'rask_slneob_tp', 'rang_slneob_tp')
sortirovka(russia_oblast1, 'rask_slneob_appg', 'rang_slneob_appg')
sortirovka(russia_oblast1_tg, 'rasktg_tp', 'rang_tp')
sortirovka(russia_oblast1_tg, 'rasktg_appg', 'rang_appg')
sortirovka(russia_oblast_mosh1, 'rask_mosh_tp', 'rang_tp')
sortirovka(russia_oblast_mosh1, 'rask_mosh_appg', 'rang_appg')
sortirovka(russia_fo1, 'rask_fo_tp', 'rang_tp')
sortirovka(russia_fo1, 'rask_fo_appg', 'rang_appg')
sortirovka(russia_fo1, 'rask_slob_fo_tp', 'rang_slob_tp')
sortirovka(russia_fo1, 'rask_slob_fo_appg', 'rang_slob_appg')
sortirovka(russia_fo1, 'rask_slneob_fo_tp', 'rang_slneob_tp')
sortirovka(russia_fo1, 'rask_slneob_fo_appg', 'rang_slneob_appg')
sortirovka(russia_tg_fo1, 'rasktg_fo_tp', 'rang_tp')
sortirovka(russia_tg_fo1, 'rasktg_fo_appg', 'rang_appg')
sortirovka(russia_mosh_fo1, 'rask_mosh_fo_tp', 'rang_tp')
sortirovka(russia_mosh_fo1, 'rask_mosh_fo_appg', 'rang_appg')
sortirovka(russia_sz1, 'rask_sz_tp', 'rang_tp')
sortirovka(russia_sz1, 'rask_sz_appg', 'rang_appg')
sortirovka(russia_sz1, 'rask_slob_sz_tp', 'rang_slob_tp')
sortirovka(russia_sz1, 'rask_slob_sz_appg', 'rang_slob_appg')
sortirovka(russia_sz1, 'rask_slneob_sz_tp', 'rang_slneob_tp')
sortirovka(russia_sz1, 'rask_slneob_sz_appg', 'rang_slneob_appg')
sortirovka(russia_tg_sz1, 'rasktg_sz_tp', 'rang_tp')
sortirovka(russia_tg_sz1, 'rasktg_sz_appg', 'rang_appg')
sortirovka(russia_mosh_sz1, 'rask_mosh_sz_tp', 'rang_tp')
sortirovka(russia_mosh_sz1, 'rask_mosh_sz_appg', 'rang_appg')
# ======================================================================================================================
# Окончательные действия
# ======================================================================================================================
# сортируем еще раз по 1 варианту
russia_oblast1.sort_values(['rask_tp'], axis=0, ascending=False, inplace=True)
russia_oblast1.reset_index(drop=True, inplace=True)
# сохраняем результаты в excel
logwrite('Сохраняем результаты в Excel')
writer = pd.ExcelWriter(ms.myear_tp + ms.mperiod.zfill(2) + '_' + xls_file, engine='xlsxwriter')
russia_oblast1.to_excel(writer, 'RussiaOblast')
russia_oblast1_tg.to_excel(writer, 'RussiaOblastTG')
russia_oblast_mosh1.to_excel(writer, 'RussiaOblastMosh')
russia_fo1.to_excel(writer, 'RussiaFO')
russia_tg_fo1.to_excel(writer, 'RussiaFOTG')
russia_mosh_fo1.to_excel(writer, 'RussiaFOMosh')
russia_sz1.to_excel(writer, 'RussiaSZ')
russia_tg_sz1.to_excel(writer, 'RussiaSZTG')
russia_mosh_sz1.to_excel(writer, 'RussiaSZMosh')
writer.save()
print('Расчет завершен. Отчет сохранен в файле: ' + ms.myear_tp + ms.mperiod.zfill(2) + '_' + xls_file)
logwrite('Расчет завершен. Отчет сохранен в файле: ' + ms.myear_tp + ms.mperiod.zfill(2) + '_' + xls_file)