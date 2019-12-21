"""
Tools used for profiling tests for efficiency
"""
from time import perf_counter_ns


class Timer(object):

    # TODO: add optional param for number of trials, then average
    def __init__(self, unit="ms", message=None):
        """
        Decorator that times the function runtime, then prints the result
        
        :param unit: (Optional, str)
            Unit that the time is displayed in, default is ms
        
        :param message: (Optional, str)
            Message that is printed with the elapsed time
        """
        self.unit = unit
        self.message = message

    def __call__(self, f):
        # TODO: Add a user friendly error message for when the () are forgotten
        """
        :param f: (func)
            The function to be timed
        """

        def wrapper_timer(*args, **kwargs):
            # times and runs the function
            before = perf_counter_ns()
            rv = f(*args, **kwargs)
            after = perf_counter_ns()
            # Calculates total time and converts to chosen units
            conversion = self.convert_time()
            time = "{:.3f}".format((after - before) / conversion)
            # prints output
            print("\n\nTime Elapsed: {0}{1}".format(time, self.unit))
            if self.message is not None:
                print("\t{}".format(self.message))
            return rv

        return wrapper_timer

    def convert_time(self):
        if self.unit == "ns":
            conversion = pow(10, 0)
        elif self.unit == "us":
            conversion = pow(10, 3)
        elif self.unit == "ms":
            conversion = pow(10, 6)
        elif self.unit == "s":
            conversion = pow(10, 9)
        elif self.unit == "min":
            conversion = 6 * pow(10, 10)
        else:
            print(
                "\n\nBad unit given to @timer, Valid units are:"
                "\n\tns, us, ms, s, min"
                "\n\tUsing default ms"
            )
            conversion = pow(10, 6)
            self.unit = "ms"
        return conversion
