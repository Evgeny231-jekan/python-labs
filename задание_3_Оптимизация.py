def ip_to_int(ip):
    parts = ip.split('.')
    return (int(parts[0]) << 24) | (int(parts[1]) << 16) | (int(parts[2]) << 8) | int(parts[3])

def int_to_ip(num):
    return f"{(num >> 24) & 255}.{(num >> 16) & 255}.{(num >> 8) & 255}.{num & 255}"

def parse_subnet(subnet):
    if '/' in subnet:
        ip_part, mask = subnet.split('/')
        mask = int(mask)
        ip_int = ip_to_int(ip_part)
        mask_bits = (0xFFFFFFFF << (32 - mask)) & 0xFFFFFFFF
        start = ip_int & mask_bits
        end = start | ((1 << (32 - mask)) - 1)
        return start, end
    else:
        ip_int = ip_to_int(subnet)
        return ip_int, ip_int

def has_conflict(black_list, white_list):
    for b_start, b_end in black_list:
        for w_start, w_end in white_list:
            if max(b_start, w_start) <= min(b_end, w_end):
                return True
    return False

def merge_ranges(ranges):
    ranges.sort()
    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

def range_to_subnets(start, end):
    subnets = []
    current = start
    while current <= end:
        if current == end:
            subnets.append(int_to_ip(current))
            break
        
        size = end - current + 1
        max_power = 1
        while max_power * 2 <= size:
            max_power = max_power * 2
        
        mask = 32
        temp = max_power
        while temp > 1:
            temp = temp // 2
            mask = mask - 1
        
        if current & (max_power - 1) == 0:
            subnets.append(f"{int_to_ip(current)}/{mask}")
            current = current + max_power
        else:
            subnets.append(int_to_ip(current))
            current = current + 1
    
    return subnets

def solve_berkomnadzor(black_subnets, white_subnets):
    black_ranges = []
    for subnet in black_subnets:
        s, e = parse_subnet(subnet)
        black_ranges.append((s, e))
    
    white_ranges = []
    for subnet in white_subnets:
        s, e = parse_subnet(subnet)
        white_ranges.append((s, e))
    
    if has_conflict(black_ranges, white_ranges):
        return None
    
    merged_black = merge_ranges(black_ranges)
    
    result = []
    for start, end in merged_black:
        subnets = range_to_subnets(start, end)
        result.extend(subnets)
    
    return result

black1 = ["149.154.167.99"]
white1 = ["149.154.167.100/30", "149.154.167.128/25"]

result1 = solve_berkomnadzor(black1, white1)
if result1 is None:
    print("-1")
else:
    print(len(result1))
    for s in result1:
        print(s)

print()

black2 = ["127.0.0.4/31", "127.0.0.6/31"]
white2 = ["127.0.0.0/30"]

result2 = solve_berkomnadzor(black2, white2)
if result2 is None:
    print("-1")
else:
    print(len(result2))
    for s in result2:
        print(s)

print()

black3 = ["127.0.0.1"]
white3 = ["127.0.0.1/32"]

result3 = solve_berkomnadzor(black3, white3)
if result3 is None:
    print("-1")
else:
    print(len(result3))
    for s in result3:
        print(s)
