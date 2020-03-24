"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256 #bytes of memory
        self.reg = [0] * 8 #register
        self.pc = 0 #program counter

    #should accept the address to read and return the value stored there.
    def ram_read(self, address):
        # print(self.ram[address])
        return self.ram[address]

    # should accept a value to write, and the address to write it to.
    def ram_write(self, address, value):
        pass
        # self.ram[address] = address

    def load(self):
        """Load a program into memory."""
        # pointer to iterate our program
        address = 0

        LDI = 0b10000010
        PRN_NUM = 0b01000111
        EIGHT = 0b00001000
        HALT = 0b00000001

        # For now, we've just hardcoded a program:
        program = [
            # From print8.ls8
            LDI, # LDI R0,8
            0b00000000,
            EIGHT,
            PRN_NUM, # PRN R0
            1,
            0b00000000,
            PRN_NUM,
            12,
            EIGHT,
            HALT, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1
    


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
        pc = 0
        running = True

        while running:
            command = self.ram[pc]

            if command == 130: # LDI
                pass
            elif command == 8: # Number 8
                print(command) #8

            elif command == 71: # PRN
                num = self.ram[pc + 1]
                print(num)
                pc += 2

            elif command == 1: # HALT
                running = False
            else:
                print(f'Unknown instruction: {command}')

            pc += 1

# if __name__=='__main__':
#     cpu = CPU()
#     cpu.load()
#     cpu.run()
    # print(cpu.ram)
        
            
