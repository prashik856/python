from connector import get_tenant_connection
from setup_database import get_tenant_user, get_tenant_password, get_db_name


def get_connection():
    tenant_user:str = get_tenant_user()
    tenant_password: str = get_tenant_password()
    db_name: str = get_db_name()

    conn = get_tenant_connection(tenant_user, tenant_password, db_name)
    return conn


def insert_into_models(conn, inner_id: str, name: str, dir: str):
    # While registry, we set views to 0
    query = ("INSERT INTO MODELS (INNERID, NAME, VIEWS, DIR) VALUES (%s, %s, 0 , %s)")
    try:
        cursor = conn.cursor()
        cursor.execute(query, (inner_id, name, dir))
        conn.commit()
        cursor.close()
    except Exception as e:
        print("Exception occured while putting data into database.")
        print(e)
        return None
    return 200


def insert_into_videos(conn, name: str, path: str):
    query = ("INSERT INTO VIDEOS (NAME, VIEWS, VIDEOPATH) VALUES (%s, 0, %s)")
    try:
        cursor = conn.cursor()
        cursor.execute(query, (name, path))
        conn.commit()
        cursor.close()
    except Exception as e:
        print("Exception occured while putting data into database.")
        print(e)
        return None
    return 200


def insert_into_tags(conn, video_id: int, model_id: int):
    query = ("INSERT INTO MODELTAGS (VIDEOID, MODELID) VALUES (%s, %s)")
    try:
        cursor = conn.cursor()
        cursor.execute(query, (video_id, model_id))
        conn.commit()
        cursor.close()
    except Exception as e:
        print("Exception occured while putting data into database.")
        print(e)
        return None
    return 200


def get_model(conn, inner_id: str):
    model: dict = {}
    query = ("SELECT ID, INNERID, NAME, VIEWS, DIR FROM MODELS WHERE `INNERID`=%s")
    try:
        cursor = conn.cursor()
        cursor.execute(query, (inner_id,))

        # print("Reading query response")
        for (id, innerid, name, views, dir) in cursor:
            model["id"] = id
            model["inner_id"] = innerid
            model["name"] = name
            model["views"] = views
            model["dir"] = dir
        cursor.close()
        return model
    except Exception as e:
        print("Exception occured while getting data from database.")
        print(e)
        return None


def get_models(conn):
    models: list = []
    query = ("SELECT ID, INNERID, NAME, VIEWS, DIR FROM MODELS")
    try:
        cursor = conn.cursor()
        cursor.execute(query)

        # print("Reading query response")
        for (id, innerid, name, views, dir) in cursor:
            model: dict = {}
            model["id"] = id
            model["inner_id"] = innerid
            model["name"] = name
            model["views"] = views
            model["dir"] = dir
            models.append(model)
        cursor.close()
        return models
    except Exception as e:
        print("Exception occured while getting data from database.")
        print(e)
        return None


def get_video(conn, name: str, path: str):
    video: dict = {}
    query = ("SELECT ID, NAME, VIEWS, VIDEOPATH FROM VIDEOS WHERE `NAME`=%s AND `VIDEOPATH`=%s")
    try:
        cursor = conn.cursor()
        cursor.execute(query, (name,path))

        # print("Reading query response")
        for (id, video_name, views, video_path) in cursor:
            video["id"] = id
            video["name"] = video_name
            video["views"] = views
            video["path"] = video_path
        cursor.close()
        return video
    except Exception as e:
        print("Exception occured while getting data from database.")
        print(e)
        return None


def get_videos(conn):
    videos: list = []
    query = ("SELECT ID, NAME, VIEWS, VIDEOPATH FROM VIDEOS")
    try:
        cursor = conn.cursor()
        cursor.execute(query)

        # print("Reading query response")
        for (id, video_name, views, video_path) in cursor:
            video: dict = {}
            video["id"] = id
            video["name"] = video_name
            video["views"] = views
            video["path"] = video_path
            videos.append(video)
        cursor.close()
        return videos
    except Exception as e:
        print("Exception occured while getting data from database.")
        print(e)
        return None


def get_tag(conn, video_id: int, model_id: int):
    tag: dict = {}
    query = ("SELECT ID, VIDEOID, MODELID FROM MODELTAGS WHERE `VIDEOID`=%s AND `MODELID`=%s")
    try:
        cursor = conn.cursor()
        cursor.execute(query, (video_id, model_id))
        
        print("Reading query response")
        for (id, video_id, model_id) in cursor:
            tag["id"] = id
            tag["video_id"] = video_id
            tag["model_id"] = model_id
        cursor.close()
        return tag

    except Exception as e:
        print("Exception occured while getting data from database.")
        print(e)
        return None

