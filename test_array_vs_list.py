#!/usr/bin/env python
"""From the preview of Dimitry Zinoviev's book "Data Science Essentials in
Python" <https://pragprog.com/book/dzpyds/data-science-essentials-in-python>
chapter 5 "Working with Tabular Numeric Data" unit 21 "Creating Arrays"
there was a note that states:

    Contrary to their name, Python “lists” are actually implemented
    as arrays, not as lists. No storage is reserved for forward pointers,
    because no forward pointers are used. Large Python lists require
    only about 13% more storage than “real” numpy arrays. However,
    Python executes some simple built-in operations, such as sum(), 5–10
    times faster on lists than on arrays. Ask yourself if you really need
    any numpy-specific features before you start a numpy project!

I have usually encountered the otherwise, but this script should test it.

Update:
Applying built-in function on a numpy-array is indeed ~2x slower than
applying it on a list. Additionally, there is a speed penalty when using
numpy's function on a list. However, numpy's functions on numpy's arrays are
and array methods are much faster.
--
Peeter Piksarv, 2015-05-13
"""

import timeit

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# List of common functions between core python and numpy which both act same
# over lists and arrays
FUNCS = ['all', 'any', 'max', 'min', 'sum']


def time_array_vs_list(func='sum', num=10000):
    """Times the particular function on a random list of a size of num.
    """

    if func not in FUNCS:
        func = 'sum'

    num_array = np.random.rand(num)
    num_list = list(num_array)

    # Arguments for timeit.timeit
    kwargs = {
        'number': 1000,
        'globals': dict(globals(), **locals()),
    }

    # The following are possible calls
    calls = [
        '{}(num_list)',     # func(num_list)
        '{}(num_array)',    # func(num_array)
        'np.{}(num_list)',  # np.func(num_list)
        'np.{}(num_array)', # np.func(num_array)
        'num_array.{}()',   # num_array.func()
    ]
    calls = [c.format(func) for c in calls]

    timings = [timeit.timeit(call, **kwargs) for call in calls]

    return timings


if __name__ == '__main__':

    N = [2**n for n in range(1, 12, 2)]
    columns = ['N', 'func(list)', 'func(array)',
               'np.func(list)', 'np.func(array)', 'array.func()']

    plot_results = False
    print_results = True

    for func in FUNCS:

        # Timing calculations for different size list/arrays for func
        data = np.array([[n, *time_array_vs_list(func='sum', num=n)] for n in N])

        df = pd.DataFrame(data, index=N, columns=columns)

        if plot_results:
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            df.plot(x='N', ax=ax, title='func = {}()'.format(func))
            ax.set_ylabel('t (ms)')
            fig.savefig(
                'test_array_vs_list-{}-run{}.png'.format(func, str(pd.datetime.now())))

        if print_results:
            print('func = {}()'.format(func))
            print(df)
            print()
