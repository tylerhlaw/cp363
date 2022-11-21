# -------------------------------------
# File: functions.py
# Project: assignment 3 for cp363
# Description: This file holds all the functions needed for assignment 3
# -------------------------------------
# Author:  Tyler Law
# ID:      200694180
# Email:   lawx4180@mylaurier.ca
# Version (date): 07.11.22
# -------------------------------------

def get_all_pub_counts(cursor, memberId=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(cursor)
    Use: rows = pub_counts(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the numbers of publications of each type data.
            Name these three fields "articles", "papers", and "books")
            if memberId is not None:
                rows containing memberId
            else:
                all member and publication rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    
    sql = """
    SELECT memberForename, memberSurname,
        (SELECT COUNT(pub.pubPubType) FROM pub WHERE pub.pubPubType = 'a' AND member.memberId = pub.pubMemberId) AS articles,        
        (SELECT COUNT(pub.pubPubType) FROM pub WHERE pub.pubPubType = 'p' AND member.memberId = pub.pubMemberId) AS papers,
        (SELECT COUNT(pub.pubPubType) FROM pub WHERE pub.pubPubType = 'b' AND member.memberId = pub.pubMemberId) AS books
    FROM member
    """
    params = []
    
    if (memberId != None):
        sql += " WHERE memberId = %s"
        params.append(memberId)
        
    sql += " ORDER BY memberSurname, memberForename"
    
    cursor.execute(sql, params)
    return cursor.fetchall();

def get_expertise_counts(cursor, memberId=None):
    """
    -------------------------------------------------------
    Use: rows = get_expertise_counts(cursor)
    Use: rows = get_expertise_counts(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the number of broad and narrow expertises
            for the member data. Name these fields "broadCount" and "narrowCount")
            if memberId is not None:
                rows containing memberId
            else:
                all member, broad, and narrow expertise rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    
    sql = """
    SELECT member.memberSurname, member.memberForename,
        (SELECT COUNT(memberBroad.memberBroadBroadId) FROM memberBroad WHERE memberId = memberBroad.memberBroadMemberId) AS broadCount,
        (SELECT COUNT(memberNarrow.memberNarrowNarrowId) FROM memberNarrow WHERE memberId = memberNarrow.memberNarrowMemberId) AS narrowCount
    FROM member
    """
    params = []
    
    if (memberId != None):
        sql += " WHERE member.memberId = %s"
        params.append(memberId)
        
    sql += " ORDER BY member.memberSurname, member.memberForename"
    
    cursor.execute(sql, params)
    return cursor.fetchall();
        
def get_broad_counts(cursor, broadId=None):
    """
    -------------------------------------------------------
    Use: rows = get_broad_counts(cursor)
    Use: rows = get_broad_counts(cursor, broadId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broadId - a keyword ID number (int)
    Returns:
        rows - (list of a broad expertise descriptions and the number of
            narrow expertises that belong to it data. Name the
            second field "narrowCount".)
            if broadId is not None:
                rows containing broadId
            else:
                all broad and narrow rows
            Sorted by broad expertise description
    -------------------------------------------------------
    """
    
    sql = """
    SELECT broad.broadDesc,
        (SELECT COUNT(narrow.narrowBroadId) FROM narrow WHERE narrow.narrowBroadId = broad.broadId) AS narrowCount
    FROM broad
    """
    params = []
    
    if (broadId != None):
        params.append(broadId)
        sql += " WHERE broad.broadId = %s"
        
    sql += " ORDER BY broadDesc"
        
    cursor.execute(sql, params)
    return cursor.fetchall()

def get_broad_member_counts(cursor, broadId=None):
    """
    -------------------------------------------------------
    Use: rows = get_broad_memberCounts(cursor)
    Use: rows = get_broad_memberCounts(cursor, broadId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broadId - a keyword ID number (int)
    Returns:
        rows - (list of a keyword description and the number of members
            that have it data. Name the second field "memberCount".)
            if broadId is not None:
                rows containing broadId
            else:
                all member and keyword rows
            Sorted by keyword description
    -------------------------------------------------------
    """
    
    sql = """
    SELECT broad.broadDesc,
        (SELECT COUNT(memberBroad.memberBroadMemberId) FROM memberBroad WHERE memberBroad.memberBroadMemberId = broad.broadId) AS memberCountm   
    FROM broad
    """
    params = []
    
    if (broadId != None):
        sql += " WHERE broad.broadId = %s"
        params.append(broadId)
        
    sql += " ORDER BY broad.broadDesc"
    
    cursor.execute(sql, params)
    return cursor.fetchall()

def get_narrow_member_counts(cursor, narrowId=None):
    """
    -------------------------------------------------------
    Use: rows = get_narrow_memberCounts(cursor)
    Use: rows = get_narrow_memberCounts(cursor, narrowId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        narrowId - a supp_key ID number (int)
    Returns:
        rows - (list of a broad expertise description, a narrow
            expertise description, and the number of members that have that
            narrow expertise data. Name the last field "memberCount".)
            if narrowId is not None:
                rows containing narrowId
            else:
                all member, broad, and narrow expertises rows
            Sorted by broad description, narrow description
    -------------------------------------------------------
    """
    
    sql = """
    SELECT broad.broadDesc, narrow.narrowDesc,
        (SELECT COUNT(memberNarrow.memberNarrowMemberId) FROM memberNarrow WHERE memberNarrow.memberNarrowNarrowId = narrow.narrowId) AS memberCount
    FROM broad, narrow
    WHERE broad.broadId = narrow.narrowBroadId
    """
    params = []
    
    if (narrowId != None):
        params.append(narrowId)
        sql += " AND narrow.narrowId = %s"
        
    sql += """
    GROUP BY broad.broadDesc, narrow.narrowDesc, memberCount
    ORDER BY broad.broadDesc, narrow.narrowDesc
    """
    
    cursor.execute(sql, params)
    return cursor.fetchall()

        
        
        
        
        
        
        
        
        
        
        
        
        