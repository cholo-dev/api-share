

from top1phsmm.api import top1phsmm
from top1phsmm.api import Autmate
from mahdix import *
from threading import Thread
from concurrent.futures import ThreadPoolExecutor as thd
import requests
connect=top1phsmm(api_key='lfqctrg88akz3oamcd1uae9j1rtph1qz1ano87m24gthyzsg6cx2ds4yjfnqxqi1')#changge it
connect_automate=Autmate()
def submite(token,post_url,order_id,quantity):
    url='https://graph.facebook.com/v13.0/me/feed'
    datas={
        'link':post_url,
        'published':'0',
        'privacy':'{"value":"SELF"}',
        'access_token':token}
    try:
        count_of_2 = opder_delev_list.count(order_id)
        if count_of_2 < quantity:
            res=requests.post(url,data=datas,headers={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate',
                'connection': 'keep-alive',
                'content-length': '0',
                'host': 'graph.facebook.com'
            }).json()
            if res['id']:
                opder_delev_list.append(order_id)
                count_of_2 = opder_delev_list.count(order_id)
                # sys.stdout.write(f'\033[1;37m[\033[38;5;81m{order_id}\033[1;37m]\033[1;32m Done Successfully Shared\033[1;31m ───────> \033[1;34m{count_of_2} \033[1;31m')
                # sys.stdout.flush()  # Ensure the output is immediately written
                # sys.stdout.write('\r') 
                # Move the cursor to the beginning of the line
                # print(f'\033[38;5;189m────────────────────────────────────────────────────────────')
            # New print structure with colors and brackets:
            print(f'\033[1;32mThis Order [\033[1;34m{order_id}\033[1;32m] on TOP1PHSMM.COM Successfully Delivered Shares [\033[1;31m{count_of_2}\033[1;32m]\n', end='\r')
    except Exception as e:
        try:
            for thdes in thdess:
                thdes.join()
                thdess.remove(thdes)
        except:pass
        # print(f'Error: {rc(mycolor)} {res['error']['message']}' ,end= '\r')
        pass



crdt = datetime.now();exdt = datetime.strptime('2025-8-30', '%Y-%m-%d')
def updating():
    exit()
if crdt > exdt:updating()


def load_tokens(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return list(file.read().splitlines())  # Return list of tokens
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied while trying to access {file_path}.")
        return []

# Use the function to load tokens
my_cookes = load_tokens('input_file.txt')
if my_cookes:
    print(f"Total Ids: {len(my_cookes)}")
else:
    print("No tokens found.")

service_id=[]
opder_delev_list=[]
wrong_url=[]
thdess=[]


def mains():
    get_orders = connect.get_orders()
    for lins in get_orders:
        service_id =lins['service_id']
        quantity =lins['quantity']
        order_link=lins['link']
        order_id =lins['id']
        status= lins['status']
        if service_id in [1204,1199,1229,1205] and quantity > 0  and 'facebook.com' in order_link and 'pending' in status  :
            if order_id not in opder_delev_list:
                opder_delev_list.append(order_id)
                # Update order status to 'In Progress'
                connect.update_order_status(order_id, status='In Progress')
                print(f"Processing Order ID: {order_id}")

                # Handle different Facebook link types
                if '/share/' in order_link:
                    retx = requests.get(order_link, headers={ 
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36', 
                        'Accept': 'application/json', 
                        'Connection': 'keep-alive'
                    }, allow_redirects=True)
                    order_link = retx.url

                print(f'{LI_WHITE}Order ID: {LI_GREEN}{order_id}')
                print(f'{LI_WHITE}Quantity: {LI_GREEN}{quantity}')
                print(f'{LI_WHITE}Link: {LI_GREEN}{order_link}')
                
                while  opder_delev_list.count(order_id)<= quantity :
                    # with thd(max_workers=40) as sub:
                        for cokis in my_cookes:
                            token=cokis.split('|')[1]
                            count_of_2 = opder_delev_list.count(order_id)
                            if count_of_2+500 >= quantity:
                                connect.set_orders_completed(order_id)
                                print(f"{LI_GREEN}The Order Is Complited : {LI_WHITE} {order_id}")
                                break
                            elif  count_of_2 < quantity:
                                try:
                                    
                                     
                                    thdes=Thread(target= submite,args=(token,order_link,order_id,quantity,))
                                    thdess.append(thdes)
                                    thdes.start()
                                    # slps(1)
                                except:
                                    pass
                                # with thd(max_workers=40) as sub:
                            #       sub.submit(submite,token,order_link,order_id)
                            
                                # slps(2)


def schedule_task():
    while True:
        mains()  # Run the main processing function
        time.sleep(600)  # Sleep for 10 minutes (600 seconds)

# Start the task
if __name__ == "__main__":
    schedule_task()

