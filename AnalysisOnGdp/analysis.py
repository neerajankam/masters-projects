import pandas as pd
import numpy as np
analysis = pd.read_excel('Countries.xlsx',index_col=0)

#print(analysis)

china = analysis.iloc[0:9,:]
#print(china)
china_gdp=china.iloc[0,2:6]
#print(china_gdp)
#print(type(china))

india = analysis.iloc[9:18,:]
india_gdp = india.iloc[0,2:6]
print(india)

usa=analysis.iloc[18:27,:]
usa_gdp=usa.iloc[0,2:6]
#print(usa_gdp)
#print(usa)

import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

gdp_ticks=[2001,2006,2011,2016]
us, =plt.plot(usa_gdp,gdp_ticks,label='USA',marker='*')
#for xy in zip(usa_gdp,gdp_ticks):
#	ax.annotate('%s%s'%xy,xy=xy,textcoords='data')

ch, =plt.plot(china_gdp,gdp_ticks,label='CHINA',marker='o')
for xy in zip(china_gdp,gdp_ticks):
	ax.annotate('%s%s'%xy,xy=xy,xytext=(30,40),textcoords='data')
ind, =plt.plot(india_gdp,gdp_ticks,label='INDIA',marker='>')
for xy in zip(india_gdp,gdp_ticks):
	ax.annotate('%s%s'%xy,xy=xy,xytext=(0,2),textcoords='data')


plt.xscale('log',basex=10)
plt.legend([us,ch,ind],['USA','CHINA','INDIA'],loc='best')
plt.xlabel('GDP(in USD)')
plt.ylabel('Year')
plt.title('Countries GDP WRT YEAR')
plt.grid(True)
plt.show()