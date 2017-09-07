# frame-level-music-tagging-dataset
Collection of 100 mp3 chinese pop song from youtube and frame-level labeled tag

此為台灣科技部計畫相關專案  
計劃網站：  
http://music-tech.cs.nthu.edu.tw/

## 說明
現行音樂標註資訊之資料庫多收錄西洋流行音樂、古典音樂為主，少有東亞、中文流行音樂。  
故本團隊於計劃中建構一中文流行音樂資料庫，除了包含歌曲本身之標記外且包含聽者之即時生理訊號，供國內外學者研究中文流行音樂使用。  

## 資料庫建構計劃
分為三階段，逐年擴增：
1. 蒐集100首中文流行歌，進行音樂資訊加註及生理訊號測量，確立資料庫雛形
2. 加大資料規模與試驗規模
3. 完善相關分析工具、方法、以及加註之資訊

## 如何使用
請安裝python3及套件mutagen、youtube_dl  
```pip install mutagen youtube_dl```

### 1.下載音樂mp3  
```python mp3/download_by_list.py```

### 2.取得音樂長度  
```python meta_data/music_length.py```

### 3.將tag縮放至適合分析的frame size，產生資料集  
```python meta_data/sparse_to_dense.py```

資料生成在csv資料夾中  
