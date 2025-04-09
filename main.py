from app import FrameWorkApp
import json

app = FrameWorkApp()


def load_users():
    with open("users.json", "r") as file:
        users = json.load(file)

    return users


@app.route("/home")
def home(request, response):
    response.text = "Home pagedan uyquli salom!"


@app.route("/about")
def about(request, response):
    response.text = "About pagedan Azizxonga salom!"


@app.route("/u/{id}")
def get_info(request, response, id):
    users = load_users()
    user = users.get(id, "Bunday user yo'q!")

    response.text = json.dumps(user)


"""
    "/home" : home,
    "/about" : about,
    "/sardor" : sardor,
    "/u/munisa" : user,
    "/u/zoir" : user
"""

"""
    "/u/id" => "/u/1"

"""







lst = [12,3,4,5,6,7]
target = 8

answer = []

for i in lst:
    if target == i:

        answer.append(-1)

