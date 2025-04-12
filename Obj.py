#1st Objective : data cleaning and preproccessing
from enum import unique
import numpy as np
import pandas as pd

# df = pd.read_csv("IntProjectPy\\GHG.csv")
# print(df.info())
# print(df.head())
# print(df.isnull().sum())
# numeric_columns = [
#     'Supply Chain Emission Factors without Margins',
#     'Margins of Supply Chain Emission Factors',
#     'Supply Chain Emission Factors with Margins'
# ]
# for col in numeric_columns:
#     df[col] = pd.to_numeric(df[col], errors="coerce")

# df['2017 NAICS Code'] = df['2017 NAICS Code'].astype(str)

# duplicate = df.duplicated().sum()
# if duplicate > 0:
#     df = df.drop_duplicates()

# unique_units = df['Unit'].unique()
# print("unique units:", unique_units)

# cleaned_df = df.copy()
# cleaned_df.to_csv('cleaned_GHG.csv',index = False)
# print(cleaned_df.info())
# print(cleaned_df.head())








#2nd_Objective:  data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv("IntProjectPy\\cleaned_GHG.csv")
# print(df.info())
# print(df.describe())

# plt.figure(figsize=(12, 6))
# sns.histplot(df['Supply Chain Emission Factors without Margins'], bins=50, kde=True, log_scale=True)
# plt.title('Distribution of Supply Chain Emission Factors')
# plt.xlabel('Emission Factors')
# plt.ylabel('Frequency')
# plt.show()

# ghgtotal = df.groupby('GHG')['Supply Chain Emission Factors without Margins'].sum().sort_values(ascending=False)
# print(ghgtotal.head(10))

# plt.figure(figsize=(12, 6))
# ghgtotal.head(10).plot(kind='bar')
# plt.title('Top 10 GHGs by Total Emission Factors')
# plt.xlabel('GHG')
# plt.ylabel('Total Emission Factor')
# plt.show()


# numeric_cols = ['Supply Chain Emission Factors without Margins', 
#                 'Margins of Supply Chain Emission Factors', 
#                 'Supply Chain Emission Factors with Margins']
# correlation = df[numeric_cols].corr()
# print(correlation)

# plt.figure(figsize=(8, 6))
# sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
# plt.title('Correlation Heatmap of Emission Factors')
# plt.show()



# major_ghgs = ['Carbon dioxide', 'Methane', 'Nitrous oxide', 'HFCs and PFCs, unspecified']
# plt.figure(figsize=(12, 6))
# sns.boxplot(x='GHG', y='Supply Chain Emission Factors with Margins',data=df[df['GHG'].isin(major_ghgs)],showfliers=False)
# plt.title('Emission Factors by Major GHGs')
# plt.xlabel('GHG')
# plt.ylabel('Emission Factors')
# plt.show()





#3rd_Objective : filtering and sorting

# df = pd.read_csv('IntProjectPy//cleaned_GHG.csv')
# co2_df = df[df['GHG'] == 'Carbon dioxide']
# print("Carbon Dioxide Data :")
# print(co2_df.head())

# ghgs_of_interest = ['Carbon dioxide', 'Methane', 'Nitrous oxide']
# majorghgs_df = df[df['GHG'].isin(ghgs_of_interest)]
# print(majorghgs_df[['2017 NAICS Title', 'GHG', 'Supply Chain Emission Factors with Margins']].head())

# sorted_by_emission = df.sort_values('Supply Chain Emission Factors with Margins', ascending=False)
# print(sorted_by_emission[['2017 NAICS Title', 'GHG', 'Supply Chain Emission Factors with Margins']].head())

# sorted_multi = df.sort_values(['2017 NAICS Title', 'Supply Chain Emission Factors with Margins'], 
#                               ascending=[True, False])
# print(sorted_multi[['2017 NAICS Code', '2017 NAICS Title', 'GHG', 'Supply Chain Emission Factors with Margins']].head())

# df['2017 NAICS Code'] = df['2017 NAICS Code'].astype(str)
# nitrous_farming = df[(df['GHG'] == 'Nitrous oxide') & 
#                      (df['2017 NAICS Code'].str.startswith('111'))].sort_values(
#                          'Supply Chain Emission Factors with Margins', ascending=False)
# print(nitrous_farming[['2017 NAICS Title', 'Supply Chain Emission Factors with Margins']].head())

# top_methane = df[df['GHG'] == 'Methane'].nlargest(5, 'Supply Chain Emission Factors with Margins')
# print(top_methane[['2017 NAICS Code', '2017 NAICS Title', 'Supply Chain Emission Factors with Margins']])







# 4th objective = Summarizing data

# df = pd.read_csv('IntProjectPy//cleaned_GHG.csv')
# print(df.describe())

# ghg_summary = df.groupby('GHG').agg({
#     'Supply Chain Emission Factors with Margins': ['mean', 'sum', 'min', 'max', 'count'],
#     'Supply Chain Emission Factors without Margins': ['mean', 'sum'],
#     'Margins of Supply Chain Emission Factors': ['mean', 'sum']
# }).round(6)
# print(ghg_summary)

# ghg_summary.columns = ['_'.join(col).strip() for col in ghg_summary.columns.values]
# ghg_summary = ghg_summary.reset_index()
# top_ghgs = ghg_summary.nlargest(5, 'Supply Chain Emission Factors with Margins_sum')
# print(top_ghgs[['GHG', 'Supply Chain Emission Factors with Margins_sum', 
#                 'Supply Chain Emission Factors with Margins_mean']])

# df['2017 NAICS Code'] = df['2017 NAICS Code'].astype(str)
# df['naics_sector'] = df['2017 NAICS Code'].str[:3]
# sector_summary = df.groupby('naics_sector').agg({
#     'Supply Chain Emission Factors with Margins': ['sum', 'mean', 'count'],
#     '2017 NAICS Title': 'first'  
# }).round(6)
# print(sector_summary.head())

# pivot_summary = pd.pivot_table(df, 
#                               values='Supply Chain Emission Factors with Margins', 
#                               index='naics_sector', 
#                               columns='GHG', 
#                               aggfunc='mean', 
#                               fill_value=0).round(6)
# print(pivot_summary.head())







# 5th objective : Comparative Analysis and Insights

df = pd.read_csv('IntProjectPy//cleaned_GHG.csv')

# Ensure NAICS Code is string for filtering
df['2017 NAICS Code'] = df['2017 NAICS Code'].astype(str)

# 1. Compare emission factors across major farming sectors (NAICS starting with '111')
farming_df = df[df['2017 NAICS Code'].str.startswith('111')]
key_ghgs = ['Carbon dioxide', 'Methane', 'Nitrous oxide']

# Group by NAICS Title and GHG for comparison
farming_comparison = farming_df[farming_df['GHG'].isin(key_ghgs)].groupby(['2017 NAICS Title', 'GHG'])[
    'Supply Chain Emission Factors with Margins'].mean().unstack().fillna(0)

print("Average Emission Factors for Key GHGs Across Farming Sectors:")
print(farming_comparison.round(6))



# 2. Analyze contribution of margins to total emissions
df['Margin Contribution (%)'] = (df['Margins of Supply Chain Emission Factors'] / 
                                 df['Supply Chain Emission Factors with Margins'] * 100).fillna(0)

margin_analysis = df.groupby('GHG')['Margin Contribution (%)'].mean().sort_values(ascending=False)
print("\nAverage Margin Contribution (%) by GHG:")
print(margin_analysis.head(10))



# 3. Identify top industries for key GHGs
top_industries_by_ghg = {}
for ghg in key_ghgs:
    top_industries = df[df['GHG'] == ghg].nlargest(5, 'Supply Chain Emission Factors with Margins')[
        ['2017 NAICS Title', 'Supply Chain Emission Factors with Margins']]
    top_industries_by_ghg[ghg] = top_industries

print("\nTop 5 Industries by Emission Factors for Key GHGs:")
for ghg, data in top_industries_by_ghg.items():
    print(f"\n{ghg}:")
    print(data)



# 4. Compare 'with margins' vs 'without margins' for key GHGs
margin_comparison = df[df['GHG'].isin(key_ghgs)].groupby('GHG').agg({
    'Supply Chain Emission Factors without Margins': 'mean',
    'Supply Chain Emission Factors with Margins': 'mean'
}).round(6)

print("\nComparison of Emission Factors (With vs Without Margins):")
print(margin_comparison)

