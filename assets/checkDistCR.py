for patch in range(0,20):
    cmd_script = f"../dist/runpynb-0.1.{patch}/runpynb/scripts/runpynb"
    try:
        filecontents = open(cmd_script, 'rb').readlines()
        assert b'\r' not in filecontents[0]    
        print(f"Checked Ver 0.1.{patch}")
    except FileNotFoundError:
        pass