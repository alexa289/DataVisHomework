

```python
import pandas as pd
import os

data_file = os.path.join('purchase_data.json')
data_file_pd = pd.read_json(data_file)
#data_file_pd.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
#--------------------------------Players Count
#Calculate total number of players
players_count =data_file_pd["SN"].value_counts()
#print('Total number of players:',data_file_pd["SN"].value_counts().sum())
players_total = pd.DataFrame([{'Total Players': players_count.sum()}])
#A different way to do the same thing
#data_file_pd["Gender"].value_counts().sum()

print('----------Player Count----------')
players_total
```

    ----------Player Count----------





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>780</td>
    </tr>
  </tbody>
</table>
</div>




```python
#--------------------------------Purchasing Analysis
#Calculate number of unique items
unique_items = data_file_pd['Item ID'].value_counts().count()
#print('Number of unique items:',unique_items)

#Calculate average purchase price
average_purchase_price = round(data_file_pd['Price'].mean(),2)
#print('Average Purchase Price:','$',average_purchase_price)

#Calculate total number of purchases
total_purchases = data_file_pd['Item Name'].count()
#print('Total number of purchases:',total_purchases)

#Calculate total revenue 
total_revenue = round(data_file_pd['Price'].sum(),2)
#print('Total Revenue:','$',total_revenue)

#Define Data Frame, restyle and reorder
purchasing_analysis_pd = pd.DataFrame([{"Number of unique items": unique_items,'Average Purchase Price': average_purchase_price,'Total number of purchases': total_purchases,'Total Revenue': total_revenue}])
purchasing_analysis_pd[["Number of unique items","Average Purchase Price","Total number of purchases","Total Revenue"]]
Purchasing_Analysis_pd = purchasing_analysis_pd.style.format({'Average Purchase Price': '${:.2f}','Total number of purchases': '${:.2f}','Total Revenue': '${:.2f}'})

print('----------Purchasing Analysis (Total)----------')
Purchasing_Analysis_pd
```

    ----------Purchasing Analysis (Total)----------





<style  type="text/css" >
</style>  
<table id="T_2efb8e52_1a7d_11e8_9569_3035add8ce64" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Average Purchase Price</th> 
        <th class="col_heading level0 col1" >Number of unique items</th> 
        <th class="col_heading level0 col2" >Total Revenue</th> 
        <th class="col_heading level0 col3" >Total number of purchases</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_2efb8e52_1a7d_11e8_9569_3035add8ce64level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_2efb8e52_1a7d_11e8_9569_3035add8ce64row0_col0" class="data row0 col0" >$2.93</td> 
        <td id="T_2efb8e52_1a7d_11e8_9569_3035add8ce64row0_col1" class="data row0 col1" >183</td> 
        <td id="T_2efb8e52_1a7d_11e8_9569_3035add8ce64row0_col2" class="data row0 col2" >$2286.33</td> 
        <td id="T_2efb8e52_1a7d_11e8_9569_3035add8ce64row0_col3" class="data row0 col3" >$780.00</td> 
    </tr></tbody> 
</table> 




```python
#--------------------------------Gender Demographics
#gender_count = data_file_pd['Gender'].value_counts()
#print(gender_count)
#Take out the duplicated players, if there is a player that purchased more than once
no_duplicates_df = data_file_pd.drop_duplicates(['SN'], keep ='last')
count_no_dup = no_duplicates_df['Gender'].value_counts()

#Percentage and Count of Male Players
only_males = no_duplicates_df.loc[no_duplicates_df['Gender']=='Male','Gender']
only_males_count = only_males.count()
only_males_perc = 100*only_males.count()/count_no_dup.sum()

#Percentage and Count of Female Players
only_females = no_duplicates_df.loc[no_duplicates_df['Gender']=='Female','Gender']
only_females_count = only_females.count()
only_females_perc = 100*only_females.count()/count_no_dup.sum()

#Percentage and Count of Other / Non-Disclosed
only_other = no_duplicates_df.loc[no_duplicates_df['Gender']=='Other / Non-Disclosed','Gender']
only_other_count = only_other.count()
only_other_perc = 100*only_other.count()/count_no_dup.sum()

gender_demographic = {'Gender': ['Female', 'Male', 'Other / Non-Disclosed'], 
        'Count of Players': [only_females_count, only_males_count, only_other_count ], 
        'Percentage of Players': [only_females_perc, only_males_perc, only_other_perc]}
gender_demographic_df = pd.DataFrame(gender_demographic, columns = ['Gender', 'Count of Players', 'Percentage of Players'])

#Reformat the DataFrame style
Gender_Demographics_pd = gender_demographic_df.style.format({'Percentage of Players': '{:.2f}%'})

print('----------Gender Demographics----------')
Gender_Demographics_pd
```

    ----------Gender Demographics----------





<style  type="text/css" >
</style>  
<table id="T_595ce346_1a7d_11e8_9947_3035add8ce64" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Gender</th> 
        <th class="col_heading level0 col1" >Count of Players</th> 
        <th class="col_heading level0 col2" >Percentage of Players</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_595ce346_1a7d_11e8_9947_3035add8ce64level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_595ce346_1a7d_11e8_9947_3035add8ce64row0_col0" class="data row0 col0" >Female</td> 
        <td id="T_595ce346_1a7d_11e8_9947_3035add8ce64row0_col1" class="data row0 col1" >100</td> 
        <td id="T_595ce346_1a7d_11e8_9947_3035add8ce64row0_col2" class="data row0 col2" >17.45%</td> 
    </tr>    <tr> 
        <th id="T_595ce346_1a7d_11e8_9947_3035add8ce64level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_595ce346_1a7d_11e8_9947_3035add8ce64row1_col0" class="data row1 col0" >Male</td> 
        <td id="T_595ce346_1a7d_11e8_9947_3035add8ce64row1_col1" class="data row1 col1" >465</td> 
        <td id="T_595ce346_1a7d_11e8_9947_3035add8ce64row1_col2" class="data row1 col2" >81.15%</td> 
    </tr>    <tr> 
        <th id="T_595ce346_1a7d_11e8_9947_3035add8ce64level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_595ce346_1a7d_11e8_9947_3035add8ce64row2_col0" class="data row2 col0" >Other / Non-Disclosed</td> 
        <td id="T_595ce346_1a7d_11e8_9947_3035add8ce64row2_col1" class="data row2 col1" >8</td> 
        <td id="T_595ce346_1a7d_11e8_9947_3035add8ce64row2_col2" class="data row2 col2" >1.40%</td> 
    </tr></tbody> 
</table> 




```python
#--------------------------------Purchasing Anaysis (Gender)
#Purchase count
gender_purchase_count= pd.DataFrame(data_file_pd.groupby('Gender')['Gender'].count())

#Purchase total
gender_purchase_total= pd.DataFrame(data_file_pd.groupby('Gender')['Price'].sum())

#Purchase average
gender_purchase_average= pd.DataFrame(data_file_pd.groupby('Gender')['Price'].mean())

#Merge the purchase count and total purchase Data Frames and rename columns
purchase_analysis_gender = pd.merge(gender_purchase_count,gender_purchase_total, left_index = True, right_index = True)
purchase_analysis_gender.rename(columns = {'Gender': 'Purchase Count', 'Price':'Total Purchase Value'}, inplace=True)


#Merge with the purchase average Data Frame and rename columns
purchase_analysis_gender_2 =  pd.merge(purchase_analysis_gender, gender_purchase_average, left_index = True, right_index = True )
purchase_analysis_gender_2.rename(columns = {'Price':'Average Purchase Price'}, inplace=True)


#Add normalized purchases into the Data Fram. calculate the sum of all elements and divide each element by the sum
purchase_analysis_gender_2['Normalized Totals'] = purchase_analysis_gender_2['Total Purchase Value']/gender_demographic['Count of Players']
purchase_analysis_gender_2

#Reformat the DataFrame style
Purchasing_Analysis_Gender = purchase_analysis_gender_2.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}', 'Normalized Totals': '${:.2f}'})

print('----------Purchasing Analysis (Gender)----------')
Purchasing_Analysis_Gender
```

    ----------Purchasing Analysis (Gender)----------





<style  type="text/css" >
</style>  
<table id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Total Purchase Value</th> 
        <th class="col_heading level0 col2" >Average Purchase Price</th> 
        <th class="col_heading level0 col3" >Normalized Totals</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64level0_row0" class="row_heading level0 row0" >Female</th> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row0_col0" class="data row0 col0" >136</td> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row0_col1" class="data row0 col1" >$382.91</td> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row0_col2" class="data row0 col2" >$2.82</td> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row0_col3" class="data row0 col3" >$3.83</td> 
    </tr>    <tr> 
        <th id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64level0_row1" class="row_heading level0 row1" >Male</th> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row1_col0" class="data row1 col0" >633</td> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row1_col1" class="data row1 col1" >$1867.68</td> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row1_col2" class="data row1 col2" >$2.95</td> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row1_col3" class="data row1 col3" >$4.02</td> 
    </tr>    <tr> 
        <th id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row2_col0" class="data row2 col0" >11</td> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row2_col1" class="data row2 col1" >$35.74</td> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row2_col2" class="data row2 col2" >$3.25</td> 
        <td id="T_aafcf362_1a7d_11e8_a5e1_3035add8ce64row2_col3" class="data row2 col3" >$4.47</td> 
    </tr></tbody> 
</table> 




```python
#--------------------------------Age Demographics

#Set min age for interval
x = 10
#Set max age for interval 
y = 40
#Set steps for interval
i = 4

#Define Bins 
data_file_pd.loc[(data_file_pd['Age'] < x), 'bin']  = "< 10"
data_file_pd.loc[(data_file_pd['Age'] >= x)         & (data_file_pd['Age'] <= x+i), 'bin']         = "10 - 14"
data_file_pd.loc[(data_file_pd['Age'] >= x+i+1)     & (data_file_pd['Age'] <= x+2*i+1), 'bin']     = "15 - 19"
data_file_pd.loc[(data_file_pd['Age'] >= x+2*(i+1)) & (data_file_pd['Age'] <= x+3*(i+1)-1), 'bin'] = "20 - 24"
data_file_pd.loc[(data_file_pd['Age'] >= x+3*(i+1)) & (data_file_pd['Age'] <= x+4*(i+1)-1), 'bin'] = "25 - 29"
data_file_pd.loc[(data_file_pd['Age'] >= x+4*(i+1)) & (data_file_pd['Age'] <= x+5*(i+1)-1), 'bin'] = "30 - 34"
data_file_pd.loc[(data_file_pd['Age'] >= x+5*(i+1)) & (data_file_pd['Age'] <= y-1), 'bin']         = "35 - 39"
data_file_pd.loc[(data_file_pd['Age'] >= y), 'bin'] = "> 40"
data_file_pd[['bin', 'Age']].count()

#Purchase count by the age range bin for each use name (not unique)
age_purchase_count_df = pd.DataFrame(data_file_pd.groupby('bin')['SN'].count())

#For unique purchase count. Homework didn't specify if we should calculate unique purchases or not, I will show the non unique in the table but I will use this for normalized values, statistically makes more sense
age_purchase_count_unique_df = pd.DataFrame(data_file_pd.drop_duplicates('SN', keep = 'last').groupby('bin')['SN'].count())

#Average Purchase Price by age range bin
age_purchase_average_df = pd.DataFrame(data_file_pd.groupby('bin')['Price'].mean())

#Merge first two DF
merged_count_avg_df = pd.merge(age_purchase_count_df, age_purchase_average_df, left_index = True, right_index = True)

#Total Purchase Value by age range bin
age_purchase_total_df = pd.DataFrame(data_file_pd.groupby('bin')['Price'].sum())

#Merge total purchase with DF and rename columns
age_demographic_pd= pd.merge(merged_count_avg_df , age_purchase_total_df, left_index = True, right_index = True)
age_demographic_pd.rename(columns = {'SN': 'Purchase Count', 'Price_x':'Average Purchase', 'Price_y':'Total Purchase'}, inplace=True)

#Normalized Totals. To calculate this I can't divide by the purchase count because I have to divide by the purchasers counts (must be unique)
age_purchase_normal = age_purchase_total_df['Price']/age_purchase_count_unique_df['SN']
age_demographic_pd['Normalized Totals'] = age_purchase_normal

#Reformat style and rename index bin to Age Range
age_demographic_pd.index.rename("Age Range", inplace = True)
Age_Demographics = age_demographic_pd.style.format({'Average Purchase': '${:.2f}', 'Total Purchase': '${:.2f}', 'Normalized Totals': '${:.2f}'})

print('----------Age Demographics----------')
Age_Demographics
```

    ----------Age Demographics----------





<style  type="text/css" >
</style>  
<table id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase</th> 
        <th class="col_heading level0 col2" >Total Purchase</th> 
        <th class="col_heading level0 col3" >Normalized Totals</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Age Range</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64level0_row0" class="row_heading level0 row0" >10 - 14</th> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row0_col0" class="data row0 col0" >35</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row0_col1" class="data row0 col1" >$2.77</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row0_col2" class="data row0 col2" >$96.95</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row0_col3" class="data row0 col3" >$4.22</td> 
    </tr>    <tr> 
        <th id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64level0_row1" class="row_heading level0 row1" >15 - 19</th> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row1_col0" class="data row1 col0" >133</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row1_col1" class="data row1 col1" >$2.91</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row1_col2" class="data row1 col2" >$386.42</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row1_col3" class="data row1 col3" >$3.86</td> 
    </tr>    <tr> 
        <th id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64level0_row2" class="row_heading level0 row2" >20 - 24</th> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row2_col0" class="data row2 col0" >336</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row2_col1" class="data row2 col1" >$2.91</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row2_col2" class="data row2 col2" >$978.77</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row2_col3" class="data row2 col3" >$3.78</td> 
    </tr>    <tr> 
        <th id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64level0_row3" class="row_heading level0 row3" >25 - 29</th> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row3_col0" class="data row3 col0" >125</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row3_col1" class="data row3 col1" >$2.96</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row3_col2" class="data row3 col2" >$370.33</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row3_col3" class="data row3 col3" >$4.26</td> 
    </tr>    <tr> 
        <th id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64level0_row4" class="row_heading level0 row4" >30 - 34</th> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row4_col0" class="data row4 col0" >64</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row4_col1" class="data row4 col1" >$3.08</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row4_col2" class="data row4 col2" >$197.25</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row4_col3" class="data row4 col3" >$4.20</td> 
    </tr>    <tr> 
        <th id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64level0_row5" class="row_heading level0 row5" >35 - 39</th> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row5_col0" class="data row5 col0" >42</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row5_col1" class="data row5 col1" >$2.84</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row5_col2" class="data row5 col2" >$119.40</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row5_col3" class="data row5 col3" >$4.42</td> 
    </tr>    <tr> 
        <th id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64level0_row6" class="row_heading level0 row6" >< 10</th> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row6_col0" class="data row6 col0" >28</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row6_col1" class="data row6 col1" >$2.98</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row6_col2" class="data row6 col2" >$83.46</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row6_col3" class="data row6 col3" >$4.39</td> 
    </tr>    <tr> 
        <th id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64level0_row7" class="row_heading level0 row7" >> 40</th> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row7_col0" class="data row7 col0" >17</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row7_col1" class="data row7 col1" >$3.16</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row7_col2" class="data row7 col2" >$53.75</td> 
        <td id="T_cdb00cf8_1a7d_11e8_a128_3035add8ce64row7_col3" class="data row7 col3" >$4.89</td> 
    </tr></tbody> 
</table> 




```python
#--------------------------------Calculate the Top Spenders

#Break down the total purchases by players
tot_purchases_by_player = pd.DataFrame(data_file_pd.groupby('SN')['Price'].sum())
#Break down the average purchases by players
avg_purchases_by_player = pd.DataFrame(data_file_pd.groupby('SN')['Price'].mean())
#Break down the purchases made by each player
count_purchases_by_player = pd.DataFrame(data_file_pd.groupby('SN')['Price'].count())

#Merge results into a table and rename 
merge_top5= pd.merge(tot_purchases_by_player, count_purchases_by_player, left_index = True , right_index = True)
top_spenders= pd.merge(merge_top5, avg_purchases_by_player, left_index = True , right_index = True)
top_spenders.rename(columns = {'Price_x': 'Total Purchase', 'Price_y':'Purchase Count', 'Price':'Average Purchase Price'}, inplace = True)

#Find the players whit more purchases in the Data Frame with sort function
top_spenders.sort_values('Total Purchase', ascending = False, inplace=True)

#Find the top 5 buyers and restyle the table
Top_Spenders = top_spenders.head(5).style.format({'Total Purchase': '${:.2f}', 'Average Purchase Price': '${:.2f}'})

print('----------Top Spenders----------')
Top_Spenders 
```

    ----------Top Spenders----------





<style  type="text/css" >
</style>  
<table id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Total Purchase</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Average Purchase Price</th> 
    </tr>    <tr> 
        <th class="index_name level0" >SN</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64level0_row0" class="row_heading level0 row0" >Undirrala66</th> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row0_col0" class="data row0 col0" >$17.06</td> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row0_col1" class="data row0 col1" >5</td> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row0_col2" class="data row0 col2" >$3.41</td> 
    </tr>    <tr> 
        <th id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64level0_row1" class="row_heading level0 row1" >Saedue76</th> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row1_col0" class="data row1 col0" >$13.56</td> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row1_col1" class="data row1 col1" >4</td> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row1_col2" class="data row1 col2" >$3.39</td> 
    </tr>    <tr> 
        <th id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64level0_row2" class="row_heading level0 row2" >Mindimnya67</th> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row2_col0" class="data row2 col0" >$12.74</td> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row2_col1" class="data row2 col1" >4</td> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row2_col2" class="data row2 col2" >$3.18</td> 
    </tr>    <tr> 
        <th id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64level0_row3" class="row_heading level0 row3" >Haellysu29</th> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row3_col0" class="data row3 col0" >$12.73</td> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row3_col1" class="data row3 col1" >3</td> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row3_col2" class="data row3 col2" >$4.24</td> 
    </tr>    <tr> 
        <th id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64level0_row4" class="row_heading level0 row4" >Eoda93</th> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row4_col0" class="data row4 col0" >$11.58</td> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row4_col1" class="data row4 col1" >3</td> 
        <td id="T_e6235e34_1a7d_11e8_a1de_3035add8ce64row4_col2" class="data row4 col2" >$3.86</td> 
    </tr></tbody> 
</table> 




```python
#--------------------------------Most Popular items

# Item ID and Purchase Count and identify the top 5.
popular_items_ID = pd.DataFrame(data_file_pd.groupby('Item ID')['Item ID'].count())
popular_items_ID.sort_values('Item ID', ascending = False, inplace = True)
#I'm setting the rows to the 6th position because there are 4 items that has the same 9 purchase count so I prefered including it too
#popular_items_ID = popular_items_ID.iloc[0:6][:]

# Item Price
#Identify the total price per Item ID and merge it with the ItemID DF
popular_items_price = pd.DataFrame(data_file_pd.groupby('Item ID')['Price'].sum())
pop_items_merge_ID_price = pd.merge(popular_items_ID, popular_items_price, left_index = True, right_index = True)

#I can get the Name and Price from the original DF, but first I need to drop the duplicated items 
drop_duplicated_items = data_file_pd.drop_duplicates(['Item ID'], keep ='last')

#Merge the two DF
popular_items = pd.merge(pop_items_merge_ID_price, drop_duplicated_items, left_index = True, right_on = 'Item ID')

#Reset the index because it's messy
popular_items.set_index(['Item ID'], inplace = True)

#Rename the columns and fix the style 
popular_items.rename(columns =  {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 'Price_x': 'Total Purchase Value'}, inplace=True)
popular_items.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})

#only show the top 5 and the columns that I need to see
popular_items2 = popular_items[['Item Name','Purchase Count','Item Price', 'Total Purchase Value']]
Most_Popular_Items = popular_items2.iloc[0:6][:]

print('----------Most Popular Items----------')
Most_Popular_Items
```

    ----------Most Popular Items----------





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Trickster</td>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Serenity</td>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
#--------------------------------Most Profitable Items
#Instead of repeating the same as before I can reuse one DF from above but with different order
profitable_items = popular_items2.sort_values('Total Purchase Value', ascending=False)
profitable_items

#Select the top 5 and restyle
most_profitable_items = profitable_items.iloc[0:5][:]
Most_Profitable_Items = most_profitable_items.style.format({"Item Price": "${:.2f}", "Total Purchase Value": "${:.2f}"}, )

print('----------Most Profitable Items----------')
Most_Profitable_Items
```

    ----------Most Profitable Items----------





<style  type="text/css" >
</style>  
<table id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Item Name</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Item Price</th> 
        <th class="col_heading level0 col3" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64level0_row0" class="row_heading level0 row0" >34</th> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row0_col0" class="data row0 col0" >Retribution Axe</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row0_col1" class="data row0 col1" >9</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row0_col2" class="data row0 col2" >$4.14</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row0_col3" class="data row0 col3" >$37.26</td> 
    </tr>    <tr> 
        <th id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64level0_row1" class="row_heading level0 row1" >115</th> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row1_col0" class="data row1 col0" >Spectral Diamond Doomblade</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row1_col1" class="data row1 col1" >7</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row1_col2" class="data row1 col2" >$4.25</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row1_col3" class="data row1 col3" >$29.75</td> 
    </tr>    <tr> 
        <th id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64level0_row2" class="row_heading level0 row2" >32</th> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row2_col0" class="data row2 col0" >Orenmir</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row2_col1" class="data row2 col1" >6</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row2_col2" class="data row2 col2" >$4.95</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row2_col3" class="data row2 col3" >$29.70</td> 
    </tr>    <tr> 
        <th id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64level0_row3" class="row_heading level0 row3" >103</th> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row3_col0" class="data row3 col0" >Singed Scalpel</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row3_col1" class="data row3 col1" >6</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row3_col2" class="data row3 col2" >$4.87</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row3_col3" class="data row3 col3" >$29.22</td> 
    </tr>    <tr> 
        <th id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64level0_row4" class="row_heading level0 row4" >107</th> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row4_col0" class="data row4 col0" >Splitter, Foe Of Subtlety</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row4_col1" class="data row4 col1" >8</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row4_col2" class="data row4 col2" >$3.61</td> 
        <td id="T_07f48d6c_1a7e_11e8_a840_3035add8ce64row4_col3" class="data row4 col3" >$28.88</td> 
    </tr></tbody> 
</table> 


