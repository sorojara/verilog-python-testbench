module lut_multiplier_2b(mul, a, b, reset);

input wire  reset;
input  wire [3:0] a;
input  wire [1:0] b;
output wire [7:0] mul;

wire [7:0] duplicate;// = 8'h00;
wire [7:0] triplicate;// = 8'h00;

assign duplicate = a << 1;
assign triplicate = duplicate + a;

assign mul = reset ? 0 : (b[1] ? (b[0] ? triplicate : duplicate) : (b[0] ? a : 8'h00));


// the "macro" to dump signals
`ifdef COCOTB_SIM
integer num_regs;
initial begin
    $dumpfile ("out/sim.vcd");
    $dumpvars (0, lut_multiplier_2b);
end
`endif

endmodule