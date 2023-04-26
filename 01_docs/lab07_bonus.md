# ステップ７（応用）：データの振り分け

## このステップで行うこと

ここから先は、ステップ６までが早く終わった方向けの応用編です。<br>

現在、`sensors` テーブルには、端末のデータが全件入ってきます。

応用編では、正常データのみを格納するテーブル`sensors_normal`と、異常データのみを格納するテーブル`sensors_abnormal`を作成し、温度によってデータの格納先を振り分けます。

## 手順

### 画面を開く




### JsonRecordSetWriter の設定

#### サービス追加・プロパティ設定

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

#### 有効化

いま作成したJsonRecordSetWriterのサービスを有効化します。<br>
（手順はHortonworksSchemaRegistryを作成した際の「有効化」の手順を参照）

以下のように、表の「State」が「Enabled」になっていれば完了です。
![enabled_setwriter.png](screenshots_lab03%2Fenabled_setwriter.png)


以上で、応用編も完了です。おつかれさまでした！

さらに詳しく知りたいことがありましたら、ご遠慮なく講師にご質問ください。

[>>トップページに戻る<<](lab00_top.md)