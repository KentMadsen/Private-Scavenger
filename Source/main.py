from Source import Program

program = Program.Program()

def main():
    initialise()
    execution()
    finalize()

def initialise():
    print('Stage: Initialise')
    program.initialise()

def execution():
    print('Stage: Execution')
    program.execute()

def finalize():
    print('Stage: Finalize')

# Entry
if __name__ == '__main__':
    main()