# ステップ１：DWHのテーブル作成

## このステップで行うこと

IoTのデータの最終的な格納先となるDWHのテーブルを作成します。

テーブルは全部で３つ、以下のものを作成します。

- sensors
  - センサーのデータを全件格納するためのテーブル


- sensors_normal
  - センサーのデータのうち、正常データのみを格納するためのテーブル


- sensors_abnormal
  - センサーのデータのうち、異常データのみを格納するためのテーブル


３つのテーブルは、すべて同じ形式（カラム）で作成します。

## 手順

### 画面を開く

トップページから、「Hue」をクリックして開きます。

![](screenshots_lab01/Hue_open.png "")

### impalaを選択

開いた画面の左上の </> マークから「impala」を選択します。

![](screenshots_lab01/select_impala.png "")

以下の赤枠の箇所が「impala」になっていることを確認します。
![](screenshots_lab01/impala_selected.png "")

### SQLの実行（sensorsテーブルの作成）

以下のSQL を入力し、実行します。

![](screenshots_lab01/SQL.png "")

↓コピペ用SQL↓
```commandline
CREATE TABLE sensors
-- CREATE TABLE sensors_normal
-- CREATE TABLE sensors_abnormal
(
 lot_no STRING,
 date_time STRING,
 door_closed SMALLINT,
 hp_temperature STRING,
 PRIMARY KEY (lot_no, date_time)
)
PARTITION BY HASH PARTITIONS 16
STORED AS KUDU
TBLPROPERTIES ('kudu.num_tablet_replicas' = '1');

```

実行したら、以下のポイントを確認します。

![](screenshots_lab01/SQL_confirm.png "")

以上で、３つのテーブルのうち「sensors」（全件格納用テーブル）が作成できました。

### SQLの実行（sensors_normal, sensors_abnormal テーブルの作成）

次は、同じ構造でさらに２つのテーブルを作成します。
SQLの「CREATE TABLE」以下を sensors_normal, sensors_abnormal に変えて、それぞれ実行します。

![](screenshots_lab01/change_SQL.png "")

実行し終わったら、以下を確認します。

![](screenshots_lab01/SQL_confirm2.png "")

以上で、テーブルの作成は完了です。
次は、[ステップ２：スキーマレジストリの作成](lab02_create_schema.md)に進みます。