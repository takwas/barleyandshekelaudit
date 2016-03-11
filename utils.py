import openpyxl

def load_active_sheet(res=None):
    res = res if res is not None else 'sheet.xlsx'
    document_workbook = openpyxl.load_workbook(res)
    sheet = document_workbook.get_sheet_by_name(
        document_workbook.get_sheet_names()[0])
    return sheet


def get_rows(start_index, stop_index):
    sheet = load_active_sheet()

    all_data = []

    for row in range(start_index, stop_index):
        row_data = []

        for col in range(3, 6):
            row_data.append(sheet.cell(row=row, column=col).value)
        
        all_data.append(tuple(row_data))

    return all_data    
