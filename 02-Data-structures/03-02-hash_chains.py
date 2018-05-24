# python2

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = ((ans * self._multiplier + ord(c)) % self._prime + self._prime)% self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(raw_input().split())


    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            try:
                self.write_chain(reversed (self.elems[query.ind]))
            except:
                print " "
            
        else:
            value = self._hash_func(query.s)
            if query.type == 'find':
                was_found = value in self.elems
                if was_found:
                    if query.s in self.elems[value]:
                        self.write_search_result(True)
                    else:
                        self.write_search_result(False) 
                else:
                    self.write_search_result(False)
            elif query.type == 'add':
                if value not in self.elems:
                    self.elems[value] = []
                    self.elems[value].append(query.s)
                else:
                    if query.s not in self.elems[value]:
                        self.elems[value].append(query.s)
            else:
                if value in self.elems:
                    if len(self.elems[value]) > 1:
                        self.elems[value].remove(query.s)
                    else:
                        self.elems.pop(value)

    def process_queries(self):
        n = int(raw_input())
        for i in range(n):
            self.process_query(self.read_query())

bucket_count = int(raw_input())
proc = QueryProcessor(bucket_count)
proc.process_queries()


