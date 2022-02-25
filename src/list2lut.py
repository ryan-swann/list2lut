
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
        if(2**i >= listLength):
            inSize = i
            break
            
    #Find how many bits for output
    max(inList)
    outSize = 0
    for i in range(100):
        if(2**i >= listLength):
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
        lutFile.write("\n\t\t\t\t%d'b%s : out = %d'b%s;" % (inSize,lutIndex,outSize,lutEntry))
        
        
    #Print END Statements
    lutFile.write("\n\t\t\tendcase\n\t\t  end\n\nendmodule\n\n\n")
        
        
        
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

S = (
    0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05,
    0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99,
    0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62,
    0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6,
    0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8,
    0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35,
    0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87,
    0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e,
    0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1,
    0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3,
    0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f,
    0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51,
    0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8,
    0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0,
    0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84,
    0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48,
)

list2lut(S,"sm4_sbox")


