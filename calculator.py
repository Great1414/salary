#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import csv

#argv
class Args(object):

    def __init__(self):
        self.args = self.sys.argv[1:]
    def get_mark(self, option):
        index = self.args.index(option)
        return self.args[index + 1]
    @property
    def config_path(self):
        return self.get_mark('-c')
    @property
    def userdata_path(self):
        return self.get_mark('-d')
    @property
    def export_path(self):
        return self.get_mark('-o')
        
args = Args()        


#configfile

class Config(object):

    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config_path = args.config_path
        config = {}
        with open(config_path) as confignews:
            for one_config in confignews.readlines():
                news = one_config.strip().split('=')[0]
                nums = one_config.strip().split('=')[1]
                config = dict(zip(news,nums))
        return config

config = Config()

#user data
class UserData(object):
    
    def __init__(self):
        self.userdata = self._read_users_data
    
    def _read_users_data(self):
        userdata_path = args.userdata_path     
        userdata = []
        with open(userdata_path) as datanews:
            for one_data in datanews.readlines():
               # idnum = one_data.strip().split(',')[0]
               # wage = one_data.strip().split(',')[1]
               # userdata = (idnum.wage)
                idnum, wage = one_data.strip().split(',')
                userdata.append((idnum, wage))
        return userdata

def __iter__(self):
    return iter(self.userdata)


#tax_income
class IncomeTax(object):
    #comployeedata = []
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
            taxwage = oneid[1] - sstax
        return taxwage
# tax_oneself
    def tax_for_one(taxwage):        
        if taxwage<=0:
            tax_self = 0
        elif taxwage<=1500:
            tax_self = taxwage*0.03
        elif taxwage<=4500:
            tax_self= taxwage*0.1-105
        elif taxwage<=9000:
            tax_self = taxwage*0.2-555
        elif taxwage<=35000:
            tax_self =  taxwage*0.25-1005
        elif taxwage<=55000:
            tax_self = taxwage*0.3-2755
        elif taxwage<=80000:
            tax_self = taxwage*0.35-5505
        else:
            tax_self = taxwage*0.45-13505
    get_money = oneid[1] - sstax - tax_self
    comployeedata = ['{}'.oneid[0],'{}'.oneid[1],'{:.2f}'.sstax, '{:.2f}'.tax_self,'{:.2f}'.get_money ]
    return comployeedata

    #output csv file
    def export(self, default = 'csv'):
        result = self.calc_fordata()
        with open(args.export_path, 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerows(result)

#exec

if __name__=='__main__':   
    get_money = IncomeTax() 
    get_money.export()
