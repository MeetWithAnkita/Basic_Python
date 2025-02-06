name = "ankita das roy".title().split()
short_name = '.'.join([n[0].upper() for n in name[:-1]]) + '.' + name[-1]
print(short_name)  # Output: A.D.Roy

short_name = '.'.join([n[0].upper() for n in name[::]]) 
print(short_name)  # Output: A.D.R

short_name = ''.join([n[0].upper() for n in name[::]]) 
print(short_name)  # Output: ADR