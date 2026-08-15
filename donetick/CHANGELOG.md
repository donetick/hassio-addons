<!-- https://developers.home-assistant.io/docs/add-ons/presentation#keeping-a-changelog -->

## 0.1.76:
## Release Notes:

Another big one! Between the backend and the app, there's a lot in here so bare with me if I miss something, will keep updating this over the next few days.

- **Offline Mode keeps getting better**: sync + versioning support landed on the backend (new `syncVersion` field so the app can reconcile changes made while offline), and on the app side offline support now covers labels, projects, and chore archiving/unarchiving too. Also fixed stuck commands blocking the sync pipeline, spurious "you're offline" flips, and ghost chores showing up when switching accounts. Offline data now properly clears on logout/session expiry/server change.

- **NFC**: cleaned up NFC permissions on Android (removed NDEF/PACE to keep Play Store happy) and fixed NFC URL generation on iOS.

- **OCR -> Task**: you can now snap/upload a photo and have it turned into a task automatically. Still early, expect it to get smarter over the next few releases.
- **Advanced Filtering improvement** : custom filters can now group results, and filter/chip navigation no longer kicks you to a new page when running as a PWA. History and activity views also got a unified toolbar with filtering built in.

- **SSO-only self-hosting**: new `disable_password_auth` config option so you can fully disable local/password login and run SSO-only through your OIDC provider. If you're locking things down for a single-household deployment this one's for you.

- **Attachments**: new attachment browser/viewer, plus draft support so uploads don't get lost mid-edit.

- **Task creation got a refresh**: reworked Add Task modal with a smarter title input and a quicker due-date/time picker.

- **Activity & History**: new detail modal so you can drill into (and edit from) any activity entry, plus proper "Missed" / "Rescheduled" status handling and a fix for points history not counting all circle members.

- **Localization**: German, Brazilian Portuguese, Japanese, and Simplified Chinese translations added — thank you to everyone contributing!

- **Login/Auth fixes**: fixed a Google Sign-In crash on iOS, OAuth2 refresh token bug, MFA handling improvements, and clearer error messages when login fails.

- **API validation is more graceful now**: instead of just failing, invalid requests come back with useful details on what went wrong.

- as a side note: for self-hosters without email configured, there's now a `log_raw_url` option to log password-reset links straight to the console.

## Special thanks:

- everyone who contributed translations (German, pt-BR, Japanese, zh-CN)  you're making Donetick usable for a lot more people!
- everyone who filed issues, tested betas, and helped shape this release. Thank you!

## What's Changed

- Make sure Origin same for SSE and server in [#659](https://github.com/donetick/donetick/pull/659)
- Update README.md in [#661](https://github.com/donetick/donetick/pull/661)
- fix: include validation details in API error responses by [@mvanhorn](https://github.com/mvanhorn) in [#606](https://github.com/donetick/donetick/pull/606)
- fix(oidc): honor preferred_username claim on OAuth2 signup by [@MaikuMori](https://github.com/MaikuMori) in [#634](https://github.com/donetick/donetick/pull/634)
- Offline Support: Add Synchronization and Versioning by [@meauxt](https://github.com/meauxt) in [#665](https://github.com/donetick/donetick/pull/665)
- Graceful Validation with Warnings, to make sure we have a non-breaking rollout by [@meauxt](https://github.com/meauxt) in [#674](https://github.com/donetick/donetick/pull/674)
- add log_raw_url option to log password reset URL in console by [@meauxt](https://github.com/meauxt) in [#675](https://github.com/donetick/donetick/pull/675)
- Bugfix/rework api input validation frontend error by [@hoborm](https://github.com/hoborm) in [#681](https://github.com/donetick/donetick/pull/681)
- feat(auth): add disable_password_auth option for SSO-only instances (fixes [#438](https://github.com/donetick/donetick/issues/438)) in [#699](https://github.com/donetick/donetick/pull/699)
- Bug fixes 06/27/2026 by [@meauxt](https://github.com/meauxt) in [#712](https://github.com/donetick/donetick/pull/712)
- unify docker file and add commit to the go releaser in [#724](https://github.com/donetick/donetick/pull/724)
- remove the uniqueness requirement on api token name in [#726](https://github.com/donetick/donetick/pull/726)
- Run migration script against sqlite always in [#731](https://github.com/donetick/donetick/pull/731)
- App: filters/settings icon alignment in [#87](https://github.com/donetick/frontend/pull/87)
- App: filter & chip navigation fixes (no more bouncing out of the PWA) in [#88](https://github.com/donetick/frontend/pull/88), [#89](https://github.com/donetick/frontend/pull/89), [#90](https://github.com/donetick/frontend/pull/90)
- App: add Brazilian Portuguese (pt-BR) translation in [#90](https://github.com/donetick/frontend/pull/90)
- App: add German translation in [#94](https://github.com/donetick/frontend/pull/94)
- App: fix points history to include all circle members in [#93](https://github.com/donetick/frontend/pull/93), [#101](https://github.com/donetick/frontend/pull/101)
- App: offline support for labels/projects/chore archiving, network listener + sync-on-reconnect in [#99](https://github.com/donetick/frontend/pull/99), [#110](https://github.com/donetick/frontend/pull/110), [#117](https://github.com/donetick/frontend/pull/117)
- App: fix reinitialize api client after server URL changes in [#106](https://github.com/donetick/frontend/pull/106)
- App: activity card status fix ('Missed'/'Rescheduled') in [#107](https://github.com/donetick/frontend/pull/107)
- App: MFA handling improvements in [#111](https://github.com/donetick/frontend/pull/111)
- App: add Japanese (ja) localization in [#112](https://github.com/donetick/frontend/pull/112)
- App: donetick.com rebase/cleanup in [#113](https://github.com/donetick/frontend/pull/113), [#114](https://github.com/donetick/frontend/pull/114)
- App: fix "anyone" assignee handling in [#116](https://github.com/donetick/frontend/pull/116), [#119](https://github.com/donetick/frontend/pull/119)
- App: NFC tag scanner support (Android) in [#118](https://github.com/donetick/frontend/pull/118)
- App: bug fixes 06-27-2026 in [#124](https://github.com/donetick/frontend/pull/124)
- App: Add Task Modal v2 — smarter title input, quick due date/time picker in [#125](https://github.com/donetick/frontend/pull/125)
- App: advanced filtering with grouping support in [#126](https://github.com/donetick/frontend/pull/126)
- App: photo/AI attachments — OCR photo to task in [#127](https://github.com/donetick/frontend/pull/127)
- App: general UX improvements in [#128](https://github.com/donetick/frontend/pull/128)
- App: dependency fixes in [#129](https://github.com/donetick/frontend/pull/129)
- App: task photo fix in [#130](https://github.com/donetick/frontend/pull/130)
- App: bugfix rounds (incl. version prep for 1.2.6/1.2.7) in [#131](https://github.com/donetick/frontend/pull/131), [#133](https://github.com/donetick/frontend/pull/133), [#134](https://github.com/donetick/frontend/pull/134), [#135](https://github.com/donetick/frontend/pull/135)
- App: integrate Fastlane, add release script in [#139](https://github.com/donetick/frontend/pull/139)
- App: more bugfixes in [#140](https://github.com/donetick/frontend/pull/140)
- App: fix iOS crash from Google Sign-In URL scheme, force fresh login before Google sign-in in [#148](https://github.com/donetick/frontend/pull/148), [#149](https://github.com/donetick/frontend/pull/149)
- App: fix notification deep links in [#151](https://github.com/donetick/frontend/pull/151)
- App: attachment upload/signing fixes, iOS sqlite metadata fix in [#152](https://github.com/donetick/frontend/pull/152), [#153](https://github.com/donetick/frontend/pull/153)

Big thanks to all the contributions in this release! Thank you for making Donetick better!

## New Contributors

- [@mvanhorn](https://github.com/mvanhorn) made their first contribution in [#606](https://github.com/donetick/donetick/pull/606)
- [@MaikuMori](https://github.com/MaikuMori) made their first contribution in [#634](https://github.com/donetick/donetick/pull/634)

**Full Changelog (backend)**: [v0.1.75...v0.1.76-beta.20](https://github.com/donetick/donetick/compare/v0.1.75...v0.1.76-beta.20)
**Full Changelog (app)**: [1.2.2...1.2.16](https://github.com/donetick/frontend/compare/4713e99...74d658f)

## 0.1.75:
## Release Notes:
We have big release and will be updating the note in the next couple days! Because am sure I miss few things!

 
- Internationalization: one of the most requested feature many been waiting for, we start the process and did early release for it! Hopefully with more contributions you will see your language support! 
- Rescheduling History: Chores now track rescheduling events in their history, giving users better visibility into how tasks have been moved over time.
- Extended Swagger / API Auth Support: Swagger and MultiAuthMiddleware now cover additional handlers, broadening API documentation and authentication coverage. 
- Label Filtering in Advanced Filters: Labels can now be used within the advanced filter system for more precise task queries.
- Smart Insights Panel: A new Smart Insights card has been added to the side panel, providing nice analysis and suggestions.(This is  a preview, might get improvement or removed :) )   
- Available for Me Quick Filter: Renamed and refined the quick filter to show chores assigned to the current user or unassigned.
- as side note: we have great improvement happen on homeassistant integration! We have calendar integration and recurrent task represent as sensor as well now! Make sure you update you integration!




Special thanks :
- to @hoborm for the dedication he put into this! Release from swagger to testing to managing issues and discord. THANK YOU !
-  @peppone18 for reporting a vulnerability and fixing it! More details in CVE when published 
- @Vi-Ku for making first contribution and jumping into open issues ! Welcome aboard!
- @scottanderson for making always cicd improvement 
- @curreta for giving homeassistant integration the love it need! And for  @torbenvanassche for helping in making that happen! 
- everyone contribute to this release and help making Donetick better!


## What's Changed
* Add 30 second grace period for CanEdit time check. by @hoborm in https://github.com/donetick/donetick/pull/480
* Fix Time.Now().UTC lint error in payment webhook by @hoborm in https://github.com/donetick/donetick/pull/528
* Add golangci-lint checks to PR workflow by @scottanderson in https://github.com/donetick/donetick/pull/414
* bugfix: Install tzdata package in runtime env. by @hoborm in https://github.com/donetick/donetick/pull/530
* Add `Code Formatting and Linting` to README.md by @scottanderson in https://github.com/donetick/donetick/pull/531
* Enforce JSON binding in chores and circles' handler by @hoborm in https://github.com/donetick/donetick/pull/511
* Fix LICENSE.MD url by @hoborm in https://github.com/donetick/donetick/pull/540
* Add various CI checks by @scottanderson in https://github.com/donetick/donetick/pull/534
* Aligned password requirements and increased max-length to 64 by @wjzijderveld in https://github.com/donetick/donetick/pull/525
* feat: allow configuring custom fromEmail and separate users for SMTP by @njoerd114 in https://github.com/donetick/donetick/pull/325
* Enabled the TaskCreated event by @wjzijderveld in https://github.com/donetick/donetick/pull/562
* Fix a bug where a non-assignee can be assigned a chore based on prior completions of the chore by @robertpyke in https://github.com/donetick/donetick/pull/565
* Fix not respected "next assigned" rules for trigger chores by @hoborm in https://github.com/donetick/donetick/pull/556
* README: Add a build step about JWT secret by @feedingaliencat in https://github.com/donetick/donetick/pull/543
* config: default RateLimit/RatePeriod to match selfhosted.yaml values by @BP602 in https://github.com/donetick/donetick/pull/559
* Feature/simple health check api by @hoborm in https://github.com/donetick/donetick/pull/527
* Fix lint errors introduced in #527 by @hoborm in https://github.com/donetick/donetick/pull/591
* docs: include config volume in 'docker run' by @omarkohl in https://github.com/donetick/donetick/pull/584
* Extend swagger+MultiAuthMiddleware for multiple handlers by @hoborm in https://github.com/donetick/donetick/pull/514
* wrap Swagger initialization command in shell execution by @meauxt in https://github.com/donetick/donetick/pull/600
* Change to serve_frontend:true by @hoborm in https://github.com/donetick/donetick/pull/603
* fix: expose is_user_creation_disabled in /resource endpoint by @Vi-Ku in https://github.com/donetick/donetick/pull/616
* fix: add cache headers for static assets with cache busting by @Vi-Ku in https://github.com/donetick/donetick/pull/618
* fix: HTML-escape display name in UpdateUserDetails by @Vi-Ku in https://github.com/donetick/donetick/pull/617
* Bump google.golang.org/grpc from 1.75.0 to 1.79.3 by @dependabot[bot] in https://github.com/donetick/donetick/pull/626


Big thanks to all the contributions in this release! Thank you for making Donetick better! 


## New Contributors
* @wjzijderveld made their first contribution in https://github.com/donetick/donetick/pull/525
* @njoerd114 made their first contribution in https://github.com/donetick/donetick/pull/325
* @robertpyke made their first contribution in https://github.com/donetick/donetick/pull/565
* @feedingaliencat made their first contribution in https://github.com/donetick/donetick/pull/543
* @BP602 made their first contribution in https://github.com/donetick/donetick/pull/559
* @omarkohl made their first contribution in https://github.com/donetick/donetick/pull/584
* @meauxt made their first contribution in https://github.com/donetick/donetick/pull/600
* @Vi-Ku made their first contribution in https://github.com/donetick/donetick/pull/616
* @dependabot[bot] made their first contribution in https://github.com/donetick/donetick/pull/626

**Full Changelog**: https://github.com/donetick/donetick/compare/v0.1.74...v0.1.75

## 1.1.74:
- Standardize time handling to UTC across the app (fixes #520).
- Force process timezone to UTC and ensure all stored/used times are normalized to UTC.
- Fix SQL Scanner not handling string values coming from SQLite (fixes #518).
## 1.1.73:
- Project Management: Organize your tasks into projects to better structure work.
- Advanced Filtering System: Create custom filters with multiple conditions (status, assignees, labels, projects, points, and dates) and pin frequently used filters to the main task screen.
- Date-only Tasks: Support for scheduling tasks on a specific date without an associated time.

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
