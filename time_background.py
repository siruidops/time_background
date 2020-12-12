#!/usr/bin/python

import os
import datetime, time

dir = "bg"

def change_background(file_name):
    os.system(
        "feh --bg-scale {}".format(file_name)
    )


def main():
    old = None
    h = 0

    while 1:
        #date_now = datetime.datetime.now()
        
        if (5 <= h < 8) and (old != "5-8"):
            old = "5-8"
            change_background(
                dir+"/5-8.png"
            )

        elif (8 <= h < 10) and (old != "8-10"):
            old = "8-10"
            change_background(
                dir+"/8-10.png"
            )

        elif (10 <= h < 13) and (old != "10-13"):
            old = "10-13"
            change_background(
                dir+"/10-13.png"
            )

        elif (13 <= h < 16) and (old != "13-16"):
            old = "13-16"
            change_background(
                dir+"/13-16.png"
            )

        elif (16 <= h < 18) and (old != "16-18"):
            old = "16-18"
            change_background(
                dir+"/16-18.png"
            )

        elif (18 <= h < 21) and (old != "18-21"):
            old = "18-21"
            change_background(
                dir+"/18-21.png"
            )

        elif ((21 <= h < 24) or (0 <= h < 5)) and (old != "21-4"):
            old = "21-4"
            change_background(
                dir+"/21-4.png"
            )
        
        else:
            pass
        h += 1
        time.sleep(1)



if __name__ == "__main__":
    main()


