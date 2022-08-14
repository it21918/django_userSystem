# Clone and run project
```bash
git clone https://github.com/it21918/django_userSystem.git
python -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cd userSystem
cp userSystem/.env.example userSystem/.env
```
edit userSystem/.env file to define
```vim
SECRET_KEY='test123'
DATABASE_URL=postgres://myprojectuser:password@localhost:/myproject
```
# run development server
```bash
python manage.py runserver
```
