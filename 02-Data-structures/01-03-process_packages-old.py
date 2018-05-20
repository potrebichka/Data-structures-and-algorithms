# python3

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
        self.finish_time_ = []

    def Process(self, request):
        # write your code here
        var_finish_time = 0
        for fin_time in self.finish_time_:
            if request.arrival_time >= fin_time:
                if len(self.finish_time_) == 1:
                    var_finish_time = self.finish_time_[-1]
                else:
                    var_finish_time = 0
                self.finish_time_.remove(fin_time)
            else:
                break
        if len(self.finish_time_) >= self.size:
            return Response(True, -1)
        elif self.finish_time_ == []:
            if request.arrival_time > var_finish_time:
                var_finish_time = request.arrival_time
            self.finish_time_.append(var_finish_time + request.process_time)
        elif request.arrival_time > self.finish_time_[-1]:
            self.finish_time.append(request.arrival_time + request.process.time)
        else:
            self.finish_time_.append(self.finish_time_[-1] + request.process_time)
        return Response(False, self.finish_time_[-1]-request.process_time)

def ReadRequests(count):
    requests = []
    #file_handler = open('tests/21.txt','r')
    #i=0
    #for line in file_handler:
    #    if i == 0:
    #        i+=1
    #        continue
    for i in range(count):
        line = raw_input()
        arrival_time, process_time = map(int, line.split())
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
        
size, count = map(int, raw_input("Enter size of buffer and number n of incoming network packets: ").split())
requests = ReadRequests(count)

buffer = Buffer(size)
responses = ProcessRequests(requests, buffer)

PrintResponses(responses)
