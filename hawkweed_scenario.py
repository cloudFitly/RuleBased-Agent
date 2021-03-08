""" File name: hawkweed_scenario.py
    Author   : Tanmay Negi   
    Date     : 09/03/2021
    Description: This file represents a scenario simulating the spread of 
                 hawkweed through Kosciuszko National Park and its
                 surroundings. It should be implemented for Part 1 of 
                 Exercise 4 of Assignment 0.

                 See the lab notes for a description of its contents.
"""
import sys
class HawkweedScenario():
    
    def __init__(self):
        
        # self._folder      = "exercise4_maps/"
        self.__contents   = None
        
        self.threshold   = None
        self.growth      = None
        self.spread      = None
        
        self.locations   = []
        self.location    = None
        
        self.conn        = {}
        self.hawkweed    = {}
        
    
    def read_scenario_file(self,path):
        try:
            self.__contents = open(path,"r").read().splitlines()
        except:
            e = sys.exc_info()[0]
            print("error:",e)
            return False
        for line in self.__contents:
            if "threshold" in line:
                self.threshold = float(line.split(" ")[1])
            if "growth" in line:
                self.growth = float(line.split(" ")[1])
            if "spread" in line:
                self.spread = float(line.split(" ")[1])
            if "start" in line:
                self.location = line.split(" ")[1]
            if "location" in line:
                self.locations.append(line.split(" ")[1])
            if "hawkweed" in line:
                temp = line.split(" ")
                self.hawkweed[temp[1]] = float(temp[2])
            if "conn" in line:
                temp = line.split(" ")
                if temp[1] not in self.conn.keys():
                    self.conn[temp[1]] = set()
                    self.conn[temp[1]].add(temp[2])
                else:
                    self.conn[temp[1]].add(temp[2])
        self._updateKnowledge()
        return True
        
    def _updateKnowledge(self):
        """
            updates agent knowledge from parsed information
        """
        
        # updating known locations
        locations = set(self.locations)
        for loc in self.conn.keys():
            locations.add(loc)
            locations.union(self.conn[loc])
        self.locations = list(locations)
        
        
        # updating hawkweed info at locs
        for loc in self.locations:
            if loc not in self.hawkweed.keys():
                self.hawkweed[loc] = 0.0
        
        # updating _conn to reflect bi=directional paths
        temp = dict(self.conn)
        for loc in self.conn.keys():
            for node in self.conn[loc]:
                if node not in self.conn.keys():
                    temp[node] = set()
                temp[node].add(loc)
        self.conn = dict(temp)
        
        
    def valid_moves(self):
        _next = list(self.conn[self.location])
        return _next+[self.location]
    
    def move(self,loc):
#         self._valid_moves = valid_moves()
        try:
            if loc not in self.valid_moves():
                raise ValueError("{} invalid move".format(loc))
            self.location = loc
            self.hawkweed[loc] = 0
        except ValueError as e:
            print(e)
    
    def contributions(self,nodes):
        """
            calculates spread contribution from [(node)] to root
        """
        _sum = 0
        for node in nodes:
            if self.hawkweed[node] >= self.threshold:
                _sum = _sum + self.hawkweed[node]*self.spread
        return _sum
    
    def  spread_hawkweed(self):
        temp = float(self.hawkweed[self.location])
        
        for loc in self.locations:
            d = float(self.hawkweed[loc])
            d = d + d*self.growth + self.contributions(self.conn[loc])
            self.hawkweed[loc] = float(d)
        
        self.hawkweed[self.location] = float(temp)
    
 