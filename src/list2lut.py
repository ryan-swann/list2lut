
def printTotoro():
    print('''\n\n
                              !         !          
                             ! !       ! !          
                            ! . !     ! . !          
                               ^^^^^^^^^ ^            
                             ^             ^          
                           ^  (0)       (0)  ^       
                          ^        ""         ^       
                         ^   ***************    ^     
                       ^   *                 *   ^    
                      ^   *   /\   /\   /\    *    ^   
                     ^   *                     *    ^
                    ^   *   /\   /\   /\   /\   *    ^
                   ^   *                         *    ^
                   ^  *                           *   ^
                   ^  *                           *   ^
                    ^ *                           *  ^  
                     ^*                           * ^ 
                      ^ *                        * ^
                      ^  *                      *  ^
                        ^  *       ) (         * ^
                            ^^^^^^^^ ^^^^^^^^^ 
                        Totoro has generated your file



    ''')


def list2lut(inList,tableName):
    '''
        Convert python list "inList" to sv module of name "tableName"
        inList    : The input list
        tableName : The output name of the module 
    
    '''
    
    
    #LUT
    lutFile = open(tableName + ".sv","w")

    #Get the length of our list
    listLength = len(inList)    
    
    #Find how many bits for selection
    inSize = 0
    for i in range(100):
        if(2**i > listLength):
            inSize = i
            break
            
    #Find how many bits for output
    max(inList)
    outSize = 0
    for i in range(100):
        if(2**i > listLength):
            outSize = i
            break  

    #Output a cutie boy to terminal
    printTotoro()

    #Output header
    lutFile.write("module %s(input logic [%d:0] in,\n\t\toutput logic [%d:0] out);\n\n" % (tableName,inSize-1,outSize-1))
    
    #Output LUT beginning
    lutFile.write("\t\talways_comb\n\t\t  begin\n\t\t\tcase(in)")
    
    #Output LUT 
    for i in range(listLength):
        lutIndex = bin(i)[2:].zfill(inSize)
        lutEntry = bin(inList[i])[2:].zfill(outSize)
        #This string is black magic
        lutFile.write("\n\t\t\t\t%d'b%s : out = 8'b%s;" % (inSize,lutIndex,lutEntry))
        
        
    #Print END Statements
    lutFile.write("\n\t\t\tendcase\n\t\t  end\n\nendmodule")
        
        
        
def list2tb(inList, tableName):
    '''
        This file takes a list and a listname and generates a testbench
        for them
    '''
    
    tbFile = open(tableName + "_tb.sv","w")



    #Get the length of our list
    listLength = len(inList)    
    
    #Find how many bits for selection
    inSize = 0
    for i in range(100):
        if(2**i > listLength):
            inSize = i
            break
            
    #Find how many bits for output
    max(inList)
    outSize = 0
    for i in range(100):
        if(2**i > listLength):
            outSize = i
            break  
            
    #Write testbench header
    tbFile.write("module %s_tb();" % (tableName))
    
    #Write input and output logic signals
    tbFile.write("\n\tlogic[%d:0] in;\n\tlogic[%d:0] out;" % (inSize-1,outSize-1))
    
    #Initalize Module
    tbFile.write("\n\n\n\t%s dut(.in(in),.out(out));" % (tableName))
    
    
    #Start writing test statements
    tbFile.write("\n\n\n\t\tinitial\n\t\t  begin")
    for i in range(listLength):
        input_bin = bin(i)[2:].zfill(inSize)
        output_bin = bin(inList[i])[2:].zfill(outSize)
        tbFile.write("\n\t\t\tin = %d'b%s;\n\t\t\t#5;" % (inSize,input_bin))
        tbFile.write('''\n\t\t\tassert(out == %d'b%s) else $error("There is an error with the table at this line");\n''' % (outSize,output_bin))
    tbFile.write("\n\t\t\t $stop;")
    tbFile.write("\n\t\t  end\nendmodule")
    

def list2do(inList,tableName):
    doFile = open(tableName + ".do","w")
    
    
    #Write some do file stuff
    doString = ('''
onbreak {resume}
# create library
if [file exists work] {
	    vdel -all
}
vlib work
# compile source files
vlog ./*.*v
vsim -voptargs=+acc %s_tb    
add wave -hex -r /%s_tb/*   
run -all 
    ''' % (tableName,tableName))
    
    doFile.write(doString)
        
        
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]
list2lut(PI,"PI")
list2tb(PI,"PI")
list2do(PI,"PI")
