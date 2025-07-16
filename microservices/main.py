from flask import Flask, request, Response, render_template
from dao import (get_model, get_connection, insert_into_models, get_video, 
                 insert_into_videos, get_tag, insert_into_tags, get_models, 
                 get_videos, get_videos_from_tags, get_video_from_id, 
                 get_model_from_id, get_models_from_tags)
import json

app = Flask(__name__)
current_version: str = "1.0.0"
conn = get_connection()

def get_app():
    return app

# Get information about specific video
'''
curl --request GET \
  http://localhost:5000/api/stars/v1/videos/1
'''
@app.route("/api/stars/v1/videos/<video_id>", methods=['GET'])
def get_video_details(video_id: str):
    # Video name needs to be unique
    video: dict = get_video_from_id(conn, video_id)
    if video is None:
        return 404
    models: list = get_models_from_tags(conn, video_id)
    video["models"] = models
    return Response(json.dumps(video), 200, mimetype='application/json')


#get information about specific model
'''
curl --request GET \
  http://localhost:5000/api/stars/v1/models/danadearmond3
'''
@app.route("/api/stars/v1/models/<inner_id>", methods=['GET'])
def get_model_details(inner_id: str):
    model: dict = get_model(conn, inner_id)
    if model is None:
        return 404
    videos: list = get_videos_from_tags(conn, model["id"])
    model["videos"] = videos
    return Response(json.dumps(model), status=200, mimetype='application/json')


# Register a model
'''
POST
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"inner_id":"danadearmond3","name":"Dana Dearmond","dir":"public/videos/Dana_Dearmond"}' \
  http://localhost:5000/api/stars/v1/models
'''
'''
GET
curl --request GET \
  http://localhost:5000/api/stars/v1/models
'''
@app.route("/api/stars/v1/models", methods=['GET', 'POST'])
def register_model():
    if request.method == 'GET':
        # just return all models
        models: list = get_models(conn)
        return Response(json.dumps(models), status=200, mimetype='application/json')
    
    if request.method == 'POST':
        # Register this model
        request_data = request.json

        inner_id: str = request_data["inner_id"]
        name: str = request_data["name"]
        dir: str = request_data["dir"]

        model: dict = get_model(conn, inner_id)
        if len(model.keys()) == 0:
            # model not registered
            print(f"Model {name} not registered.")
            code = insert_into_models(conn, inner_id, name, dir)
            if code == None:
                return render_template("Error putting data into database."), 500
            else:
                return Response("", status=200, mimetype='application/json')
        else:
            return Response(json.dumps(model), status=201, mimetype='application/json')


'''
POST
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"DanaDearmond.mp4","path":"videos/Dana_Dearmond/DanaDearmond.mp4"}' \
  http://localhost:5000/api/stars/v1/videos
'''
'''
GET
curl --request GET \
  http://localhost:5000/api/stars/v1/videos
'''
@app.route("/api/stars/v1/videos", methods=['GET', 'POST'])
def register_video():
    if request.method == 'GET':
        videos: list = get_videos(conn)
        return Response(json.dumps(videos), status=200, mimetype='application/json')
    
    if request.method == 'POST':
        # Register this video
        request_data = request.json
        name: str = request_data["name"]
        video_path: str = request_data["path"]

        video: dict = get_video(conn, name)
        if len(video.keys()) == 0:
            print(f"Video {name} not registered.")
            code = insert_into_videos(conn, name, video_path)
            if code == None:
                return render_template("Error putting data into database."), 500
            else:
                return Response("", status=200, mimetype='application/json')
        else:
            return Response(json.dumps(video), status=201, mimetype='application/json')


'''
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"inner_id":"danadearmond3","name":"DanaDearmond.mp4","path":"videos/Dana_Dearmond/DanaDearmond.mp4"}' \
  http://localhost:5000/api/stars/v1/tags
'''
# Register a video to model
@app.route("/api/stars/v1/tags", methods=['POST'])
def tag_video_model():
    request_data = request.json
    name: str = request_data["name"]
    path: str = request_data["path"]
    inner_id: str = request_data["inner_id"]

    video: dict = get_video(conn, name, path)
    model: dict = get_model(conn, inner_id)

    if len(video.keys()) == 0 or len(model.keys()) == 0:
        print("Video: " + str(video) + ". Model: " + str(model))
        return render_template("Video or model not found"), 404
    
    # check if tag is present
    tag: dict = get_tag(conn, video["id"], model["id"])

    if len(tag.keys()) == 0:
        print(f"Tag with {video["name"]} and {model["inner_id"]} not registered.")
        code = insert_into_tags(conn, video["id"], model["id"])
        if code == None:
            return render_template("Error putting data into database."), 500
        else:
            return Response("", status=200, mimetype='application/json')
    else:
        return Response(json.dumps(tag), status=201, mimetype='application/json')


# Get videos information
# @app.route("/api/stars/v1/videos", methods=['GET'])
# def get_user_version(model_id: str):
#     response = {}
#     data = {}

#     data["version"] = current_version
#     data["user"] = user
#     response["status_code"] = "200"
#     response["data"] = data

#     string_response: str = json.dumps(response)
#     return string_response


# # Get video information
# @app.route("/api/stars/v1/videos/<video_id>", methods=['GET'])
# def get_user_version(video_id: str):
#     response = {}
#     data = {}

#     data["version"] = current_version
#     data["user"] = user
#     response["status_code"] = "200"
#     response["data"] = data

#     string_response: str = json.dumps(response)
#     return string_response
