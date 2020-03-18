import pandas as pd
import matplotlib.pylab as plt
import cufflinks as cf
from plotly.subplots import make_subplots
from plotly import tools

cf.go_offline()
inData=pd.read_csv(r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')

modifiedData=inData.groupby('Country/Region').sum().transpose()

dataOneCountry=[]
for country in modifiedData.columns:
    onlyMoreThan10Temp=modifiedData[modifiedData[country]>100][country].iloc[2:]
    onlyMoreThan10Temp=onlyMoreThan10Temp.reset_index()[country]
    dataOneCountry.append(onlyMoreThan10Temp.copy())
    

pd.DataFrame(dataOneCountry).dropna(how='all').transpose().iplot(yaxis_type='log')

traces=[]
pd.to_datetime(inData[inData['Country/Region']=='Poland'].transpose().iloc[4:].index)

PolandData=inData[inData['Country/Region']=='Poland'].transpose().iloc[4:]
PolandData.index=pd.to_datetime(PolandData.index)

plt.plot(PolandData[pd.to_datetime('2020-03-01'):],'*')
plt.xticks(rotation='vertical')
plt.ylabel('Liczba zarażonych')
plt.title('Polska')
plt.show()

plt.semilogy(PolandData[pd.to_datetime('2020-03-01'):],'*')
plt.xticks(rotation='vertical')
plt.ylabel('Liczba zarażonych')
plt.title('Polska - log plot')
plt.show()


ItalyData=inData[inData['Country/Region']=='Italy'].transpose().iloc[4:]
ItalyData.index=pd.to_datetime(ItalyData.index)
plt.plot(ItalyData[pd.to_datetime('2020-02-15'):],'*')
plt.xticks(rotation='vertical')
plt.ylabel('Liczba zarażonych')
plt.title('Włochy')
plt.show()

ItalyData=inData[inData['Country/Region']=='Italy'].transpose().iloc[4:]
ItalyData.index=pd.to_datetime(ItalyData.index)
plt.semilogy(ItalyData[pd.to_datetime('2020-02-15'):],'*')
plt.xticks(rotation='vertical')
plt.ylabel('Liczba zarażonych')
plt.title('Włochy - log plot')
plt.show()


SpainData=inData[inData['Country/Region']=='Spain'].transpose().iloc[4:]
SpainData.index=pd.to_datetime(SpainData.index)
plt.plot(SpainData[pd.to_datetime('2020-01-15'):],'*')
plt.xticks(rotation='vertical')
plt.ylabel('Liczba zarażonych')
plt.title('Hiszpania')
plt.show()

plt.semilogy(SpainData[pd.to_datetime('2020-01-15'):],'*')
plt.xticks(rotation='vertical')
plt.ylabel('Liczba zarażonych')
plt.title('Hiszpania - log plot')
plt.show()