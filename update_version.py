import json


def get_prop(path):
    props = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and "=" in line:
                key, val = line.split("=", 1)
                props[key.strip()] = val.strip()
    return props


def increment_version(props):
    number = props["version"].lstrip("v")
    part = number.split(".")
    part[-1] = str(int(part[-1]) + 1)
    props["version"] = "v" + ".".join(part)
    props["versionCode"] = str(int(props["versionCode"]) + 1)
    return props


def save_props(path, props):
    with open(path, "w", encoding="utf-8") as f:
        for key, val in props.items():
            f.write(f"{key}={val}\n")


def get_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


props = get_prop("module/module.prop")
print(f"before:  {props['version']} (code: {props['versionCode']})")

props = increment_version(props)
print(f"after: {props['version']} (code: {props['versionCode']})")

save_props("module/module.prop", props)

update = get_json("module/update.json")
update["version"] = props["version"]
update["versionCode"] = int(props["versionCode"])
save_json("module/update.json", update)
