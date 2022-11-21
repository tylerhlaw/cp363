"""
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-09-30"
-------------------------------------------------------
Runs simple test code against the DCRIS database with both
direct connections and SSH tunneling.
-------------------------------------------------------
"""
# pylint: disable=broad-except

# Imports
from Connect import Connect
from Tunnel import Tunnel

# Constants - connection definition files
DCRIS_FILE = "dcris.txt"
HOPPER_FILE = "hopper.txt"


def get_test_data():
    """
    -------------------------------------------------------
    Reads data from the DCRIS 'broad' table.
    Use: get_test_data()
    -------------------------------------------------------
    """
    # Connect to the DCRIS database with an option file
    conn = Connect(DCRIS_FILE)
    # Get the connection cursor object
    cursor = conn.cursor
    # Define a SQL query
    sql = "SELECT * FROM broad"
    # Execute the query from the connection cursor
    cursor.execute(sql)
    # Print the column names from the query result
    print("Columns:")
    print(cursor.column_names)
    print()
    # Get and print the contents of the query results (raw results)
    rows = cursor.fetchall()
    print(f"Row count: {cursor.rowcount}")
    print()

    print("Data:")
    for row in rows:
        print(row)
    # Close the Connect object
    conn.close()
    return


def test_connect():
    """
    -------------------------------------------------------
    Direct database server connection.
    -------------------------------------------------------
    """
    print("Standard Connection")
    print()

    try:
        get_test_data()
    except Exception as e:
        print(str(e))


def test_connect_tunnel():
    """
    -------------------------------------------------------
    Database server connection using ssh tunneling.
    -------------------------------------------------------
    """
    print("SSH Tunnel Connection")
    print()

    try:
        tunnel = Tunnel(HOPPER_FILE)

        with tunnel.tunnel:
            get_test_data()
    except Exception as e:
        print(str(e))


# for testing
if __name__ == "__main__":
    # Test both connections
    test_connect()
    print()
    print("-" * 80)
    print()
    test_connect_tunnel()
