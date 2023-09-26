from fastapi import FastAPI
from hasher import hasher

app = FastAPI()

# password = 42
# pw_string = str(password)
# print(pw_string)
# thesalt = "mysaltstring"
# print(thesalt)

@app.get("/")
async def root(pw_string, thesalt):
    print("begin call")
    res = hasher(pw_string, thesalt)
    return {res}
