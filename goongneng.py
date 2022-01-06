import copy
import time
import xlrd as xlrd
import xlwt as xlwt

from xlutils import copy

class Gongn:
    def __init__(self):
        pass
    def Write_xl(self,xl_name,location_x,info1,info2,info3,info4,save_name):#写入表格信息
        book = xlwt.Workbook()
        sheet = book.add_sheet(xl_name)
        sheet.write(location_x,0,info1)
        sheet.write(location_x, 1, info2)
        sheet.write(location_x, 2, info3)
        sheet.write(location_x, 3, info4)
        book.save(save_name)
    def Read_xl(self,xl_name,sheet_id):#读取表格信息
        book = xlrd.open_workbook(xl_name)
        #sheet = book.sheet_by_name("zhaogou")#表名打开
        sheet = book.sheet_by_index(sheet_id)#sheet_id打开
        names = book.sheet_names()
        data = sheet.cell(0,0).value
        ty = sheet.cell(0,0).ctype
        print(data)

    def change_xl(self,xl_name,location_x,info1,info2,info3,info4,save_name):#,info,,location_y
        rb = xlrd.open_workbook(xl_name)
        wb = copy.copy(rb)
        #wb.get_sheet(0)
        sheet = wb.get_sheet(0)
        #sheet.write(location_x,location_y,info)
        sheet.write(location_x, 0, info1)
        sheet.write(location_x, 1, info2)
        sheet.write(location_x, 2, info3)
        sheet.write(location_x, 3, info4)
        #sheet.write(0,0,"zhao")
        wb.save(save_name)
        # data = sheet.cell(0, 0).value
        # print(data)

    def Get_time(self):
        tm = time.localtime(time.time())
        #print("{0}年{1}月{2}日 {3}: {4}:{5}".format(tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec))
        t = ("{0}年{1}月{2}日 {3}: {4}:{5}".format(tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec))
        return t
        #print(now_time)
# if __name__ =="__main__":
#     g = Gongn()
#     g.Write_xl()
#     g.Read_xl()
#     g.change_xl()
#     g.Get_time()