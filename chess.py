# Расчет отчета Шахматка
import pymysql as mysql
import pandas as pd
from datetime import datetime
import chess_scripts as cs

xls_file   = 'CHESS_MATRIX.xlsx'
log_name   = 'CHESS_MATRIX.log'
# запись лога===========================================================================================================
def logwrite(string):
    datetimeobj = datetime.now()
    timestampstr = datetimeobj.strftime("%Y-%m-%d %H:%M:%S.%f")
    f = open(log_name, 'a')
    try:
        f.writelines(timestampstr + ' REPORT_CHESS: ' + string + '\\n')
    finally:
        f.close
# ======================================================================================================================
# подключаем БД (mysql)
con = mysql.connect('localhost', 'root', '3151020', 'matrix_giz')
# расчет общей части шахматки
chess_russia = pd.read_sql(cs.sql_chess_russia, con, index_col='oblast')
chess_russia['zar_tp']            = pd.to_numeric((chess_russia['zar_tp']))
chess_russia['zar_appg']          = pd.to_numeric((chess_russia['zar_appg']))
chess_russia['zar_slob_tp']       = pd.to_numeric((chess_russia['zar_slob_tp']))
chess_russia['zar_slob_appg']     = pd.to_numeric((chess_russia['zar_slob_appg']))
chess_russia['zar_slneob_tp']     = pd.to_numeric((chess_russia['zar_slneob_tp']))
chess_russia['zar_slneob_appg']   = pd.to_numeric((chess_russia['zar_slneob_appg']))
chess_russia['ras_tp']            = pd.to_numeric((chess_russia['ras_tp']))
chess_russia['ras_appg']          = pd.to_numeric((chess_russia['ras_appg']))
chess_russia['ras_slob_tp']       = pd.to_numeric((chess_russia['ras_slob_tp']))
chess_russia['ras_slob_appg']     = pd.to_numeric((chess_russia['ras_slob_appg']))
chess_russia['ras_slneob_tp']     = pd.to_numeric((chess_russia['ras_slneob_tp']))
chess_russia['ras_slneob_appg']   = pd.to_numeric((chess_russia['ras_slneob_appg']))
chess_russia['neras_tp']          = pd.to_numeric((chess_russia['neras_tp']))
chess_russia['neras_appg']        = pd.to_numeric((chess_russia['neras_appg']))
chess_russia['neras_slob_tp']     = pd.to_numeric((chess_russia['neras_slob_tp']))
chess_russia['neras_slob_appg']   = pd.to_numeric((chess_russia['neras_slob_appg']))
chess_russia['neras_slneob_tp']   = pd.to_numeric((chess_russia['neras_slneob_tp']))
chess_russia['neras_slneob_appg'] = pd.to_numeric((chess_russia['neras_slneob_appg']))
chess_russia['rask_tp']           = chess_russia['ras_tp'] / (chess_russia['ras_tp'] + chess_russia['neras_tp']) * 100
chess_russia['rask_appg']         = chess_russia['ras_appg'] / (chess_russia['ras_appg'] + chess_russia['neras_appg']) * 100
chess_russia['rask_slob_tp']      = chess_russia['ras_slob_tp'] / (chess_russia['ras_slob_tp'] + chess_russia['neras_slob_tp']) * 100
chess_russia['rask_slob_appg']    = chess_russia['ras_slob_appg'] / (chess_russia['ras_slob_appg'] + chess_russia['neras_slob_appg']) * 100
chess_russia['rask_slneob_tp']    = chess_russia['ras_slneob_tp'] / (chess_russia['ras_slneob_tp'] + chess_russia['neras_slneob_tp']) * 100
chess_russia['rask_slneob_appg']  = chess_russia['ras_slneob_appg'] / (chess_russia['ras_slneob_appg'] + chess_russia['neras_slneob_appg']) * 100
chess_russia['zar_abs']           = (chess_russia['zar_tp'] - chess_russia['zar_appg']) / chess_russia['zar_tp'] * 100
chess_russia['zar_slob_abs']      = (chess_russia['zar_slob_tp'] - chess_russia['zar_slob_appg']) / chess_russia['zar_slob_tp'] * 100
chess_russia['zar_slneob_abs']    = (chess_russia['zar_slneob_tp'] - chess_russia['zar_slneob_appg']) / chess_russia['zar_slneob_tp'] * 100
chess_russia['ras_abs']           = (chess_russia['ras_tp'] - chess_russia['ras_appg']) / chess_russia['ras_tp'] * 100
chess_russia['ras_slob_abs']      = (chess_russia['ras_slob_tp'] - chess_russia['ras_slob_appg']) / chess_russia['ras_slob_tp'] * 100
chess_russia['ras_slneob_abs']    = (chess_russia['ras_slneob_tp'] - chess_russia['ras_slneob_appg']) / chess_russia['ras_slneob_tp'] * 100
chess_russia['neras_abs']         = (chess_russia['neras_tp'] - chess_russia['neras_appg']) / chess_russia['neras_tp'] * 100
chess_russia['neras_slob_abs']    = (chess_russia['neras_slob_tp'] - chess_russia['neras_slob_appg']) / chess_russia['neras_slob_tp'] * 100
chess_russia['neras_slneob_abs']  = (chess_russia['neras_slneob_tp'] - chess_russia['neras_slneob_appg']) / chess_russia['neras_slneob_tp'] * 100
chess_russia_out = chess_russia[['zar_tp', 'zar_abs', 'zar_slob_tp', 'zar_slob_abs', 'zar_slneob_tp', 'zar_slneob_abs',
                                 'ras_tp', 'ras_abs', 'ras_slob_tp', 'ras_slob_abs', 'ras_slneob_tp', 'ras_slneob_abs',
                                 'neras_tp', 'neras_abs', 'neras_slob_tp', 'neras_slob_abs', 'neras_slneob_tp', 'neras_slneob_abs',
                                 'rask_tp', 'rask_appg', 'rask_slob_tp', 'rask_slob_appg', 'rask_slneob_tp', 'rask_slneob_appg']].copy()
# расчет общей части шахматки - тяжкие
chess_russia_tg = pd.read_sql(cs.sql_chess_russia_tg, con, index_col='oblast')
chess_russia_tg['zar_tp']            = pd.to_numeric((chess_russia_tg['zar_tp']))
chess_russia_tg['zar_appg']          = pd.to_numeric((chess_russia_tg['zar_appg']))
chess_russia_tg['ras_tp']            = pd.to_numeric((chess_russia_tg['ras_tp']))
chess_russia_tg['ras_appg']          = pd.to_numeric((chess_russia_tg['ras_appg']))
chess_russia_tg['neras_tp']          = pd.to_numeric((chess_russia_tg['neras_tp']))
chess_russia_tg['neras_appg']        = pd.to_numeric((chess_russia_tg['neras_appg']))
chess_russia_tg['rask_tp']           = chess_russia_tg['ras_tp'] / (chess_russia_tg['ras_tp'] + chess_russia_tg['neras_tp']) * 100
chess_russia_tg['rask_appg']         = chess_russia_tg['ras_appg'] / (chess_russia_tg['ras_appg'] + chess_russia_tg['neras_appg']) * 100
chess_russia_tg['zar_abs']           = (chess_russia_tg['zar_tp'] - chess_russia_tg['zar_appg']) / chess_russia_tg['zar_tp'] * 100
chess_russia_tg['ras_abs']           = (chess_russia_tg['ras_tp'] - chess_russia_tg['ras_appg']) / chess_russia_tg['ras_tp'] * 100
chess_russia_tg['neras_abs']         = (chess_russia_tg['neras_tp'] - chess_russia_tg['neras_appg']) / chess_russia_tg['neras_tp'] * 100
chess_russia_tg_out = chess_russia_tg[['zar_tp', 'zar_abs', 'ras_tp', 'ras_abs', 'neras_tp', 'neras_abs', 'rask_tp', 'rask_appg']].copy()

# расчет квалификационной части
# Россия
#print(cs.func_chess(14, cs.var_arh))

# вывод в файлы
writer = pd.ExcelWriter(cs.myear_tp + cs.mperiod.zfill(2) + '_' + xls_file, engine='xlsxwriter')
chess_russia_out.to_excel(writer, 'CHESS_RUSSIA_TP')
chess_russia_tg_out.to_excel(writer, 'CHESS_RUSSIA_TG_TP')
writer.save()