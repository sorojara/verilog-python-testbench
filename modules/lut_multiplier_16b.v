`include "lut_multiplier_8b.v"

module lut_multiplier_16b(mul, a, b, reset);

input wire reset;
input  wire [15:0] a;
input  wire [15:0] b;
output wire [31:0] mul;

wire [7:0] a1;
wire [7:0] a2;
wire [7:0] b1;
wire [7:0] b2;

assign a1 = a[15:8];
assign a2 = a[7:0];
assign b1 = b[15:8];
assign b2 = b[7:0];

wire [15:0] mult_C1;
wire [15:0] mult_C2;
wire [15:0] mult_C3;
wire [15:0] mult_C4;

wire [31:0] buff1;
wire [31:0] buff2;
wire [31:0] buff3;
wire [31:0] buff4;

lut_multiplier_8b mult1(
    .reset(reset),
	.a(a2),
	.b(b2),
	.mul(mult_C1)
	);

lut_multiplier_8b mult2(
    .reset(reset),
	.a(a2),
	.b(b1),
	.mul(mult_C2)
	);

lut_multiplier_8b mult3(
    .reset(reset),
	.a(a1),
	.b(b2),
	.mul(mult_C3)
	);

lut_multiplier_8b mult4(
    .reset(reset),
	.a(a1),
	.b(b1),
	.mul(mult_C4)
	);

assign buff1 = mult_C1;
assign buff2 = mult_C2 << 8;
assign buff3 = mult_C3 << 8;
assign buff4 = mult_C4 << 16;

assign mul = buff1 + buff2 + buff3 + buff4;

// the "macro" to dump signals
`ifdef COCOTB_SIM
integer num_regs;
initial begin
    $dumpfile ("out/sim.vcd");
    $dumpvars (0, lut_multiplier_16b);
end
`endif

endmodule