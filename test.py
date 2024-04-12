import asyncio
import aiohttp


url = 'https://profile.xboxlive.com/users/me/profile/settings'


with open('tokens.txt', 'r') as file:
    tokens = [line.strip() for line in file]

async def check_token(token):
    # Define the headers with the token
    headers = {
        'Authorization': token,
        'X-XBL-Contract-Version': '2',
        'Accept-Language': 'en-US',
        'Connection': 'keep-alive'
    }
    

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            status_code = response.status
            if status_code in [200, 201, 202, 204]:
                print(f"Token responded with status code {status_code}")
            else:
                print(f"Token did not respond with a desired status code. Status code: {status_code}")

async def main():
    tasks = [check_token(token) for token in tokens]
    await asyncio.gather(*tasks)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
