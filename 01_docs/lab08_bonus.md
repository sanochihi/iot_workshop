# ステップ８（応用）：データの振り分け

## このステップで行うこと

ここから先は、ステップ７までが早く終わった方向けの応用編です。<br>

現在、`sensors` テーブルには、端末のデータが全件入ってきます。

応用編では、正常データのみを格納するテーブル`sensors_normal`と、異常データのみを格納するテーブル`sensors_abnormal`を作成し、温度によってデータの格納先を振り分けます。

## 手順

以下の手順で行います。

(1) テーブルの作成（正常のみ／異常のみデータ格納用）<br>
(2) DB格納処理の追加<br>
(3) コントローラーサービスの追加<br>
(4) 振り分け処理の追加<br>
(5) NiFiの実行・確認

### (1) テーブルの作成（正常のみ／異常のみデータ格納用）

基本編で作成した`sensors`と同じ構造で、以下のテーブルを作成します。

- sensors_normal
  - センサーのデータのうち、正常データのみを格納するためのテーブル

- sensors_abnormal
  - センサーのデータのうち、異常データのみを格納するためのテーブル

#### 実施内容

[手順１](lab01_create_DB.md)と同じ要領で、 SQLの「CREATE TABLE」以下を sensors_normal, sensors_abnormal に変えて、それぞれ実行します。

![](screenshots_lab08/change_SQL.png "")

実行し終わったら、以下を確認します。

![](screenshots_lab08/SQL_confirm.png "")

以上で、テーブルの作成は完了です。

### (2) DB格納処理の追加

手順(1)で作成したテーブルに、データを追加するプロセッサーを追加します。

#### 実施内容

NiFi の画面を開き、「サーバー処理」のプロセッサーグループの中に入ります。



### コントローラーサービスの追加

NiFi のコントローラーサービスに、JsonRocordSetWriterを追加します。<br>
これは、後の手順で作成する振り分け処理を行う際に、振り分けたデータをスキーマに従って書き込みできるようにするためのものです。

#### 実施内容

##### 設定画面を開く

[ステップ３の手順(1)「設定画面を開く」](https://github.com/sanochihi/iot_workshop/blob/main/01_docs/lab03_NiFi1.md#%E8%A8%AD%E5%AE%9A%E7%94%BB%E9%9D%A2%E3%82%92%E9%96%8B%E3%81%8F)を参考に、NiFi のコントローラーサービスの設定画面を開きます。

##### サービス追加・プロパティ設定

画面右側の「＋」マークをクリックし、出てきた画面の検索窓に「json」と入力します。<br>
いくつかのサービスが表示される中から、「JsonTreeReader」を選択します。
![JsonRecordSetWriter.png](screenshots_lab03%2FJsonRecordSetWriter.png)

画面右側の歯車のマークをクリックし、出てきた画面の「PROPERTIES」タブを以下の要領で設定します。

設定内容：　※前の手順と同様、入力欄をダブルクリックすると選択肢のリストが出てきます
- Schema Write Strategy
  - HWX Schema Reference Attributes
- Schema Access Strategy
  - Use 'Schema Name' Property
- Schema Registry
  - HortonworksSchemaRegistry

![SetWriter_settings.png](screenshots_lab03%2FSetWriter_settings.png)

選択できたら、「APPLY」をクリックします。

##### 有効化

いま作成したJsonRecordSetWriterのサービスを有効化します。<br>
（手順はHortonworksSchemaRegistryを作成した際の「有効化」の手順を参照）

以下のように、表の「State」が「Enabled」になっていれば完了です。
![enabled_setwriter.png](screenshots_lab03%2Fenabled_setwriter.png)


### 振り分け処理の追加



以上で、応用編も完了です。おつかれさまでした！

さらに詳しく知りたいことがありましたら、ご遠慮なく講師にご質問ください。

[>>トップページに戻る<<](00_top.md)