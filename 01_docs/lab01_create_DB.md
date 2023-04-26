# ステップ１：DWHのテーブル作成

## このステップで行うこと

IoTのデータの最終的な格納先となるDWHのテーブルを作成します。

## 手順

### 画面を開く

トップページから、「Hue」をクリックして開きます。

![](screenshots_lab01/Hue_open.png "")

以下の画面で、管理者ユーザーのユーザー名とパスワードを設定します。（Hueでは、初回ログイン時に設定したユーザー名とパスワードが、そのまま管理者ユーザーのユーザー名とパスワードになります。）

ユーザー名、パスワードともに`admin`と入力し「アカウントを作成」をクリックします。
![Hue_1stLogin.png](screenshots_lab01%2FHue_1stLogin.png)

### impalaを選択

開いた画面の左上の </> マークから「impala」を選択します。

![](screenshots_lab01/select_impala.png "")

以下の赤枠の箇所が「impala」になっていることを確認します。
![](screenshots_lab01/impala_selected.png "")

### SQLの実行①（sensorsテーブルの作成）

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

基本編で使用するテーブルは以上です。

次は、[「ステップ２：スキーマレジストリの作成」](lab02_create_schema.md)に進みます。

早く終わった方は、応用編として、以下の手順も実施してみてください。

### （応用編）SQLの実行②（sensors_normal, sensors_abnormal テーブルの作成）

#### 実施すること

応用編では、さらに２つのテーブルを作成します。

先ほど作成した`sensors`と同じ構造で、以下のテーブルを作成します。

- sensors_normal
  - センサーのデータのうち、正常データのみを格納するためのテーブル


- sensors_abnormal
  - センサーのデータのうち、異常データのみを格納するためのテーブル

#### 実施内容

SQLの「CREATE TABLE」以下を sensors_normal, sensors_abnormal に変えて、それぞれ実行します。

![](screenshots_lab01/change_SQL.png "")

実行し終わったら、以下を確認します。

![](screenshots_lab01/SQL_confirm2.png "")

以上で、テーブルの作成は完了です。

次は、[「ステップ２：スキーマレジストリの作成」](lab02_create_schema.md)に進みます。

[>>トップページに戻る<<](lab00_top.md)