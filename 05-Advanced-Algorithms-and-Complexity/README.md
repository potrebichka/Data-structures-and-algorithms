## 1-1. Evacuating People.
*An algorithm for finding maximum flow in a network to determine how fast people can be evacuated from the given city.*

**Input:** The first line of the input contains integers n and m — the number of cities and the number of roads respectively. Each of the next m lines contains three integers u, v and c describing a particular road — start of the road, end of the road and the number of people that can be transported through this road in one hour. u and v are the 1-based indices of the corresponding cities.
The city from which people are evacuating is the city number 1, and the capital city is the city number n.

**Output:** The maximum number of people that can be evacuated from the city nu,ber 1 each hour.

## 1-2. Assigning Airline Crews to Flights.
*The airline offers a bunch of flights and has a set of crews that can work on those flights. However, the flights are starting in different cities and at different times, so only some of the crews are able to work on a particular flight. You are given the pairs of flights and associated crews that can work on those flights. You need to assign crews to as many flights as possible and output all the assignments.* An Algorithm for finding maximum matching in bipartite graph to assign airline crews to flights in the most efficient way.

**Input:** The first line of the input contains integers n and m — the number of flights and the number of crews respectively. Each of the next n lines contains m binary integers (0 or 1). If the j-th integer in the i-th line is 1, then the crew number j can work on the flight number i, and if it is 0, then it cannot.

**Output**: Output n integers — for each flight, output the 1-based index of the crew assigned to this flight. If no crew is assigned to a flight, output −1 as the index of the crew corresponding to it. All the positive indices in the output must be between 1 and m, and they must be pairwise different, but you can output any number of −1’s. If there are several assignments with the maximum possible number of flights having a crew assigned, output any of them.

## 1-3. Stock Charts.
*Find the most compact way of visualising stock price data using charts.*
You’re in the middle of writing your newspaper’s end-of-year economics summary, and you’ve decided that you want to show a number of charts to demonstrate how different stocks have performed over the course of the last year. You’ve already decided that you want to show the price of n different stocks, all at the same k points of the year. A simple chart of one stock’s price would draw lines between the points (0, price_0),(1, price_1), . . . ,(k − 1, price_k−1), where price_i is the price of the stock at the i-th point in time. In order to save space, you have invented the concept of an overlaid chart. An overlaid chart is the
combination of one or more simple charts, and shows the prices of multiple stocks (simply drawing a line for each one). In order to avoid confusion between the stocks shown in a chart, the lines in an overlaid chart may not cross or touch.
Given a list of n stocks’ prices at each of k time points, determine the minimum number of overlaid charts you need to show all of the stocks’ prices

**Input:** The first line of the input contains two integers n and k — the number of stocks and the number of points in the year which are common for all of them. Each of the next n lines contains k integers. The i-th of those n lines contains the prices of the i-th stock at the corresponding k points in the year.

**Output:**The minimum number of overlaid charts to visualize all the stock price data you have.
