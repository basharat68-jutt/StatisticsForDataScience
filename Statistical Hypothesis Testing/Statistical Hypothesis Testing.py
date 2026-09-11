"""Z Test"""
#Example-1
"""A teacher claims that the mean score of students in his class
is greater than 82 with a standard deviation  of 120.if a 
sample of 81 students was selected with a mean score of 90."""
#sample data k through ye ptaa krna hai k population data k bary jo bola gea tha bo sahi hai k nehein

import scipy.stats as st
import numpy as np
print(st.norm.ppf(0.95)) #yahan z ki value direct he nikaaal di hai

s_x = 90
p_u = 82
p_std = 20
n = 81
ap = 0.05

z_cal = (s_x - p_u)/(p_std/np.sqrt(n))
z_table = st.norm.ppf(1-ap)

if z_table < z_cal:
    print("Ha  is right")
else:
    print("H0 is right")

"""Example-2"""
#Scenario: imagin you work for an e-commerce company, and your team is responsible for
# analyzing customer purchase data. You want to determine wheather a new website design
# has led to a significant increase in the average purchase amount compared to the old design.

#Data: You have collected data from a random sample of 30 customers who made purchase
#  on the old website design and 30 customers who made purchase on the new design.
#  You have the sample mean, sample strandard deviation and sample sizes for both
#  groups.

old_design_data = np.array([45.2,42.8,38.9,43.5,41.0,44.6,40.5,42.7,39.8,41.4,44.3,39.7,42.1,40.6,43.0,42.2,41.5,39.6,44.0,43.1,38.7,43.9,42.0,41.9,42.8,43.7,41.3,40.9,42.5,41.6])
new_design_data = np.array([48.5,49.1,50.2,47.8,48.7,49.9,48.0,50.5,49.8,49.6,48.2,48.9,49.7,50.3,49.4,50.1,48.6,48.3,49.0,50.0,48.4,49.3,49.5,48.8,50.6,50.4,48.1,49.2,50.7,50.8])
print(len(new_design_data),len(old_design_data))
pop_std = 2.5
n_sample = 30
apl = 0.05
mean_new = np.mean(new_design_data)
mean_old = np.mean(old_design_data)
z_cal = (mean_new - mean_old)/ (pop_std / np.sqrt(n_sample))
print(z_cal)
z_table = st.norm.ppf(1-apl)
print(z_table)

if z_cal > z_table:
    print("Ha is right")
else:
    print("H0 is right")

"""T-Test"""
#Example-1:
    #A manufacture claims that the average weight of a bag of potato chips is 150
    #grams.A sample of 25 bags is taken, and the average weightd is found to be 148
    #grams, with a standard deveation of 5 grams. Test the manufacture's claim using
    #one-tailed t-test with a signigicance level of 0.05.
#we have to find that who is telling truth a manufacturer or we?
"""
1-first step to find null hypothesis and alternative hypothesis
2-decide significant level alfa
"""

import scipy.stats as st
t_table = st.t.ppf(0.05,24) #degree of freedom(df) is 24 which is find by n-1 = 24
print(t_table)

"""Example-2"""
    #A company wnats to tesst wheter there is a difference in productivity between
    #two teams. They randomly select 20 employees from each team and record their
    #productivity scores. The mean productivity score fo team A is 80 with a standard
    #deviation of 5, while the mean procuctivity of score for team B is 75 with a
    #standard deviation of 6. Test at a 5% level of sidnificance whether there is a
    #difference productivity between the two teams.

t_table_2 = st.t.ppf(0.25,38) #here finding table value through this
print(t_table_2)

t_cal = (80-75)/(np.sqrt((25/20)+(24/20)))
print(t_cal)

"""Example-3"""
"""A company wants to test whether a new training program improves the typing
        speed of its employees. The typing speed of 20 empoyees was recorded before
        and after the training program. The data is gien below. Test at a 5% level
        of significance whether the training program has an effect on the typing
        speed of the employees"""

t_table_3 = st.t.ppf(1-0.025,19) #alfa is 0.25 and 19 is df(degree of freedom)
print(t_table_3)

before = np.array([50,60,45,65,55,70,40,75,80,65,70,60,50,55,45,75,60,50,65,70])
after = np.array([60,70,55,75,65,80,50,85,90,70,75,65,55,60,50,80,65,55,70,75])

std_a = np.std(after)
std_b = np.std(before)
mean_a = np.mean(after)
mean_b = np.mean(before)

t_cal = (mean_a-mean_b)/(np.sqrt(((std_a*std_b)/len(after))+((std_b*std_b)/len(before))))
print(t_cal)

"""Chi Square Testing"""
#Example-1
    #A fair dice is rolled 120 times and the following results are obtained
        #face1: 22 times
        #Face2: 17 times
        #Face3: 20 times
        #Face4: 26 times
        #Face5: 22 times
        #Face6: 13 times
#Test at a 5% level of significance whether the die is fair.

ob = np.array([22,17,20,26,22,13])
ex = np.array([20,20,20,20,20,20])

print(np.sum(np.square(ob-ex)/ex)) #chi square calculated value

"""Example-2"""
    #A study was conducted to investigate whether three is a relationship
    #between gender and the preferred genre of music. a sample of 235 prople
    #was selected, and the data collected is shown below. Test at a 5% level of significance
    #whether there is a significant association between gender and music preference.

row1 = np.array([40,45,25,10])
row2 = np.array([35,30,20,30])

sum_r1 = np.sum(row1)
sum_r2 = np.sum(row2)
print(sum_r1,sum_r2)

sum_col1 = row1 + row2
print(sum_col1)