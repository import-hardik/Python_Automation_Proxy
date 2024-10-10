# Python_Automation_Proxy

### Automating an unnecessary (but unavoidable) task for students who just want to get on Wi-Fi and get things done.

---

## The Problem (Yes, it needed a solution!)

So, here’s the deal: Our college generously offers Wi-Fi to students. Yay! But there's a catch (isn't there always?). To keep cyber-villains at bay, the network requires you to configure a proxy, which allows internet access through a tightly controlled gateway.

Here’s where the fun begins: While the proxy works great on campus, it’s a whole other story when you’re home. The proxy blocks your home network from connecting to websites, so every day, like clockwork, we switch the proxy on when we're at college and off when we're at home. Fun, right? (Hint: no, it’s not.)

---

## The Solution

Meet **Python_Automation_Proxy**, the script you never knew you needed! This handy little program automatically toggles the proxy based on the Wi-Fi network you're connected to. It can run as a startup process, so you don’t even have to think about it. Set it and forget it – let Python do the work while you enjoy uninterrupted web browsing both on campus and at home.

---

## How It Works (Spoiler: It’s simple)

This script is as low maintenance as it gets. It checks which Wi-Fi network you're connected to:
- If you're on the college network, it’ll enable the proxy.
- If you’re on your home network, the proxy gets switched off. No more manually tinkering with settings.

---

## Libraries Used

- **subprocess**: That’s it! We like to keep things clean and lean.

---

## Follow Me on GitHub for More Fun Scripts!

Why stop here? If you enjoyed this script (or just enjoyed not having to fiddle with proxies), check out more of my work. Who knows, you might just automate your way out of a few more annoyances.

Logging out… with zero proxy issues. 🎉
