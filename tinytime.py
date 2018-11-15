# tinytime, base 60 representation for time and date
#
# Python 2 library
#
# Copyright 2018 Antti Kervinen <antti.kervinen@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms and conditions of the GNU Lesser General Public
# License, version 2.1, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St - Fifth Floor, Boston, MA
# 02110-1301 USA.

import datetime
import os
import re
import sys
import time

# 24h "0:00" == "O:00"               O
# quarters                  F              U              j
symbols60 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx'
assert len(symbols60) == 60

def int_to_tinyb60(num):
    b60digits = []
    while num > 0:
        b60digits.append(symbols60[num % 60])
        num = num / 60
    return "".join(reversed(b60digits))

def epoch_to_tinyb60(num):
    # divisor: sec, min, h, the rest
    divisor = (60, 60, 24, 60, 60, 60, 60, 60, 60)
    b60digits = []
    i = 0
    while num > 0:
        b60digits.append(symbols60[num % divisor[i]])
        num = num / divisor[i]
        i += 1
    return "".join(reversed(b60digits))

def tinyb60_to_epoch(epoch_str):
    h_m_s = tinyb60_to_int(epoch_str[-3:])
    d = tinyb60_to_int(epoch_str[:-3])
    return d*60*60*24 + h_m_s

def tinyb60_to_int(tinyb60):
    num = 0
    syms = list(tinyb60)
    k = 1
    while syms:
        sym = syms.pop()
        try:
            num += k * symbols60.index(sym)
        except ValueError:
            raise ValueError('illegal symbol in tiny60 value: %r' % (sym,))
        k *= 60
    return num

def strfclock(clock_str):
    t = tinyb60_to_int(clock_str)
    s = str(t % 60).zfill(2)
    t /= 60
    m = str(t % 60).zfill(2)
    t /= 60
    h = str(t).zfill(2)
    return "%s:%s:%s" % (h, m, s)

def strfepoch(epoch_str, fmt="%F %T"):
    if os.name == "nt":
        fmt = fmt.replace("%F", "%Y-%m-%d").replace("%T", "%H:%M:%S")
    epoch_num = tinyb60_to_epoch(epoch_str)
    return datetime.datetime.fromtimestamp(epoch_num).strftime(fmt)

def timediff(seconds):
    unit = ("s", "m", "h", "d")
    divisor = (60, 60, 24)
    res = []
    t = seconds
    res.append("%ss" % (t % 60,))
    t /= 60
    if t > 0:
        res.append("%sm" % (t % 60,))
    t /= 60
    if t > 0:
        res.append("%sh" % (t % 24,))
    t /= 24
    if t > 0:
        res.append("%sd" % (t,))
    res.reverse()
    return "".join(res)
