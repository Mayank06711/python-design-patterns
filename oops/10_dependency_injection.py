"""
================================================================================
EXERCISE 10 — Dependency Injection (Notification System)
================================================================================
Build a notification system where the service doesn't know HOW notifications
are sent — it just knows they CAN be sent.

YOUR TASK:
1. Create NotificationChannel ABC with abstract method `send(recipient: str, message: str) -> str`
   - send() returns a confirmation string (format specified per channel below)
2. Create EmailChannel(NotificationChannel) — send returns "Email to {recipient}: {message}"
3. Create SMSChannel(NotificationChannel) — send returns "SMS to {recipient}: {message}"
4. Create PushChannel(NotificationChannel) — send returns "Push to {recipient}: {message}"
5. Create NotificationService class:
   - __init__(self, channels: list[NotificationChannel]) — receives channels via DI
   - notify(recipient: str, message: str) -> list[str] — sends via ALL channels, returns list of confirmations
   - add_channel(channel: NotificationChannel) — add a new channel at runtime
   - remove_channel(channel_type: type) — remove all channels of a given type
     (e.g., remove_channel(SMSChannel) removes all SMS channels)

RULES:
- NotificationService must NEVER import or create channel objects itself
- All channels are INJECTED from outside
- Adding a new channel type (e.g., WhatsApp) should require ZERO changes to NotificationService

Run this file to test:  python 10_dependency_injection.py
================================================================================
"""
from abc import ABC, abstractmethod
from typing import List
# ── YOUR CODE BELOW ──────────────────────────────────────────────────────────
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str)->str:
        pass

class EmailChannel(NotificationChannel):
    def send(self, recipient:str, message:str)->str:
        return f"Email to {recipient}: {message}"

class SMSChannel(NotificationChannel):
    def send(self, recipient:str, message:str)->str:
        return f"SMS to {recipient}: {message}"

class PushChannel(NotificationChannel):
    def send(self, recipient:str, message:str)->str:
        return f"Push to {recipient}: {message}"

class NotificationService:
    def __init__(self, channel_list: List[NotificationChannel]):
        self.channel_list = channel_list
    
    def  notify(self, recipient: str, message: str)->List[str]:
        confirmation = []
        for channel in self.channel_list:
            confirmation.append(channel.send(recipient, message))
        return confirmation
    
    def add_channel(self, channel: NotificationChannel):
        self.channel_list.append(channel)

    def remove_channel(self, channel_type):
        self.channel_list[:] = [
            channel for channel in self.channel_list
            if not isinstance(channel, channel_type)
        ]

# ── YOUR CODE ABOVE ──────────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════════════════════════════
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ══════════════════════════════════════════════════════════════════════════════

def run_tests():
    passed = 0
    failed = 0

    # Test 1: Single channel (Email only)
    try:
        service = NotificationService([EmailChannel()])
        results = service.notify("alice@test.com", "Hello!")
        assert results == ["Email to alice@test.com: Hello!"], f"Got {results}"
        print("  [PASS] Test 1: Single email channel works")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 1: Single channel — {e}")
        failed += 1

    # Test 2: Multiple channels
    try:
        service = NotificationService([EmailChannel(), SMSChannel(), PushChannel()])
        results = service.notify("bob", "Welcome!")
        expected = [
            "Email to bob: Welcome!",
            "SMS to bob: Welcome!",
            "Push to bob: Welcome!",
        ]
        assert results == expected, f"Got {results}"
        print("  [PASS] Test 2: All three channels fire")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 2: Multiple channels — {e}")
        failed += 1

    # Test 3: Add channel at runtime
    try:
        service = NotificationService([EmailChannel()])
        service.add_channel(SMSChannel())
        results = service.notify("charlie", "Hi!")
        expected = ["Email to charlie: Hi!", "SMS to charlie: Hi!"]
        assert results == expected, f"Got {results}"
        print("  [PASS] Test 3: Channel added at runtime")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 3: Add channel — {e}")
        failed += 1

    # Test 4: Remove channel by type
    try:
        service = NotificationService([EmailChannel(), SMSChannel(), PushChannel()])
        service.remove_channel(SMSChannel)
        results = service.notify("dave", "Bye!")
        expected = ["Email to dave: Bye!", "Push to dave: Bye!"]
        assert results == expected, f"Got {results}"
        print("  [PASS] Test 4: SMS channel removed by type")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 4: Remove channel — {e}")
        failed += 1

    # Test 5: No channels = empty results (no crash)
    try:
        service = NotificationService([])
        results = service.notify("nobody", "Hello?")
        assert results == [], f"Expected [] but got {results}"
        print("  [PASS] Test 5: No channels = empty list (no crash)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 5: No channels — {e}")
        failed += 1

    # Test 6: New channel type WITHOUT changing NotificationService
    try:
        class WhatsAppChannel(NotificationChannel):
            def send(self, recipient: str, message: str) -> str:
                return f"WhatsApp to {recipient}: {message}"

        service = NotificationService([WhatsAppChannel(), EmailChannel()])
        results = service.notify("eve", "New channel!")
        expected = ["WhatsApp to eve: New channel!", "Email to eve: New channel!"]
        assert results == expected, f"Got {results}"
        print("  [PASS] Test 6: New WhatsApp channel works (zero changes to service)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 6: New channel type — {e}")
        failed += 1

    # Test 7: Each channel is a NotificationChannel instance
    try:
        e = EmailChannel()
        s = SMSChannel()
        p = PushChannel()
        assert isinstance(e, NotificationChannel), "EmailChannel must be a NotificationChannel"
        assert isinstance(s, NotificationChannel), "SMSChannel must be a NotificationChannel"
        assert isinstance(p, NotificationChannel), "PushChannel must be a NotificationChannel"
        print("  [PASS] Test 7: All channels are NotificationChannel instances")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 7: isinstance check — {e}")
        failed += 1

    # Test 8: Remove channel that doesn't exist (no crash)
    try:
        service = NotificationService([EmailChannel()])
        service.remove_channel(SMSChannel)  # SMS was never added
        results = service.notify("frank", "Still here!")
        assert results == ["Email to frank: Still here!"], f"Got {results}"
        print("  [PASS] Test 8: Removing non-existent channel type doesn't crash")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 8: Remove non-existent — {e}")
        failed += 1

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{passed+failed} tests passed")
    if failed == 0:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")


if __name__ == "__main__":
    run_tests()
