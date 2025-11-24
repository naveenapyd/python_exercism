def response(hey_bob):
    a = hey_bob.rstrip()
    if (a.endswith("?")) and (a.isupper()):
        return "Calm down, I know what I'm doing!"
    if a.endswith("?"):
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if len(hey_bob) == 0 or not hey_bob.strip():
        return "Fine. Be that way!"
    return "Whatever."
