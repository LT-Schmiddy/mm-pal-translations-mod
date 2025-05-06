import os, sys, json
from pathlib import Path

maximum_message = 0x354C
starting_location = 0x00B3F70C

proot = Path(__file__).parent
mm_rom_file = proot.joinpath("mm-pal.z64")

with mm_rom_file.open('rb') as mm_rom:
    mm_rom.seek(starting_location)
    
    storage_buffer = []
    
    i = 0
    while i < maximum_message:
        char = mm_rom.read(1)
        
        if char == b'\xBF':
            out_bytes = b"".join(storage_buffer)
            print(f"{hex(i)}: {out_bytes}")
            
            storage_buffer.clear()
            i += 1
        else:
            storage_buffer.append(char)
        