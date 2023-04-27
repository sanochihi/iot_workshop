# ステップ１：DWHのテーブル作成

## このステップで行うこと

データの最終的な格納先となる、DWHのテーブルを作成します。

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

以下のSQL を入力し、実行します。（コピー用のSQLが画像の下にあります）

![](screenshots_lab01/SQL.png "")

↓コピー用SQL↓
```commandline
CREATE TABLE sensors

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

次は、[「ステップ２：スキーマレジストリの作成」](lab02_create_schema.md)に進みます。

[>>トップページに戻る<<](00_top.md)