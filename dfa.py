""" File name:   dfa.py
    Author:      <tanmay negi>
    Date:        <12/03/2021>
    Description: This file defines a function which reads in
                 a DFA described in a file and builds an appropriate datastructure.

                 There is also another function which takes this DFA and a word
                 and returns if the word is accepted by the DFA.

                 It should be implemented for Exercise 3 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""

class dfa():
    def __init__(self):
        self.initial = None
        self.accepting = []
        self.contents = None
        self.table = {}
        self.__path = None
    
    def load_dfa(self,path):
        """ This function reads the DFA in the specified file and returns a
        data structure representing it. It is up to you to choose an appropriate
        data structure. The returned DFA will be used by your accepts_word
        function. Consider using a tuple to hold the parts of your DFA, one of which
        might be a dictionary containing the edges.

        We suggest that you return a tuple containing the names of the start
        and accepting states, and a dictionary which represents the edges in
        the DFA.

        (str) -> Object
        """
        self.__path = path
        self.contents = open(path,"r").read().splitlines()
        for line in self.contents:
            if not self.initial and ("initial" in line):
                self.initial = line.split(" ")[1]
            if not self.accepting and ("accepting" in line):
                self.accepting = line.split(" ")[1:]
            if "transition" in line:
                temp = line.split(" ")
                if temp[1] not in self.table.keys():
                    self.table[temp[1]] = {}
                    self.table[temp[1]][temp[3]] = temp[2]
                else:
                    self.table[temp[1]][temp[3]] = temp[2]
        return (self.initial,self.accepting,self.table)
    
    def accepts_word(self,word):
        """ This function takes in a DFA (that is produced by your load_dfa function)
        and then returns True if the DFA accepts the given word, and False
        otherwise.

        (Object, str) -> bool
        """
        if not self.initial or not self.accepting or not self.table:
            print("dfa not loaded")
            return False
        print("parsed by",self.__path)
        current_state = self.initial
        for ch in word:
            if ch not in self.table[current_state].keys():
                return False
            current_state = self.table[current_state][ch]
        return True if current_state in self.accepting else False
