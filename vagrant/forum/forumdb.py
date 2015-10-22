#
# Database access functions for the web forum.
#

import time
import psycopg2
import bleach

## Database connection
DB = []

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect('dbname=forum');
    cursor = DB.cursor();
    sql = "select time, content from posts order by time desc";
    cursor.execute(sql);

    # List Comprehensions (https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions)
    # a = [str(wi) for wi in wordids]
    # is the same as
    # a = []
    # for wi in wordids:
    #     a.append(str(wi))
    posts = ({'content': str(row[1]), 'time': str(row[0])} for row in cursor.fetchall())

    DB.close();
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    content = bleach.clean(content);
    DB = psycopg2.connect('dbname=forum');
    cursor = DB.cursor();
    cursor.execute("insert into posts (content) values (%s)", (content,));
    DB.commit();
    DB.close();
    # t = time.strftime('%c', time.localtime())
    # DB.append((t, content))
