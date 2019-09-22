def weight_on_planets():
    # write your code here
    weight = input("What do you weigh on earth?")
    # calculate weight on mars
    mars_weight = float(weight) * 0.38
    # calculate weight on jupiter
    jupiter_weight = float(weight) * 2.34
    # print outputs
    print(" \n On Mars you would weigh " + str(mars_weight) + " pounds.")
    print(" On Jupiter you would weigh " + str(jupiter_weight) + " pounds.")


if __name__ == '__main__':
    weight_on_planets()
