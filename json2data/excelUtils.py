# -*- coding: utf-8 -*-

import re

import xlwings as xw

def get_sheet(file_name, sheet_name='Sheet0', is_vba=False):
    if not is_vba:
        return xw.Book(file_name).sheets[sheet_name]
    else:
        return xw.Book.caller().sheets[sheet_name]


def column_letter_to_number(letter, columnA=0):
    """
    字母列号转数字
    columnA: A列是第几列(0 or 1)? 默认0
    return: int
    """

    ab = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter0 = letter.upper()
    w = 0
    for _ in letter0:
        w *= 26
        w += ab.find(_)
    return w - 1 + columnA


def column_number_to_letter(number, columnA=0):
    """
    数字转字母列号
    columnA: A列是第几列(0 or 1)? 默认0
    return: str in upper case
    """

    ab = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = number - columnA
    x = n % 26
    if n >= 26:
        n = int(n / 26)
        return column_number_to_letter(n, 1) + ab[x + 1]
    else:
        return ab[x + 1]


def number_to_letter(row_num, col_num, columA=0):
    col = column_number_to_letter(number=col_num, columA=columA)
    return '{0}{1}'.format(col, row_num)


def split_2_number(range_name='A1'):
    row_num = get_row_number(range_name)
    col_num = get_column_number(range_name)
    return col_num, row_num


def get_column_number(range_name='A1', columA=0):
    return column_letter_to_number(get_column_name(range_name), columA)


def get_column_name(range_name='A1'):
    col = re.sub('\d', '', range_name)
    return col


def get_row_number(range_name='A1'):
    row_num = re.sub('\D', '', range_name)
    return int(row_num)
