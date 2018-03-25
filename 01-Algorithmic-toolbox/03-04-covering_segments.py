##### python2
import sys

def optimal_points(segments):
    points = []

    while len(segments[0]) > 0:
	    # choose the minimum end coordinate as the safe move
        point = min(segments[1])
        points.append(point)
        # delete all intervals which has the start point less or equal as point coordinate
        for i in range(0, len(segments[0]):
            if segments[0][i] <= point:
                segments[0].pop(i)
                segments[1].pop(i)
        
    return points
'''
#python3
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
'''		

# Input
n = int(raw_input())
#n = int(raw_input("Enter number n of segments: "))
segments = list()
start = list()
end = list()
i=0
while i < n:
    input = raw_input().split()
	#input = raw_input("Enter the coordinates of endpoints of segment: ").split()
    input[0], input[1] = int(input[0]), int(input[1])
    start.append(input[0])
    end.append(input[1])
    segments.append(start)
    segments.append(end)
    i+= 1
points = optimal_points(segments)

#Output
print len(points)
for p in points: 
    print(p)
