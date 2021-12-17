#!/usr/bin/tclsh
### --------------------------------------------------------------------
### counter.tcl: Assign signals on init to gtkwave
### Author: Ricardo Soro
### --------------------------------------------------------------------


set all_facs [list]
gtkwave::addSignalsFromList "adder.clk"
gtkwave::highlightSignalsFromList "adder.clk"
gtkwave::/Edit/Color_Format/Indigo

gtkwave::addSignalsFromList "adder.reset"
gtkwave::highlightSignalsFromList "adder.reset"
gtkwave::/Edit/Color_Format/Blue

gtkwave::addSignalsFromList "adder.a"
gtkwave::highlightSignalsFromList "adder.a"
gtkwave::/Edit/Color_Format/Green
gtkwave::/Edit/Data_Format/Decimal

gtkwave::addSignalsFromList "adder.b"
gtkwave::highlightSignalsFromList "adder.b"
gtkwave::/Edit/Color_Format/Green
gtkwave::/Edit/Data_Format/Decimal

gtkwave::addSignalsFromList "adder.sum"
gtkwave::highlightSignalsFromList "adder.sum"
gtkwave::/Edit/Color_Format/Red
gtkwave::/Edit/Data_Format/Decimal


# zoom full
gtkwave::/Time/Zoom/Zoom_Full

# Print

#gtkwave::/File/Print_To_File PDF {Letter (8.5" x 11")} Full output/conductual.pdf
