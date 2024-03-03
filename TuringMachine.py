R = lambda : "Right"
L = lambda : "Left"

#Function delta_from_file gets a txt file with a transition function (program) 
#and mounts a dictionary that corresponds to the function
def delta_from_file (path) :
    file = open (path, "r")
    content = lambda file : [line for line in file]
    lines = content (file)
    delta = {}
    for line in lines :
        toks = line.split (" ")
        p0, p2 = toks [0], toks[2]
        p1 = "" if toks [1] == "_" else toks [1]
        p3 = "" if toks [3] == "_" else toks [3]
        p4_partial = toks [4][0 : len(toks [4]) - 1]
        p4 = "-" if p4_partial == "S" else p4_partial
        delta.update ({(p0, p1) : (p2, p3, p4)})
    return delta

#Function CONFIG_LOG just stores the step-by-step processing of the Turing Machine as a String
def CONFIG_LOG (state, config, delta) :
    headpos = config [0]
    tape = config [1]
    EL = lambda tape, pos, head : tape [pos] if pos != head else "-> " + str (tape [pos])
    TAPE_WITH_HEAD = lambda tape, headpos : [EL (tape, i, headpos) for i in range (len (tape))]
    r = tape [headpos]
    s = "Current config: we are in state " + str (state) + ", reading " + str (r)
    s = s + " with head in position " + str (headpos) + " of tape " + str (TAPE_WITH_HEAD (tape, headpos)) + ".\n"
    next = delta [(state, r)]
    s = s + "Now we (I) are going to state " + next [0] + ", (II) write " + str (next[1])
    s = s + " on where the head is pointing to, and (III) move to the " + next [2] + " direction...\n"
    return s

def NEXTCONFIG (state, config, delta) :
    headpos = config [0]
    tape = config [1]
    r = tape [headpos]
    next = delta [(state, r)]
    newheadpos = headpos + 1 if next [2] == R () else headpos - 1 if next [2] == L () else headpos
    newtape = tape [0:headpos] + [next [1]] + tape [headpos + 1 : ]
    newstate = next [0]
    return (newheadpos, newtape, newstate)

def PROCESS_TM (tm, config, input, description) :
    headpos = config [0]
    tape = config [1]
    currentstate = config [2]
    delta = tm [3]
    initialstate = tm [4]
    acceptstate = tm [5]
    rejectstate = tm [6]
    if (currentstate == acceptstate) :
        print ("Input " + input + " ACCEPTED for TM with description " + "[" + description + "]" + "!! End of TM processing...")
    elif (currentstate == rejectstate) :
        print ("Input " + input + " REJECTED for TM with description " + "[" + description + "]" + "... End of TM processing...")
    else :
        print (CONFIG_LOG (currentstate, config, delta))
        PROCESS_TM (tm, NEXTCONFIG (currentstate, config, delta), input, description)

PROCESS_TM_INIT = lambda tm, input, description : PROCESS_TM (tm, INITIALCONFIG (input), input, description)

#Function GENTAPE gets an input and generates a tape with that input...
GENTAPE = lambda strinput : [""] * 5 + [e for e in strinput] + [""] * 5

#Function INITIALCONFIG gets an input and 
#    (I) generates a tape for that input
#    , (II) starts in q0 as the current state
#    , (III) starts with the head at position 5 of the tape
INITIALCONFIG = lambda input : (5, GENTAPE (input), "q0")

#Function TM returns a tuple with 7 values corresponding to a specific Turing Machine
def TM (path, Q, sigma, gamma, initialstate, accept, reject) :
    DELTA = lambda : delta_from_file (path)
    return (Q, sigma, gamma, delta_from_file (path), initialstate, accept, reject)

def TM_VERIFY_EVEN () :
    FILEPATH = lambda : "C:\\Users\\samue\\Software\\eclipse-workspace\\ATCUNIFOR\\src\\VerifyEven.txt"
    DELTA = lambda : delta_from_file (FILEPATH ())
    Q = lambda : {"q0", "q1", "qAccept", "qReject"}
    SIGMA = lambda : {"0", "1"}
    GAMMA = lambda : {"0", "1", ""}
    return TM (FILEPATH (), Q (), SIGMA (), GAMMA (), "q0", "qAccept", "qReject")

def TM_VERIFY_MAJOR_THAN () :
    FILEPATH = lambda : "C:\\Users\\samue\\Software\\eclipse-workspace\\ATCUNIFOR\\src\\VerifyMajorThan.txt"
    DELTA = lambda : delta_from_file (FILEPATH ())
    Q = lambda : {"q0", "qVai1", "qAccept", "qReject"}
    SIGMA = lambda : {"A", "B", "C", "D"}
    GAMMA = lambda : {"0", "1", "A", "B", "C", "D"}
    return TM (FILEPATH (), Q (), SIGMA (), GAMMA (), "q0", "qAccept", "qReject")

PROCESS_TM_INIT (TM_VERIFY_EVEN (), "1010", "Turing machine that accepts inputs with even number of 0's")
PROCESS_TM_INIT (TM_VERIFY_MAJOR_THAN (), "ABDDCB", "Turing machine that checks if left operand is bigger than the right operand")
PROCESS_TM_INIT (TM_VERIFY_MAJOR_THAN (), "ADDDCB", "Turing machine that checks if left operand is bigger than the right operand")
