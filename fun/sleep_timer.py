import os
import time
import argparse


# from memory_profiler import profile


# @profile
def main(delay_sec):
    passed_time = 0
    step_delay = 10
    while passed_time < delay_sec:
        print(f"{passed_time} mins have passed. {delay_sec - passed_time}s left.")
        time.sleep(step_delay)
        passed_time += step_delay
    os.system("pmset sleepnow")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--delay_sec", type=int, default=300)

    args, _ = parser.parse_known_args()
    main(args.delay_sec)
