from datetime import datetime, timedelta
import pickle
import shelve
from socket import socketpair


class Move:
    """Move is a dance move"""

    def __init__(self, time, limb, what):
        self.time = time
        self.limb = limb
        self.what = what

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}({self.time!r}, {self.limb!r}, {self.what!r})"


second = timedelta(seconds=1)
now = datetime.now()

move1 = Move(now + 1 * second, "jump", "to the left")
move2 = Move(now + 2 * second, "jump", "to the right")
move3 = Move(now + 3 * second, "jump", "on your hips")
move4 = Move(now + 4 * second, "jump", "bring it tight")

# Example of dumps and loads methods. Dumps into bytes and loads from bytes.

data = pickle.dumps(move1)
print(data)
print(type(data))

move1d = pickle.loads(data)
print(move1d)
print(type(move1d))
print("=============")

# Example of dump and load methods. Dump bytes into file and loads from file of bytes.
# Load from file loads list of objects.

with open("move1.pkl", "wb") as out:
    pickle.dump(move1, out)

with open("move1.pkl", "rb") as in_put:
    move1s = pickle.load(in_put)

print(move1s)
print(type(move1s))
print("=============")
dance = [move1, move2, move3, move4]
with open("dance.pkl", "wb") as out:
    pickle.dump(dance, out)

with open("dance.pkl", "rb") as in_put:
    moves = pickle.load(in_put)
print(moves)
print(type(moves))
print("=============")

# Streaming pickle example

ws, rs = socketpair()
w, r = ws.makefile("wb"), rs.makefile("rb")

pickle.dump(move1, w)
pickle.dump(move2, w)
pickle.dump(move3, w)
pickle.dump(move4, w)
w.flush()

for _ in range(4):
    move = pickle.load(r)
    print(f"{move.limb} {move.what}")
print("=============")
db = shelve.open("dance.db")
db["1"] = move1
db["2"] = move2
db["3"] = move3
db["4"] = move4

db.close()

db = shelve.open("dance.db")
print(db["1"])
print(db["2"])
print(db["3"])
print(db["4"])
