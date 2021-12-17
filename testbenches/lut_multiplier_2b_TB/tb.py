import cocotb
import random

import sys
sys.path.insert(0, '../../')
from co_common.clock import Clock_wrapper

Clock = Clock_wrapper(1,'ns')

@cocotb.test()
async def test_lut_multiplier_2b(dut):

    # the clock cycle is defined
    await Clock.ticks(1)

    # reset signal set to 1
    dut.reset = 1;

    #simulation is currently at time zero
    
    #Forcing 1 tick simulation
    await Clock.ticks(1)

    dut.reset = 0;

    # -------------------------------   O ----------------------------------------
    # FIRST SIMULATION CHECK EXAMPLE:
    dut.a = 1
    dut.b = 2

    # Timer() processes any queued events until the time specified is finished
    await Clock.ticks(3)

    # Check if the simulated values are the expected ones
    expected = 2
    print ("MUL Value: " + str(dut.mul.value))
    #assert(dut.mul == expected)

    # Print success testing
    success_assertion(dut, expected)

    # -------------------------------   O ----------------------------------------
    # SECOND SIMULATION CHECK EXAMPLE:

    dut.a = 5
    dut.b = 1
    await Clock.ticks(3)
    expected = 5
    #assert(dut.mul == expected)
    success_assertion(dut, expected)


    # -------------------------------   O ----------------------------------------
    # THIRD SIMULATION CHECK EXAMPLE:

    dut.a = 3
    dut.b = 0
    await Clock.ticks(3)
    expected = 0
    #assert(dut.mul == expected)
    success_assertion(dut, expected)

    # -------------------------------   O ----------------------------------------
    # FOURTH SIMULATION CHECK EXAMPLE:

    dut.a = 3
    dut.b = 3
    await Clock.ticks(3)
    expected = 9
    #assert(dut.mul == expected)
    success_assertion(dut, expected)


@cocotb.test()
async def test_adder_complex_input(dut):

    # initial stae
    dut.reset = 1;

    await Clock.ticks(1)

    dut.reset = 0;
    dut.a = 0
    dut.b = 0

    while int(dut.a) < 15:
        await Clock.ticks(1)
        expected = int(dut.a) * int(dut.b)
        dut._log.info(f"A: {int(dut.a)} - B: {int(dut.b)}")
        dut._log.info(f"CHECKING: {int(dut.mul)} against an expected: {expected}")
        assert(dut.mul == expected)
        success_assertion(dut, expected)
        dut.a = int(dut.a) + 1
        dut.b = random.randint(0,3)
   

def success_assertion(dut, expected):
    message = f"SUCCESS with a={int(dut.a)} and b={int(dut.b)} with a result output of {int(dut.mul)} and a expected value of {expected}"
    dut._log.info(message)
