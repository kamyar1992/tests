def float_counter(starter: float, final: float, step: float):
    counter = starter
    while counter <= final:
        yield counter
        counter += step


for item in float_counter(2.1, 2.2, 0.01):
    # print(round(item, 2))
    print("{:.2f}".format(round(item, 2)))
