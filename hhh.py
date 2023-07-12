import numpy as np; np.random.seed(sum(map(ord, 'calplot')))
import pandas as pd
import calplot
import matplotlib.pyplot as plt

all_days = pd.date_range('1/1/2019', periods=730, freq='D')
days = np.random.choice(all_days, 500)
events = pd.Series(np.random.randn(len(days)), index=days)
calplot.calplot(events, cmap='YlGn', colorbar=False)
plt.show()