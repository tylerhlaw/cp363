# -------------------------------------
# File: functions.py
# Project: assignment 1 for cp363
# Description: This function holds all the functions needed for assignment 2
# -------------------------------------
# Author:  Tyler Law
# ID:      200694180
# Email:   lawx4180@mylaurier.ca
# Version (date): 24.10.22
# -------------------------------------

def get_member_publications(cursor, pubTitle=None, pubType=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = get_member_publications(cursor)
    Use: rows = get_member_publications(cursor, pubTitle=v1)
    Use: rows = get_member_publications(cursor, pubType=v2)
    Use: rows = get_member_publications(cursor, pubTitle=v1, pubType=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        pubTitle - a partial pubTitle (str)
        pubType - a single letter publication type (str)
    Returns:
        rows - (list of member's last name, member's first
            name, the title of a publication, and the full publication
            type (i.e. 'article' rather than 'a') data)
            if pubTitle and/or pubType are not None:
                rows containing pubTitle and/or pubType
            else:
                all member and publication rows
            Sorted by last name, first name, publication title
    -------------------------------------------------------
    """
    
    #Creating original query and variables
    sql = """SELECT member.memberSurname, member.memberForename, pub.pubTitle, pubType.pubTypeDesc
    FROM pub
    JOIN member ON member.memberId=pub.pubMemberId
    JOIN pubType ON pub.pubPubType=pubType.pubType"""
    rows = []
    data = []
    
    #Adding conditions to SQL Query
    if (pubTitle != None):
        sql += " WHERE pub.pubTitle LIKE %s"
        data.append("%" + pubTitle + "%")
        if (pubType != None):
            sql += " AND pub.pubPubType = %s"
            data.append(pubType)
    elif (pubType != None):
        sql += " WHERE pub.pubPubType = %s"
        data.append(pubType)
              
    sql += " ORDER BY member.memberSurname, member.memberForename, member.memberTitle"
        
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    
    return rows        
   
def get_publication_counts(cursor, memberId=None, pubType=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = get_publication_counts(cursor)
    Use: rows = get_publication_counts(cursor, memberId=v1)
    Use: rows = get_publication_counts(cursor, pubType=v2)
    Use: rows = get_publication_counts(cursor, memberId=v1, pubType=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
        pubType - a publication type (str)
    Returns:
        rows - (list of member's last name, member's first
            name, and the number of publications of type
            pubType data)
            if memberId or pubType is not None:
                rows containing memberId and/or pubType
            else:
                all member names and publication counts
            Sorted by last name, first name
    -------------------------------------------------------
    """
    
    sql = """
    SELECT member.memberSurname, member.memberForename, COUNT(pub.pubPubType)
    FROM pub
    INNER JOIN member ON pub.pubMemberId = member.memberId
    """
    rows = []
    params = []

    if(memberId is not None):
        sql += " WHERE member.memberId = %s"
        params.append(memberId)
        if(pubType is not None):
            sql += " AND pub.pubPubType = %s"
            params.append(pubType)

    elif(pubType is not None):
        sql += " WHERE pub.pubPubType = %s"
        params.append(pubType)

    sql += """ 
    GROUP BY pub.pubMemberId
    ORDER BY member.memberSurname, member.memberForename;
    """

    cursor.execute(sql, params)
    rows = cursor.fetchall()
     
    return rows

def get_broad_counts(cursor, memberId=None):
    """
    -------------------------------------------------------
    Queries the member and broad tables.
    Use: rows = get_broad_counts(cursor)
    Use: rows = get_broad_counts(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
    Returns:
        rows - (list of member's last name, member's first
            name, and the number of broad expertises they hold data)
            if memberId is not None:
                rows containing memberId
            else:
                all member and broad expertise rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    
    sql = """
        SELECT member.memberSurname, member.memberForename, COUNT(broad.broadDesc)
        FROM member
        INNER JOIN memberBroad ON memberBroad.memberBroadMemberId = member.memberId
        INNER JOIN broad ON memberBroad.memberBroadBroadId = broad.broadId"""
    data = []
    rows = []
    
    if (memberId != None):
        sql += " WHERE member.memberId = %s"
        data.append(memberId)
        
    sql += """ GROUP BY member.memberSurname, member.memberForename
        ORDER BY member.memberSurname, member.memberForename"""
    
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    
    return rows

def get_all_expertises(cursor, memberId=None):
    """
    -------------------------------------------------------
    Queries the member, broad, and narrow tables
    Use: rows = get_all_expertises(cursor)
    Use: rows = get_all_expertises(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
    Returns:
        rows - (list of member's last name, member's first
            name, a broad description, and a narrow description data)
            if memberId is not None:
                rows containing memberId
            else:
                all member and expertise rows
            Sorted by last name, first name, broad description, narrow
                description
    -------------------------------------------------------
    """
    
    sql = """
        SELECT member.memberSurname, member.memberForename, broad.broadDesc, narrow.narrowDesc
        FROM member
        INNER JOIN memberBroad ON member.memberId = memberBroad.memberBroadMemberId
        INNER JOIN broad ON broad.broadId = memberBroad.memberBroadBroadId
        INNER JOIN narrow ON narrow.narrowBroadId = memberBroad.memberBroadBroadId
    """
    data = []
    rows = []
    
    if (memberId != None):
        sql += " WHERE member.memberId = %s"
        data.append(memberId)
        
    sql += """
        GROUP BY member.memberSurname, member.memberForename, broad.broadDesc, narrow.narrowDesc
        ORDER BY member.memberSurname, member.memberForename, broad.broadDesc, narrow.narrowDesc
    """
    
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    
    return rows