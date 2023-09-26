import hashlib
import os

def hasher(pw_string, thesalt):
    print(pw_string)
    print(thesalt)
    pwandsalt = pw_string+thesalt
    hashed = hashlib.md5(pwandsalt.encode())
    print(hashed)
    output = hashed.hexdigest()
    trunc = output[:6]
    print(output)
    print(trunc)
    return(output)