#!/usr/bin/env python3

from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('simple_chart.html')
    fig = figure()

    total_vals = int(input('Values to include in chart ==> '))
    x_vals = list(range(total_vals))
    y_vals = []

    for i in x_vals:
        val = int(input(f'Y axis value for x_vals[{i}] ==> '))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
