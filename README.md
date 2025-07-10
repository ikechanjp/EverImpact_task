# EverImpact – メンバー進捗レポート

ブラウザだけで動く **HTML + JavaScript + Tailwind CSS** 製のタスク管理ダッシュボードです。メンバーごとのコース作成進捗をネオン調 UI で可視化します。

---

## 🚀 はじめかた

1. 本リポジトリを **クローン / ダウンロード** し、`index.html` をブラウザで開きます。  
   ビルド不要・インターネット接続も不要です。
2. ネオングラデーションとタイトルが表示されたら準備完了です。

---

## 👤 ユーザー登録・切替

1. `あなたの名前` フィールドに任意の名前を入力。
2. **スタート** をクリックすると新しいユーザープロファイルが作成され、タスクが複製されます（`localStorage` に保存）。
3. 既存ユーザーはフォーム下のチップに表示されます。クリックで切替え。
4. 進捗を **削除** したい場合は、同じ入力欄に対象の名前を入力して **削除** ボタンを押してください。

---

## 📋 タスク操作

・カード右上の ▾ で展開／折りたたみ。  
・チェックボックスでタスク／サブタスクを完了・未完了に切替。  
・サブタスクがすべて完了すると親タスクも自動で完了になります。

操作は即時 `localStorage` に保存されます。

---

## 👥 メンバー一覧

1. ヘッダーの **メンバー** ボタンで一覧を表示／非表示。  
2. 全メンバーを完了率順で表示し、ネオンイエローのバーで進捗を可視化します。

---

## 💾 データ保存仕様

| キー | 内容 |
| --- | --- |
| `users` | 登録ユーザー名の配列 |
| `tasks_<ユーザー名>` | 各ユーザーのタスク状態（JSON 文字列） |

ブラウザのストレージをクリア、または **削除** ボタンで個別リセット可能です。

---

## 🎨 カスタマイズ

* `index.html` 内の `getInitialProjectPlan()` を編集してタスクやアイコンを変更できます。
* Tailwind に以下のネオンパレットを追加済み:
  * `neon-pink`, `neon-blue`, `neon-purple`, `neon-yellow`

---

## 🛠 開発メモ

* 依存ライブラリは Tailwind と Lucide の CDN のみ。
* 主要ブラウザ（Chrome / Edge 最新版）で動作確認済み。
* フォークしてご自由に改造してください！


A lightweight, **pure HTML + JavaScript + Tailwind CSS** dashboard for tracking course-creation progress across multiple members.

---

## 🚀 Getting Started

1. **Clone or download** this repository and open `index.html` in your browser.  
   (No build step – runs locally out of the box.)
2. You’ll see a neon-gradient background and a title.

---

## 👤 ユーザー登録 / Switching Users

1. Enter your name in the field labelled `あなたの名前`.
2. Click **スタート**.  
   • A new user profile is created (saved in `localStorage`).  
   • The default project plan is duplicated for this user.
3. Existing usernames are shown as chips under the form. Click a chip to switch.
4. To **delete** a user and all its progress, type the exact name in the input and press **削除**.

---

## 📋 タスク管理

Each card represents a major task; click the chevron (▾) to expand/collapse.

• Check or un-check a task box to mark it complete/active.  
• Expanded cards show subtasks with individual checkboxes.  
• Subtask completion automatically updates the parent task’s status.

Progress is saved instantly to `localStorage`.

---

## 👥 メンバー進捗一覧

• Click **メンバー** in the header to toggle the members section.  
• All registered users are displayed, sorted by completion percentage.  
• Neon-yellow horizontal bars visualize progress.  
• Click **メンバー** again to hide the list.

---

## 💾 Data Persistence

Data lives entirely in the browser:

| Key | Purpose |
| --- | --- |
| `users` | Array of registered usernames |
| `tasks_<username>` | Serialized task array for the user |

Clearing browser storage or using **削除** removes data.

---

## 🎨 Customization

* Edit `getInitialProjectPlan()` in `index.html` to change tasks / icons.
* Tailwind palette extended with:
  * `neon-pink`, `neon-blue`, `neon-purple`, `neon-yellow`.
* Modify styles directly in markup or via Tailwind config.

---

## 🛠 Development Notes

* No frameworks, bundlers, or dependencies other than Tailwind & Lucide CDN.
* Tested on latest Chrome / Edge.
* Feel free to fork and adapt!


