from openai import OpenAI
from config import API_KEY,BASE_URL, TIMEOUT, MODEL, MAX_RETRY
from logger import logger

import time

""" 
Maintanabilit: Keeping code centalized : saperation of responsibility
Reliability: Error handling also implement retry and backoff
Observabilit: Proper looging

Now there will be only one connection to model and each agent use this to 
communication with model 
 """
client = OpenAI(base_url=BASE_URL, api_key=API_KEY, timeout=TIMEOUT)


def call_llm(messages):
    for attempt in range(1, int(MAX_RETRY)+1):
        try:
            logger.info(f"LLM request attempt {attempt}")
            response = client.chat.completions.create(model=MODEL, messages=messages)
            logger.info( "LLM request successful")
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"LLM request failed: {e}")

            if attempt == MAX_RETRY:
                logger.error("Maximum retry limit reached")
                raise RuntimeError("LLM request failed after "f"{MAX_RETRY} attempts.")

            wait_time = attempt * 2
            logger.info( f"Retrying in {wait_time} seconds")
            time.sleep(wait_time)
