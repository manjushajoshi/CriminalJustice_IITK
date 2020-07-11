#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:43:58 2020

@author: manjusha
"""

#dowry deaths 214
#murder 576
#dowry prohibition act 34
#cruelty by husband or his relative  6443
#PROTECTION OF WOMEN FROM DOMESTIC VIOLENCE ACT  6
import plotly
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
plotly.offline.init_notebook_mode(connected=True)
 
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

V = [214, 576,34,644,6]
L=['Dowry deaths','Generic Murder count','dowry prohibition act','cruelty by husband or his relative','PROTECTION OF WOMEN FROM DOMESTIC VIOLENCE ACT']
fig = {
  "data": [
    {
      "values": V,
      "labels": L,
      "domain": {"x": [0, .48]},
      "name": "Maharashtra-2018",
      "marker": {'colors': [
                     '#e6f2ff',
                     '#99ccff',
                     '#ccccff',
                     '#cc99ff',
                     '#ff99ff',
                     '#ff6699',
                     '#ff9966',
                     '#ff6600',
                     '#ff5050',
                     '#ff0000'
                    ]
                },
      "textinfo":"percent+label",
      "textfont": {'color': '#FFFFFF', 'size': 15},
      "hole": .4,
      "type": "pie"
    } ],
    "layout": {
        "title":"Women Crime in Maharashtra-2018",
        "annotations": [
            {
                "font": {
                    "size": 25,
                    "color": '#5A5A5A'
                },
                "showarrow": False,
                "text": "2018",
                "x": 0.20,
                "y": 0.5
            }
        ]
    }
}



#plotly.iplot(fig, filename='pie-custom-colors')
plotly.offline.plot(fig)