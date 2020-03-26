import soloutils


def controller_versions__monkey_patch(controller):
    code, controller_str, stderr = soloutils.command(controller, 'cat /VERSION')
    # Have to add two unpacking variables and split on newline,
    # as the `/VERSION` file now contains 4 lines instead of one line with 2 tokens separated by a space
    version, ref, _name, _ = controller_str.strip().split('\n')
    return {
        "version": version,
        "ref":     ref,
    }


def solo_versions__monkey_patch(solo):
    code, solo_str, stderr = soloutils.command(solo, 'cat /VERSION')
    # ^ Same as comment above ^
    version, ref, _name, _ = solo_str.strip().split('\n')
    return {
        "version": version,
        "ref":     ref,
    }


soloutils.controller_versions = controller_versions__monkey_patch
soloutils.solo_versions = solo_versions__monkey_patch

if __name__ == "__main__":
    soloutils.wifi.main({"--name": "REPLACE WITH WIFI SSID", "--password": "REPLACE WITH WIFI PASSWORD"})
