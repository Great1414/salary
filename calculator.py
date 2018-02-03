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
    comployeedata = []
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
# tax_oneself
              
	    if taxwage<=0:
    	        tax_self = 0
	    elif taxwage<=1500:
   		tax_self = taxwage*0.03
	    elif taxwage<=4500:
   		tax_sel f= taxwage*0.1-105
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
        comployeedata = [oneid[0], oneid[1], sstax, tax_self, get_money ]
        return comployeedata

    #output csv file
    def export(self, default = 'csv')
        result = self.calc_fordata()
        with open(sys.argv[3]) as f:
            writer = csv.writer(f)
            writer.writerows(result)

#exec

if __name__=='__main__':   
 
    for arg in sys.argv[1:]:
        print('{0},{1},{2:.2f},{3:.2f},{4:.2f}'.format(self.calc_fordata()))

