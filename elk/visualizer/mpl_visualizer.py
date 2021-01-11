import matplotlib.pyplot as plt
import matplotlib.animation as animation
from gps_container import get_data


def visualize():
    """Docstring."""

    # import the data
    data = get_data()

    # let's look at a smaller dataset
    data = data[:1000]

    # calculate the domain
    xrange = (min(data, key=lambda x: x.long).long,
              max(data, key=lambda x: x.long).long)
    yrange = (min(data, key=lambda x: x.lat).lat,
              max(data, key=lambda x: x.lat).lat)

    # setup the plotting environment
    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    ax.set_xlim(*xrange)
    ax.set_ylim(*yrange)
    point = ax.plot(data[0].long, data[0].lat, c='blue', marker='o', ms=2.5)[0]
    text = ax.text(xrange[0], yrange[0], data[0].timestamp)

    def animate(i):
        text.set_text(data[i].timestamp)
        point.set_xdata(data[i].lat)
        point.set_ydata(data[i].long)
        return

    ani = animation.FuncAnimation(fig, animate, frames=100, interval=250,
                                  repeat_delay=2000)
    ani.save('test_ani.gif')
    return


if __name__ == '__main__':
    visualize()
