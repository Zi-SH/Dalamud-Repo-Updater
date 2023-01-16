from conditions.conditions import conditions

def checkConditions(plugin: dict) -> bool:
    if len(conditions) >= 1:
        for condition in conditions:
            for key in condition:
                if plugin[key] != condition [key]:
                    return False
        return True
    return True