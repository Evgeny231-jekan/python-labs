import re

class InvalidHTMLImageError(Exception):
    pass

def is_html_image_tag(string):
    if not isinstance(string, str):
        return False
    pattern = r'^<img\s+[^>]*src=["\'][^"\']+["\'][^>]*\s*/?>$'
    return bool(re.match(pattern, string, re.IGNORECASE))

def validate_html_image_tag(string):
    if not isinstance(string, str):
        raise InvalidHTMLImageError("Аргумент должен быть строкой")
    if not string.strip():
        raise InvalidHTMLImageError("Строка не может быть пустой")
    if not is_html_image_tag(string):
        raise InvalidHTMLImageError(f"Некорректный HTML-тег изображения: {string}")
    return string

if __name__ == "__main__":
    print(is_html_image_tag('<img src="image.jpg">'))
    print(is_html_image_tag('<img src="photo.png" alt="text">'))
    print(is_html_image_tag('<img src="pic.gif" />'))
    print(is_html_image_tag('<div src="image.jpg">'))
    print(is_html_image_tag('img src="image.jpg"'))
    
    try:
        print(validate_html_image_tag('<img src="valid.jpg">'))
        print(validate_html_image_tag('invalid'))
    except InvalidHTMLImageError as e:
        print(e)
