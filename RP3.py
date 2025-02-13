import csv
import matplotlib.pyplot as plt
import numpy as np

#List of windspeeds that will be read from the csv file
windspeed = []

#Reads from the csv file
with open('windspeeds.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    writer = csv.writer(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        windspeed.append(row[0])
    windspeed.remove('\ufeff')

#Converts from km/h to m/s
for i in range(len(windspeed)):
    windspeed[i] = float(windspeed[i])/3.6

#Weibull distribution parameters
k = 2.4229 #Shape factor
c = 6.5226 #Scale factor

#Weibull probability density function
def weibull_prob_density(v):
    return (k/c)*(v/c)**(k-1)*np.exp(-(v/c)**k)

y_val = [0]

#Numerical integration to find probabilities of each windspeed
def expected_val(prob_density):

    n = 1000000  # Approaching infinity
    a = 0  # Approaching negative infinity
    b = 10*c  # Approaching infinity

    delta_x = (b - a) / n
    x_val= [a]
    approx = 0
    for i in range(1, n + 1):
        xi = x_val[i - 1] + delta_x
        x_val.append(xi)
        yi = prob_density(xi) * xi
        y_val.append(prob_density(xi))
        approx += yi
    approx *= delta_x

    #Graphing Weibull distribution
    plt.plot(x_val, y_val)
    plt.xlim(0, 23.5)
    plt.ylim(0, 0.17)
    plt.title('Weibull Distribution of Wind speed (m/s) in Churchill, MB')
    plt.xlabel('Wind speed (m/s)')
    plt.ylabel('Probability')
    plt.show()
    return approx


print(expected_val(weibull_prob_density))

#Graphing histogram based on csv data
plt.hist(windspeed, bins = 100)
plt.title('Wind speed (m/s) in Churchill, MB from 2013-2025')
plt.xlabel('Wind speed (m/s)')
plt.ylabel('Number of Occurrences')
plt.xlim(0, 23.5)
plt.show()