import cProfile
import pstats
import io

# import my_code

pr = cProfile.Profile()
pr.enable()


def my_func():
    """
    The function to be profiled.
    Instead one could write the original in a seperate file as:
        def main():
            ...
        if __name__ == '__main__':
            main()
    and save it as my_code.py and import it at the top
    of this code by its name and finally:
    my_results = my_code.main()

    """
    return


my_result = my_func()  # or my_code.main()

pr.disable()
s = io.StringIO()
# sorting by tottime
ps = pstats.Stats(pr, stream=s).sort_stats("tottime")
ps.strip_dirs()

ps.print_stats()
# save the stats locally
output_name = "profiler.txt"
with open(output_name, "w+") as f:
    f.write(s.getvalue())
