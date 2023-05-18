#%%
import reliability.Distributions as dt
import reliability.Fitters as fit
import reliability.Other_functions as of
import pandas as pd
import matplotlib.pyplot as plt
# %%
data = dt.Weibull_Distribution(25,4).CDF(show_plot=False)
data2 = dt.Weibull_Distribution(25,4).PDF(show_plot=False)
# %%
fit.Fit_Everything(data, show_probability_plot=False, show_best_distribution_probability_plot=False, show_histogram_plot=False, show_PP_plot=False)
# %%
fit.Fit_Beta_2P(data)
# %%
data = dt.Weibull_Distribution(500,3).random_samples(10)
# %%
fit_w = fit.Fit_Weibull_2P(data)
#%%
x_lower, x_point, x_upper = fit_w.distribution.CDF(CI_type='time', CI_y=0.7)
plt.arrow(x=0, y=0.7, dx=x_upper, dy=0)
plt.arrow(x=x_lower,y=0, dx=0, dy=0.7)
plt.arrow(x=x_point,y=0, dx=0, dy=0.7)
plt.arrow(x=x_upper,y=0, dx=0, dy=0.7)
plt.text(x=x_lower, y=0.1, s='test', rotation=90)
# %%
from reliability.Datasets import automotive
# %%
fit_model = fit.Fit_Weibull_2P(automotive().failures, right_censored=automotive().right_censored)
# %%
y_lower, y_point, y_upper = fit_model.distribution.SF(CI_type='reliability', CI_x=100000)
# plt.scatter(x=[100000,100000,100000],y=[y_lower, y_point, y_upper])
plt.arrow(x=0, y=y_lower, dx=100000, dy=0)
plt.arrow(x=0, y=y_point, dx=100000, dy=0)
plt.arrow(x=0, y=y_upper, dx=100000, dy=0)
plt.arrow(x=100000, y=0, dx=0, dy=y_upper)