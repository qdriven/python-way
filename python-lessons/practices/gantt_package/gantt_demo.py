# -*- coding: utf-8 -*-

import plotly.figure_factory as ff
import plotly

df = [dict(Task="Job A", Start='2018-01-01', Finish='2018-02-28'),
      dict(Task="Job B", Start='2018-03-05', Finish='2018-04-15'),
      dict(Task="Job C", Start='2019-02-20', Finish='2018-05-30')]


fig = ff.create_gantt(df)
plotly.offline.plot(fig, filename='gantt-simple-gantt-chart.html')

#
# import plotly
# import plotly.graph_objs as go
#
# plotly.offline.plot({
#     "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#     "layout": go.Layout(title="hello world")
# }, auto_open=True)


