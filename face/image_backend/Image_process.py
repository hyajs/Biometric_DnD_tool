import requests,json
from http.client import HTTPSConnection
import urllib
import cv2



# this function is used to find the attribute level with highest probability
def max_value(name, number, probability,test_dict):
    if name in test_dict:
        if test_dict[name][1] < probability:
            test_dict[name] = [number, probability]
        else:
            pass
    else:
        test_dict[name] = [number, probability]
    return test_dict


# sending faces to find the corrosponding face locations and save the cropped face to the given location
# if multiple faces are detected, program will only take the first one
def image_process(filepath, directory,id):
    img = cv2.imread(filepath)
    url = 'https://australiaeast.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceAttributes=age'
    image_data = open(filepath, "rb").read()
    headers = {
        'Content-Type': 'application/octet-stream',
        #password needed
        # 'Ocp-Apim-Subscription-Key': ''
    }

    r = requests.post(url, data=image_data, headers=headers)
    js = r.json()
    process = js[0]['faceRectangle']
    age = js[0]['faceAttributes']['age']

    x,y,x2,y2 = process['top'],process['left'],process['height'],process['width']
    imgcropped = img[x:x + x2, y:y + y2]

    destination = directory + str(id)+'.png'
    cv2.imwrite(destination, imgcropped)
    return age


# using the corrosponding face locations to upload data to BM and retrieve the results
def bio_metric(fileroute,id):
    attributes = ['aggressive', 'confident', 'intelligent', 'calm', 'humble', 'sociable', 'attractive', 'weird',
                  'responsible', 'kind', 'caring']
    attribute_result = {}
    conn = HTTPSConnection('australiaeast.api.cognitive.microsoft.com')
    dest = fileroute + '/'+str(id) + '.png'
    image_data = open(dest, "rb").read()
    headers = {
        # Request headers
        'Content-Type': 'multipart/octet-stream',
        # 'Prediction-key': '',
    }
    params = urllib.parse.urlencode({
        # Request parameters
        # 'projectId': '',
        # 'publishedName': '',
        # 'application': ''
    })

    body = {
        image_data
    }
    try:
        conn.request("POST",
                     "/customvision/v3.1/Prediction/{projectId}/classify/iterations/{publishedName}/image?%s" % params,
                     body, headers)
        response = conn.getresponse()

        data = response.read()
        js = json.loads(data)
        jss = js['predictions']
        for js in jss:

            try:
                for element in attributes:
                    if element in js['tagName']:
                        max_value(js['tagName'][0:-2], js['tagName'][-1], js['probability'],attribute_result)
            except:
                pass
        conn.close()
        return attribute_result
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
