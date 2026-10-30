<!-- https://developers.home-assistant.io/docs/add-ons/presentation#keeping-a-changelog -->

## 0.1.84:
## Release Notes:

This release is has a lot of quality of life improvments :like smarter notifications, better feedback when things fail,better representation on action and permissions. 
PLUS a lot of new features! We added initial support for project board/list views(, and sharing for labels and filters  plus the app got a share extension!( so now you can share a photo with donetick and create task with that as attachment!) , a project widget(for both of course IOS and Android). we also add supoprt for few themes now to pick a different colors that match your style!
As always, bear with me if I miss something, will keep updating this over the next few days.

- **Smart notifications**: notification profiles is a  per-user preferences and daily/weekly digest generation. Approval and redemption requests now go through a proper notification dispatcher, and you get notified on assignments and pending approvals too. 

- **Project board and list views**: projects now have board and list views, not just the one layout.( the list view has been something sitting and waiting for release for a while! so it finally make it! it early release so keep that in mind )

- **Labels and filters get sharing + privacy**: labels and filters can now be shared or kept private, with per-recipient privacy respected in broadcasts.


- **App side (frontend v1.2.56 → v1.2.62)**: a share extension so you can share into Donetick from other apps, a project widget, priority in the chore action menu plus offline sync improvements, a fix for fields bleeding on smaller screens like the iPhone 13, and the 1016 fixes batch.

- **Home Assistant integration**: optional HA user mapping so the right person gets completion credit, opt-in reassignment to any circle member, fixed task creation attribution, `complete_task` now returns the history entry plus a `delete_history` option (@ChrisB85), calendar due dates fixed to the HA timezone, a round of small fixes (@csandbrink entity registry helper, the server's reason when it refuses a reassignment, frontend test in CI, HACS minimum raised), local brand assets (@frenck), and documented completion/reschedule services.

## Special thanks:

- @csandbrink for the HA completion-credit mapping, reassignment work, and small fixes
- @ChrisB85 for the complete_task history entry and delete_history
- @frenck for the brand assets
- @torbenvanassche for wrangling the HA integration side
- everyone who filed issues, tested betas, and helped shape this release. Thank you!

## What's Changed

Backend (`donetick/donetick`):

- Notification improvement: FCM/bridge, join-request message format in https://github.com/donetick/donetick/pull/916
- Digest notifications: profiles, preferences, daily/weekly digests in https://github.com/donetick/donetick/pull/919
- Project board and list views in https://github.com/donetick/donetick/pull/924 and https://github.com/donetick/donetick/pull/927
- Label/filter sharing + privacy (ACL) in https://github.com/donetick/donetick/pull/936
- Notification dispatcher for approvals, assignments, redemptions in https://github.com/donetick/donetick/pull/940 and https://github.com/donetick/donetick/pull/941
- 1028 fixes: don't notify yourself on assignment in https://github.com/donetick/donetick/pull/943
- fix(circle): correct user_id selection in GetCircleUsers query (direct commit)

App (`donetick/frontend`, v1.2.56 → v1.2.62):

- 1016 fixes in https://github.com/donetick/frontend/pull/327
- Share extension for the Donetick app in https://github.com/donetick/frontend/pull/330
- ChoreActionMenu: priority + offline sync improvements in https://github.com/donetick/frontend/pull/331
- Project widget in https://github.com/donetick/frontend/pull/332
- Fix fields bleeding on smaller screens (iPhone 13) in https://github.com/donetick/frontend/pull/333

Home Assistant (`donetick/donetick-hass-integration`, main since v0.1.83):

- Docs: card completion and reschedule services by @csandbrink in https://github.com/donetick/donetick-hass-integration/pull/71
- Completion credit for assigned/completed-by by @csandbrink in https://github.com/donetick/donetick-hass-integration/pull/72
- Local brand assets by @frenck in https://github.com/donetick/donetick-hass-integration/pull/73
- Opt-in reassignment to any circle member by @torbenvanassche in https://github.com/donetick/donetick-hass-integration/pull/74
- HA user mapping for completion credit by @torbenvanassche in https://github.com/donetick/donetick-hass-integration/pull/75
- Fix calendar due dates in the HA timezone by @torbenvanassche in https://github.com/donetick/donetick-hass-integration/pull/77
- Integration small fixes by @csandbrink in https://github.com/donetick/donetick-hass-integration/pull/78
- complete_task returns history entry + delete_history by @ChrisB85 in https://github.com/donetick/donetick-hass-integration/pull/80
- Fix task creation attribution by @torbenvanassche in https://github.com/donetick/donetick-hass-integration/pull/81

## Unreleased

- Fix `disable_signup` so enabling it blocks new account registration.

## 0.1.83:
## Changelog
* 9b2ea2b94a73e496dff8ad2b7258afced412d978: fix(chore): restore handler changes lost in the reward-store merge (@pcbeingused333)
* 466f2cd97adf75b834174fce41d71f68f422ee00: fix(label): remove chore labels attached by another member (@pcbeingused333)
* 8687826cf9d0c0f0da5e1a2a4b9f370a1c74600d: Merge pull request #897 from pcbeingused333/fix/restore-chore-handler-after-reward-merge (@meauxt)
* 549e44c836de6b54f026624ccce9d6e8df726a30: Merge pull request #898 from pcbeingused333/fix/remove-labels-added-by-other-members (@meauxt)

## 0.1.82:
## Donetick v0.1.82

Big one again! This release is headlined by project sharing with selected members or even making it private! reward store,  calendar sync plus a whole lot of fixes and a big push on the Home Assistant side. Bare with me if I miss something, will keep updating this over the next few days.


- **Share projects with selected members**: private projects now have a third option — share with specific circle members, not just "only me" or "whole circle". You can preview the effect before saving, assignees who lose access get trimmed(@raulanatol and  @helgehelge123)

- **Home Assistant integration**: a huge push by @torbenvanassche (THANK YOU!)  per-user task cards, task reassignment, inline task editing with native HA date/time controls, label and date filters on the task card, persistent completed-task history, label colors and row spacing, points and interval displays, a cleaned-up card editor, much faster load times, Anyone-task fixes, and a startup race fix. The repo also got a GPLv3 license and the README's server-version warning removed. If you haven't updated the integration yet, please go ahead and do it and enjoy the new Donetick card by @torbenvanassche ! 

- **New Edit View**: a Huge thanks again for @torbenvanassche! yes been killing it this release. He revamped our edit screen and now look much nicer and more intuitive. Thanks also to Cornel, who put the original design together, and we iterated on it! 

- **Reward store is here**: members can now spend their hard-earned points on parent-defined rewards. Each redemption goes through an admin/manager approval step, mirroring the chore completion approval flow. The app got a full rewards page too  browse the store, redeem, and (for admins) work through the approval queue. (@jandreaucodes) (you can see it Points Page)

- **Calendar sync**: the iCal endpoint is back, plus per-user calendar tokens that can be revoked — subscribe to your chores from any calendar app. There's a calendar sync settings screen in the app to manage it. (Thanks to @joouha for the original iCal work.)

- **API keys, new format**: keys now use a `dt_` prefix with hashed storage. and not we store hash of them Thanks to (@yildiz-fatih) 

- **Join-request notifications**: push notifications when a circle join request is approved or declined, so nobody is left wondering.

- **Scheduler fixes**: DST drift is fixed — local time of day stays stable across DST transitions and the chore timezone is applied to rolling `day_of_the_month` dates. Weekday chores can also start on a selected day now. (@DelayLama, @theluckystrike)

- **Delegation fix**: you can delegate tasks to other circle members again. (@RichtarikOliver)

- **Permissions**: circle admins/managers can now update and delete chores via the API (@torbenvanassche), and task completion actions landed for Things (@torbenvanassche). Editing a chore without labels no longer wipes its labels. (@helgehelge123)

- **Donetick Bridge foundation **: new optional hosted bridge for self-hosters more to come in next release 

- **Device tokens**: token replacement at the device limit and proper upsert, so re-logging in on a device doesn't pile up stale tokens.

- **Self-hosting**: `selfhosted.yaml` is auto-generated on first startup (@omarkohl). Also removed the self-hosted GHCR build workflow that got added by mistake in an earlier PR.

- **App side (frontend v1.2.56)**: reward store UI, calendar sync settings, project sharing UI, privacy controls on projects, "always available" tasks UI, a task editor wizard proposal (@torbenvanassche), task completion action controls, settings UI improvements (profile, points, activities, declining circle join requests), API token settings with copy, app icon badge counts, better speech recognition, R8 shrinking/obfuscation for the Android build, PKCE support and backend-sent OAuth scopes in the app (@Mark Dietzer), Italian translations restored (@Rello75cl), Arabic/French/Chinese updates, Crowdin plural-form

## Special thanks:

- @jandreaucodes for the reward store
- @helgehelge123 and @raulanatol for project sharing and the labels fix
- @torbenvanassche for the Home Assistant overhaul, API permissions, and Things completion actions
- @yildiz-fatih for the new API key format
- @DelayLama for the DST drift fix
- @theluckystrike for the weekday start fix
- @RichtarikOliver for the delegation fix
- @joouha for the iCal endpoint
- @omarkohl for the selfhosted.yaml auto-generate
- @Mark Dietzer for PKCE and scopes in the app
- @Rello75cl for restoring the Italian translations
- @Conor O'Callaghan for text updates
- everyone who filed issues, tested betas, and helped shape this release. Thank you!

## What's Changed

Backend (`donetick/donetick`):

- Auto-generate selfhosted.yaml on first startup by @omarkohl in https://github.com/donetick/donetick/pull/583
- Fix DST drift: stable local time across DST, timezone-aware rolling dates by @DelayLama in https://github.com/donetick/donetick/pull/809
- Add iCal endpoint by @joouha in https://github.com/donetick/donetick/pull/631
- 1006 fixes (incl. #748) in https://github.com/donetick/donetick/pull/870
- Can't delegate task to other circle member by @RichtarikOliver in https://github.com/donetick/donetick/pull/871
- Calendar ICS: token model + repository in https://github.com/donetick/donetick/pull/872
- Allow circle admins/managers to update and delete chores via API by @torbenvanassche in https://github.com/donetick/donetick/pull/874
- Start weekday chores on a selected day by @theluckystrike in https://github.com/donetick/donetick/pull/868
- Donetick Bridge integration in https://github.com/donetick/donetick/pull/875
- Task completion actions for Things by @torbenvanassche in https://github.com/donetick/donetick/pull/878
- Push notifications for join request approvals/declines in https://github.com/donetick/donetick/pull/883
- Device token upsert + replacement at device limit in https://github.com/donetick/donetick/pull/849
- Keep labels when an update omits labelsV2 by @helgehelge123 in https://github.com/donetick/donetick/pull/881
- Share projects with selected circle members by @helgehelge123 in https://github.com/donetick/donetick/pull/882
- Standardize API key format with hashed storage and dt_ prefix by @yildiz-fatih in https://github.com/donetick/donetick/pull/800
- Reward store: redeem points for admin-defined rewards by @jandreaucodes in https://github.com/donetick/donetick/pull/841
- Remove self-hosted build workflow (added by mistake) in https://github.com/donetick/donetick/pull/888

App (`donetick/frontend`, v1.2.55 → v1.2.56):

- Use backend-sent scopes with fallback by @Mark Dietzer in https://github.com/donetick/frontend/pull/162
- Implement PKCE support by @Mark Dietzer in https://github.com/donetick/frontend/pull/164
- Fix #818 in https://github.com/donetick/frontend/pull/278
- Privacy control on projects + inherit on tasks in https://github.com/donetick/frontend/pull/274
- Always available tasks in https://github.com/donetick/frontend/pull/277
- Assignees selection visual feedback in https://github.com/donetick/frontend/pull/284
- Service worker updates in https://github.com/donetick/frontend/pull/285
- Restore complete Italian translations by @Rello75cl in https://github.com/donetick/frontend/pull/287
- Paywall prompts for free-plan limits in https://github.com/donetick/frontend/pull/289
- Calendar sync settings in https://github.com/donetick/frontend/pull/291
- Fix: isPlus account mistakenly reversed in https://github.com/donetick/frontend/pull/292
- Crowdin plural forms + translation safety checks in https://github.com/donetick/frontend/pull/297, https://github.com/donetick/frontend/pull/296
- Task completion action controls by @torbenvanassche in https://github.com/donetick/frontend/pull/305
- Task editor wizard by @torbenvanassche in https://github.com/donetick/frontend/pull/306
- Share projects with selected circle members by @helgehelge123 in https://github.com/donetick/frontend/pull/308
- Project members improvements in https://github.com/donetick/frontend/pull/314
- Mobile navbar title in https://github.com/donetick/frontend/pull/315
- Settings UI: profile + decline circle join requests in https://github.com/donetick/frontend/pull/316
- Settings UI: user points + user activities in https://github.com/donetick/frontend/pull/317
- API token settings UI in https://github.com/donetick/frontend/pull/318
- Reward store UI in https://github.com/donetick/frontend/pull/319
- Notification template design in https://github.com/donetick/frontend/pull/320
- Desktop top margin, notifications look, collapsible EditChore in https://github.com/donetick/frontend/pull/321
- Arabic + French localizations in https://github.com/donetick/frontend/pull/322
- Paywall event fix in https://github.com/donetick/frontend/pull/323
- R8 shrinking + obfuscation in release build in https://github.com/donetick/frontend/pull/324
- Donetick Bridge integration in https://github.com/donetick/frontend/pull/325
- Capacitor Badge integration + sync in https://github.com/donetick/frontend/pull/326
- Fixes in https://github.com/donetick/frontend/pull/307, https://github.com/donetick/frontend/pull/309, https://github.com/donetick/frontend/pull/269
- Translation batches in https://github.com/donetick/frontend/pull/273, https://github.com/donetick/frontend/pull/279, https://github.com/donetick/frontend/pull/281, https://github.com/donetick/frontend/pull/286, https://github.com/donetick/frontend/pull/280, https://github.com/donetick/frontend/pull/293

Home Assistant Integration(`donetick/donetick-hass-integration`, main since v0.1.80, Yes sorry we don't yet have proper versioning there):

- Project support by @postwait in https://github.com/donetick/donetick-hass-integration/pull/51
- Per-user task cards by @torbenvanassche in https://github.com/donetick/donetick-hass-integration/pull/58
- Task card bugfixes by @torbenvanassche in https://github.com/donetick/donetick-hass-integration/pull/60
- Task card label filter by @torbenvanassche in https://github.com/donetick/donetick-hass-integration/pull/63
- Fix card startup race by @torbenvanassche in https://github.com/donetick/donetick-hass-integration/pull/64
- Fix Anyone tasks by @torbenvanassche in https://github.com/donetick/donetick-hass-integration/pull/66
- Task sensor points interval by @torbenvanassche in https://github.com/donetick/donetick-hass-integration/pull/67
- Task completion history by @torbenvanassche in https://github.com/donetick/donetick-hass-integration/pull/68
- Card editor cleanup in https://github.com/donetick/donetick-hass-integration/pull/69, https://github.com/donetick/donetick-hass-integration/pull/70


<img width="334" height="742" alt="image" src="https://github.com/user-attachments/assets/39cc77f4-b65e-4e1e-8716-bea6385d9476" />
<img width="333" height="743" alt="image" src="https://github.com/user-attachments/assets/055576b4-2c42-448b-81a3-432c9a1e6cf0" />

## 0.1.80:
## Changelog
* e88d8bea62405ca02288f93dd70efab8c0f1ff2c: Merge pull request #863 from donetick/lint-and-test-1003 (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.79:
## What's Changed
* Update README.md by @meauxt in https://github.com/donetick/donetick/pull/661
* feat(storage): add storage.path_style option for S3  by @MaikuMori in https://github.com/donetick/donetick/pull/635
* Bugfix/rework api input validation by @hoborm in https://github.com/donetick/donetick/pull/607
* add log_raw_url option to log password reset URL in console by @meauxt in https://github.com/donetick/donetick/pull/675
* Graceful Validation with Warnings. to make sure we have a non-breaking by @meauxt in https://github.com/donetick/donetick/pull/674
* Offline Support: Add Synchronization and Versioning by @meauxt in https://github.com/donetick/donetick/pull/665
* bug bash 1 by @meauxt in https://github.com/donetick/donetick/pull/692
* bugbash 2 by @meauxt in https://github.com/donetick/donetick/pull/691
* Use URL-safe base64 for password reset and verification links by @chetmac in https://github.com/donetick/donetick/pull/689
* improve storage implementation by @meauxt in https://github.com/donetick/donetick/pull/709
* Bug fixes by @meauxt in https://github.com/donetick/donetick/pull/705
* feat(auth): add disable_password_auth option for SSO-only instances (#438) by @louim in https://github.com/donetick/donetick/pull/699
* Bug fixes 06 27 2026 by @meauxt in https://github.com/donetick/donetick/pull/712
* Bugfix/rework api input validation frontend error by @hoborm in https://github.com/donetick/donetick/pull/681
* unify with donetick.com by @meauxt in https://github.com/donetick/donetick/pull/723
* Feature/donetick com support 2 by @meauxt in https://github.com/donetick/donetick/pull/724
* make sure Signing/serving now agree by @meauxt in https://github.com/donetick/donetick/pull/725
* remove the uniqueness  requirement on api token name by @meauxt in https://github.com/donetick/donetick/pull/726
* strength api access and bug fixes  by @meauxt in https://github.com/donetick/donetick/pull/730
* Run migration script agains sqlite always by @meauxt in https://github.com/donetick/donetick/pull/731
* Fix anyone as assignees by @meauxt in https://github.com/donetick/donetick/pull/744
* Send reminders to all circle members for chores assigned to "Anyone" by @meauxt in https://github.com/donetick/donetick/pull/746
* Make sure removing and changing label bump syncverison by @meauxt in https://github.com/donetick/donetick/pull/762
* Add payment routes back by @meauxt in https://github.com/donetick/donetick/pull/773
* Implement bumpChoreSyncVersions for chore by @meauxt in https://github.com/donetick/donetick/pull/769
* Implement user-scoped tombstones for chore visibility changes and enh… by @meauxt in https://github.com/donetick/donetick/pull/780
* Fix:  issue where update was consider rescheduled by @meauxt in https://github.com/donetick/donetick/pull/776
* Refactor UndoChore logic to simplify state restoration and remove unu… by @meauxt in https://github.com/donetick/donetick/pull/783
* Add timeout to Discord webhook client by @bunlongheng in https://github.com/donetick/donetick/pull/781
* Release 0.1.77 by @meauxt in https://github.com/donetick/donetick/pull/774
* streamline locking logic in UpdateChoreVisibility method by @meauxt in https://github.com/donetick/donetick/pull/786
* fix(db): check existence of labels and notification_meta columns by @vFones in https://github.com/donetick/donetick/pull/791
* fix(workflows): update Go version to 1.24.3 in go-build.yml by @meauxt in https://github.com/donetick/donetick/pull/802

## New Contributors
* @chetmac made their first contribution in https://github.com/donetick/donetick/pull/689
* @bunlongheng made their first contribution in https://github.com/donetick/donetick/pull/781
* @vFones made their first contribution in https://github.com/donetick/donetick/pull/791

**Full Changelog**: https://github.com/donetick/donetick/compare/v0.1.76...v0.1.79

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
