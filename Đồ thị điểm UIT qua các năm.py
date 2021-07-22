import pylab
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

title_text = 'ĐIỂM THI THPT QUỐC GIA KHỐI A QUA CÁC NĂM Ở UIT'
footer_text = 'made by Hoang Minh'
fig_background_color = 'lightcyan'
fig_border = 'steelblue'
data =  [
            [                       2013, 2014, 2015 , 2016 , 2017 , 2018 , 2019 , 2020],
            ['Khoa học máy tính'  , 24.5, 26.5, 22.75, 21   , 25.75, 22.4 , 24.55, 27.2],
            ['MMT & TH dữ liệu'   , 25  , 27  , 22.5 , 21   , 24.5 , 21.2 , 23.2 , 26  ],
            ['Kỹ thuật phần mềm'  , 27.5, 28.5, 24.25, 24   , 27   , 23.2 , 25.3 , 27.7],
            ['Hệ thống thông tin' , 24.5, 26.5, 22.5 , 21.75, 24.5 , 21.1 , 23.5 , 26.3],
            ['Kỹ thuật máy tính'  , 24.5, 26.5, 22.75, 21   , 24.75, 21.7 , 23.8 , 26.7],
            ['Công nghệ thông tin', 24.5, 27  , 22.75, 22   , 25.75, 22.5 , 24.65, 27  ],
            ['An toàn thông tin'  , 24.5, 27.5, 22.75, 22.25, 25.5 , 22.25, 24.45, 26.7],
            ['Thương mại điện tử' , 0   , 0   , 22.25, 21.75, 24   , 21.2 , 23.9 , 26.5],
            ['Khoa học dữ liệu'   , 0   , 0   , 0    , 0    , 0    , 20.6 , 23.5 , 25.9],
        ]
# Pop the headers from the data array
year = column_headers = data.pop(0)
rows = [x.pop(0) for x in data]

markA = [i for i in data[0]]
markB = [i for i in data[1]]
markC = [i for i in data[2]]
markD = [i for i in data[3]]
markE = [i for i in data[4]]
markF = [i for i in data[5]]
markG = [i for i in data[6]]
yearH = [i for i in year if i >= 2015 ]
markH = [i for i in data[7] if i != 0]
yearI = [i for i in year if i >= 2018 ]
markI = [i for i in data[8] if i != 0]

# while I'm at it.
cell_text = []
for row in data:
    cell_text.append([f'{x:1.1f}' for x in row])

# Get some pastel shades for the colors
colors = plt.cm.BuPu(np.linspace(0.15, 0.45, len(rows)))

# with an explicit figsize here can produce better outcome.
plt.figure(
           edgecolor=fig_border,
           facecolor=fig_background_color,
           tight_layout={'pad':1},
           figsize=(9,9.25)
          )
# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      colLabels=column_headers,
                      rowColours=colors,
                      colColours=colors,
                      rowLoc='right'
                      )
# Draw plot
plt.plot(year,markA,
        color='m',
        linestyle='-',
        marker= '.',
        markersize=7)
plt.plot(year,markB,
        color='b',
        linestyle='--',
        marker= '.',
        markersize=7)
plt.plot(year,markC,
        color='g',
        linestyle='-.',
        marker= '.',
        markersize=7)
plt.plot(year,markD,
        color='r',
        linestyle=':',
        marker= '.',
        markersize=7)
plt.plot(year,markE,
        color='c',
        linestyle='-',
        marker= '.',
        markersize=7)
plt.plot(year,markF,
        color='y',
        linestyle='--',
        marker= '.',
        markersize=7)
plt.plot(year,markG,
        color='tab:purple',
        linestyle='-.',
        marker= '.',
        markersize=7)
plt.plot(yearH,markH,
        color='k',
        linestyle=':',
        marker= '.',
        markersize=7)             
plt.plot(yearI,markI,
        color='b',
        linestyle='-',
        marker= '.',
        markersize=7)
plt.ylabel("Điểm")
plt.legend(rows)
plt.axis("tight")
plt.style.use('bmh')
# Scaling is the only influence we have over top and bottom cell padding.
# Make the rows taller (i.e., make cell y scale larger).
the_table.scale(1, 1.5)
# Hide axes
ax = plt.gca()
ax.axes.xaxis.set_ticklabels([])
# Add title
plt.suptitle(title_text)
# Add footer
plt.figtext(0.95, 0.95, footer_text, horizontalalignment='right', size=8, weight='light')
# Without plt.draw() here, the title will center on the axes and not the figure.
plt.draw()
#Create image. plt.savefig ignores figure edge and face colors, so map them.
fig = plt.gcf()
plt.savefig('UIT_Marks.png',
        bbox='tight',
        edgecolor=fig.get_edgecolor(),
        facecolor=fig.get_facecolor(),
        dpi=155
        )
# Go to x,y on windows
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_geometry("+1000+0")
ax.grid(True)
plt.show()