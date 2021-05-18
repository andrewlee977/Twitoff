"""Main app/routing file for Twitoff"""
from os import getenv
from flask import Flask, render_template
from .models import DB, User, Tweet
from .twitter import add_or_update_user


def create_app():
    """Creates and configures an instance of the flask application"""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template("base.html", title="Home", users=User.query.all())

    @app.route('/populate')
    def populate():
        # insert_users(["elonmusk", "jackblack", "jeffbezos", "brianchesky"])

        # insert_tweets(["We need a carbon tax!", "I'm a comedian", "Blue Origin for the win!",
        #                 "I love Airbnb!", "We must colonize Mars", "Hello, world!"], 'elonmusk')
        add_or_update_user('elonmusk')
        add_or_update_user('jackblack')

        return render_template("base.html", title="Home", users=User.query.all(), tweets=Tweet.query.all())

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template("base.html", title="Home", users=User.query.all())


    return app


# def insert_users(usernames):
#     for id_index, username in enumerate(usernames):
#         user = User(id=id_index, username=username)
#         DB.session.add(user)
#         DB.session.commit()

# def insert_tweets(tweets, user):
#     userObject = User.query.filter(User.username == user).one()
#     for id_index, tweet in enumerate(tweets):
#         tweet = Tweet(id=id_index, text=tweet, user=userObject)
#         DB.session.add(tweet)
#         DB.session.commit()
