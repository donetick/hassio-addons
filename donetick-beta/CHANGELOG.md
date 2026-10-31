## 0.1.76-beta.3:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Unreleased

- Expose optional S3-compatible storage settings while preserving existing backend configuration by default.
- Export the S3 provider as `s3` and expose attachment limits, quota, and public asset settings.
- Document self-hosted S3 services and explicit local filesystem opt-in for development, with a startup warning.
- Fix `disable_signup` so enabling it blocks new account registration.

## 0.1.86-beta.1:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 0bda3b38cf3f75bb152e00f00d9bbec3de3b1f88: feat: add circle ID, privacy flag, and assignment strategy to chore details (@meauxt)
* 9706cbd2e329b2f788074f61446ff67676654040: Merge pull request #944 from donetick/fix-permission-chore-details (@meauxt)

## 0.1.84-beta.6:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* dbfba02777cf37ae49986e4a33c4d55ad0a4684a: feat: add support for assignment and pending approval notifications (@meauxt)
* e44a89040f3fe1c4ea0908594bbeb8180d4ec290: Refactor notification handling to use a dispatcher for pending approval and redemption requests (@meauxt)
* 9a72aaf009792d6d24085ca64bec9aafd9b66e94: feat: enhance chore notification handling and add planning tests (@meauxt)
* fea4cd3a0bb26ff83c7a104b05184c74b52457a0: feat: update notification priority handling and preferences for improved user experience (@meauxt)
* 49319331ba324762a77c63052937e538d8374d9f: Merge pull request #940 from donetick/notificaiton-enhance-approvals (@meauxt)
* 36ba835a57355ff669b1688ca3af169f0a81a84b: Merge pull request #941 from donetick/notificaiton-enhance-approvals-remove-priority (@meauxt)

## 0.1.84-beta.5:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 437a640d6d825bd9dc08b46f19ad946b119e995e: Implement item sharing and privacy features for labels and filters (@meauxt)
* ff6508e3fef16b8a5eef1117f04b50c4f347f7f1: Enhance chore broadcasting to handle private labels per recipient and add tests for label privacy (@meauxt)
* 93eac37a878c72e8403b2c0bbb6f6f0f06fd13fd: Merge pull request #936 from donetick/label-filter-acl (@meauxt)

## 0.1.84-beta.4:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 5dd158ab6905e46e37f63740d66e021e7ab015ba: Add Support for Project Views (@meauxt)
* c96c88fd730ca176690c5f36eb1457e8053397a9: Apply fixes (@meauxt)
* 54e4432b847aa47faf7568eb28e29f7e269b91fa: Merge pull request #924 from donetick/project-board-and-list-view (@meauxt)
* bb3c895e141dd583d63d63de0f40e235e534a195: Add tests for chore creation and append logic in project sections (@meauxt)
* 64651537a808a3c7649da20b68945bd4d55e9d65: Merge pull request #927 from donetick/projecd-board-and-list-view-patch (@meauxt)
* 2a0e1dc23a18b377747ce1ccb30bb91b660d137f: Return success count in SendToDeviceTokens when no failures occur (@meauxt)

## 0.1.84-beta.2:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 3cca362e405dfb238cc21582acb54bff04eb99c6: fix(account): remove password requirement for account deletion (@meauxt)
* b09cbf813c296e3b556d010f95921f525f5d47a9: Merge pull request #913 from donetick/reduce-account-deletion-restriction (@meauxt)
* ee533c414edee91be16429ebf8756ad0a5697e9d: Revert "fix(account): remove password requirement for account deletion" (@meauxt)
* 663e7fdf44a2ac949edb133858fe86efd10aa706: Merge pull request #914 from donetick/revert-913-reduce-account-deletion-restriction (@meauxt)

## 0.1.84-beta.1:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 9b2ea2b94a73e496dff8ad2b7258afced412d978: fix(chore): restore handler changes lost in the reward-store merge (@pcbeingused333)
* 466f2cd97adf75b834174fce41d71f68f422ee00: fix(label): remove chore labels attached by another member (@pcbeingused333)
* 8687826cf9d0c0f0da5e1a2a4b9f370a1c74600d: Merge pull request #897 from pcbeingused333/fix/restore-chore-handler-after-reward-merge (@meauxt)
* 549e44c836de6b54f026624ccce9d6e8df726a30: Merge pull request #898 from pcbeingused333/fix/remove-labels-added-by-other-members (@meauxt)

## 0.1.83-beta.1:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* acb859a047075aa2a398c5a893f8e44088b42238: fix: fetch full tag history in go-release checkout (@meauxt)
* 9d9921d45efe336a1a17a81bb55d1a3af4b046a6: Merge pull request #894 from donetick/fix/go-release-checkout-tags (@meauxt)

## 0.1.81-beta.7:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* f12c0564b500fff5c4e51c9b9cb3cc85cd3bbc60: Refactor chore deletion and subtask update broadcasting to pass entire chore object (Mo Tarbin <mhed.t91@gmail.com>)

## 0.1.81-beta.6:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 2406da730e772b87da809c8aa7f03239304638b7: Merge pull request #849 from donetick/fixes-0920 (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.81-beta.5:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* b27733a75f265a2a4bd76a194b9dadbe646754f0: Merge pull request #868 from theluckystrike/fix/donetick-weekday-start (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.81-beta.4:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 0de14d36cbd4f57ae93cf7df2466e73167c6ec40: Merge pull request #874 from torbenvanassche/develop (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.81-beta.3:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* cb3ac38d112374c2c86dad8db950e093df713552: Merge pull request #872 from donetick/calendar-ics (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.81-beta.1:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* f123b3e93bd89141cb0a21ab1f4e7114a783990c: Merge pull request #583 from omarkohl/jip/auto-generate-selfhosted-yaml/qxqnktqw (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.80-beta.5:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 560c4b86b111c9c58058bd4186301640590d5a1f: Merge pull request #578 from omarkohl/jip/clarify-docker-compose-is-for/yunzmlrw (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.80-beta.4:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* b125c4a888fbf0f95bd4ef4a1e139af3dc27292b: Merge pull request #858 from donetick/fix-hassio-integration (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.80-beta.3:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 656525838e83f21bfd584efd25bd435b1e6cec8a: Merge pull request #830 from wesleymerrick/fix/email-app-host-env-var (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.80-beta.2:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 3875c21ac5f578a76c0619266836b5abe4b08319: Merge pull request #850 from donetick/fixes-0920-just-duedate (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.80-beta.1:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 15bbf141eb2e17b577fa802ed0d12157f97fcf44: Merge pull request #802 from donetick/fix-go-release (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.78-beta.3:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 0fb2a3cd017a6efb6a779f262dfef68357d4d011: fix(migration): handle case where no notification targets are created (Mo Tarbin <mhed.t91@gmail.com>)

## 0.1.78-beta.2:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* be6070d66d72c9a93e83f224ea9b8d4365e0cf01: Merge pull request #791 from vFones/fix/column-in-migrations-not-existing (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.78-beta.1:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 06f06f70b3114bcd03fdd7662fac6740f92c3fcf: Merge pull request #786 from donetick/chore-visibility-lock (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.77-beta.5:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* c34f62b9d4b748141be7d7839b476736b9008960: fix: add timeout to Discord webhook http client (#781) (Bunlong Heng <bheng.code@gmail.com>)

## 0.1.77-beta.4:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 0a5d15359259ee2e19797501ea02a21b2febd302: Fix:  issue where update was consider rescheduled (#776) (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.77-beta.3:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 627fe471acf908653404398e3129ae7b060b327a: Implement bumpChoreSyncVersions to manage sync versions for chore updates (#769) (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.77-beta.2:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 8f339f7b12658e2d8dc7ba18102d4f220267ac70: Make sure removing and changing label bump syncverison (#762) (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.77-beta.1:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 59e89003a7ececead5da402fda22a3eeeb3f54ab: Send reminders to all circle members for chores assigned to "Anyone" (#746) (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.76-beta.23:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 59e89003a7ececead5da402fda22a3eeeb3f54ab: Send reminders to all circle members for chores assigned to "Anyone" (#746) (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.76-beta.22:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* a0c4bd66cf931edfb3cc4259301824c0809be516: gofmt (Mo Tarbin <mhed.t91@gmail.com>)

## 0.1.76-beta.21:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* fbd5b15f2ec3a3a4858c8e04b85a4501c494ebe8: Merge remote-tracking branch 'origin/main' into develop-m (Mo Tarbin <mhed.t91@gmail.com>)

## 0.1.76-beta.20:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 8737077cf2cc470eaafc7450ef4a6f53f30fd86d: Run migration script agains sqlite always (#731) (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.76-beta.19:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* efbe9c86c99d1ef9f249d869596ebdfb83165deb: remove the uniqueness  requirement on api token name (#726) (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.76-beta.18:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 964213ec79cb54b82c795a66a7f8210226d6ee7b: unify docker file and add commit to the go releaser (#724) (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.76-beta.17:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* ff0629c5755e346db27a693d945e355a3b8b9f4b: Bugfix/rework api input validation frontend error (#681) (Mihaly Hobor <hoborm@users.noreply.github.com>)

## 0.1.76-beta.16:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* ff0629c5755e346db27a693d945e355a3b8b9f4b: Bugfix/rework api input validation frontend error (#681) (Mihaly Hobor <hoborm@users.noreply.github.com>)

## 0.1.76-beta.15:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 12afbdcc1d3f7811de26d1e76ee11bf92f7f728f: Bug fixes 06 27 2026 (#712) (Mohamad Tarbin <mhed.t91@gmail.com>)

## 0.1.76-beta.14:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 88f6ebc80683ea55f4cf0ec36e4a038fc4d14191: feat(auth): add disable_password_auth option for SSO-only instances (#438) (#699) (Louis-Michel Couture <louim_1@hotmail.com>)

## 0.1.76-beta.13:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 0d160aa90143e0942cfc100332828d88e993835d: add syncVersion field to Event struct for version handling (Mo Tarbin <mhed.t91@gmail.com>)

## 0.1.76-beta.12:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 0d160aa90143e0942cfc100332828d88e993835d: add syncVersion field to Event struct for version handling (Mo Tarbin <mhed.t91@gmail.com>)

## 0.1.76-beta.9:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* 0ca432c1f7731ef9c4c2f00aad7f2f845ef9c2b3: Merge branch 'develop' of https://github.com/donetick/donetick into develop (Mo Tarbin <mhed.t91@gmail.com>)

## 0.1.76-beta.8:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.


## What's Changed
* add log_raw_url option to log password reset URL in console by @meauxt in https://github.com/donetick/donetick/pull/675
* fix(oidc): honor preferred_username claim on OAuth2 signup by @MaikuMori in https://github.com/donetick/donetick/pull/634
* Graceful Validation with Warnings. to make sure we have a non-breaking by @meauxt in https://github.com/donetick/donetick/pull/674
* fix: include validation details in API error responses by @mvanhorn in https://github.com/donetick/donetick/pull/606
* Offline Support: Add Synchronization and Versioning by @meauxt in https://github.com/donetick/donetick/pull/665

## New Contributors
* @mvanhorn made their first contribution in https://github.com/donetick/donetick/pull/606

**Full Changelog**: https://github.com/donetick/donetick/compare/v0.1.76-beta.6...v0.1.76-beta.8

## 0.1.76-beta.6:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* cfc9e4c5687e48ab22d42f59f6b392847af8323e: Bugfix/rework api input validation (#607) (Mihaly Hobor <hoborm@users.noreply.github.com>)

## 0.1.76-beta.5:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* cfc9e4c5687e48ab22d42f59f6b392847af8323e: Bugfix/rework api input validation (#607) (Mihaly Hobor <hoborm@users.noreply.github.com>)

## 0.1.76-beta.4:
> [!WARNING]
> This release is intended for testing purposes only. Please do not use it with production data, as frequent updates and architectural changes may occur between pre-release versions.

## Changelog
* cfc9e4c5687e48ab22d42f59f6b392847af8323e: Bugfix/rework api input validation (#607) (Mihaly Hobor <hoborm@users.noreply.github.com>)

## Changelog
* fcd3bb270b83b691e0ca4f6f6bf9ec47d50bee99: Merge branch 'develop' of https://github.com/donetick/donetick into develop (Mo Tarbin <mhed.t91@gmail.com>)

<!-- https://developers.home-assistant.io/docs/add-ons/presentation#keeping-a-changelog -->
