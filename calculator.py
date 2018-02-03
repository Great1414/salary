#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import csv

#argv
class Args(object):

    def __init__(self):
        self.args = self.sys.argv[1:]

#configfile

class Config(Args):

    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {}
        with open(sys.argv[1]) as confignews:
            for one_config in confignews:
                news = one_config.strip().split('=')[0]
                nums = one_config.strip().split('=')[1]
                config = dict(zip(news,nums))
        return config

#user data
class UserData(Args):
    
    def __init__(self):
        self.userdata = self._read_users_data
    
    def _read_users_data(self):     
        userdata = {}
        with open(syis.argv[2]) as datanews:
            for one_data in datanews:
                idnum = one_data.strip().split('=')[0]
                wage = one_data.strip().split('=')[1]
                userdata = (idnum.wage)
        return userdata


#tax_income
class IncomeTax():
    #salary after tax
    def calc_fordata(self):
    #social security tax
    for oneid in userdata._read_user_data:
        if oneid[1] < config._read_config('JiShuL'):
            sstax = config._read_config('JiShuL')*0.165
        elif  oneid[1] > config._read_config('JiShuH'):
            sstax = config._read_config('JiShuH')*0.165
        else:
            sstax = oneid[1]*0.165

    #tax for oneself
def tax(taxwage):

    if taxwage<=0:
        return 0
    elif taxwage<=1500:
        return taxwage*0.03
    elif taxwage<=4500:
        return taxwage*0.1-105
    elif taxwage<=9000:
        return taxwage*0.2-555
    elif taxwage<=35000:
        return taxwage*0.25-1005
    elif taxwage<=55000:
        return taxwage*0.3-2755
    elif taxwage<=80000:
        return taxwage*0.35-5505
    else:
        return taxwage*0.45-13505

if __name__=='__main__':    
    for arg in sys.argv[1:]:
        try:    
            num = int(arg.split(':')[0])
            wage = int(arg.split(':')[1])
        except:
            print('Parameter Error')
        taxwage =  wage*(1-0.165)-3500
        money = wage*(1-0.165) - tax(taxwage)
        #salary = dict(num = money)
        #for key, value in salary.items():
        print('{}:{:.2f}'.format(num,money))

#exec
