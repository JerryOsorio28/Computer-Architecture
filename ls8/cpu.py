"""CPU functionality."""

import sys

#OP CODES
LDI = 0b10000010 #130 / This instruction sets a specified register to a specified value.
PRN_REG = 0b01000111 #71 / Should print the value of a register
EIGHT = 0b00001000 #8 / Should print the number 8
HALT = 0b00000001 #1 / Halt the CPU (and exit the emulator).
ADD = 0b10100000 #160 / Add the value in two registers and store the result in registerA.
MUL = 0b10100010 #162 / Multiply the values in two registers together and store the result in registerA.

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256 #bytes of memory
        self.reg = [0] * 12 #register
        self.pc = 0 #program counter

    #should accept the address to read and return the value stored there.
    def ram_read(self, address):
        # print(self.ram[address])
        return self.ram[address]

    # should accept a value to write, and the address to write it to.
    def ram_write(self, address, value):
        self.ram[address] = value

    def load(self, filename):
        """Load a program into memory."""

        # pointer to iterate our program
        address = 0
        
        filename = sys.argv[1]

        try:
            with open(filename) as f:
                for line in f:

                    #  Ignore comments
                    comment_split = line.split('#')

                    # Strip whitespace
                    num = comment_split[0].strip()

                    # Ignore blank lines
                    if num == '':
                        continue

                    integer = int(num, 2)
                    self.ram[address] = integer
                    address += 1

        except FileNotFoundError:
            print('File not found')
            sys.exit(2)

        # For now, we've just hardcoded a program:
        # program = [
        #     # From print8.ls8
        #     EIGHT,
        #     LDI, # LDI R0,8
        #     65,
        #     2,
        #     LDI, # LDI R0,8
        #     20,
        #     3,
        #     ADD,
        #     2,
        #     3,
        #     PRN_REG,
        #     2,
        #     HALT # HLT
        # ]
        # program = [
        #   10000010, 
        #   0, 
        #   1000, 
        #   10000010, 
        #   1, 
        #   1001, 
        #   10100010, 
        #   0, 
        #   1, 
        #   1000111, 
        #   0, 
        #   1
        # ]
        

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1
    


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

        print('pc', self.pc)
        print('ram', self.ram)
        print('reg', self.reg)

        while running:
            command = self.ram[self.pc]

            if command == LDI: # LDI
                num = self.ram[self.pc + 1] #0
                reg = self.ram[self.pc + 2] # 8
                self.reg[reg] = num
                self.pc += 3

            elif command == ADD: # ADD
                reg_a = self.ram[self.pc + 1]
                reg_b = self.ram[self.pc + 2]
                self.reg[reg_a] += self.reg[reg_b]
                self.pc += 3

            elif command == MUL: # MUL
                reg_a = self.ram[self.pc + 1]
                reg_b = self.ram[self.pc + 2]
                self.reg[reg_a] *= self.reg[reg_b]
                self.pc += 3

            elif command == EIGHT: # Number 8
                print('command', command)
                self.pc += 1

            elif command == PRN_REG: # PRN
                reg = self.ram[self.pc + 1]
                print('reg', self.reg[reg])
                self.pc += 2

            elif command == HALT: # HALT
                running = False
            else:
                print(f'Unknown instruction: {command}')
                sys.exit(1)


# if __name__=='__main__':
#     cpu = CPU()
#     cpu.load()
#     cpu.run()
    # print(cpu.ram)
        
            
