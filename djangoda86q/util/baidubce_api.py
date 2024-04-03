#coding:utf-8
__author__ = "ila"
import urllib.request, json
import base64
import urllib.parse
import requests

class BaiDuBce(object):
    def get_alitoken(self,client_id, client_secret):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret + ''
        request = urllib.request.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read()
        access_token = 'err'

        if (content):
            # print(content)
            access_token = json.loads(content.decode('utf-8'))['access_token']
            # print(access_token)

        return access_token

    def open_pic2base64(self,image):
        f = open(image, 'rb')
        img = base64.b64encode(f.read()).decode('utf-8')
        return img

    def bd_check2pic(self,client_id, client_secret, image1, image2):

        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
        params = json.dumps(
            [{"image": self.open_pic2base64(image1), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
             {"image": self.open_pic2base64(image2), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"}])

        access_token = self.get_alitoken(client_id, client_secret)
        request_url = request_url + "?access_token=" + access_token

        params = params.encode("utf-8")

        req = urllib.request.Request(url=request_url, data=params)
        req.add_header('Content-Type', 'application/json')

        res = urllib.request.urlopen(req)
        content = res.read()

        score = 0
        if content:
            try:
                score = json.loads(content.decode('utf-8'))['result']['score']
            except:
                pass

        return score

    def ocr_checkpic(self, client_id, client_secret, image):

        access_token = self.get_alitoken(client_id, client_secret)
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={}".format(access_token)

        payload={"image": self.open_pic2base64(image)}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", request_url, headers=headers, data=payload)
        json_res = json.loads(response.text)

        return json_res.get("words_result")[0].get("words")

    def dish_checkpic(self, client_id, client_secret, image):

        access_token = self.get_alitoken(client_id, client_secret)
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish?access_token={}".format(access_token)

        payload={"image": self.open_pic2base64(image), "baike_num": 1}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", request_url, headers=headers, data=payload)
        json_res = json.loads(response.text)

        return json_res.get("result")[0]

    def animal_checkpic(self, client_id, client_secret, image):

        access_token = self.get_alitoken(client_id, client_secret)
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal?access_token={}".format(access_token)

        payload={"image": self.open_pic2base64(image), "baike_num": 1}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", request_url, headers=headers, data=payload)
        json_res = json.loads(response.text)

        return json_res.get("result")[0]

    def plant_checkpic(self, client_id, client_secret, image):

        access_token = self.get_alitoken(client_id, client_secret)
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant?access_token={}".format(access_token)

        payload={"image": self.open_pic2base64(image), "baike_num": 1}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", request_url, headers=headers, data=payload)
        json_res = json.loads(response.text)

        return json_res.get("result")[0]


if __name__=='__main__':
    client_id = 'x20xOjtOsAtbQhm2WBuifuQw'  # ak
    client_secret = 'O7yMp2dmOnCtQtBokUt1gN6hgFCcLLcp'  # sk

    # 本地图片地址，根据自己的图片进行修改
    image1 = 'nude1.jpg'
    image2 = 'nude2.jpg'

    bdb=BaiDuBce()
    bdb.bd_check2pic(client_id, client_secret, image1, image2)