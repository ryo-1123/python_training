# python_training
Python : TODOアプリ作成
 - Trello風学習サポートアプリ
   - 目標の登録
   - 目標にリンクした行動目標の登録
   - 目標・行動目標の一覧表示
   - 目標・行動目標の編集
   - 各目標の学習時間の統計表示
 - コードの実行手順
   - 仮想環境の作成
   `python3 -m venv vnev`
   - 仮想環境の有効化
   `source venv/bin/activate`
   - Djangoのインストール
   `pip install -U Django==2.2.* django-debug-toolbar`
   - アプリのClone
   `git clone https://github.com/ryo-1123/python_training.git`
   - アプリの立ち上げ
   `python manage.py runserver`
 - 実行に必要な環境
   - Python 3.6.*
   - Django 2以上