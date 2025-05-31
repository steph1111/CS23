"""
File:       fsm.py
Author:     Stephanie L'Heureux
Email:      stephanielh1111@gmail.com
Due:        Sat May 31, 2025 7:00pm
CS23:       Program Three (FSM)
"""
import sys

class FSM:
    def __init__(self, filename):
        with open(filename) as file:
            self.deterministic = file.readline().strip() == "deterministic"
            self.states     = file.readline().strip().split()[1]
            self.inputs     = file.readline().strip().split()[1]
            self.start      = file.readline().strip().split()[1]
            self.accepting  = set(file.readline().strip().split()[1::])
            file.readline()
            self.transitions = dict()
            self.epsilon = dict(set()) 
            for line in file:
                c, n, s = line.split()
                if s == "-1":
                    if c not in self.epsilon:
                        self.epsilon[c] = set(n)
                    else:
                        self.epsilon[c].add(n)
                else:
                    if c not in self.transitions:
                        self.transitions[c] = {s : n}
                    else:
                        self.transitions[c][s] = n

    def run(self, inputs: list):
        self.inputs = inputs
        if self.deterministic:
            self._detrm()
        else:
            self._non_detrm()

    def _detrm(self):
        current = self.start
        for symbol in self.inputs:
            current = self.transitions[current][symbol]
    
        if current in self.accepting:
            print("accepted\n")
        else:
            print("rejected\n")


    def _non_detrm(self):

        def check_epsilon():
            for c in current.copy():
                    if c in self.epsilon:
                        current.remove(c)
                        current.update(self.epsilon[c])

        current = {self.start}
        check_epsilon()

        for s in self.inputs:
            new_current = set()
            check_epsilon()
            for c in current:
                if c in self.transitions:
                    new_current.add(self.transitions[c][s])
            current = new_current

        accept = False
        for state in current:
            if state in self.accepting:
                accept = True
                break

        if accept:
            print("accepted")
        else:
            print("rejected")


if __name__ == "__main__":
    fsm = FSM(sys.argv[1])
    for line in sys.stdin:
        fsm.run(line.split())
