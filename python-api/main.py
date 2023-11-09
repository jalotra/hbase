# Does what ? 
"""
Simple CRUD ops on top of APACHE HBASE, uses thrift to talk to HBASE.
"""
import happybase
from pprint import pprint

if __name__ == "__main__":
    connection = happybase.Connection('localhost', 9090, autoconnect=True)

    # create table ? 
    connection.create_table("jalotra_test", families={
        "family_1" : dict(max_versions=2),
        "family_2" : dict(max_versions = 5)
    })

    pprint(connection.tables())