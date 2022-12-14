## 运行示例代码
首先确保你的电脑已经安装 Python 3.8 、npm 6.14 或以上的版本。

下载项目后，修改配置文件 `drf_vue_blog/settings.py` ：

```python
# drf_vue_blog/settings.py

...
# 修改为 True
DEBUG = True
...
```

在 **PowerShell 命令行**中进入项目目录，并创建**虚拟环境**：

```bash
python -m venv venv
```

> 若上述方法不成功，则可以通过 `virtualenv` 库创建虚拟环境，效果相同。具体方法请搜索。

运行**虚拟环境**（Windows环境）:

```bash
venv\Scripts\activate.bat
```

或（Linux环境）：

```bash
source venv/bin/activate
```

自动安装所有依赖项：

```bash
pip install -r requirements.txt
```

然后进行数据迁移：

```bash
python manage.py migrate
```

运行后端服务器：
```bash
python manage.py runserver
```

新创建一个 PowerShell 命令行窗口，进入项目的 `frontend/` 目录，安装前端依赖项：

```bash
npm install
```

运行前端服务器：

```bash
npm run serve
```

至此前后端开发服务器就都启动了。

浏览器中输入地址 `http://localhost:8080/` 访问博客界面，输入 `http://127.0.0.1:8000/api/` 访问接口数据。

数据库文件 `db.sqlite3` 以及媒体文件夹 `media` 中的内容是方便读者查看示例效果而存在的。

管理员账号：dusai  密码：admin123456

如果你想清除所有数据及媒体文件，将它们直接删除，并运行：

```bash
python manage.py createsuperuser
```

即可重新创建管理员账号。
