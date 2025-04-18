# LINEWatcher ✨

LINE画像を「保存するだけ」で自動命名、自動移動。もうメンドくさい保存はさようなら！

---

## 🌐 Overview

LINEから保存された画像の…
- メチャメチャな名前
- 拡張子がない
- 同じ名前で上書きされる

🚫 そんなLINE画像保存のイライラをまるごと解決します！

---

## 🚀 Features

- 監視フォルダに画像が保存されると自動検出
- 日付+時間+3桁連番で自動命名 (ex: LINE_20250325_153245_001.jpg)
- 指定フォルダへ自動移動
- 拡張子なしのLINEファイルもJPEGとして処理
- Windows通知で保存完了を表示
- タスクトレイ常駐
- 起動時自動起動対応 (bat + vbs)

---

## 📁 How to Use

### 【初回】
1. `line_watcher_v7.py`を Python or exe で起動
2. 監視元と保存先をダイアログで指定
3. 自動リネーム開始!

### 【通常】
- LINEの画像を「名前を付けて保存」するだけ
- 同時にLINEWatcherが自動命名、移動、通知

---

## 💪 Startup Support (Optional)

1. `install_startup.bat`を実行すればPC起動時に自動起動
2. スタートアップを消すときは `remove_startup.bat`を実行

---

## 🔍 Sample Behavior

```
STEP 1: LINE画像を保存
STEP 2: 自動で保存先フォルダへ移動
STEP 3: リネーム＋保存完了通知
```

---

## 🛋️ Files

- `line_watcher_v7.py`	... メインスクリプト
- `linewatcher_icon.ico`	... exe化用アイコン
- `install_startup.bat`	... スタートアップ登録
- `remove_startup.bat`	... スタートアップ解除
- `create_shortcut.vbs`	... bat用ショートカット作成補助
- `README.txt`		... 導入手順まとめ（zip内）

---

## ⚠️ Notice

- 本ツールは無料・無保証です。自己責任でご利用ください。
- ご意見・不具合は GitHub Issues または note コメントへ

---

## 👤 Author

- 開発者：@mi-so-lawyer（[noteで記事も公開中](https://note.com/)）
- GitHub: [https://github.com/mi-so-lawyer/LINEWatcher](https://github.com/mi-so-lawyer/LINEWatcher)

---

## 🔄 License

MIT License

> 🆕 **2025年3月更新：PDF対応しました！**

拡張子が付かないLINE画像・PDFを、自動で正しくリネーム・整理するツールです。

✅ 画像もPDFも保存するだけで自動判別  
✅ 日時＋通し番号で命名して保存先へ移動  
✅ 拡張子のない画像でも自動で `.jpg` に変換  
✅ `.pdf` ファイルにも完全対応！（v1.1.0～）

> 🆕 **2025年4月更新：Word，Excel対応しました！**


📢 LINEWatcher v1.2.0 を公開しました！

✅ PDF・Word・Excel ファイルも中身で自動判定して正しい拡張子を付けて保存  
✅ `.docx`, `.xlsx`, `.pdf`, `.jpg`, `.png` に対応！  
✅ 保存するだけで自動リネーム → 自動移動 → 通知表示！



