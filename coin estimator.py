import pandas as pd

#print('Please select "g" or "oz"')
metric = input()

dict = {'Coin':['pennies', 'nickles', 'dimes', 'quarters'],
               'Grams':[2.5, 5, 2.268, 5.67],
               'Ounces':[0,0,0,0],
               'Number':[0,0,0,0],
               'In Each Wrapper':[50,40,50,40],
               'Wrappers Needed':[0,0,0,0],
               'Total Value':[0,0,0,0]
}

pd_dict = pd.DataFrame(dict)

print(pd_dict.loc['pennies','grams'])


#for key in dict:
#    print('What is the weight of your ' + key + '?')
#    userWeight[key] = input()
#weight_pd = pd.DataFrame(ouncesWeight)
#print(weight_pd)