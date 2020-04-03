from bokeh.plotting import figure, output_file, show #Window to plot, output name,server

if __name__ == '__main__':
    output_file('HTML_plot')
    fig = figure()
    print( type(fig) )

    total_vals = int(input('How many values to plot: '))
    x_vals = list(range(total_vals))
    y_vals = [];
    
    for x in x_vals:
        val = int(input(f"'Y' value for {x}: "))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width = 2)
    show(fig)

