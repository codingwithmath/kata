strs = ["neet","code","love","you"]

joined = ",".join(strs)

print(joined.split(","))

def encode(self, strs: List[str]) -> str:
    if len(strs) == 0:
        return None
    return ",".join(strs)