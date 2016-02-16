#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 file: dajarendar.py
 author: kubor
 licence: Copyright(c) 2015 Ryuichi Kubo
          released under the MIT licence.
          http://opensource.org/licenses/mit-license.php
 desc: show calendar with "dajare"
"""

from calendar import TextCalendar as cal
import datetime
import json
import os
import random
import sys

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')


def getDajare():
    """get dajare from json"""
    dajson = os.path.join(DATA_PATH, 'dajare.json')
    with open(dajson, 'rb') as f:
        daja_d = json.load(f, encoding='utf8')
        com = random.sample(daja_d.keys(), 1)[0]
        return com, daja_d[com]


def showDajarendar(com, dajare):
    """print dajarendar to stdout"""
    d = datetime.date.today()
    calendar = cal().formatmonth(d.year, d.month)
    return sys.stdout.write('{0}[{1:^18}]\n{2}\n'.format(
        calendar, com.encode('utf8'), dajare.encode('utf8')))


def main():
    com, dajare = getDajare()
    showDajarendar(com, dajare)
    sys.exit(0)

if __name__ == '__main__':
    main()
