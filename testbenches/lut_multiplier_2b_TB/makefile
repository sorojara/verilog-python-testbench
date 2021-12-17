SOURCE_DIRECTORY = ../../modules
TESTING_MODULE = lut_multiplier_2b.v
VERILOG_SOURCES = $(SOURCE_DIRECTORY)/$(TESTING_MODULE)  
SIM=icarus
TOPLEVEL_LANG=verilog
COCOTB_REDUCED_LOG_FMT=1
SIM_BUILD = out
COMPILE_ARGS = -D COCOTB_SIM=1 -I"$(SOURCE_DIRECTORY)" 
CURRENT = $(shell pwd)
COCOTB_LOG_LEVEL = ERROR
PLUSARGS = -vcd-none

# TOPLEVEL is the name of the toplevel module in your Verilog file:
TOPLEVEL=lut_multiplier_2b

# MODULE is the name of the Python test file:
MODULE=tb

# Current makefile was based on COCOTB Makefiles

#--------------------------------------- O -------------------------------------------
# NOTE: keep this at 80 chars.
define help_targets =
Targets
=======
sim                   Unconditionally re-run the simulator (default)
gtk                   Visualize the result waveforms as a preconfig GTKwave                              
gtk-simple            Visualize the result waveforms as a non config GTKwave
clean-results         Delete results file
help                  This help text

endef

# NOTE: keep this at 80 chars.
define help_makevars =
Variables
=========

The following variables are makefile variables:

Makefile-based Test Scripts
---------------------------
GUI                       Set this to 1 to enable the GUI mode in the simulator
SIM                       Selects which simulator Makefile to use
WAVES                     Enable wave traces dump for Riviera-PRO and Questa
VERILOG_SOURCES           A list of the Verilog source files to include
COMPILE_ARGS              Arguments to pass to compile stage of simulation
SIM_ARGS                  Arguments to pass to execution of compiled simulation
EXTRA_ARGS                Arguments for compile and execute phases
PLUSARGS                  Plusargs to pass to the simulator
COCOTB_HDL_TIMEUNIT       Default time unit for simulation
COCOTB_HDL_TIMEPRECISION  Default time precision for simulation
CUSTOM_COMPILE_DEPS       Add additional dependencies to the compilation target
CUSTOM_SIM_DEPS           Add additional dependencies to the simulation target
SIM_BUILD                 Define a scratch directory for use by the simulator
SCRIPT_FILE               Simulator script to run (for e.g. wave traces)

endef

define newline


endef

ifeq ($(MAKECMDGOALS),help)
    $(info $(help_targets))
    $(info $(help_makevars))
    help_envvars := $(subst %,${newline},$(shell cocotb-config --help-vars | tr \\n %))
    $(info ${help_envvars})
    $(error "Stopping after printing help")
endif

SIM_LOWERCASE := $(shell echo $(SIM) | tr A-Z a-z)

COCOTB_MAKEFILES_DIR := $(realpath $(shell cocotb-config --makefiles))

include $(COCOTB_MAKEFILES_DIR)/Makefile.deprecations

HAVE_SIMULATOR = $(shell if [ -f $(COCOTB_MAKEFILES_DIR)/simulators/Makefile.$(SIM_LOWERCASE) ]; then echo 1; else echo 0; fi;)
AVAILABLE_SIMULATORS = $(patsubst .%,%,$(suffix $(wildcard $(COCOTB_MAKEFILES_DIR)/simulators/Makefile.*)))

ifeq ($(HAVE_SIMULATOR),0)
    $(error "Couldn't find makefile for simulator: "$(SIM_LOWERCASE)"! Available simulators: $(AVAILABLE_SIMULATORS)")
endif

include $(COCOTB_MAKEFILES_DIR)/simulators/Makefile.$(SIM_LOWERCASE)

all: 
	make sim

gtk:
	gtkwave out/sim.vcd -S config/sim.tcl

gtk-simple:
	gtkwave out/sim.vcd

make clean-results:
	rm $(COCOTB_RESULTS_FILE)