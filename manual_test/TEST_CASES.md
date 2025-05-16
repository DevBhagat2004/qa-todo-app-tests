# Todo App Test Cases

## 📱 Core Features
### TC-101: Add Task
**Steps:**
1. Install [Todoist APK](https://d.apkpure.com/b/APK/com.todoist?version=latest)
2. Tap "+" → Enter "Buy milk" → Save
**Expected:** Task appears
**Actual:** ✅ Passed (Android 13)

## 🐞 Bug Reports
### TC-201: Crash on Empty Task
**Steps:**
1. Tap "+" → Leave field blank → Save
**Expected:** Error message
**Actual:** ❌ Crashes (Android 12)  
[Screenshot](./bug_reports/crash_blank.png)
