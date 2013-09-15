
class turing_machine:
    def __init__(self,initial_tape,initial_position,initial_m_configuration_symbol,list_of_m_configurations):
        
        self.tape = list(initial_tape)
        self.position = initial_position
        self.current_m_configuration_symbol = initial_m_configuration_symbol
        self.list_of_m_configurations = list_of_m_configurations
    
        
    def shift_right(self):
        self.position = self.position + 1
        if len(self.tape) < self.position:
            self.tape.append('_')
    def shift_left(self):
        self.position = self.position - 1
    def erase(self):
        self.tape[self.position -1] = "_"
    def print_character(self, str):
        
        #print self.position
        
        self.tape[self.position-1] = str
        #print self.tape
       
    
    def perform_list_of_operation(self,list_of_operations):
        operations_to_function_dictionary = {'R':self.shift_right, 'L': self.shift_left, 'E': self.erase, 'P':self.print_character}
        
        for operation_string in list_of_operations:
            #print operation_string
            if operation_string == '':
                l = 2
            elif operation_string[0] == "P":
                self.print_character(operation_string[1])
            else:
                operations_to_function_dictionary[operation_string]()
            
    def run_one_iteration(self):
        current_tape_symbol = self.tape[self.position -1]
        for m_configuration in self.list_of_m_configurations:
            #print m_configuration.m_configuration_symbol + self.current_m_configuration_symbol
            if (m_configuration.m_configuration_symbol == self.current_m_configuration_symbol) and is_accepted_symbol_of_m_configuration(current_tape_symbol,m_configuration):
                self.perform_list_of_operation(m_configuration.list_of_operations)
                self.current_m_configuration_symbol = m_configuration.final_m_congfig_symbol
                return None
        print "failed" +self.current_m_configuration_symbol + self.tape[self.position-1]
    def print_Turing_machine_current_state(self):
        print self.current_m_configuration_symbol + " | " + str(self.position) + " | " + "".join(self.tape)
    
class m_configuration:
    
    def __init__(self,m_configuration_symbol,list_of_characters,list_of_operations,final_m_configuration_symbol):
        self.m_configuration_symbol = m_configuration_symbol
        self.list_of_characters = list_of_characters
        self.list_of_operations = list_of_operations
        self.final_m_congfig_symbol = final_m_configuration_symbol.strip()
        
    def __repr__(self):
        return "%s%s%s%s" % (self.m_configuration_symbol,self.list_of_characters,self.list_of_operations,self.final_m_congfig_symbol)
             
def get_m_configuration_object_from_line(line):
    list_of_elements = line.split('|') # 
    m_configuration_symbol = list_of_elements[0].strip()
    list_of_characters = [char.strip() for char in list_of_elements[1].split(',')]
    list_of_operations = [operation.strip() for operation in list_of_elements[2].split(',')]
    final_m_configuration_symbol = list_of_elements[3]
    #print list_of_characters
    return m_configuration(m_configuration_symbol,list_of_characters,list_of_operations,final_m_configuration_symbol)
    
def is_accepted_symbol_of_m_configuration(current_symbol,m_configuration1):
    #print m_configuration1.final_m_congfig_symbol
    if current_symbol == '_':
        return "none" in m_configuration1.list_of_characters
    elif "any" in m_configuration1.list_of_characters:
        return True
    elif current_symbol in m_configuration1.list_of_characters:
        return True
    else:
        return False     
        
def load_turing_machine_from_file(file_name):
    file = open(file_name, 'r')
    #tm = file.read()
    initial_tape = list(file.readline().rstrip())
    if initial_tape ==  []:
        initial_tape = ['_']
    #print "initial tape" + str( initial_tape)
        
    initial_position = int(file.readline().rstrip())
    initial_m_configuration_symbol = file.readline().rstrip()
    list_of_m_configurations = []
    for line in file:
        list_of_m_configurations.append(get_m_configuration_object_from_line(line))
    #print "loaded turing machine"
    return turing_machine(initial_tape,initial_position,initial_m_configuration_symbol,list_of_m_configurations)

def print_x_amount_of_iterations_from_turing_machine_file(tm_file):
    x = input("how many iterations would you like to see?")
    Turing_Machine = load_turing_machine_from_file(tm_file)
    for i in range(x):
        Turing_Machine.run_one_iteration()
        Turing_Machine.print_Turing_machine_current_state()
        

        
print_x_amount_of_iterations_from_turing_machine_file("turing_machine_file.txt")


        
        
    
    
        
        
        
        
    