import eel
eel.init('UI')  # 假设您的HTML/CSS/JavaScript文件都放在`web`目录下

@eel.expose  # 暴露Python函数给JavaScript
def greet_python(name):
    return f"Hello, {name}!"

eel.start('main.html', size=(1920, 1080), port=5349)  # 启动应用，打开`main.html`