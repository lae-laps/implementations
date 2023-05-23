#!/usr/bin/env python
# Line simulator

import os
import time

class Line:
    def __init__(self):
        self.collision = None
        self.status = True              # if set to False the line is idle
        self.transmission_counter = 0
        self.frames = [1, 2, 43, 543, 4, 4, 5, 4]

        max_transmission_counter = 10
        delay = 1

    def abort(self):
        print("sending jam signal and stopping transmission")
        os.exit(1)

    def close_cleanly(self):
        print("closing line")
        return

    def send_jam_signal(self):
        print("error: could not transmmit data - sent jam signal")
        self.transmission_counter += 1
        if self.transmission_counter >= max_transmission_counter:
            self.abort()
        else:
            self.sleep(delay)
            send()

    def send(self):
        self.transmission_counter = 1

        counter = 0
        for frame in self.frames:
            if self.collision:
                self.send_jam_signal()
            print(f"sending frame {counter} : {frame}")
            counter += 1

        self.close_cleanly()

    def assemble_frame(self):
        while not self.status:
            time.sleep(delay)
        self.send()

if __name__ == "__main__":
    line = Line()
    line.assemble_frame()
