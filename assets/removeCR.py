cmd_script = './runpynb/scripts/runpynb'

# https://stackoverflow.com/questions/13953639/check-carriage-return-is-there-in-a-given-string
with open(cmd_script, 'rb+') as f:
    content = f.read()
    f.seek(0)
    f.write(content.replace(b'\r', b''))
    f.truncate()

filecontents = open(cmd_script, 'rb').readlines()
assert b'\r' not in filecontents[0]    