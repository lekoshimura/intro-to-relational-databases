#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect();
    curs = conn.cursor();
    sql = 'delete from matches';
    curs.execute(sql);
    conn.commit();
    conn.close();


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect();
    curs = conn.cursor();
    sql = 'delete from players';
    curs.execute(sql);
    conn.commit();
    conn.close();


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect();
    curs = conn.cursor();
    sql = 'select count(*) from players';
    curs.execute(sql);
    row = curs.fetchone();
    conn.close();
    return row[0];


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect();
    curs = conn.cursor();
    curs.execute('insert into players (name) values (%s)', (bleach.clean(name),));
    conn.commit();
    conn.close();


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect();
    curs = conn.cursor();
    sql = '''
        select
        p.id,
        p.name,
        (select count(*) from matches m where m.winner = p.id) as wins,
        (select count(*) from matches m where m.winner = p.id or m.loser = p.id) as matches
        from players p;
        ''';
    curs.execute(sql);
    standings = curs.fetchall();
    conn.close();
    return standings;


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect();
    curs = conn.cursor();
    sql = 'insert into matches (winner, loser) values (%s, %s)';
    curs.execute(sql % (winner, loser));
    conn.commit();
    conn.close();


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect();
    curs = conn.cursor();
    sql = '''
        select
        p.id,
        p.name,
        (select count(*) from matches m where m.winner = p.id) as wins
        from players p
        order by wins desc;
        ''';
    curs.execute(sql);
    rows_number = curs.rowcount;
    pairings = [];
    current_row = 0;
    while (current_row < rows_number):
        row_a = curs.fetchone();
        current_row += 1;
        row_b = curs.fetchone();
        current_row += 1;
        pairings.append((
            row_a[0],
            row_a[1],
            row_b[0],
            row_b[1]
        ))
    conn.close();
    return pairings;
