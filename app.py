from flask import Flask
from redis import Redis

app = Flask(__name__)
redisDb = Redis(host='redis-db-service', port=6379)

@app.route('/')
def welcomeToKodeKloud():
    redisDb.incr('visitorCount')
    visitCount = str(redisDb.get('visitorCount').decode('utf-8'))
    return f"Welcome to KodeKloud! You are visitor #{visitCount}."

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)