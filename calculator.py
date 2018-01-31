#!/usr/bin/env python3
import sys

def tax(taxwage):

    if taxwage<=0:
        return 0
    elif 0<taxwage<=1500:
        return taxwage*0.03
    elif 1500<taxwage<=4500:
        return taxwage*0.1-105
    elif 4500<taxwage<=9000:
        return taxwage*0.2-555
    elif 9000<taxwage<=35000:
        return taxwage*0.25-1005
    elif 35000<taxwage<=55000:
        return taxwage*0.3-2755
    elif 55000<taxwage<=80000:
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


