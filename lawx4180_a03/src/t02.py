# Imports
from Connect import Connect
from Tunnel import Tunnel
from functions import get_expertise_counts

# Constants - connection definition files
DCRIS_FILE = "dcris.txt"
HOPPER_FILE = "hopper.txt"

conn = Connect(DCRIS_FILE)
cursor = conn.cursor

rows = get_expertise_counts(cursor, memberId=69)

for row in rows:
    print(row)
