from app import FrameWorkApp
import json

app = FrameWorkApp()

def load_view():
    with open("view.json", "r") as file:
        return json.load(file)

def save_view(data):
    with open("view.json", "w") as file:
        json.dump(data, file, indent=4)

def load_admins():
    with open("admins.json", "r") as file:
        return json.load(file)

def save_admins(data):
    with open("admins.json", "w") as file:
        json.dump(data, file, indent=4)

@app.route("/home")
def home(request, response):
    data = load_view()
    data["view"] += 1
    save_view(data)
    response.text = f"Home pagedan uyquli salom! - {data['view']}"

@app.route("/about")
def about(request, response):
    data = load_view()
    data["view2"] += 1
    save_view(data)
    response.text = f"About paged salom! - {data['view2']}"

@app.route("/u/{id}")
def get_info(request, response, id):
    admins = load_admins()

    if id in admins:
        admins[id]["view"] += 1
        save_admins(admins)
        response.text = json.dumps(admins[id], indent=4)
    else:
        response.text = "Bunday user yo'q!"