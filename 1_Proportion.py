#%%
from statsmodels.stats.proportion import proportions_ztest

# %%
count1 = 50
nobs1 = 200
count2 = 70
nobs2 = 200

stat, pval = proportions_ztest([count1, count2], [nobs1, nobs2])

print(f"Test statistic: {stat:.4f}")
print(f"P-value: {pval:.4f}")