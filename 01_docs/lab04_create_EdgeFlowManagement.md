# ステップ４：端末からのデータ送信の仕組みを作る

## このステップで行うこと

今までの手順では、中央のサーバーで管理対象の端末データを受信する準備をしてきました。

今度は、管理対象の端末側に配布するプログラムを作っていきます。

![edge_NiFi.png](screenshots_lab04%2Fedge_NiFi.png)

## 手順

### 画面を開く

トップページから、「Edge Flow Manager」をクリックして開きます。

![open_efm.png](screenshots_lab04%2Fopen_efm.png)

出てきた画面で、左側の田の字のようなマークをクリックします。「iot-1」というクラスが既に作成されているので、選択し、「OPEN」をクリックします。

![open.png](screenshots_lab04%2Fopen.png)

### 端末とNiFiを接続する

ハンズオンでは以下のとおり、端末で発生するMQTTを取得するプロセッサーと、その情報を指定したIPアドレスに飛ばすためのリモートプロセスグループを講師側で事前に作成してあります。
![ready_made.png](screenshots_lab04%2Fready_made.png)

上記のプロセッサーとリモートプロセスグループを接続してみましょう。

Consume MQTT プロセッサーにカーソルを当てると、以下のように→が表示されます。
その状態で→部分をクリックし、リモートプロセスグループ（雲のマーク）までドラッグ＆ドロップします。

![drug_relation1.png](screenshots_lab04%2Fdrug_relation1.png)


以下の画面が表示されますので、[ステップ３](lab03_NiFi1.md)の手順(3)でコピーしておいたポートのIDをペーストし「CREATE」をクリックします。
![setId.png](screenshots_lab04%2FsetId.png)

今追加されたリレーションの真ん中の四角をダブルクリックし、設定画面を開きます。<br>
FLOWFILE EXPIRATION を 60 seconds に設定し、「APPLY」をクリックします。
![configure_relation.png](screenshots_lab04%2Fconfigure_relation.png)

以上で、フローの作成は完了です。次は、作成したフローを公開します。

### フローを公開する

画面右上の「ACTIONS」をクリックし、配下の「Publish」を選択します。

![publish.png](screenshots_lab04%2Fpublish.png)

以下の画面が表示されるので、「PUBLISH」をクリックします。
![publish2.png](screenshots_lab04%2Fpublish2.png)

以上で、端末からのデータ送信の仕組み作りは完了です。
次は、[「ステップ５：NiFiの準備②」](lab05_NiFi2.md)に進みます。

[>>トップページに戻る<<](lab00_top.md)