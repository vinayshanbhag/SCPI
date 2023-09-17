import sys
import pyvisa

def main():
    args = sys.argv[1:]
    if len(args) !=2:
        print(f"Usage: {sys.argv[0]} <gpib_address> <output_file_name>")
        exit()
    instr_addr = sys.argv[1]
    fname = sys.argv[2]

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
    print('\n----------------')    
    dvm.close()
    rm.close()
    

if __name__ == "__main__":
    main()
    

