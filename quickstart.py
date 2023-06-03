""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import os


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username="coderefer", password="Vamsi@2391")

with smart_run(session):
    # general settings
    # session.set_dont_include(["friend1", "friend2", "friend3"])
    users = session.target_list(os.path.join(os.getcwd() + '/files/', "users.txt"))
    # activity
    # session.like_by_tags(["photography"], amount=10)
    # session.set_do_comment(enabled=True)
    session.set_action_delays(enabled=True,
                              like=3,
                              comment=5,
                              follow=4.17,
                              unfollow=28,
                              story=10)
    session.set_skip_users(skip_private=False)
    session.set_do_like(100)
    session.interact_by_users(users,10)
    session.end()
