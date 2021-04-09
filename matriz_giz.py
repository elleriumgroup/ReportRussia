import os
import pymysql as mysql
import datetime as dt

con = mysql.connect('localhost', 'root', '3151020', 'matrix_giz')

def CleanGraph():
    global g01, g02, g03, g04, g05, g06, g07, g08, g09, g10
    global g11, g12, g13, g14, g15, g16, g17, g18, g19, g20
    global g21, g22, g23, g24, g25, g26, g27, g28, g29, g30
    global g31, g32, g33, g34, g35, g36, g37, g38, g39, g40
    global g41, g42, g43, g44, g45, g46, g47, g48, g49, g50
    global g51, g52, g53, g54, g55, g56, g57, g58, g59, g60
    global g61, g62, g63, g64, g65, g66, g67, g68, g69, g70
    global g71, g72, g73, g74, g75, g76, g77, g78, g79, g80
    global g81, g82, g83, g84, g85, g86, g87, g88, g89, g90
    global g91, g92, g93, g94, g95, g96, g97, g98, g99
    g01 = g02 = g03 = g04 = g05 = g06 = g07 = g08 = g09 = g10 = '0'
    g11 = g12 = g13 = g14 = g15 = g16 = g17 = g18 = g19 = g20 = '0'
    g21 = g22 = g23 = g24 = g25 = g26 = g27 = g28 = g29 = g30 = '0'
    g31 = g32 = g33 = g34 = g35 = g36 = g37 = g38 = g39 = g40 = '0'
    g41 = g42 = g43 = g44 = g45 = g46 = g47 = g48 = g49 = g50 = '0'
    g51 = g52 = g53 = g54 = g55 = g56 = g57 = g58 = g59 = g60 = '0'
    g61 = g62 = g63 = g64 = g65 = g66 = g67 = g68 = g69 = g70 = '0'
    g71 = g72 = g73 = g74 = g75 = g76 = g77 = g78 = g79 = g80 = '0'
    g81 = g82 = g83 = g84 = g85 = g86 = g87 = g88 = g89 = g90 = '0'
    g91 = g92 = g93 = g94 = g95 = g96 = g97 = g98 = g99 = '0'

def scanline(s):
    mas = [0] * 100
    global form, r, myear, mperiod, oblast, oid

    if s[0] == '!':
        rline = s.split(' ')
        form = rline[2]               # форм
        r = rline[3]                  # раздел
        myear = rline[4]              # год
        mperiod = rline[5]            # месяц
        oid = str(rline[6].zfill(4))  # код области
    else:
        dline = s.split(' ')
        iCount = len(dline)
        for x in range(iCount):
            if x == 0:
                mas[0] = dline[x].zfill(2)
            else:
                mas[x] = int(dline[x])
    # формируем строку вставки в файл
    s = f'''insert into matrix(oid, form, myear, mperiod, r, s,
        g01, g02, g03, g04, g05, g06, g07, g08, g09, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20,
        g21, g22, g23, g24, g25, g26, g27, g28, g29, g30, g31, g32, g33, g34, g35, g36, g37, g38, g39, g40,
        g41, g42, g43, g44, g45, g46, g47, g48, g49, g50, g51, g52, g53, g54, g55, g56, g57, g58, g59, g60,
        g61, g62, g63, g64, g65, g66, g67, g68, g69, g70, g71, g72, g73, g74, g75, g76, g77, g78, g79, g80,
        g81, g82, g83, g84, g85, g86, g87, g88, g89, g90, g91, g92, g93, g94, g95, g96, g97, g98, g99) values (
                              '{oid}', {form}, {myear}, {mperiod}, {r}, {mas[0]},
                               {mas[1]},  {mas[2]},  {mas[3]},  {mas[4]},  {mas[5]},  {mas[6]},  {mas[7]},  {mas[8]},  {mas[9]},  {mas[10]},
                               {mas[11]}, {mas[12]}, {mas[13]}, {mas[14]}, {mas[15]}, {mas[16]}, {mas[17]}, {mas[18]}, {mas[19]}, {mas[20]},
                               {mas[21]}, {mas[22]}, {mas[23]}, {mas[24]}, {mas[25]}, {mas[26]}, {mas[27]}, {mas[28]}, {mas[29]}, {mas[30]},
                               {mas[31]}, {mas[32]}, {mas[33]}, {mas[34]}, {mas[35]}, {mas[36]}, {mas[37]}, {mas[38]}, {mas[39]}, {mas[40]},
                               {mas[41]}, {mas[42]}, {mas[43]}, {mas[44]}, {mas[45]}, {mas[46]}, {mas[47]}, {mas[48]}, {mas[49]}, {mas[50]},
                               {mas[51]}, {mas[52]}, {mas[53]}, {mas[54]}, {mas[55]}, {mas[56]}, {mas[57]}, {mas[58]}, {mas[59]}, {mas[60]},
                               {mas[61]}, {mas[62]}, {mas[63]}, {mas[64]}, {mas[65]}, {mas[66]}, {mas[67]}, {mas[68]}, {mas[69]}, {mas[70]},
                               {mas[71]}, {mas[72]}, {mas[73]}, {mas[74]}, {mas[75]}, {mas[76]}, {mas[77]}, {mas[78]}, {mas[79]}, {mas[80]},
                               {mas[81]}, {mas[82]}, {mas[83]}, {mas[84]}, {mas[85]}, {mas[86]}, {mas[87]}, {mas[88]}, {mas[89]}, {mas[90]},
                               {mas[91]}, {mas[92]}, {mas[93]}, {mas[94]}, {mas[95]}, {mas[96]}, {mas[97]}, {mas[98]}, {mas[99]});'''
    return s


def InsertStr(s):
    cur = con.cursor()
    cur.execute(s)
    con.commit()
    return s

def ClearZeroStr():
    cur = con.cursor()
    cur.execute('delete from matrix where s = 0;')
    con.commit()

# directory = r'c:\ReportRussia\giz'
directory = 'giz'
files = os.listdir(directory)
for file in files:
    print(str(dt.datetime.now()) + ' Начата обработка файла: ' + file)
    f = open(directory + "\\" + file)
    for line in f:
        sqlstr = scanline(line)
        InsertStr(sqlstr)
    ClearZeroStr()
    print(str(dt.datetime.now()) + ' Обработка файла: ' + file + ' закончена')