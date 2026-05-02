import asyncio
import sys



async def transform_payload(user_id, delay_ms, payload):
    delay_s = int(delay_ms)/1000
    await asyncio.sleep(delay_s)
    return user_id, payload.upper()



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    tasks = []
    for _ in range(n):
        user_id, delay_ms, payload = sys.stdin.readline().strip().split()
        task = transform_payload(user_id, delay_ms, payload)
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    for user_id, payload in results:
        print(f"{user_id}:{payload}")



if __name__ == "__main__":
    asyncio.run(main())