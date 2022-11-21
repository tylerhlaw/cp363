from Connect import Connect
from Tunnel import Tunnel
from functions import get_expertises

# Constants - connection definition files
DCRIS_FILE = "dcris.txt"
HOPPER_FILE = "hopper.txt"

conn = Connect(DCRIS_FILE)
cursor = conn.cursor

rows = get_expertises(cursor, broad=None, narrow=None)

for row in rows:
    print(row)