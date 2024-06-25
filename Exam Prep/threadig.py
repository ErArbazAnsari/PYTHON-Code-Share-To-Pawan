import threading  # importing the threading module


def print_cube(num):

    # function to print cube of given num
    print("Cube: {}".format(num * num * num))
def print_square(num):


    print("Square: {}".format(num * num))  # function to print square of given num
if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(100000000000000000000000000000000000000,))
    t1.start()
    t2.start()  # starting thread 1
# starting thread 2
    t1.join()
    t2.join()  # wait until thread 1 is completely executed
# wait until thread 2 is completely executed
print("Done!")
