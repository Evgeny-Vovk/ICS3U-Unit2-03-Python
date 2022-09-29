# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: September 2022
# ICS3U-Unit2-03.py File, learning input process and output in python.

import constants


def main():

    # input
    radius_of_circle = int(input("Type in the radius of your circle(mm): "))

    # process
    perimeter_of_circle = constants.TAU * radius_of_circle

    # output
    print("\nThe perimeter of the circle is {} mm.".format(perimeter_of_circle))

    print("\n\nDone.")


if __name__ == "__main__":
    main()
