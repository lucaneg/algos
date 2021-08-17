import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import sys

class CompsWrapper:
    def __init__(self):
        self.comps = 0
    
def provide_array():
    # the first arg is always the script name
    nargs = len(sys.argv) - 1
    if nargs == 0:
        n = int(input("Enter the number of elements (0 or negative will trigger manual input):"))
        if n <= 0:
            array = input("Insert array elements separated by a space (elements will NOT be shuffled):").split()
        else:
            array = [random.randint(0, 999999) for i in range(n)]
    elif nargs == 1:
        print('Generating random array of ' + sys.argv[1] + ' elements')
        array = [random.randint(0, 999999) for i in range(int(sys.argv[1]))]
    else:
        array = [int(i) for i in ' '.join(sys.argv[1:]).split()]
        print('Using the following array ' + str(array))
    return array

def display(array, title, array_and_comparisons):
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rec = ax.bar(range(len(array)), array, align = 'edge', color = 'green')
    text = ax.text(0.02, 0.95, "", transform = ax.transAxes)

    epochs = [0]
    def update_plot(array_and_comparisons, rec, epochs):
        for rec, val in zip(rec, array_and_comparisons[0]):
            rec.set_height(val)
        epochs[0] += 1
        text.set_text("#ops {}, #comps {}".format(epochs[0], array_and_comparisons[1]))
    
    an = anim.FuncAnimation(fig, func = update_plot, fargs = (bar_rec, epochs), frames = array_and_comparisons, interval = 1, repeat = False)
    plt.show()
