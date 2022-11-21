from Connect import Connect
from Tunnel import Tunnel
from functions import get_member_broad

# Constants - connection definition files
DCRIS_FILE = "dcris.txt"
HOPPER_FILE = "hopper.txt"

conn = Connect(DCRIS_FILE)
cursor = conn.cursor

rows = get_member_broad(cursor, memberId=None, broadId=None)

for row in rows:
    print(row)
