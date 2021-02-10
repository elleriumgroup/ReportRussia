import pandas as pd
from datetime import datetime
import os.path
import sys

# Ввод названия матрицы для обработки
myear_tp    = input('Введите год расчета (последние 2 цифры): ')
mperiod     = input('Введите месяц расчета: ')
file_matrix = myear_tp+mperiod.zfill(2)+'_RUSSIA_MATRIX.xlsx'
log_name    = 'RUSSIA_MATRIX.log'

# запись лога===========================================================================================================
def logwrite(string):
    datetimeobj = datetime.now()
    timestampstr = datetimeobj.strftime("%Y-%m-%d %H:%M:%S.%f")
    f = open(log_name, 'a')
    try:
        f.writelines(timestampstr + ' REPORT_RUSSIA: ' + string + '\\n')
    finally:
        f.close      
# ======================================================================================================================
if os.path.exists(file_matrix):
    logwrite(f'Входная матрица существует {file_matrix}, запуск расчета')
else:
    print(f'Входной файл матрицы не существует: {file_matrix}')
    logwrite(f'Входной файл матрицы не существует: {file_matrix}')
    sys.exit()
#обработка матриц

russia_oblast1      = pd.read_excel(file_matrix, sheet_name='RussiaOblast')
russia_oblast1_tg   = pd.read_excel(file_matrix, sheet_name='RussiaOblastTG')
russia_oblast_mosh1 = pd.read_excel(file_matrix, sheet_name='RussiaOblastMosh')
russia_fo1          = pd.read_excel(file_matrix, sheet_name='RussiaFO')
russia_tg_fo1       = pd.read_excel(file_matrix, sheet_name='RussiaFOTG')
russia_mosh_fo1     = pd.read_excel(file_matrix, sheet_name='RussiaFOMosh')
russia_sz1          = pd.read_excel(file_matrix, sheet_name='RussiaSZ')
russia_tg_sz1       = pd.read_excel(file_matrix, sheet_name='RussiaSZTG')
russia_mosh_sz1     = pd.read_excel(file_matrix, sheet_name='RussiaSZMosh')

#Матрица Области
russia_oblast = russia_oblast1[['rang_tp', 'rang_appg', 'oblast_tp', 'zar_tp', 'zar_appg',
                                'ras_tp', 'ras_appg', 'neras_tp', 'neras_appg', 'rask_tp', 'rask_appg']].copy()
russia_oblast.reset_index(drop=True, inplace=True)
russia_oblast.sort_values('rang_tp', axis=0, ascending=True, inplace=True)

russia_oblast_slob = russia_oblast1[['rang_slob_tp', 'rang_slob_appg', 'oblast_tp','zar_slob_tp', 'zar_slob_appg', 
                                     'ras_slob_tp', 'ras_slob_appg', 'neras_slob_tp', 'neras_slob_appg', 'rask_slob_tp', 'rask_slob_appg']].copy()
russia_oblast_slob.reset_index(drop=True, inplace=True)
russia_oblast_slob.sort_values('rang_slob_tp', axis=0, ascending=True, inplace=True)

russia_oblast_slneob = russia_oblast1[['rang_slneob_tp', 'rang_slneob_appg', 'oblast_tp','zar_slneob_tp', 'zar_slneob_appg', 
                                     'ras_slneob_tp', 'ras_slneob_appg', 'neras_slneob_tp', 'neras_slneob_appg', 'rask_slneob_tp', 'rask_slneob_appg']].copy()
russia_oblast_slneob.reset_index(drop=True, inplace=True)
russia_oblast_slneob.sort_values('rang_slneob_tp', axis=0, ascending=True, inplace=True)

russia_oblast_tg = russia_oblast1_tg[['rang_tp', 'rang_appg', 'oblast_tp', 'zartg_tp', 'zartg_appg', 'rastg_tp',
       'rastg_appg', 'nerastg_tp', 'nerastg_appg', 'rasktg_tp', 'rasktg_appg']].copy()
russia_oblast_tg.reset_index(drop=True, inplace=True)
russia_oblast_tg.sort_values('rang_tp', axis=0, ascending=True, inplace=True)

russia_oblast_mosh = russia_oblast_mosh1[['rang_tp', 'rang_appg', 'oblast_tp', 'zar_mosh_tp', 'zar_mosh_appg',
       'ras_mosh_tp', 'ras_mosh_appg', 'neras_mosh_tp', 'neras_mosh_appg', 'rask_mosh_tp', 'rask_mosh_appg']].copy()
russia_oblast_mosh.reset_index(drop=True, inplace=True)
russia_oblast_mosh.sort_values('rang_tp', axis=0, ascending=True, inplace=True)

russia_fo = russia_fo1[['rang_tp', 'rang_appg', 'oblast_tp', 'zar_fo_tp', 'zar_fo_appg',
                        'ras_fo_tp', 'ras_fo_appg', 'neras_fo_tp', 'neras_fo_appg', 'rask_fo_tp', 'rask_fo_appg']].copy()
russia_fo.reset_index(drop=True, inplace=True)
russia_fo.sort_values('rang_tp', axis=0, ascending=True, inplace=True)

russia_fo_slob = russia_fo1[['rang_slob_tp', 'rang_slob_appg', 'oblast_tp', 'zar_slob_fo_tp', 'zar_slob_fo_appg',
                             'ras_slob_fo_tp', 'ras_slob_fo_appg', 'neras_slob_fo_tp', 'neras_slob_fo_appg', 'rask_slob_fo_tp', 'rask_slob_fo_appg']].copy()
russia_fo_slob.reset_index(drop=True, inplace=True)
russia_fo_slob.sort_values('rang_slob_tp', axis=0, ascending=True, inplace=True)

russia_fo_slneob = russia_fo1[['rang_slneob_tp', 'rang_slneob_appg', 'oblast_tp', 'zar_slneob_fo_tp', 'zar_slneob_fo_appg',
                               'ras_slneob_fo_tp', 'ras_slneob_fo_appg', 'neras_slneob_fo_tp', 'neras_slneob_fo_appg', 'rask_slneob_fo_tp', 'rask_slneob_fo_appg']].copy()
russia_fo_slneob.reset_index(drop=True, inplace=True)
russia_fo_slneob.sort_values('rang_slneob_tp', axis=0, ascending=True, inplace=True)

russia_tg_fo = russia_tg_fo1[['rang_tp', 'rang_appg', 'oblast_tp', 'zartg_fo_tp', 'zartg_fo_appg',
                              'rastg_fo_tp', 'rastg_fo_appg', 'nerastg_fo_tp', 'nerastg_fo_appg',
                              'rasktg_fo_tp', 'rasktg_fo_appg']].copy()
russia_tg_fo.reset_index(drop=True, inplace=True)
russia_tg_fo.sort_values('rang_tp', axis=0, ascending=True, inplace=True)

russia_mosh_fo = russia_mosh_fo1[['rang_tp', 'rang_appg', 'oblast_tp', 'zar_mosh_fo_tp', 'zar_mosh_fo_appg',
       'ras_mosh_fo_tp', 'ras_mosh_fo_appg', 'neras_mosh_fo_tp',
       'neras_mosh_fo_appg', 'rask_mosh_fo_tp', 'rask_mosh_fo_appg']].copy()
russia_mosh_fo.reset_index(drop=True, inplace=True)
russia_mosh_fo.sort_values('rang_tp', axis=0, ascending=True, inplace=True)

russia_sz = russia_sz1[['rang_tp', 'rang_appg', 'oblast_tp', 'zar_sz_tp', 'zar_sz_appg',
                        'ras_sz_tp', 'ras_sz_appg', 'neras_sz_tp', 'neras_sz_appg', 'rask_sz_tp', 'rask_sz_appg']].copy()
russia_sz.reset_index(drop=True, inplace=True)
russia_sz.sort_values('rang_tp', axis=0, ascending=True, inplace=True)

russia_sz_slob = russia_sz1[['rang_slob_tp', 'rang_slob_appg', 'oblast_tp', 'zar_slob_sz_tp', 'zar_slob_sz_appg',
                        'ras_slob_sz_tp', 'ras_slob_sz_appg', 'neras_slob_sz_tp', 'neras_slob_sz_appg', 'rask_slob_sz_tp', 'rask_slob_sz_appg']].copy()
russia_sz_slob.reset_index(drop=True, inplace=True)
russia_sz_slob.sort_values('rang_slob_tp', axis=0, ascending=True, inplace=True)

russia_sz_slneob = russia_sz1[['rang_slneob_tp', 'rang_slneob_appg', 'oblast_tp', 'zar_slneob_sz_tp', 'zar_slneob_sz_appg',
                        'ras_slneob_sz_tp', 'ras_slneob_sz_appg', 'neras_slneob_sz_tp', 'neras_slneob_sz_appg', 'rask_slneob_sz_tp', 'rask_slob_sz_appg']].copy()
russia_sz_slneob.reset_index(drop=True, inplace=True)
russia_sz_slneob.sort_values('rang_slneob_tp', axis=0, ascending=True, inplace=True)

russia_tg_sz = russia_tg_sz1[['rang_tp', 'rang_appg', 'oblast_tp', 'zartg_sz_tp', 'zartg_sz_appg',
                              'rastg_sz_tp', 'rastg_sz_appg', 'nerastg_sz_tp', 'nerastg_sz_appg',
                              'rasktg_sz_tp', 'rasktg_sz_appg']].copy()
russia_tg_sz.reset_index(drop=True, inplace=True)
russia_tg_sz.sort_values('rang_tp', axis=0, ascending=True, inplace=True)

russia_mosh_sz = russia_mosh_sz1[['rang_tp', 'rang_appg', 'oblast_tp', 'zar_mosh_sz_tp', 'zar_mosh_sz_appg',
       'ras_mosh_sz_tp', 'ras_mosh_sz_appg', 'neras_mosh_sz_tp',
       'neras_mosh_sz_appg', 'rask_mosh_sz_tp', 'rask_mosh_sz_appg']].copy()
russia_mosh_sz.reset_index(drop=True, inplace=True)
russia_mosh_sz.sort_values('rang_tp', axis=0, ascending=True, inplace=True)

writer = pd.ExcelWriter(file_matrix[:4] + '_RUSSIA_REPORT.xlsx', engine='xlsxwriter')
try:
    russia_oblast.to_excel(writer, 'OBLAST')
    russia_oblast_slob.to_excel(writer, 'OBLAST_SLOB')
    russia_oblast_slneob.to_excel(writer, 'OBLAST_SLNEOB')
    russia_oblast_tg.to_excel(writer, 'OBLAST_TG')
    russia_oblast_mosh.to_excel(writer, 'OBLAST_MOSH')
    russia_fo.to_excel(writer,'FO')
    russia_fo_slob.to_excel(writer,'FO_SLOB')
    russia_fo_slneob.to_excel(writer,'FO_SLNEOB')
    russia_tg_fo.to_excel(writer,'FO_TG')
    russia_mosh_fo.to_excel(writer,'FO_MOSH')
    russia_sz.to_excel(writer,'SZ')
    russia_sz_slob.to_excel(writer,'SZ_SLOB')
    russia_sz_slneob.to_excel(writer,'SZ_SLNEOB')
    russia_tg_sz.to_excel(writer,'SZ_TG')
    russia_mosh_sz.to_excel(writer, 'SZ_MOSH')
finally:
    writer.save()
    print('Расчет завершен. Данные сохранены: ' + file_matrix[:4] + '_RUSSIA_REPORT.xlsx')