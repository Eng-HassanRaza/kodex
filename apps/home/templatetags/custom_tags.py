from django import template

register = template.Library()


def layer_color(value):
    # if arg is first_name: return the first string before space
    if value < 10 :
        return "green"
    # if arg is last_name: return the last string before space
    if value >=10 and value < 20:
        return "yellow"
    # if arg is title_case: return the title case of the string
    if value > 19:
        return "red"
    return value


def layer_icon(value):
    # if arg is first_name: return the first string before space
    if value < 10 :
        return "bi bi-emoji-smile"
    # if arg is last_name: return the last string before space
    if value >=10 and value < 20:
        return "bi bi-emoji-neutral"
    # if arg is title_case: return the title case of the string
    if value > 19:
        return "bi bi-emoji-angry"
    return value


register.filter('layer_color', layer_color)
register.filter('layer_icon', layer_icon)