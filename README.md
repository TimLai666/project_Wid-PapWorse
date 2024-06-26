# project Rid-PapWorse: 擺脫爛文書工作－文書工作資訊系統化計畫
### 此計畫旨在利用單一軟體紀錄文書內容，並可自動生成文書檔案，以取代繁雜、令人惱怒的文書工作。
#### 此計畫的軟體須符合下列條件：
- **輕量級**：免安裝、便攜且盡量跨平台。
- **內建資料庫**：內含獨立資料庫以紀錄文書內容，資料跟著程式走。
- **支援文字與照片**：同時支援文字與各種格式的照片資料。
- **可自訂模板**：可以自由調整輸出文件要包含的內容、樣式與排版。(或可利用現有文件作為模板)
- **輸出可編輯文件**：不只要可以輸出pdf，也要可以輸出像.doc這樣可以直接編輯的檔案。
- **自動更新**：可自動檢查並更新主程式（二進制執行檔），且不影響到現有資料。
- **不會遭誤報為病毒**：使用自然人憑證數位簽章。
#### 預計使用的技術：
- python eel (資料處理邏輯)
- html, css, javascript (gui)
- sqlite（資料庫）

## SwiftDocz
### Rid-PapWorse計畫的益思社實現
#### 大致邏輯：
- 社團資訊為一個class
- 每個class在資料庫中為一個表
- 用戶可新增或刪除「檔案總表」的檔案
- 「檔案總表」列出所有需要的檔案名稱，實際檔案內容可自動根據資料庫資料生成，或由用戶上傳檔案
- 用戶從檔案總表中拖拉到「檔案結構表」來組織評鑑檔案的資料夾結構
#### todo:
- 建立本屆檔案的頁面
- 編輯社團資訊的頁面
- 新增活動的頁面
- 管理活動的頁面&管理會議記錄的頁面(類似file manager)
- 組織「檔案總表」和「檔案結構表」的頁面
- 管理每個檔案的檔案內容的頁面（可選擇生成或上傳，類似學習歷程那樣）(UI完成)

### 進度指標
| 階段 | 目標 | 是否已達成 |
| ---- | ---- | --------- |
| 第一階段 | 由使用者提供檔案，可自動將檔案放到對應的目錄，並可由使用者自訂目錄結構 | 否 |
| 第二階段 | 將文書內容儲存在資料庫中，並可自動生成.pdf和.doc/.docx等可編輯檔 | 否 |
| 第三階段 | 可由使用者自訂生成文件的模板 | 否 |
| 第四階段 | 所有操作皆可透過圖形化介面進行，使用者無需具備相關技術知識 | 否 |
| 第五階段 | 可靠且不會影響使用者資料的自動更新機制 | 否 |
