import sys
import pyvisa

cal_entries=['30 mV DC','300 mV DC','3 V DC','30 V DC','300 V DC','Not used','All AC Volts ranges','30 Ω 2W,4W','300 Ω 2W,4W','3 KΩ 2W,4W','30 KΩ 2W,4W','300 KΩ 2W,4W','3 MΩ 2W,4W','30 MΩ 2W,4W','300 mA DC','3 A DC','Not used','300 mA and 3 A AC','Not used']

def get_offset_const(s):
    if int(s)>900000:
        return (int(s)-1_000_000)
    else:
        return int(s)

def get_gain_const(s):
    gain_digits = [int(i,16) if int(i,16)<8 else int(i,16)-16 for i in s]
    result = 1
    for idx,digit in enumerate(gain_digits):
        #print(idx, digit, digit/(10*10**(idx+1)))
        result += digit/(10*10**(idx+1))
    return round(result,6)

def validate(calib, print_result=True):
    r = [hex(i&0x0F).split('x')[1].upper() for i in calib]
    #data = [hex(i) for i in calib]
    #r = [hex(int(i,16)&int('0x0F',16)).split('x')[1] for i in data]
    i = 1
    idx=0
    result=[]
    hdr = "byteidx|     raw     |offset|gain |chk| chksum validation |result|offset_const|gain_constant|range              "
    if print_result:print(f"\nCalibration mode is {'off' if int(r[0])==0 else 'on'}\n")
    if print_result:print("-"*len(hdr));print(hdr);print("-"*len(hdr))
    
    while (i<248):
        if print_result:print(f"{i:3d}:{i+12:3d}|{(calib[i:i+13]).decode()}|{''.join(r[i:i+6]).upper()}|{''.join(r[i+6:i+11]).upper()}|{''.join(r[i+11:i+13]).upper():3s}", end="")
        val = sum([int(i,16) for i in r[i:i+11]])
        crc = int(''.join(r[i+11:i+13]),16)
        if print_result:print(f"|{val:4d} + {crc:4d} = {val+crc:5d}|{'Pass' if (val+crc)==255 else 'Fail':6s}|{get_offset_const(''.join(r[i:i+6]).upper()):12d}|{get_gain_const(''.join(r[i+6:i+11]).upper()):13.6f}|{cal_entries[idx]}")
        result.append((val+crc)==255)
        i+=13
        idx+=1
    if print_result: print("-"*len(hdr))
    return all(result)    

def main():
    args = sys.argv[1:]
    if len(args) !=2:
        print("Usage: ")
        print("\nRead calibration data from hp3478a and write to file:")
        print(f"{sys.argv[0]} <gpib_address> <output_file_name>")
        print("\nValidate calibration data from file:")
        print(f"{sys.argv[0]} -v <calibration_data_file_name>")
        exit()

    if args[0] == '-v':
        fname = args[1]
        result = bytearray()
        try:
            with open(fname,'rb') as f:
                result = f.read()
        except:
            print(f"Failed to read file {fname}")
        validate(bytes(result))
    else:
        instr_addr = args[0]
        fname = args[1]

        rm = pyvisa.ResourceManager()
        try:
            dvm = rm.open_resource(instr_addr)
            dvm.query('F1')
        except:
            print(f"Failed to open device at {instr_addr}")
            exit()

        result = bytearray()
        for addr in range(256):
            dvm.write_raw(bytes([ord('W'), addr]))
            val = dvm.read_raw()
            result.append(ord(val))

        try:
            with open(fname,'xb') as f:
                f.write(bytes(result))
        except:
            print(f"Failed to write to file {fname}")
            

        print('\n--- cal data ---')
        for i,b in enumerate(bytes(result)):
            if i>0 and i%16==0: print()
            print(chr(b),end='')
        print('\n----------------\n')    
        validate(bytes(result))
        dvm.close()
        rm.close()
    

if __name__ == "__main__":
    main()
    

