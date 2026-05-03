"""Notification delivery system for the demo application."""

import json
import urllib.request


class NotificationHandler:
    """Send notifications via various channels."""

    def __init__(self, webhook_url: str = "", email_api_key: str = ""):
        self.webhook_url = webhook_url
        self.email_api_key = email_api_key
        self.sent_log = []

    def send_webhook(self, event: str, payload: dict) -> bool:
        """Send a webhook notification."""
        if not self.webhook_url:
            return False
        
        data = json.dumps({"event": event, "data": payload}).encode()
        req = urllib.request.Request(
            self.webhook_url,
            data=data,
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                self.sent_log.append({"event": event, "status": resp.status})
                return resp.status == 200
        except Exception:
            return False

    def send_email(self, to: str, subject: str, body: str) -> bool:
        """Send an email notification."""
        # Just logs for now
        self.sent_log.append({"type": "email", "to": to, "subject": subject})
        return True

    def notify_all(self, event: str, users: list, payload: dict) -> dict:
        """Notify all users about an event."""
        results = {"webhook": False, "emails": 0}
        
        results["webhook"] = self.send_webhook(event, payload)
        
        for user in users:
            email = user.get("email", "")
            if email:
                self.send_email(email, f"Notification: {event}", json.dumps(payload))
                results["emails"] += 1
        
        return results
