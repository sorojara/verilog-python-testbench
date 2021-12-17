`include "lut_multiplier_2b.v"

module lut_multiplier_4b(mul, a, b, reset);

input wire reset;
input  wire [3:0] a;
input  wire [3:0] b;
output wire [7:0] mul;

wire [1:0] b1;
wire [1:0] b2;

wire [7:0] mult_C1;
wire [7:0] mult_C2;
wire [7:0] buff_C2;

lut_multiplier_2b mult1(
    .reset(reset),
	.a(a),
	.b(b[1:0]),
	.mul(mult_C1)
	);

lut_multiplier_2b mult2(
    .reset(reset),
	.a(a),
	.b(b[3:2]),
	.mul(mult_C2)
	);

assign buff_C2 = mult_C2 << 2;
assign mul = buff_C2 + mult_C1;


// the "macro" to dump signals
`ifdef COCOTB_SIM
integer num_regs;
initial begin
    $dumpfile ("out/sim.vcd");
    $dumpvars (0, lut_multiplier_4b);
end
`endif

endmodule