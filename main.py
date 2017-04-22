from flask import Flask, g, send_from_directory, jsonify, json
from FinalScript.TweetAnalyzer import userInfo
import pymysql.cursors

app = Flask(__name__, static_url_path='', static_folder='client/public')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'mysql_db'):
        # g.mysql_db = connect_db()
        g.mysql_db = pymysql.connect(
            host='localhost',
            user='root',
            #password='passwd',
            db='ssdi',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    return g.mysql_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'mysql_db'):
        g.mysql_db.close()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/data/<path:username>')
def data(username):
    info = userInfo(username)

    tweetInfo = json.dumps({
        'chartData': [info['earlyTweet'], info['midTweet'], info['eveningTweet'], info['lateTweet']],
        'wordData': info['commonWords']
    })

    with get_db().cursor() as cursor:
        # Create a new record
        sql = "REPLACE INTO `twitter_results` (`twitterHandle`, `tweetInfo`) VALUES (%s, %s)"
        cursor.execute(sql, (username, tweetInfo))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    get_db().commit()

    return jsonify(
        username=username,
        chartData=[info['earlyTweet'], info['midTweet'], info['eveningTweet'], info['lateTweet']],
        wordData=info['commonWords']
    )

if __name__ == '__main__':
    app.run()
