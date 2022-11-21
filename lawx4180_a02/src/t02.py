# Imports
from Connect import Connect
from Tunnel import Tunnel
from functions import get_publication_counts

# Constants - connection definition files
DCRIS_FILE = "dcris.txt"
HOPPER_FILE = "hopper.txt"

conn = Connect(DCRIS_FILE)
cursor = conn.cursor

rows = get_publication_counts(cursor, memberId=33, pubType='b')

for row in rows:
    print(row)
