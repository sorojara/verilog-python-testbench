import cocotb
import random

import sys
sys.path.insert(0, '../../')
from co_common.clock import Clock_wrapper

Clock = Clock_wrapper(1,'ns')

@cocotb.test()
async def test_adder(dut):
    Clock = Clock_wrapper(1,'ns',dut.clk)

    # reset signal set to 1
    dut.reset = 1;

    #simulation is currently at time zero
    
    #Forcing 1 tick simulation
    await Clock.force_tick_signaled()

    dut.reset = 0;

    # -------------------------------   O ----------------------------------------
    # FIRST SIMULATION CHECK EXAMPLE:
    dut.a = 1
    dut.b = 2

    
    await Clock.ticks(3, True)

    # Check if the simulated values are the expected ones
    expected = 3
    assert(dut.sum == expected)

    # Print success testing
    success_assertion(dut, expected)

    # -------------------------------   O ----------------------------------------
    # SECOND SIMULATION CHECK EXAMPLE:

    dut.a = 4
    dut.b = 20
    await Clock.ticks(3, True)
    expected = 24
    assert(dut.sum == expected)
    success_assertion(dut, expected)


    # -------------------------------   O ----------------------------------------
    # THIRD SIMULATION CHECK EXAMPLE:

    dut.a = 6
    dut.b = 9
    await Clock.ticks(3, True)
    expected = 15
    assert(dut.sum == expected)
    success_assertion(dut, expected)

@cocotb.test()
async def test_adder_complex_input(dut):

    Clock = Clock_wrapper(1,'ns',dut.clk)

    # initial stae
    dut.reset = 1;

    await Clock.force_tick_signaled()

    dut.reset = 0;
    dut.a = 0
    dut.b = 0

    while int(dut.a) <= 25:
        await Clock.ticks(1, True)
        expected = int(dut.a) + int(dut.b)
        assert(dut.sum == expected)
        success_assertion(dut, expected)
        dut.a = int(dut.a) + 1
        dut.b = random.randint(0,25)
        



def success_assertion(dut, expected):
    message = f"SUCCESS with a={int(dut.a)} and b={int(dut.b)} with a result output of {int(dut.sum)} and a expected value of {expected}"
    dut._log.info(message)
