import cocotb
from cocotb.triggers import Timer, ClockCycles
from cocotb.clock import Clock

import co_common.data

class Clock_wrapper:
    def __init__(self, cycle, time_scale, signal = None):
        self.cycle = cycle
        self.time_scale = time_scale
        
        if signal:
            self.signal = None
            # the clock cycle is defined
            self.clk_cycle = (signal,self.cycle,self.time_scale)
            # CLOCK is generated
            self._start_clock(Clock(*self.clk_cycle))
        else:
            self.signal = None

    def _start_clock(self, clock):
        cocotb.fork(clock.start())

    @cocotb.coroutine
    async def _continuous_time(self, time):
        await Timer(time, units=self.time_scale)
    
    @cocotb.coroutine
    async def continuous_ticks(self, ticks):
        await self._continuous_time(ticks * self.cycle)

    @cocotb.coroutine
    async def force_tick_signaled(self):
        await cocotb.triggers.ClockCycles(*self.clk_cycle)

    @cocotb.coroutine
    async def force_ticks_signaled(self, ticks):
        await self._continuous_time(ticks * self.cycle)
    
    @cocotb.coroutine
    async def ticks(self, ticks, signaled = False):
        if signaled and self.signal:
            await self.force_ticks_signaled(ticks)
        else:
            await self.continuous_ticks(ticks)

