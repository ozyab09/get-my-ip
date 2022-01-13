## Sending your current IP address to your Telegram account 

Sending works only on first start and when your external IP will change.

# Run with docker

```bash
docker run -d \
    --restart=always \
    -e TELEGRAM_ID='your_telegram_id'\
    -e BOT_TOKEN='your_bot_token' \
    ozayb/get-my-ip
```
