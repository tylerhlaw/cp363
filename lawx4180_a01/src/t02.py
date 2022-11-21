# Imports
from Connect import Connect
from Tunnel import Tunnel
from functions import get_publications

# Constants - connection definition files
DCRIS_FILE = "dcris.txt"
HOPPER_FILE = "hopper.txt"

conn = Connect(DCRIS_FILE)
cursor = conn.cursor

rows = get_publications(cursor, memberId=33, pubPubType='b')

for row in rows:
    print(row)
