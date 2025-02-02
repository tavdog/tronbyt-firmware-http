# Read the binary WebP file
input_file = "/Users/tavis/code/tronbyt-firmware-http/lib/assets/xscreensaver.webp"
output_file = "output.h"

with open(input_file, "rb") as f:
    binary_data = f.read()

# Create C header file content
header_name = "ASSET_NOAPPS_WEBP"
line_length = 16  # Number of bytes per line in the array
hex_lines = []

# Convert binary data to hex-encoded string lines
for i in range(0, len(binary_data), line_length):
    line = "".join(f"\\x{byte:02X}" for byte in binary_data[i:i + line_length])
    hex_lines.append(f'    "{line}"')

# Join lines and format the C code
c_code = f"""// Generated by 'tbt dev firmware-asset', don't edit manually!
#include <stddef.h>
#include <stdint.h>
const size_t {header_name}_LEN = {len(binary_data)};
const uint8_t {header_name}[] =
{',\n'.join(hex_lines)};
"""

# Write to an output file
with open(output_file, "w") as f:
    f.write(c_code)

print(f"C header file saved to {output_file}")