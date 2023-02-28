#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import manufacturing as mn
# %%
raw = pd.read_excel('EPIX_ClickRatio_PR.xlsx')
# %%
def tweak_raw(raw):
    return(raw
    .assign(Size = raw.ProductName.str.split(",").str[1].str.replace('mm',''))
    .drop_duplicates('SerialNumber', keep='first')
    .iloc[:,6:]
    .astype({'Size':'category'})
    .melt(id_vars='Size', value_vars=['Item7','Item17','Item27','Item37','Item47'], value_name='ClickRatio', var_name='Button')
    .assign(Button = lambda df : df.Button.map({'Item7':'btn1','Item17':'btn2','Item27':'btn3','Item37':'btn4','Item47':'btn5'}))
    )
tweak_raw(raw)
# %%
mn.ppk_plot(tweak_raw(raw).ClickRatio,
            lower_specification_limit=0.17, 
            upper_specification_limit=0.5, 
            show_dppm=True)
# %%
plt.figure(dpi=200, figsize=(8,5));
plt.title('ClickRatio for each button for each size in PR build')
sns.violinplot(tweak_raw(raw), x='Size',y='ClickRatio',hue='Button', inner='points');
plt.axhline(0.17, color='r', linestyle='--')
plt.axhline(0.5, color='r', linestyle='--')