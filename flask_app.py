from flask import Flask, jsonify, request

app = Flask(__name__)

contacts=[
    {
        "id":1,
        "Name":"Lily",
        "Contact":"1234567843",
        "Done":False
    },
    {
        "id":2,
        "Name":"Tina",
        "Contact":"3456789201",
        "Done":False
    },
    {
        "id":3,
        "Name":"Mary",
        "Contact":"2498750185",
        "Done":False
    },
]

@app.route("/")
def home_screen():
    return "Contact storage"

@app.route("/get-data")

def get_contact():
    return jsonify({
        "data":contacts
    })

@app.route("/add-data")

def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    
    contact=[
        {
    
            "id":contacts[-1]["id"]+1,
            "Name":request.json.get("Name",""),
            "Contact":request.json.get("Contact",""),
            "Done":False
        }
    ]
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"successfully updated!"
    })
    




if (__name__ == "__main__"):
    app.run(debug=True)


