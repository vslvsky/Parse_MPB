import pandas as pd
import DataBase_wb as dbase
import VitalityBooster as vb

select_product = """select * from "statistics".products"""
select_orders = """select date(date) as date_order, * from "statistics".orders"""

def get_excel_MPB():
    """получение данных из MPBoost"""
    data_MPB = pd.read_excel("deliveries.xlsx", sheet_name="Без группировки (NEW)")
    #переименование пустых
    dbase.Event_More.replace_none(data_MPB)
    data_MPB.columns = ["name", "lastname", "phone", "kod", "status", "nmid", "techsize", "article_name", "source_id",
                        "price", "date_order", "date_sale", "where"]
    return data_MPB

# connect to WB
wb = vb.MessengerSQL(dbase.PSLQ_jino_WB())
wb.connect()

def get_product():
    """запрос продуктов из постгреса"""
    df_product = wb.send_command(select_product)
    dbase.Event_More.conversion_integer(df_product, ["nmid"])
    return df_product