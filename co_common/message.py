from cocotb.handle import ModifiableObject

import co_common.data as data

radix_values = ['bin', 'dec', 'hex']


def print_state(dut, radix='dec'):
    if radix in radix_values:
        subhandles = dut._sub_handles
        name = dut._name
        for key in subhandles:
            if type(subhandles[key]) == ModifiableObject:
                print(f"{key}: {radix_value(subhandles[key].value, radix)}")
                print('--------------------')
    else:
        print('Please select a valid Radix value (\'bin\', \'dec\' or \'hex\')')

def print_result(dut, input_list, output_list, radix='dec'):
    input_tag = 'Input: ' if len(input_list) < 2 else 'Inputs: ' 
    ret = f'{input_tag}: {_print_from_list(dut, input_list, radix)}\n'
    output_tag = 'Output: ' if len(output_list) < 2 else 'Outputs: ' 
    ret += f'{output_tag}: {_print_from_list(dut, output_list, radix)}'
    return ret

def print_single_compare(dut, expected_value, signal_name, radix='dec'):
    return f"CHECKING {signal_name} = {data.get_value(signal_name,radix)} against an expected: {expected_value}"

def print_batch_compare(dut, expected_values, signal_list, radix='dec'):
    ret = ''
    if len(signal_list) == len(expected_values):
        for i in signal_list:
            ret += f"CHECKING {i} = {data.get_value(dut,i,radix)} against an expected: {expected_values.get(i, 'UNDEFINED')}\n"
        else:
            key = signal_list[-1]
            val = data.get_value(dut,key,radix)
            if val:
                ret += f"CHECKING {key} = {data.get_value(dut,key,radix)} against an expected: {expected_values.get(key, 'UNDEFINED')}"
    return ret
    

def _print_from_list(dut, signal_list, radix):
    subhandles = dut._sub_handles 
    ret = ''
    if signal_list:
        for i in signal_list:
            val = subhandles.get(i)
            if val:
                ret += f'{i} = {radix_value(val,radix)}, '
        else:
            key = signal_list[-1]
            val = subhandles.get(key)
            if val:
                ret += f'{key} = {radix_value(val,radix)}. '
    return ret



def radix_value(value, radix):
    if radix == 'bin':
        buffer = bin(value)
    elif radix == 'dec':
        buffer = int(value)
    elif radix == 'hex':
        buffer = hex(value)
    return str(buffer)