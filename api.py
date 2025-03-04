import requests
import json
import re
from fb_atm import Page
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor as thd
darkblue = "\033[34m"

class top1phsmm:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_key_V2 = 'rfiecqd5p0ucagww27epdswm6n5jymd8jac30ucns4ux1xc713mdzynr6iyh3zfo' 
        self.headers = {
            'Content-Type': 'application/json',
            'X-Api-Key': self.api_key
        }

    def update_order_link(self, orderID, text='Order is Done Successfully!'):
        return requests.post(
            f'https://top1phsmm.com/adminapi/v2/orders/{orderID}/edit-link',
            headers=self.headers,
            json={'link': text}
        ).text

    def update_order_status(self, orderID, status='In Progress'):
        url = "https://top1phsmm.com/adminapi/v1"
        data = {
            "key": self.api_key_V2,
            "action": "setInprogress",  # This should set the status to "In Progress"
            "id": orderID
        }

        try:
            response = requests.post(url, json=data, headers=self.headers)
            if response.status_code == 200:
                response_data = response.json()
                print(f"Order {orderID} status updated to In Progress.")
                return response_data
            else:
                print(f"Failed to update order status. HTTP Status Code: {response.status_code}")
                return response.text
        except Exception as e:
            print(f"An error occurred while updating the order status: {e}")
            return None

    def set_orders_completed(self, orderID):
        url = "https://top1phsmm.com/adminapi/v1"
        data = {
            "key": self.api_key_V2,
            "action": "setCompleted",  # Action to mark the order as completed
            "id": orderID
        }

        try:
            # Send the request to mark the order as completed
            response = requests.post(url, json=data, headers=self.headers)

            if response.status_code == 200:
                response_data = response.json()
                return response_data
            else:
                print(f"Failed to set order as completed. HTTP Status Code: {response.status_code}")
                return response.text
        except Exception as e:
            print(f"An error occurred while marking the order as completed: {e}")
            return None

    def get_orders(self):
        response = requests.get('https://top1phsmm.com/adminapi/v2/orders', headers=self.headers).json()
        order_list = response['data']['list']
        return order_list


class Autmate(Page):  # Changed from Autmate to Automate
    def __init__(self):
        super().__init__()
        self.headers_web = {  # Define your headers here
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Accept': 'application/json',
            'Connection': 'keep-alive'
        }

    def get_postID(self, url):
        try:
            response = requests.get(url, headers=self.headers_web).text
            # First try extracting 'post_id' from newer Facebook URLs
            post_id = re.search('"post_id":"(.*?)"', str(response))
            if post_id:
                return post_id.group(1)
            
            # Otherwise, try extracting 'story_fbid' for older Facebook URLs
            post_id = re.search('story_fbid=(.*?)&', str(response))
            if post_id:
                return post_id.group(1)
            
            # If both fail, return None
            return None
        except Exception as e:
            print(f"Error extracting post ID from {url}: {e}")
            return None