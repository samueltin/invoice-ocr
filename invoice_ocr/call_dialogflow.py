import requests
import logging
import os

logger = logging.getLogger(__name__)

DF_SESSION_ID = "1337"
DF_TOKEN=os.environ['INVOICE_OCR_DIALOGFLOW_TOKEN']
DF_URL='https://api.dialogflow.com/v1/query?v=20150910'
DF_PROJECT_ID = 'invoice-items'


def get_response(utter):

    data = {
        "lang": "zh-cn",
        "query": utter,
        "sessionId": DF_SESSION_ID,
        "timezone": "Asia/Hong_Kong"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(DF_TOKEN)
    }

    resp = requests.post(DF_URL, json=data, headers=headers)
    if resp.status_code == 200:
        temp = resp.json()
        logger.debug("result from df=%s", temp)
        # print("result from df={}".format(temp))
        intentName = temp['result']['metadata']['intentName']
        logger.debug("Intent=%s", intentName)
        # print("Intent={}".format(intentName) )
        return intentName
    else:
        logger.error("Error calling DF: status_code=%d, text=%s", resp.status_code, resp.text)

if __name__ == '__main__':
    get_response('無線充電器蘋果')