
onbreak {resume}
# create library
if [file exists work] {
	    vdel -all
}
vlib work
# compile source files
vlog ./*.*v
vsim -voptargs=+acc PI_tb    
add wave -hex -r /PI_tb/*   
run -all 
    