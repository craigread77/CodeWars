def ips_between(start, end):
    start_addresses = [int(bit) for bit in start.split('.')]
    end_addresses = [int(bit) for bit in end.split('.')]

    bit_values = [16777216, 65536, 256, 1]

    start_total = sum([start_addresses[i] * bit_values[i] for i in range(4)])
    end_total = sum([end_addresses[i] * bit_values[i] for i in range(4)])


    return end_total - start_total

    
   



ips_between('10.0.0.0', '10.0.0.50')