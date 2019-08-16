def say_hello(language):
    language = language.lower()

    def hello_in_language():
        if language == 'english':
            return 'Hello'
        elif language == 'chinese':
            return '你好'
        elif language == 'spanish':
            return 'Hola'
        elif language == 'italian':
            return 'Salve'
        elif language == 'french':
            return 'Bonjour'
        elif language == 'hindi':
            return 'नमस्ते'
        elif language == 'thai':
            return 'สวัสดีครับ' # male version

    print(hello_in_language())