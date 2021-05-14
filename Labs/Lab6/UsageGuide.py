import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib as mpl 
import pandas

# fig = plt.figure() #an empty figure with no axes
# fig.suptitle('no axes on this figure') #Adding a title
# fig, ax_lst = plt.subplots(2,2) # a figure with a 2x2 grid of Axes
# plt.show()

#To convert to a pandas data frame
# a = pandas.DataFrame(np.random.rand(4,5),columns=list('abcde'))
# a_asarray = a.values

# b = np.matrix([[1,2],[3,4]])
# b_asarray = np.asarray(b)

# x = np.linspace(0,2,100)

# plt.plot(x,x,label='linear')
# plt.plot(x,x**2,label='quadratic')
# plt.plot(x,x**3,label='cubic')

# plt.xlabel('x label')
# plt.ylabel('y label')

# plt.title("Simple Plot")

# plt.legend()

# plt.show()

# x = np.arange(0,10,.2)
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x,y)
# plt.show()

# def my_plotter(ax, data1, data2, param_dict):
#     out = ax.plot(data1,data2, **param_dict)
#     return out

# # Which you would then use as:

# data1, data2, data3, data4 = np.random.randn(4,100)
# fig, ax = plt.subplots(1,1)
# my_plotter(ax, data1,data2,{'marker':'x'})
# plt.show()

# # 2 subplots:
# fig, (ax1, ax2) = plt.subplots(1,2)
# my_plotter(ax1, data1, data2, {'marker': 'x'})
# my_plotter(ax2, data3, data4, {'marker': 'o'})
# plt.show()

# y = np.random.rand(100000)
# y[50000:] *= 2
# y[np.logspace(1,np.log10(50000), 400).astype(int)] = -1
# mpl.rcParams['path.simplify'] = True

# mpl.rcParams['path.simplify_threshold'] = 0.0
# plt.plot(y)
# plt.show()

# mpl.rcParams['path.simplify_threshold'] = 1.0
# plt.plot(y)
# plt.show()

# mpl.rcParams['path.simplify_threshold'] = 1.0

# # Setup, and create the data to plot
# y = np.random.rand(100000)
# y[50000:] *= 2
# y[np.logspace(1,np.log10(50000), 400).astype(int)] = -1
# mpl.rcParams['path.simplify'] = True

# mpl.rcParams['agg.path.chunksize'] = 0
# plt.plot(y)
# plt.show()

# mpl.rcParams['agg.path.chunksize'] = 10000
# plt.plot(y)
# plt.show()

# import matplotlib.style as mplstyle
# mmlstyle.use('fast')
# mplstyle.use(['dark_background','ggplot','fast'])

# np.random.seed(19680801)
# data = np.random.randn(2,100)

# fig, axs = plt.subplots(2,2,figsize=(5,5))
# axs[0,0].hist(data[0])
# axs[1,0].scatter(data[0], data[1])
# axs[0,1].plot(data[0], data[1])
# axs[1,1].hist2d(data[0], data[1])
# plt.show()