# -------------------------------------
# File: functions.py
# Project: assignment 1 for cp363
# Description: This function holds all the functions needed for assignment 1
# -------------------------------------
# Author:  Tyler Law
# ID:      200694180
# Email:   lawx4180@mylaurier.ca
# Version (date): 17.10.22
# -------------------------------------

def get_broad(cursor, broadId=None):
    """
    -------------------------------------------------------
    Queries the broad table.
    Use: rows = get_broad(cursor)
    Use: rows = get_broad(cursor, broadId=v)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broadId - a broad ID (int)
    Returns:
        rows - (list of broad table data)
            if broadId is not None:
                rows matching broadId
            else:
                the entire broad table
            Sorted by broad description
    -------------------------------------------------------
    """

    rows = []
    query = "SELECT * FROM broad"
    
    if (broadId != None):
        query += " WHERE broadId = %s"
        
    data = []
    if(broadId != None):
        data.append(broadId)
        
    cursor.execute(query, data)
    rows = cursor.fetchall()
    
    return rows


def get_publications(cursor, memberId=None, pubPubType=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = get_publications(cursor)
    Use: rows = get_publications(cursor, memberId=v1)
    Use: rows = get_publications(cursor, pubPubType=v2)
    Use: rows = get_publications(cursor, memberId=v1, pubPubType=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
        pubPubType - a publication type (str)
    Returns:
        rows - (list of pub table data)
            if memberId and/or pubPubType are not None:
                rows matching memberId and/or pubPubType
            else:
                the entire pub table
            Sorted by publication title
    -------------------------------------------------------
    """

    rows = []
    query = "SELECT * FROM pub"

    #Adding where clause if necessary
    if (memberId != None or pubPubType != None):
        query += " WHERE"
        if (memberId != None):
            query += " pubMemberId = %s"  
        if(memberId != None and pubPubType != None):
            query += " and"
        if (pubPubType != None):
            query += " pubPubType = %s"
    
    data = []    
    if (memberId != None):
        data.append(memberId)
    if (pubPubType != None):
        data.append(pubPubType)
            
    cursor.execute(query, data)
    rows = cursor.fetchall()
    
    return rows

def get_member_broad(cursor, memberId=None, broadId=None):
    """
    -------------------------------------------------------
    Queries the vMemberBroad view.
    Use: rows = get_member_broad(cursor)
    Use: rows = get_member_broad(cursor, memberId=v1)
    Use: rows = get_member_broad(cursor, broadId=v2)
    Use: rows = get_member_broad(cursor, memberId=v1, broadId=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
        broadId - a broad ID number (int)
    Returns:
        rows - (list of vMemberBroad view data)
            if memberId and/or broadId are not None:
                rows matching memberId and/or broadId
            else:
                the entire vMemberBroad view
            Sorted by member last name, first name, and broad description
    -------------------------------------------------------
    """
    
    rows = []
    query = "SELECT * FROM vMemberBroad"
    
    if (memberId != None or broadId != None):
        query += " WHERE"
        if (memberId != None):
            query += " memberId = %s"
        if (memberId != None and broadId != None):
            query += " AND"
        if (broadId != None):
            query += " broadId = %s"
            
    query += " ORDER by memberSurname, memberForename, broadDesc"
            
    data = []
    if (memberId != None):
        data.append(memberId)
    if (broadId != None):
        data.append(broadId)
        
    cursor.execute(query, data)
    rows = cursor.fetchall()
    
    return rows

def get_expertises(cursor, broad=None, narrow=None):
    """
    -------------------------------------------------------
    Queries the vBroadNarrow view.
    Use: rows = get_expertises(cursor)
    Use: rows = get_expertises(cursor, broad=v1)
    Use: rows = get_expertises(cursor, narrow=v2)
    Use: rows = get_expertises(cursor, broad=v1, narrow=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broad - a partial broad expertise description (str)
        narrow - a partial narrow expertise description (str)
    Returns:
        rows - (list of vBroadNarrow view data)
            if broad and/or narrow are not None:
                rows containing broad and/or narrow
            else:
                the entire vBroadNarrow view
            Sorted by broad description, narrow broad description
    -------------------------------------------------------
    """
    
    rows = []
    query = "SELECT * FROM vBroadNarrow"
    
    if (broad != None or narrow != None):
        query += " WHERE"
        if (broad != None):
            query += " broadDesc LIKE %s"
        if (broad != None and narrow != None):
            query += " AND"
        if (narrow != None):
            query += " narrowDesc LIKE %s"
            
    query += " ORDER BY broadDesc, narrowDesc"
    
    data = []
    if (broad != None):
        data.append(broad)
    if (narrow != None):
        data.append(narrow)
        
    cursor.execute(query, data)
    rows = cursor.fetchall();
    
    return rows