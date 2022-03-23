#!/usr/bin/env python
# coding: utf-8

# In[23]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

prog = pd.read_csv("progress.csv", parse_dates=['when'])
with plt.xkcd(): # why not? but you'll need to apt install fonts-humor-sans
    fig, ax = plt.subplots(figsize=(6,6)) # width, height in inches
    sns.lineplot(
        ax=ax,data=prog,x="when",y="words",
        markers=True,marker="o",markersize=8,
        markerfacecolor='white',markeredgecolor='tab:blue',markeredgewidth=2)
    ax.set(
        ylim=(0,1.1*prog.words.max()),
        title="Dissertation Progress"
    )
    fig.autofmt_xdate() # slant those dates
    fig.tight_layout()
    fig.savefig("progress.png")

