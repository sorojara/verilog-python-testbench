def get_value(dut, key, radix='dec'):
    buff =  getattr(dut, key)
    return radix_value(buff, radix) if buff else 'UNDEFINED'

def radix_value(value, radix):
    radix = radix.lower()
    if radix == 'bin':
        buffer = bin(value)
    elif radix == 'dec':
        buffer = int(value)
    elif radix == 'hex':
        buffer = hex(value)
    return str(buffer)


#Update radix_value to use this decorators
decorators = {
    'bin': bin,
    'dec': int,
    'hex': hex
}