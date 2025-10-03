<!-- https://developers.home-assistant.io/docs/add-ons/presentation#keeping-a-changelog -->
## 1.1.64:
- Added support for managed sub-accounts! This has been one of the most requested features.
- You can now create unassigned tasks that anyone in your group can pick up.
- Add the Ability to assign an assignee in a task in a sentence by using @


## 1.1.60:
Improve impersonate user functionality and fix the issue where the user is unable to start, pause, and complete tasks
Release new version for app store and new Android APK
add count of unplanned tasks, overdue, and pending approval on calendar view
few cosmetic updates for History Card
Show user details on timer session


## 1.1.58:

we miss few releases so there few change between 1.1.58 and 1.1.53 added them here: 
- Fixed issue where users are unable to join a new circle
- Improved chore visibility logic  
- Fixed issue where self-hosted instance did not have plus features

- **Apple App Store Launch**: Official launch of Donetick on the Apple App Store for both iPhone and iPad
- **Task Approval System**: Added support for requiring approval for tasks
- **Enhanced Calendar Views**: Calendar monthly view with priority colors and dual-month display for tablets
- **Dashboard Improvements**: New "Tasks by Assignee" card and user switcher replacing welcome card
- **Mobile-First UI**: Overhauled user interface with better safe area handling and more intuitive modal interactions
- **Quick Access**: Added user profile quick access in the top right corner




## 1.1.53:
- **Home Assistant Integration Update**: Added support for the latest Donetick integration, enabling full control of Things and management of Tasks (add, edit, delete) directly from Home Assistant.
- **Individual To-Do Lists**: Each user now has a personal to-do list, in addition to a master list for the entire circle.
- Various bug fixes and stability improvements.

> [!NOTE]
> If you have previously installed the Donetick integration, you might need to remove it and re-add it to ensure compatibility with the latest version. 
> you can check the [Donetick Integration](https://github.com/donetick/donetick-hass-integration) for more details on how to set it up.


## 1.1.52:
- Fixed issue that was preventing tasks from being skipped [#259](https://github.com/donetick/donetick/pull/259)
- Fixed OCID login bug
- Fixed bug where due dates were automatically updated when saving tasks [#263](https://github.com/donetick/donetick/pull/263), [#260](https://github.com/donetick/donetick/pull/260)
- Fixed error when loading Things with no history
## 1.1.51:
- **Quick Task Actions**: Swipe on tasks to start, pause, edit, or delete for faster management on mobile.
- **Navigation Bar Update**: Improved padding, sticky positioning, and responsive layout for better mobile experience.
- **UI Enhancements**: Refined design for Things, Labels, and History to match Donetick’s overall look.
- **Keyboard Shortcuts**: Added shortcuts for faster task creation on desktop, with hints shown on Command/Ctrl.
- **Timer Management**: Start, pause, and track time spent on tasks across devices, including break tracking.
- **UserPoints & Activities**: Enhanced filtering, layout, and new graphs for better insights.

## 1.1.45:
- **Dashboard Redesign**: Dashboard is now optimized for table/mount use. Managers/admins can complete tasks for others, with identity selection in the top-right card.
- **UI Enhancements**: Calendar updated to match Donetick design. Added "Recent Changes" card for last 7 days' activity. Compact mode introduced for smaller cards and improved space usage.
- **Task Management**: Task descriptions now support Markdown rich text editing and image uploads (if storage is configured).
- **Storage**: File uploads supported via S3-compatible storage.
- **Multi-Factor Authentication (MFA)**: Endpoints for MFA setup, confirmation, disabling, and verification. Backup code regeneration and improved expiration date formatting.
- **Circle Management**: Added ChangeMemberRole endpoint with role validation. GetCircleUsers now includes user images.
- **Build/Versioning**: Build and configuration now include versioning info.
- **Fixes**: OIDC authentication issues resolved and other minor fixes.


## 1.1.43:
- **Task in a Sentence**: Advanced task input parsing with dynamic highlighting for Priority, Due Date, Frequency, and Labels.
- **Initial Offline Mode**: View and manage cached tasks offline; some actions queue for later execution.
- Fix hardcoded email address by @Alone2 in [#149](https://github.com/donetick/donetick/pull/149).
- Include CircleID in notifications by @glombek in [#174](https://github.com/donetick/donetick/pull/174).
- Correct unarchive message by @stefan-matic in [#181](https://github.com/donetick/donetick/pull/181).
- New Contributors: @Alone2, @glombek, @stefan-matic.

## 1.1.38:
- Fix bug that disabled notifications when task created by task in sentence
## 1.1.37:
- **Nest Sub-tasks**: Added support for nested sub-tasks.
- **Webhook Notification Target**: Added support for webhook as the only notification target.
- **Task Filtering by Assignee**: Support filtering tasks by assignee and storing it as the default view.
- **User Preference for Default Group By**: Save user preference for default group by for task view.

## 1.1.36:
- **Subtasks**: Added support for subtasks. Each task can now have steps or subtasks. These can be completed and tracked separately. When a recurrent task is completed, its subtasks are reset.
- **Group By and Section Persistence**: Persisted the "group by" setting in the main view. If you select "group by due date," "priority," etc., this setting will be preserved. When you return to donetick from the same device, you will see the same grouping. Additionally, the collapsed/expanded state of sections is now persisted.
- **Rolling Chore Due Date Logic**: Added logic to ensure the next due date for rolling chores is the later of the completed date or the originally calculated next due date, particularly for day-of-the-month scheduling.
## 1.1.35
Support completing task from eAPI (i.e. Home Assistant integration)
Fix issue with the Notiitcation 

## 1.1.34
Update Error Page
Fix issue where settings page not loading 

## 1.0.33
Add Support for Webhook!
Notification and task not generate event can be consume via webhooks
Add Modal to Edit things
Add a custom 404 page
Fix Bug in Update things with Type strings
(Release Note)[https://github.com/donetick/donetick/releases/tag/v0.0.33]


## 1.0.32
* Add support for SSO with OIDC ( test with Authentik)
* fix issue with completing overdue chores


## 1.0.30
Timeout increased to 10s, build validation added, and notification ID fix implemented.
Filtering by priority/label enabled and detail view design updated.
Schedule logic simplified and Things UI refreshed.

## 1.0.30
fix bug where Only admin point redeemable
## 1.0.29
Fix issue while redeeming points 
## 1.0.28

- **Improved Main View for Large Screens (Tablet, Desktop)**:  
  The main view now includes a side calendar where you can easily see all your scheduled tasks (both assigned to you and others in your circle).  

- **Updated Configuration Loading**:  
  Added support for environment-specific overrides.  

- **API Support**:  
  You can now create tasks and chores via the API.  

- **Points System Upgrade**:  
  Introduced the ability to redeem points!  

- **Task in sentence**: I am excited about this one specifically. the focus is to minimize the click and field switching when creating a task. You would click the input field and type everything into one sentence. Donetick will attempt to parse the details and will show the modal to show you what has been processed
You will open Donetick. click on the top field and type the task once you are done press enter. and task created. you can set due dates, recurrent tasks, and priorities all in one shot.
> [!WARNING]
> This may cause tasks to fail to be scheduled or created properly. If you encounter this issue, please open an issue in the repository.


  **Usage:**  
  - **Priority**: For the highest priority, use any of the following keywords: `P1`, `Urgent`, `Important`, or `ASAP`.  
    Use `P2`, `P3`, or `P4` for lower priorities.  
  -  **Due date**: Specify dates with phrases like tomorrow, next week, Monday, or   August 1st at 12 pm.
  -  **Frequency/Reccurent**: Set recurring tasks with terms like daily, weekly, monthly,  yearly, or patterns such as every Tuesday and Thursday.

## What's Changed
* IsRolling tests by @johan-autohome in https://github.com/donetick/donetick/pull/73
* Bugfix: error when disabling push notifications by @dkhalife in https://github.com/donetick/donetick/pull/58




## 1.0.20
- Add Support for Points
- Fix Issue with NFC tag 
## 1.0.19
- Support Loading Archived Tasks
- fix issue in assignee different users for task
## 1.0.18
- Improve UI and support sorting by date
- Support Pushover
- fix bugs when attempt to send notification
- Support to disable login

## 1.0.17:
Add support for tasks api to work with homeassistant integration


## 1.0.16:
Add Support Label across the tasks
Add Label Manager

## 1.0.15:
Support Password reset
Add Priotity support for tasks

## 1.0.7:
Update to Donetick V0.0.12
Update Dockerfile and Docker image push command
Improve the My Chore UX and add filter button