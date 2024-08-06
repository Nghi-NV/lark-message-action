#!/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import json
import argparse

def build_card_message(args):
    elements = [
        {
            "tag": "column_set",
            "flex_mode": "none",
            "background_style": "default",
            "columns": [
                {
                    "tag": "column",
                    "width": "weighted",
                    "weight": 1,
                    "vertical_aign": "top",
                    "elements": [
                        {
                            "tag": "div",
                            "text": {
                                "content": args.content,
                                "tag": "lark_md"
                            }
                        }
                    ]
                }
            ]
        }
    ]

    message_card = {
        "msg_type": "interactive",
        "card": {
            "config": {
                "wide_screen_mode": False
            },
            "header": {
                "title": {
                    "tag": "plain_text",
                    "content": args.title
                },
                "template": args.header_color
            },
            "elements": elements
        }
    }

    message_card_json = json.dumps(message_card, indent=4, ensure_ascii=False)
    return message_card_json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Notify Lark')
    parser.add_argument('--title', type=str, help='Title', required=True)
    parser.add_argument('--content', type=str, help='Content', required=True)
    parser.add_argument('--header-color', type=str, help='Header color', default="green")
    parser.add_argument('--lark-bot-notify-webhook', type=str, help='Lark webhook', required=True)
    args = parser.parse_args()

    message = build_card_message(args)
    print("Notify message: ", message)
    subprocess.run(["curl", "-X", "POST", "-H", "Content-Type: application/json", "-d", message, args.lark_bot_notify_webhook], check=True)
    print("Notify message sent succeed")