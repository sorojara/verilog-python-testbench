`include "lut_multiplier_16b.v"

module lut_multiplier_32b(mul, a, b, reset);

input wire reset;
input  wire [31:0] a;
input  wire [31:0] b;
output wire [63:0] mul;

wire [15:0] a1;
wire [15:0] a2;
wire [15:0] b1;
wire [15:0] b2;

assign a1 = a[31:16];
assign a2 = a[15:0];
assign b1 = b[31:16];
assign b2 = b[15:0];

wire [31:0] mult_C1;
wire [31:0] mult_C2;
wire [31:0] mult_C3;
wire [31:0] mult_C4;

wire [63:0] buff1;
wire [63:0] buff2;
wire [63:0] buff3;
wire [63:0] buff4;

lut_multiplier_16b mult1(
    .reset(reset),
	.a(a2),
	.b(b2),
	.mul(mult_C1)
	);

lut_multiplier_16b mult2(
    .reset(reset),
	.a(a2),
	.b(b1),
	.mul(mult_C2)
	);

lut_multiplier_16b mult3(
    .reset(reset),
	.a(a1),
	.b(b2),
	.mul(mult_C3)
	);

lut_multiplier_16b mult4(
    .reset(reset),
	.a(a1),
	.b(b1),
	.mul(mult_C4)
	);

assign buff1 = mult_C1;
assign buff2 = mult_C2 << 16;
assign buff3 = mult_C3 << 16;
assign buff4 = mult_C4 << 32;

assign mul = buff1 + buff2 + buff3 + buff4;

// the "macro" to dump signals
`ifdef COCOTB_SIM
integer num_regs;
initial begin
    $dumpfile ("out/sim.vcd");
    $dumpvars (0, lut_multiplier_32b);
end
`endif

endmodule