# -*- coding: utf-8 -*-

import xlwings as xw
import pandas as pd

from . import excelUtils as uts


class Json2Excel(object):
    def __init__(self, excel_filename, json_data, sheet_name='sheet0', range_name='A1',
                 show_index=False, show_header=True, column_autofit=True,
                 columns=[]):
        self.json_data = json_data
        self.excel_filename = excel_filename
        self.sheet_name = sheet_name
        self.range_name = range_name
        self.flag_index = show_index
        self.flag_header = show_header
        self.columns = columns
        self.column_autofit = column_autofit

    def __fill_body(self, data):
        df = pd.read_json(data, orient='records')
        if self.columns:
            df = df.filter(items=self.columns, axis=1)

        xw.Book(self.excel_filename).sheets[self.sheet_name] \
            .range(self.range_name).options(index=self.flag_index, header=self.flag_header) \
            .value = df
        r, c = uts.split_2_number(self.range_name)
        c1 = uts.convert_to_letter(c, 0)
        c2 = uts.convert_to_letter(c + len(df.columns) - 1, 0)
        data_range_name = '{0}:{1}'.format(c1, c2)
        if self.column_autofit:
            xw.Book(self.excel_filename).sheets[self.sheet_name].range(
                data_range_name).columns.autofit()

    def make(self, title_callback=None, body_callback=None):
        data = self.json_data
        if title_callback is not None:
            title_callback(self, data[0])

        if body_callback is not None:
            body_callback(self, data)
        else:
            self.__fill_body(data)
