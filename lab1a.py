import picar_4wd as fc
import random
import time
speed = 30
#mine is inverted
def main():
    while True:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue
        tmp = scan_list[3:7]
        if tmp != [2,2,2,2]:
            fc.backward(1)
            #optional sleep
            # time.sleep(1)
            #take whichever sum is greater and start turning that opposite way
            if(sum(scan_list[:4]) > sum(scan_list[5:])):
                fc.turn_left(10)
            elif(sum(scan_list[:4]) < sum(scan_list[5:])):
                fc.turn_right(10)
            else:
                fc.backward(1)

            #random direction code
            # fc.backward(10)
            # time.sleep(1)
            # fc.stop()
            # turn = random.randint(0, 1)
            # if turn == 0:
            #     fc.turn_right(speed)
            # else: 
            #     fc.turn_left(speed)
                
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
