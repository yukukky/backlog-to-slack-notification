# backlog-to-slack-notification
## About
Notification script from backlog to slack.

Convert backlog mentions to slack mentions.

Backlogの通知をSlackへ送る。

BacklogのメンションをSlackのメンションへ変換。
## For User(EN)
1. Add Incoming Webhook at Slack Channel.
1. Change mention_list.json.
    1. add Nulab unique ID. (see https://apps.nulab.com/profile/account)
    1. add Slack Member ID.
1. deploy GCP Cloud Function.
    1. set trigger type `HTTP`.
    1. Set the environment variable `SLACK_WEBHOOK_URL` to the Incoming Webhook URL.
    1. Set the environment variable `BACKLOG_ORG_URL` to the backlog organization URL.
    1. deploy main.py, mention_list.json, requirements.txt
1. Set Backlog Workspace Webhook.
    1. set GCP Cloud Functions URL.
      (https://support.backlog.com/hc/en-us/articles/115015420967-Webhooks)

## For User(JP)
1. Incoming WebhookをSlackに追加し、Webhook URLを取得
1. mention_list.jsonを書き換える
    1. NulabユニークIDを追加 https://apps.nulab.com/profile/account
    1. Slack Member IDを追加
1. GCPのCloud Functionsにデプロイ（Python3.9）
    1. トリガーのタイプはHTTP
    1. 環境変数 `SLACK_WEBHOOK_URL` にIncoming Webhook URLをセット
    1. 環境変数 `BACKLOG_ORG_URL` 組織URLをセット
    1. main.py, mention_list.json, requirements.txtをデプロイ
1. プロジェクト設定＞インテグレーション＞Webhookを設定
    1. WebHook URLにCloud Functionsで発行されたURLをセット
      (https://support-ja.backlog.com/hc/ja/articles/360036147713-Webhook)



## For Developer
1. install pipenv
2. exec 'pipen install --dev'
