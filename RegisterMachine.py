instructions = lambda path : [line for line in open (path, "r")]
#Expected instructions are the following: I r, D r, J q
compile_rm_ind = lambda instructions, size : len ([e for e in instructions if e [0] in {'I', 'D', 'J', 'P'} ]) == len (instructions)

compile_rm_file = lambda instructions : compile_rm_ind (instructions, 5)
compile_rm = lambda instructions : compile_rm_ind (instructions, 4)

#initregisters = lambda r, value : [0 if e != r else value for e in range (0, 10)]

def interpret_rm (instructions, ind_instr, registers) :
    instruction = instructions [ind_instr]
    if (instruction [0] == 'I') :
        register = int (instruction [2:])
        registers [register] = registers [register] + 1
        return interpret_rm (instructions, ind_instr + 1, registers) if ind_instr < len (instructions) else registers
    elif (instruction [0] == 'D') :
        register = int (instruction [2:])
        if (registers [register] != 0) :
            registers [register] = registers [register] - 1
            return interpret_rm (instructions, ind_instr + 2, registers) if ind_instr + 2 < len (instructions) else registers
        else :
            return interpret_rm (instructions, ind_instr + 1, registers) if ind_instr + 1 < len (instructions) else registers
    elif (instruction [0] == 'P') :
        register = int (instruction [2:])
        print (registers [register])
        return interpret_rm (instructions, ind_instr + 1, registers) if ind_instr + 1 < len (instructions) else registers
    else : #It has to be a Jump J
        ind = int (instruction [2:])
        new_ind_instr = ind_instr + ind
        return interpret_rm (instructions, new_ind_instr, registers) if new_ind_instr < len (instructions) else registers

#def run_register_machine (path, registers) :
#    instrs = instructions (path)
#    print ("Running Register Machine from path " + path)
#    if (compile_rm (instrs)) :
#        finalregisters = interpret_rm (instrs, 0, registers)
#        print ("    Resulting Configuration for Registers: " + str (finalregisters))
#    else :
#        print ("    COMPILING ERROR!!")

def run_register_machine_instrs (instructions, registers) :
    print ("Running Register Machine with instructions " + str (instructions))
    if (compile_rm (instructions)) :
        finalregisters = interpret_rm (instructions, 0, registers)
        print ("    Resulting Configuration for Registers: " + str (finalregisters))
    else :
        print ("    COMPILING ERROR!!")

#CLEAR MACHINE: D +7 ; J +2 ; J -2
CLEAR = lambda r : ["D +" + str (r), "J +2", "J -2"]

#MOVE MACHINE:
MOVE = lambda r, s : CLEAR (s) + ["D +" + str (r), "J +3", "I +" + str (s), "J -3"]

#DIRTY ADD MACHINE (the first ADD created by Enderton...):
DIRTYADD = lambda r1, r2, r3 : ["D +" + str (r1), "J +4", "I +" + str (r2), "I +" + str (r3), "J -4"]

#COPY MACHINE:
COPY = lambda r, middle, s : CLEAR (s) + MOVE (r, middle) + DIRTYADD (middle, r, s)

#ADD MACHINE:
ADD = lambda r1, r2, r0 : CLEAR (r0) + MOVE (r1, 3) + DIRTYADD (3, r1, r0) + MOVE (r2, 3) + DIRTYADD (3, r2, r0)

#MULTIPLY MACHINE
MULTIPLYAUX = lambda r1, r2, r0 : ["D +" + str (r2), "J +50"] + ADD (r1, 5, r0) + COPY (r0, 7, 5)
MULTIPLYAUX2 = lambda r1, r2, r0, multiplyaux : multiplyaux + ["J -" + str (len (multiplyaux))]
MULTIPLY = lambda r1, r2, r0 : MULTIPLYAUX2 (r1, r2, r0, MULTIPLYAUX (r1, r2, r0))

REG = lambda : [0, 4, 0, 0, 3, 0, 0, 13, 0, 0]

m = MULTIPLY (4, 1, 0)

print ("")
run_register_machine_instrs (m, REG ())
