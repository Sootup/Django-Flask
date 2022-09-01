# import time 

# def func1(x):
#     print(x*2)
#     time.sleep(3)
#     print('func1 - OK')
    
    
# def func2(x):
#     print(x*3)
#     time.sleep(4)
#     print('func2 - ok')
    
# def main():
#     func1(2)
#     func2(2)
    
# print(time.strftime('%X'))

# # main()
# print(type(func1))
# print(type(func2(4)))


# print(time.strftime('%X'))
 
#Новый внешний вид асинк 
        
# import time
# import asyncio


# async def func1(x):
#     print(x*2)
#     await asyncio.sleep(3)
#     print('func1 - OK')
    
# async def func2(x):
#     print(x*3)
#     await asyncio.sleep(4)
#     print('func2 - ok')
    
# async def main():
#     task1 = asyncio.create_task(func1(2))
#     task2 = asyncio.create_task(func2(3))
    
#     print(type(task1))
#     print(task1.__class__.__base__)
    
#     await task1
#     await task2

# print(time.strftime('%X'))

# asyncio.run(main())

# print(time.strftime('%X'))    
# print(type(func1))
# print(type(func2(3)))

#Старый внешний вид


# import time
# import asyncio


# async def func1(x):
#     print(x*2)
#     await asyncio.sleep(3)
#     print('func1 - OK')
    
# async def func2(x):
#     print(x*3)
#     await asyncio.sleep(4)
#     print('func2 - ok')
    
# print(time.strftime('%X'))

# loop = asyncio.get_event_loop()
# task1 = loop.create_task(func1(2))
# task2 = loop.create_task(func2(3))

# loop.run_until_complete(asyncio.wait([task1, task2]))


# print(time.strftime('%X'))


# import asyncio

# async def get_conn(host, port):
#     class Conn:
#         async def put_data(self):
#             print('Отправки данных')
#             await asyncio.sleep(2)
#             print('Данные отправлены')
            
#         async def get_data(self):
#             print('получаем данные')
#             await asyncio.sleep(2)
#             print('Данные получены')
            
#         async def close(self):
#             print('Закрываем соединение')
#             await asyncio.sleep(2)
#             print('Соединение закрыто')
            
#     print('Устанавлваем соединение...')
#     await asyncio.sleep(2)
#     print('Соединение установлено')
#     return Conn()


# class Connection:
#     def __init__(self, host,port):
#         self.host = host
#         self.port = port
        
        
#     async def __aenter__(self):
#         self.conn = await get_conn(self.host, self.port)
#         return self.conn
    
#     async def __aexit__(self, exc_type, exc, tb):
#         await self.conn.close()
        
# async def main():
#     async with Connection('localhost', 9001) as conn:
#         send_task = asyncio.create_task(conn.put_data())
#         receive_task=asyncio.create_task(conn.get_data())
        
#         await send_task
#         await receive_task
        
        
# asyncio.run(main())        
            
                    
        
import time
import requests
import asyncio 
from aiohttp import ClientSession
import logging

async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}        
        async with session.get(url=url,params=params) as response:
            weather_json = await response.json()
            print(f'{city}:{weather_json["weather"][0]["main"]}')


async def main(cities):
    tasks = []
    for city in cities:
        logger = logging.info(f'делаем запрос по городу {city}')
        print(logger)
        tasks.append(asyncio.create_task(get_weather(city)))
    for task in tasks:
        await task


cities= ['Minsk', 'Moscow', 'Tokio', 'London','New York','Delhi','Tokyo','Minsk']


print(time.strftime('%X'))
asyncio.run(main(cities))
print(time.strftime('%X'))
