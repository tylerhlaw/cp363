# Imports
from Connect import Connect
from Tunnel import Tunnel
from functions import get_broad

# Constants - connection definition files
DCRIS_FILE = "dcris.txt"
HOPPER_FILE = "hopper.txt"

conn = Connect(DCRIS_FILE)
cursor = conn.cursor

rows = get_broad(cursor)

for row in rows:
    print(row)
