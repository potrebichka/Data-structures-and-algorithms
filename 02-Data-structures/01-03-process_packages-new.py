# python2

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        #queue of packets
        self.finish_time_ = []

    def Process(self, request):
        # write your code here
        self.finish_time_ = [time for time in self.finish_time_ if time > request.arrival_time]
        if len(self.finish_time_) + 1 > self.size:  
            return Response(True, -1)
        elif len(self.finish_time_) == 0:
            self.finish_time_.append(request.arrival_time+request.process_time)
            return Response(False, request.arrival_time)
        else:
            self.finish_time_.append(self.finish_time_[-1]+request.process_time)
            return Response(False, self.finish_time_[-2])
            

def ReadRequests(count):
    requests = []
    '''
    file_handler = open('tests/21','r')
    i=0
    for line in file_handler:
        if i == 0:
            i+=1
            continue
        arrival_time, process_time = map(int, line.strip().split())
        requests.append(Request(arrival_time, process_time))
    '''
    for i in range(count):
        arrival_time, process_time = map(int, raw_input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

size, count = map(int, raw_input().strip().split())
requests = ReadRequests(count)

buffer = Buffer(size)
responses = ProcessRequests(requests, buffer)

PrintResponses(responses)