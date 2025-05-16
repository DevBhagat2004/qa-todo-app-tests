# Comprehensive Test Cases for Todo App

## 🔍 Functional Tests
### TC-101: Add Single Task
**Steps:** 
1. Tap "+" → Enter "Buy milk" → Save
**Expected:** Task appears
**Actual:** ✅ Passed (Android 13)

### TC-102: Delete Task
**Steps:**
1. Swipe left → Tap delete
**Expected:** Task removed
**Actual:** ❌ 2s delay (iOS)

## 🚨 Edge Cases
### TC-201: 1000-character Task
**Steps:**
1. Enter long text → Save
**Expected:** Text truncated
**Actual:** ❌ UI overlap

### TC-202: Offline Mode
**Steps:**
1. Disable network → Add task
**Expected:** Offline warning
**Actual:** ❌ Silent fail
