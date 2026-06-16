import os
import sys
import time

import xlwings as xw

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))


def result_to_excel(result_df, file_name):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(os.path.join(BASE_DIR, r"bin\template\普通参数留痕模板.xlsx"))
    ws = wb.sheets['普通参数模板']
    last_row = ws.range('A1').end('down').row
    ws.range("A2:A" + str(last_row)).api.EntireRow.Delete()
    ws.range('A2').value = result_df.values
    wb.save(os.path.join(BASE_DIR, f'{file_name}-普通参数留痕result-' + time.strftime("%Y%m%d%H%M%S") + '.xlsx'))
    app.quit()
