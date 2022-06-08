import pandas as pd
from matplotlib import pyplot as plt

def __get_ylim(ser):
  if type(ser) is list:
    ser = pd.concat(ser)
    
  return ser.max() + ser.max() * 0.1


def multiple_plot_bars(ser, title, xlabel, ylabel):
  fig, axes = plt.subplots(nrows=len(ser), figsize=(len(ser[0]) * 1.3, len(ser) * 4))
  fig.subplots_adjust(hspace=0.3)
  axes[0].set_title(title + '\n', fontsize=14)

  for ax, idx in zip(axes, range(len(axes))):
    ax.set(xlabel=xlabel, ylabel=ylabel, ylim=[0, __get_ylim(ser)])
    ax.bar_label(ax.bar(ser[idx].index, ser[idx].round(2)))
  plt.show()


def single_plot_bars(ser, title, xlabel, ylabel):
  fig, ax = plt.subplots(figsize=(len(ser) * 1.3, 4))
  ax.set_title(title + '\n', fontsize=14)
  
  ax.set(xlabel=xlabel, ylabel=ylabel, ylim=[0, __get_ylim(ser)])
  ax.bar_label(ax.bar(ser.index, ser.round(2)))
  plt.show()


def plot_bars(ser, title, xlabel, ylabel):
  if type(ser) is list:
    multiple_plot_bars(ser, title, xlabel, ylabel)
  else:
    single_plot_bars(ser, title, xlabel, ylabel)