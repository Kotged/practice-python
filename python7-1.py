format_tuple = (1736, 3.1415, 'pi', 1748, 'Mechanica')
format_string="Euler first used {2} = {1} in his {0} work {4}, and continued in his widely-read {3} work Introductio in analysin infinitorum. In hexadecimal system, {2} is {5}"
print(format_string.format(format_tuple[0], round(format_tuple[1],2), format_tuple[2], format_tuple[3], format_tuple[4], round(format_tuple[1],2).hex()))