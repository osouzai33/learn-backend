import requests
import asyncio
import time

res = requests.post(
    "http://127.0.0.1:8000/items/",
    json={"name": "T-shirt", "price": 10000, "description": "しろいTシャツ"},
)

responce = requests.get(
    "http://127.0.0.1:8000/sample/",
    headers={"Authorization":"Bearer A123456789"},
)

print(res.status_code)
print(res.text) 

print(responce.status_code)
print(responce.text)
print(responce.headers)

async def sleep_time(sec):
    loop = asyncio.get_running_loop()
    res = await loop.run_in_executor(
        None, requests.get, f"http://127.0.0.1:8000/sleep_time/?sec={sec}"
    )
    return res.text

async def main():
    print(f"main start {time.strftime('%X')}")
    results = await asyncio.gather(sleep_time(3), sleep_time(2))
    print(results)
    print(f"main end {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main())