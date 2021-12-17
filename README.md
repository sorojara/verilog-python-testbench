# Verilog Python TestBench  

This project is an approach to python testbench genration to simplify the Verilog testing while keeping a big test case flexibility by defining the Test Plan in Python with the posibility of reading Verilog signals during any step of the simulations and use them as input for other signals offering the capability of defining responsive testing while asserting the results in a similar way to the one used in PyTest to replicate the ScoreBoard. The testing nature of this project opens the possibility to simplify the inclusion of software development techniques like Continous Integration into Verilog devlopment to adjust it to the rising DevOps techniques.

*TLDR:*
**Define Complex Verilog Tests in a Simple Way.**

## Overview
This repository offers a base project for testing individual Verilog modules which can be used as some kind of template for developing your own verilog module testing environment.

### Technology Stack
This project is mainly based on Python 3; which use COCOTB as the testing framework and Verilog (Icarus-Verilog) as the Verilog Compiler. Finally as an extra feature, GTKwave is the selected Signal Viewer because of its flexible configuration with TCL Scripts.

This testing environment is mainly tested and developed in a Debian-Based Linux environment and it is the recommended SO to use this project. Other platforms are not tested yet and are labeled as unsupported.  

## Installation
Once you make sure you have installed Python3 at least in 3.5

`sudo apt install python3`

Then you should make sure of install Make

`sudo apt install make`

You must proceed with the Icarus Verilog Installation


`sudo apt install iverilog`

After that you should install GTKwave

`sudo apt-get install -y gtkwave`

Then you must create your Virtual Environment, while this is not fully needed to execute this project, it is strongly recommended to use Virtualenv. To do this please cd into the projects root

```bash
# Install Virtualenv
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv

# Create
python3 -m venv env

#Activate the Virtual Environment (recurrent step)
source env/bin/activate

#Install required packages
pip install -r requirements.txt
```

Then you must make sure that your Icarus Verilog installation supports the Verilog 2012 Standard, to do this you must do the following command:

` iverilog -g --help`

which should return the available supported generation which should look something like this:


```
Supported generations are:

1995 -- IEEE1364-1995
2001 -- IEEE1364-2001
2005 -- IEEE1364-2005
2012 -- IEEE 1800-2012


Other generation flags:

specify | no-specify  
verilog-ams | no-verilog-ams
std-include | no-std-include
relative-include | no-relative-include
xtypes | no-xtypes
icarus-misc | no-icarus-misc
io-range-error | no-io-range-error
strict-ca-eval | no-strict-ca-eval

system-verilog  
```

From which you must make sure to at least have available the is


`2012 -- IEEE 1800-2012`

If thats the case you should skip the next step, Otherwise you must modify COCOTB makefiles to use your must recent Verilog Version, to do that you must execute the following command:

*** ----ONLY DO IF YOU DONT HAVE INSTALLED 2012 VERILOG STANDARD---- ***
`nano +59 $(cocotb-config --makefiles)$(echo /simulators/Makefile.icarus)`

And look for the line that looks like:

`COMPILE_ARGS += -f $(SIM_BUILD)/cmds.f -g2012 # Default to latest SystemVerilog standard`

And change it for:

`COMPILE_ARGS += -f $(SIM_BUILD)/cmds.f -g2005 # Manually downgraded for Iverilog integration purposes`

And proceed to save it by pressing the keys:
*Ctrl+X \-> Y \-> Enter *
*** ------------------------------End of conditional step------------------------------***

And finally your installation is complete.


**REMEMBER:** Always make sure that your virtualenv is active by running the command `source env/bin/activate` before executing a project or starting to develop.

*To be sure that your virtualenv is topic, make sure that theres a `(env)` behind your username in the terminal. ie: `(env) user@my-pc:`*

### Container-Based Alternative
In case of having problems installing the previous requirements, there is a makefile in the root of the project to use a Docker Image developed for this project which can be used to compile and run tests, (visualization in GTKwave is excluded and must be runned outside the container).

To use this solution it is needed to instal docker following the next steps:

```bash
sudo apt-get update

sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
gnupg \
lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo docker run hello-world #test if everything installed well
```

once everything is correctly installed you can run make in the project root and navigate to your prefered testbench; where you can execute it using the steps in the next section.

## Execution
Since the Makefile includes two main under support recipes the two commands available are:

### - make
This is the main command and this will execute the test plans defined in tb.py

### - make GTK
This must be executed after doing a `make` and it will open GTKwave with the specified signals

### - make GTK-simple
This is similar to `make gtk` but do not preload any configuration

### - make clean-results
Delete the results.xml file

## TCL file
Inside each testbench directory there is a config folder which contains a TCL file which is used to specify which signals and how should they be shown in GTKwave. To specify the way a signal will be shown, you should add the following information for each signal to be shown:

```markdown
gtkwave::addSignalsFromList "adder.sum"

gtkwave::highlightSignalsFromList "adder.sum"

gtkwave::/Edit/Color_Format/Red

gtkwave::/Edit/Data_Format/Decimal
```
Where the first two lines tell GTKwave to select and highlight the signal. To Specify the signal to be added it should be referenced by {module}.{signal} and submodules can be referenced just by using a dot in the same way ({module}.{submodule}.{signal}). The other two lines are to specify the color and the radix (data type) used to show the signal in the viewer. You can create these files for each testbench so every time you execute make GTK you dont have to pick your desired signals or color code them.


## Verilog Modules
All the testable verilog modules are stored in the modules directory; this modules must be compilable in a Verilog compiler (ideally Icarus Verilog) and synthesisable. This modules might include other modules which must be stored in this folder too.

## Testbench Folder
This project store every testbench in its own folder inside the testbenches folder. Every single testbench folder has the same internal structure which is displayed below.


├── \_\_init__.py # Python package Marker
├── makefile # Makefile based on [Cocotb](https://github.com/cocotb/cocotb) ones
├── config # Configuration Folder
│ └── sim.tcl # TCL file for GTKwave
├── out # output files
│ ├── cmds.f # command file autogenerated
│ └── sim.vvp # simulation vvp file
└── tb.py # simulation file (testbench and scoreboard)

  

While most of this files and structure has already been covered in this file, the tb.py file is one of the most import ones because this is where all the tests are defined; this file serves the purpose of a testbench and a scoreboard at the same time. The structure of the file is similar to a test file (pytest) but instead of using pytest decorators, you must use cocotb decorators. A simple example of how a test should look is shown below but the design and flow of the test can be as complex as the developer wants to. Another important part of the example is the use of the Clock_wrapper object which is going to be discussed in the next section dedicated to the co_common library.
  

``` python

@cocotb.test() #cocotb test decorator
async  def  test_adder(dut): #must be an async function
	Clock = Clock_wrapper(1,'ns',dut.clk)

	# reset signal set to 1 (setting an input value)
	dut.reset = 1;
	
	#simulation is currently at time zero
	#Forcing 1 tick simulation
	await Clock.force_tick_signaled()
	
	dut.reset = 0;

	# FIRST SIMULATION CHECK EXAMPLE:
	dut.a = 1
	dut.b = 2
	await Clock.ticks(3, True)
	
	# Check if the simulated values are the expected ones

	expected = 3
	assert(dut.sum == expected)
```

## Co_common library

The co_common library is a set of testing tools developed for simplifing the test technical part letting the developer focus on the testing flow. The library includes modules that cover the testing process; the modules are described below.

### clock module
The clock module is a class that offers a set of different ticking clock generators.

### data module
The data module is focused on the interaction with the signals in the module; it includes methods for accessing the data in those signals. 

### message module
The message module is focused on the generation of human readable messages that describe the state of the testing process.