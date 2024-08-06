
# lark-message-action
Github action that send message to Lark

# Inputs

## ``lark-bot-notify-webhook``
Required: **YES**.  

Lark Bot Notify Webhook

## ``lark-signature-verification``
Required: **No**.  

Lark signature verification

## ``title``
Required: **YES**.  

Notify title

## ``content``
Required: **YES**.  

Notify content

## ``header-color``
Required: **No**.  
Default: **green**

Notify header color


# Usage Example

## Simple Workflow

```yaml
# .github/workflows/main.yml
name: Main
on: [push]

jobs:
  my_job:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Upload to Next Cloud
        uses: Nghi-NV/lark-message-action@v1
        with:
          title: "Notification"
          content: "Hello"
          header-color: "red"
          lark-bot-notify-webhook: ${{ secrets.LARK_BOT_NOTIFY_WEBHOOK }}
          lark-signature-verification: ${{ secrets.LARK_BOT_SIGNATURE_VERIFICATION }}
          
```