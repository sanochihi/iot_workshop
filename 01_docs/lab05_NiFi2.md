# ステップ５：NiFiの準備②

## このステップで行うこと

これまでのステップで、端末とサーバー間でのデータ授受の仕組みが整いました。

このステップでは、端末から受信したデータをDWHに格納する流れを作ります。

## 手順

### 画面を開く

トップページから、「NiFi」をクリックして開きます。

![open_NiFi.png](screenshots_lab05%2Fopen_NiFi.png)

### スキーマ名の設定

#### プロセッサーの作成（Update Attribute）

画面左上から、プロセッサーのアイコンを選択し、インプットポート（[ステップ３](lab03_NiFi1.md)の手順(3)で作成したもの）の下あたりにドラッグ＆ドロップします。

![drug1.png](screenshots_lab05%2Fdrug1.png)

すると、プロセッサーの種類を選択する画面が起動します。<br>
右上の検索窓に`updatea`まで入力すると、「UpdateAttribute」が絞り込み表示されますので、この状態で「ADD」をクリックします。

![updateAttribute.png](screenshots_lab05%2FupdateAttribute.png)

#### プロセッサーの名称設定

今作成したプロセッサをダブルクリックし、出てきた画面の「Name」欄に「スキーマ名を設定」と入力します。

![setname.png](screenshots_lab05%2Fsetname.png)

#### プロセッサーの詳細設定

PROPERTIES タブを選択し、右側の＋マークをクリックします。<br>
出てきた画面の「Property Name」に`schema.name`と入力し「OK」をクリックします。
![properties.png](screenshots_lab05%2Fproperties.png)

さらに入力欄が表示されるので、`SensorData`と入力し「OK」をクリックします。
![SensorData.png](screenshots_lab05%2FSensorData.png)

以下のポイントを確認し、「APPLY」をクリックします。<br>
※「スキーマレジストリの名称」は、[ステップ２](lab02_create_schema.md)で作成したスキーマの名称のことです。
![confirm.png](screenshots_lab05%2Fconfirm.png)

#### ポートとプロセッサの接続

「端末データ取得」のポートと、今作成した「スキーマ名を設定」のプロセッサを、以下のようにドラッグ＆ドロップしてつなぎます。

![drug_edit.gif](screenshots_lab05%2Fdrug_edit.gif)

出てきた画面の「ADD」をクリックします。

![add.png](screenshots_lab05%2Fadd.png)

### 用語説明

今の手順で実施したように、NiFi上の各要素（プロセッサーやポートなど）を接続する矢印のことを、「リレーション」といいます。

![relation.png](screenshots_lab05%2Frelation.png)

### データベースへの書き込み

#### プロセッサーの作成（putKudu）

画面左上から、プロセッサーのアイコンを選択し、先ほど作成した「スキーマ名を設定」の下あたりにドラッグ＆ドロップします。



すると、プロセッサーの種類を選択する画面が起動します。<br>
右上の検索窓に`putku`まで入力すると、「putKudu」が絞り込み表示されますので、この状態で「ADD」をクリックします。
![putkudu.png](screenshots_lab05%2Fputkudu.png)

#### プロセッサーの名称設定

今作成したプロセッサをダブルクリックし、出てきた画面の「Name」欄に「スキーマ名を設定」と入力します。

![setname.png](screenshots_lab05%2Fsetname.png)

#### プロセッサーの詳細設定

PROPERTIES タブを選択し、右側の＋マークをクリックします。<br>
出てきた画面の「Property Name」に`schema.name`と入力し「OK」をクリックします。
![properties.png](screenshots_lab05%2Fproperties.png)

さらに入力欄が表示されるので、`SensorData`と入力し「OK」をクリックします。
![SensorData.png](screenshots_lab05%2FSensorData.png)

以下のポイントを確認し、「APPLY」をクリックします。<br>
※「スキーマレジストリの名称」は、[ステップ２](lab02_create_schema.md)で作成したスキーマの名称のことです。
![confirm.png](screenshots_lab05%2Fconfirm.png)

#### リレーションの設定

「端末データ取得」のポートと、今作成した「スキーマ名を設定」のプロセッサを、以下のようにドラッグ＆ドロップしてつなぎます。

![drug_edit.gif](screenshots_lab05%2Fdrug_edit.gif)


以上で、NiFiの準備②は完了です。あともう一息です！

次は、[lab06_query_DB.md](lab06_query_DB.md)に進みます。

[>>トップページに戻る<<](lab00_top.md)