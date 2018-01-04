#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     12/01/2017
# Copyright:   (c) user 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import math
import random
num_of_population=10
def f(x): # x is an array, t
    valid_cost = 288 * x[0]+ 141 * x[1] + 0.01 * x[1] ** 2+ 217 * x[2]-30000<=0
    valid_time = sum(x) - 100.0 <= 0
    valid_x = (x[0]>=0) and (x[1]>=0) and (x[2]>=0)
    valid = valid_cost and valid_time and valid_x
    return (13.0 * np.sqrt(x[0])+ 2.0 * x[1]+ 20.0 * (np.log( x[2] + 1.0)) - 0.002*(288.0 * x[0]+ 141.0 * x[1] + 0.01 * x[2] ** 2.0+ 217.0 * x[2])  - 2.0 * (100.0 - sum(x)  ) ) if valid else 0.0

def num_to_gene(num):
    x_gene_string_temp = np.binary_repr(num, width=6)       # Change int x into a binary number
    x_gene_string = ""                                      # Make the binary number to Right-to-Left (the left boolian represents "1"
    for i in x_gene_string_temp:
        x_gene_string = i+x_gene_string
    return x_gene_string

def x_to_chromozom(x):
    x_chromozom=""
    for i in range(len(x)):
        gene_string = int_to_gene(x[i])
        x_chromozom += gene_string
    return np.array(map(int,x_chromozom))

# print str(x_to_chromozom(x))

def gene_to_x(gene):
    x=0
    for i in range(len(gene)):
        if gene[i]==1:
            x+= 2**i
    return x

def chromozom_to_x(chromozom):
    x = np.array([0, 0, 0])
    j=0
    for i in [0,6,12]:
        x[j]= gene_to_x(chromozom[i:i+6])
        j+= 1
    return x


def random_chromozom():
    temp=np.array([0,0,0])
    for i in range(3):
        temp[i]= random.randint(0,63)
    return x_to_chromozom(temp)


def init_pop(num_of_population):
    list_of_chromozoms= []
    for i in range(num_of_population):
        list_of_chromozoms.append(random_chromozom())
    return list_of_chromozoms

pop_test= init_pop(num_of_population)

def calc_fit(pop):
    optimizatiom_value_list=[]
    sum_list=0
    p_list=[]
    for i in range(len(pop)):
        temp=chromozom_to_x(pop[i])
        temp2=0
        if f(temp)>=0:
            temp2=f(temp)
        else:
            temp2=1/abs(f(temp))
        optimizatiom_value_list.append(temp2)
        sum_list+= temp2
    for i in range(len(pop)):
        p_list.append(optimizatiom_value_list[i]/sum_list)
    return p_list

calc_fit_test= calc_fit(pop_test)
print str(calc_fit_test)

def mutate(chromozom):
    for i in range(len(chromozom)):
        temp_random= random.randint(1,6)
        if temp_random==1:
            if chromozom[i]==0:
                chromozom[i]=1
            else:
                chromozom[i]=0
    return chromozom

def select_parents(pop):
    list_of_parents=[]
    for i in range(len(pop)/2):
        first_parent= np.random.choice(5,1,replace=False,p=calc_fit(pop))











