from conditions.conditions import conditions

def checkConditions(plugin: dict) -> bool:
    for condition in conditions:
        for key in condition:
            if plugin[key] != condition [key]:
                return False
    return True