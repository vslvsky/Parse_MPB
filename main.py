import datetime
from get_data import *

#pd.set_option("display.max_columns", 400)
#pd.set_option("display.width", 200000)

if __name__ == '__main__':

    left = get_excel_MPB()
    right = get_product()

    #join
    result = pd.merge(left=left, right=right, on=["nmid", "techsize"])

    #выборка
    result = result[["status", "nmid", "techsize", "barcode", "price", "date_order", "date_sale", "subject", "article_name_y", "source_id"]]

    #получение даты
    currentDate = datetime.date.today()
    date = currentDate.strftime("%Y-%m-%d")

    #создание файла
    name = f"parse_MPB_{date}.xlsx"
    result.to_excel(name)