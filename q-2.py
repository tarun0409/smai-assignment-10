import math

sequence_dict = dict()
transition_dict = dict()

sequence_dict['E'] = dict()
sequence_dict['5'] = dict()
sequence_dict['I'] = dict()

sequence_dict['E']['A'] = 0.25
sequence_dict['E']['C'] = 0.25
sequence_dict['E']['G'] = 0.25
sequence_dict['E']['T'] = 0.25

sequence_dict['5']['A'] = 0.05
sequence_dict['5']['C'] = 0
sequence_dict['5']['G'] = 0.95
sequence_dict['5']['T'] = 0

sequence_dict['I']['A'] = 0.4
sequence_dict['I']['C'] = 0.1
sequence_dict['I']['G'] = 0.1
sequence_dict['I']['T'] = 0.4

transition_dict = dict()
transition_dict['#'] = dict()
transition_dict['E'] = dict()
transition_dict['5'] = dict()
transition_dict['I'] = dict()

transition_dict['#']['#'] = 0
transition_dict['#']['E'] = 1.0
transition_dict['#']['5'] = 0
transition_dict['#']['I'] = 0
transition_dict['#']['$'] = 0

transition_dict['E']['#'] = 0
transition_dict['E']['E'] = 0.9
transition_dict['E']['5'] = 0.1
transition_dict['E']['I'] = 0
transition_dict['E']['$'] = 0

transition_dict['5']['#'] = 0
transition_dict['5']['E'] = 0
transition_dict['5']['5'] = 0
transition_dict['5']['I'] = 1.0
transition_dict['5']['$'] = 0

transition_dict['I']['#'] = 0
transition_dict['I']['E'] = 0
transition_dict['I']['5'] = 0
transition_dict['I']['I'] = 0.9
transition_dict['I']['$'] = 0.1


# sequence = "CTTCATGTGAAAGCAGACGTAAGTCA"
# state_path = "EEEEEEEEEEEEEEEEEE5IIIIIII"
print 'Enter the sequence : '
sequence = raw_input()
print 'Enter the state path : '
state_path = raw_input()


state_path = "#" + state_path + "$"
prob = 0

for i in range(0,len(state_path)-1):
    curr_state = state_path[i]
    next_state = state_path[i+1]
    if i < len(sequence):
        sm = math.log(sequence_dict[next_state][sequence[i]])
    else:
        sm = 0
    tm = math.log(transition_dict[curr_state][next_state])
    prob += (sm + tm)

print
print 'Log probability : ' + str(prob)
print
    

