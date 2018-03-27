#python2
#import sys

#You are organizing an online lottery. To participate, a person bets on a single
#integer. You then draw several ranges of consecutive integers at random.
#A participant's payoff then is proportional to the number of ranges that
#contain the participant's number minus the number of ranges that does not
#contain it. You need an efficient algorithm for computing the payoffs for all
#participants. A naive way to do this is to simply scan, for all participants, the
#list of all ranges. However, you lottery is very popular: you have thousands
#of participants and thousands of ranges. For this reason, you cannot afford
#a slow naive algorithm

def fast_count_segments(starts, ends, points):
    cnt = []
    cnt_dict = {}
    #write your code here
    segments_num = 0
	# add to new array all points and starts and ends with marks about left, point, right
    # and then sort by point
	list_points = [(x, 'l') for x in starts]
    list_points += [(x, 'p') for x in points]
    list_points += [(x, 'r') for x in ends]
    list_points.sort()
    
	# go through new sorted array
    for position, type_point in list_points:
	    # if point with mark left, than we went in new segment, so add 1 to number of
		# current segments
        if type_point == 'l':
            segments_num += 1
		# if point marked right, we went out of segment. Subtract from number of
		# current segment
        elif type_point == 'r':
            segments_num -= 1
		# if point marked as point, so we add this point and number of current 
        # segments to dictionary 
        else:
            cnt_dict[position] = segments_num
	# extract information for points from dictionary
    for point in points:
        cnt.append(cnt_dict[point])
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

input = raw_input().split()
data = list(map(int, input))
s = data[0]
p = data[1]
starts, ends = [], []
for i in range (0, s):
    input2 = raw_input().split()
    data2 = list(map(int, input2))
    starts.append(int(data2[0]))
    ends.append(int(data2[1]))
input3 = raw_input().split()
points = list(map(int, input3))
    #use fast_count_segments
cnt = naive_count_segments(starts, ends, points)
for x in cnt:
    print x,